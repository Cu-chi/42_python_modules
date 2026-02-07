def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    new_storage = None
    data = "[ENTRY 001] New quantum algorithm discovered\n"
    data += "[ENTRY 002] Efficiency increased by 347%\n"
    data += "[ENTRY 003] Archived by Data Archivist trainee\n"
    try:
        print("Initializing new storage unit: new_discovery.txt")
        new_storage = open("new_discovery.txt", "w")
        print("Storage unit created successfully...\n")

        print("Inscribing preservation data...")
        new_storage.write(data)
        print(data)
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if new_storage is not None:
            new_storage.close()


if __name__ == "__main__":
    main()
