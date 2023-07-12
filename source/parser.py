import argparse

parser = argparse.ArgumentParser(description="My first and simple CLI program.")

parser.add_argument("--name", help="Your name.")

args = parser.parse_args()


# With no exclusion
def is_name() -> bool:
    if args.name is None:
        return False
    else:
        return True


def parse_name() -> None:
    if args.name:
        print(f"Hello, {args.name}!")
