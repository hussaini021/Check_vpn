import os
import sys
import vpn2
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

try:
    import vpn2
except Exception as e:
    print("FAILED TO LOAD VPN ENGINE")
    print(e)
    sys.exit(1)


def main():
    print("=== VPN GUARD PRO ANALYSIS ===")

    if hasattr(vpn2, "check_dns"):
        print(vpn2.check_dns())

    if hasattr(vpn2, "check_webrtc"):
        print(vpn2.check_webrtc())

    if hasattr(vpn2, "check_proxy"):
        print(vpn2.check_proxy())

    if hasattr(vpn2, "risk_score"):
        print("RISK SCORE:", vpn2.risk_score())


if __name__ == "__main__":
    main()
