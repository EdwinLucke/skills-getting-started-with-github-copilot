# Browser User-Journey Tests

These Playwright tests exercise student signup through the browser against a local application server.

From the repository root, install the development dependencies and Chromium:

```sh
python -m pip install -r requirements-dev.txt
python -m playwright install chromium
```

On Linux, if Chromium reports missing system libraries, install them with:

```sh
python -m playwright install-deps chromium
```

Run the user-journey suite with:

```sh
python -m pytest -q tests/userjourneys
```
