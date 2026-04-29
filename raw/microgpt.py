name=raw/microgpt.py
#!/usr/bin/env python3
"""
Downloader helper for including Karpathy's microgpt gist into raw/.
This script fetches the raw gist and saves it to raw/microgpt_raw.py.
Usage: python raw/microgpt.py --fetch

Note: This script downloads the gist at user action time (it does not embed the third-party code into the scaffold).
"""

import sys
from pathlib import Path

RAW_URL = "https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/microgpt.py"
OUT_PATH = Path(__file__).parent / "microgpt_raw.py"


def fetch():
    # Try requests first, fallback to urllib
    try:
        import requests
        r = requests.get(RAW_URL, timeout=15)
        r.raise_for_status()
        text = r.text
    except Exception:
        try:
            from urllib.request import urlopen
            with urlopen(RAW_URL, timeout=15) as fh:
                text = fh.read().decode('utf-8')
        except Exception as e:
            print("Cannot fetch file: requests not available and urllib failed:", e)
            sys.exit(1)

    OUT_PATH.write_text(text, encoding='utf-8')
    print(f"Saved microgpt raw file to {OUT_PATH}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--fetch', action='store_true', help='Download the microgpt raw file into raw/microgpt_raw.py')
    args = parser.parse_args()
    if args.fetch:
        fetch()
    else:
        print("This file is a downloader. Run with --fetch to download the microgpt gist into raw/")
