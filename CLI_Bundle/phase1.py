import argparse

def main():
    parser = argparse.ArgumentParser(description="GRCP Phase 1: Discovery")
    parser.add_argument('--prompt', required=True)
    args = parser.parse_args()
    print(f"Phase 1: Discovering ideas for '{args.prompt}'...")

if __name__ == "__main__":
    main()
