from cli_version import run_cli_version
#from gui_version import run_gui_version
import traceback

# def main():
#     while True:
#         choice = input("Would you like to use the CLI or GUI version? Enter 'CLI' or 'GUI': ").strip().lower()
#         if choice == 'cli':
#             run_cli_version()
#             break
#         elif choice == 'gui':
#             run_gui_version()
#             break
#         else:
#             print("Invalid choice. Please try again.")

#modify the old main into try/except
def main():
    while True:
        try:
            choice = input("Would you like to use the CLI or GUI version? Enter 'CLI' or 'GUI': ").strip().lower()
            if choice == 'cli':
                run_cli_version()
                break
            elif choice == 'gui':
                print("GUI version is not available yet. Please try again.")
                #run_gui_version()
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception:
            print("Something went wrong. Please try again.")
            traceback.print_exc()


    
if __name__ == "__main__":
    main()
