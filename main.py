from cli_version import run_cli_version
import traceback
import argparse

def main(input_data):
    print("Recived Input: ", input_data)
    try:
        run_cli_version(input_data)
    except Exception:
        print("Something went wrong. Please try again.")
        traceback.print_exc()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test script for PHP to call')
    parser.add_argument('--input', required=True, help='Input data (URL or Postcode)')
    
    args = parser.parse_args()
    main(args.input)

