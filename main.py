from cli_version import run_cli_version
from gui_version import run_gui_version

def main():
    while True:
        choice = input("Would you like to use the CLI or GUI version? Enter 'CLI' or 'GUI': ").strip().lower()
        if choice == 'cli':
            run_cli_version()
            break
        elif choice == 'gui':
            run_gui_version()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()