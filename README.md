
# renderPyBass

`renderPyBass` is a Python-based tool designed to keep free-plan Render web apps "awake" by periodically sending requests.
The goal is to avoid the **"Render is deploying"** screen that appears when a site on Render's free plan is accessed after being idle.
This can be critical for **new websites** that desperately need to give a good **first impression** to visitors without forcing them to face a long loading time or an intimidating deployment interface.

## Why the Name?

The name **renderPyBass** is a play on words:

* **Bypass** → letters switched to avoid direct naming
* **Bass** → a reference to the bass fish, known for lurking and waiting for the right moment — much like how this script quietly keeps your app ready for visitors.
* **Py** → written in Python.

## Features

* Fetches and validates public HTTPS proxies before use.
* Rotates proxies to prevent rate limiting or blocking.
* Random wait intervals between requests (0–300 seconds) to mimic natural traffic.
* Avoids repeated downtime-causing requests by filtering only valid proxies.

## How It Works

1. **Proxy Fetching** — The script gathers a list of publicly available HTTPS proxies.
2. **Proxy Validation** — Each proxy is tested against your target Render site.
3. **Keep-Alive Requests** — Periodically sends requests to the target URL through working proxies.
4. **Randomized Delays** — Sleep time between requests is randomized to avoid suspicious patterns.

## Requirements

* Python 3.8+
* Required packages:

  ```bash
  pip install requests
  ```

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/renderPyBass.git
   cd renderPyBass
   ```
2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. Run the script:

   ```bash
   python renderPyBass.py
   ```

## Disclaimer

This script is for **educational purposes** only. ;) ak fahem
