def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    try:
        print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("STATUS: Crisis handled, system stable")

    try:
        print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt", "r") as file:
            print("Access authorized")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("STATUS: Crisis handled, security maintained")

    try:
        print("\nROUTINE ACCESS: Attempting access to"
              "'standard_archive.txt'...")
        with open("standard_archive.txt") as file:
            print(f"SUCCESS: Arrchive recovered - \"{file.read()}\"")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("STATUS: Normal operations resumed")
    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
