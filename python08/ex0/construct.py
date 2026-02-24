#!/usr/bin/env python3
import sys
import site
import os


def venv_state() -> bool:
    return "VIRTUAL_ENV" in os.environ or sys.base_prefix != sys.prefix


def main() -> None:
    venv: bool = venv_state()
    if venv:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        path_split: list[str] = sys.prefix.split("/")
        print(f"Virtual Environment: {path_split[-1]}")
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("\nPackage installation path:")
        print(site.getsitepackages()[0])
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows\n")
        print("Then run this program again")


if __name__ == "__main__":
    main()
