from cli_local import run_cli_local
from gui_version import run_gui_version
import traceback

#modify the old main into try/except
def main():
    while True:
        try:
            choice = input("Would you like to use the CLI or GUI version? Enter 'CLI' or 'GUI': ").strip().lower()
            input_data = input("Enter postcode or Zoopla URL: ")
            if choice == 'cli':
                run_cli_local(input_data)
                break
            elif choice == 'gui':
                run_gui_version()
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception:
            print("Something went wrong. Please try again.")
            traceback.print_exc()



if __name__ == "__main__":
    main()