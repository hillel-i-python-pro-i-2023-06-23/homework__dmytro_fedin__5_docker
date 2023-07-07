import argparse
from faker import Faker


fake = Faker()

fake_name = fake.name()


def print_fake_name() -> None:
    print(f"My name is {fake_name}.")


parser = argparse.ArgumentParser(description="My first and simple CLI program.")

parser.add_argument("--name", help="Your name.")

args = parser.parse_args()


def is_name() -> bool:
    if args.name is None:
        return False
    else:
        return True


def parse_name() -> None:
    if args.name:
        print(f"Hello, {args.name}!")


def main() -> None:
    if is_name():
        parse_name()
        print_fake_name()
    else:
        print("Tell me Your name, please. (Run cmd [--help] for help)")
        # msg = "Failed"


if __name__ == "__main__":
    main()
