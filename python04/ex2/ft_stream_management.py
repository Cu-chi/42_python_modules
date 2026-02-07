import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    archivist_id: str = input("Input Stream active. Enter archivist ID: ")
    status_report: str = input("Input Stream active. Enter status report: ")
    sys.stdout.write(f"\n[STANDARD] Archive status from {archivist_id}: ")
    sys.stdout.write(f"{status_report}\n")
    sys.stdout.flush()
    sys.stderr.write("[ALERT] System diagnostic: Communication channels "
                     "verified")
    sys.stderr.flush()
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.flush()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
