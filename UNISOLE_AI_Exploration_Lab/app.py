"""Entry point for the UNISOLE AI Exploration Lab."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).parent


def main() -> None:
    print("UNISOLE AI Exploration Lab scaffold is ready.")
    print(f"Project root: {PROJECT_ROOT}")


if __name__ == "__main__":
    main()
