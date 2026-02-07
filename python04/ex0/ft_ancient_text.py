def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    f = None
    try:
        print("Accessing Storage Vault: ancient_fragment.txt")
        f = open("ancient_fragment.txt", "r")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f.read())
        print("\nData recovery complete. ", end="")
    except FileNotFoundError as e:
        print(f"Error accessing storage vault: '{e.filename}' not found")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if f is not None:
            f.close()
            print("Storage unit disconnected.")


if __name__ == "__main__":
    main()
