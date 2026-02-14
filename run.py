import os
import vpn2
import os
import sys
git pull

import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

try:
    import vpn2
except Exception as e:
    print("FAILED TO LOAD CYTHON MODULE:")
    print(e)
    sys.exit(1)


def safe_run(func, name):
    try:
        return func()
    except Exception as e:
        return f"{name} FAILED: {e}"


def main():
    print("=== VPN GUARD PRO ANALYSIS ===\n")

    start = time.time()

    if hasattr(vpn2, "check_dns"):
        print(safe_run(vpn2.check_dns, "DNS CHECK"))

    if hasattr(vpn2, "check_webrtc"):
        print(safe_run(vpn2.check_webrtc, "WEBRTC CHECK"))

    if hasattr(vpn2, "check_proxy"):
        print(safe_run(vpn2.check_proxy, "PROXY CHECK"))

    if hasattr(vpn2, "risk_score"):
        print("RISK SCORE:", safe_run(vpn2.risk_score, "RISK SCORE"))

    elapsed = round(time.time() - start, 2)
    print(f"\nAnalysis finished in {elapsed}s")


if __name__ == "__main__":
    main()
