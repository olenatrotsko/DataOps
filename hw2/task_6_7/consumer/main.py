from pathlib import Path
from urllib.request import urlopen
import time

SHARED_FILE = Path("/shared/messages.txt")
PRODUCER_URL = "http://producer:8000"

while True:
    # Test Docker networking
    try:
        with urlopen(PRODUCER_URL, timeout=3) as response:
            print(f"NETWORK: {response.read().decode()}", flush=True)
    except Exception as exc:
        print(f"NETWORK ERROR: {exc}", flush=True)

    # Test shared Docker volume
    if SHARED_FILE.exists():
        messages = SHARED_FILE.read_text().splitlines()

        if messages:
            print(f"VOLUME: {messages[-1]}", flush=True)

    time.sleep(5)
