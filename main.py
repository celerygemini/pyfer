import pyfer
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Encrypt and decrypt message strings."
    )
    parser.add_argument("key", type=str, help="Encryption key.")
    parser.add_argument("message", type=str, help="Message.")
    args = parser.parse_args()

    mac = pyfer.Machine(args.key)
    res = mac.scramble(args.message)
    print(res)
