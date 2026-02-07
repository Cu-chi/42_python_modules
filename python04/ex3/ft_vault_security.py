def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    classified = None
    protocols = None
    try:
        with open("classified_data.txt", "r") as classified:
            print("\nSECURE EXTRACTION:")
            print(classified.read())
        with open("security_protocols.txt", "a") as protocols:
            log: str = "[CLASSIFIED] New security protocols archived\n"
            print("\nSECURE PRESERVATION:")
            protocols.write(log)
            print(log, end="")
    except FileNotFoundError as e:
        print(f"Error classified data: '{e.filename}' not found")
    except Exception as e:
        print(f"Error: {e}")
    if protocols and protocols.closed and classified and classified.closed:
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")
    elif protocols and classified:
        print("Error: critical error, vault not closed")


if __name__ == "__main__":
    main()
