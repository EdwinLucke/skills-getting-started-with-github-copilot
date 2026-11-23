import socket
import subprocess
import sys
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

import pytest
from playwright.sync_api import Browser, Page, sync_playwright


@pytest.fixture(scope="session")
def live_app():
    project_root = Path(__file__).resolve().parents[2]
    with socket.socket() as socket_server:
        socket_server.bind(("127.0.0.1", 0))
        port = socket_server.getsockname()[1]

    process = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "uvicorn",
            "src.app:app",
            "--host",
            "127.0.0.1",
            "--port",
            str(port),
        ],
        cwd=project_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    base_url = f"http://127.0.0.1:{port}"

    try:
        deadline = time.monotonic() + 15
        while time.monotonic() < deadline:
            if process.poll() is not None:
                output, _ = process.communicate()
                raise RuntimeError(f"Uvicorn exited before startup:\n{output}")

            try:
                with urlopen(f"{base_url}/activities", timeout=0.5) as response:
                    if response.status == 200:
                        break
            except (TimeoutError, URLError):
                time.sleep(0.1)
        else:
            raise RuntimeError("Uvicorn did not become ready within 15 seconds")

        yield base_url
    finally:
        if process.poll() is None:
            process.terminate()
        try:
            process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
            process.communicate()


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
