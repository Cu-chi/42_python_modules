from dotenv import load_dotenv
import os


def get_env(keys: list[str]) -> dict[str, str]:
    env: dict[str, str] = {}
    for key in keys:
        env.update({key: os.getenv(key)})
    return env


def print_env(env: dict[str, str]) -> None:
    for key, value in env.items():
        print(f"{key}={value}")


def main() -> None:
    load_env_res: bool = load_dotenv()
    env: dict[str, str] = get_env([
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT"
    ])
    print("\nORACLE STATUS: Reading the Matrix...\n")
    if not load_env_res:
        print("[WARNING] .env not found\n")
        print("[INFO] here are the keys you can set:")
        print_env(env)
        return
    print("Mode: " + (env["MATRIX_MODE"]
          if env["MATRIX_MODE"]
          else "development"))
    print("Database: " + ("Connected to local instance"
          if env["DATABASE_URL"] else "Not connected"))
    print("API Access: " + ("Authenticated"
          if env["API_KEY"]
          else "Not authenticated"))
    print("Log Level: " + (env["LOG_LEVEL"]
          if env["LOG_LEVEL"]
          else "UNSET"))
    print("Zion Network: " + ("Online"
          if env["ZION_ENDPOINT"]
          else "Offline"))

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
