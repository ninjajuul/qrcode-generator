**QR Code Generator**

A simple Python script that generates QR codes from any text or URL. Just type or paste your input, and the script creates a scannable QR code, saves it as a PNG in the same folder as the script, and displays it right in your terminal for a quick preview.

**Features**

* Generate QR codes from any text or URL.
* Automatically names the file after the website domain (e.g. `github.com.png`).
* Displays an ASCII preview of the QR code directly in the terminal.
* Saves the PNG in the same folder as the script, regardless of where it's run from.
* Simple and lightweight.
* Easy to modify or integrate into other projects.

**Requirements**

* Python 3.7 or newer
* `qrcode`
* `Pillow` (installed automatically via `qrcode[pil]`)

**Installation**

Clone this repository:

```
git clone https://github.com/yourusername/QR-Code-Generator
cd QR-Code-Generator
```

Create a virtual environment (recommended):

Linux/macOS
```
python3 -m venv venv
source venv/bin/activate
```

Windows
```
python -m venv venv
venv\Scripts\activate
```

Install the required package:

```
pip install qrcode[pil]
```

**Usage**

Run the script:

```
python qr_generator.py
```

When prompted, enter a URL or text:

```
Enter text or URL to encode:
```

Example:

```
Enter text or URL to encode:
https://github.com
```

The script will display an ASCII preview of the QR code in the terminal and save a PNG version in the same folder.

**Example Output**

```
██████████████  ████  ██    ██████████████
██          ██  ████    ██  ██          ██
██  ██████  ██  ██████████  ██  ██████  ██
██  ██████  ██        ██    ██  ██████  ██
██  ██████  ██  ██  ██████  ██  ██████  ██
██          ██    ████      ██          ██
██████████████  ██  ██  ██  ██████████████
                    ██                    
██    ████████████  ████  ██    ██  ██████
  ██████  ██      ████  ████████          
██    ██  ████  ██  ██████████      ██████
████  ██                ████  ████  ██  ██
  ██  ████  ████  ██      ██    ████      
                ████          ██████  ████
██████████████  ██    ██████    ██        
██          ██  ████████    ██    ████████
██  ██████  ██  ██  ██        ██████  ██  
██  ██████  ██  ██    ██  ████    ██      
██  ██████  ██          ████    ████  ████
██          ██      ████    ████  ████████
██████████████  ██      ██████████        

QR code saved to: /path/to/folder/github.com.png
```

**File Naming**

* URLs are automatically converted into safe filenames based on their domain (e.g. `https://www.google.com` → `google.com.png`).
* Plain text with no domain defaults to `qrcode.png`.

**Limitations**

* Very long text/URLs may require a higher QR code `version` to encode successfully.
* Terminal rendering may look distorted depending on font and terminal size — the saved PNG is always accurate regardless.
* Generating multiple QR codes for the same domain will overwrite the previous file unless the filename is changed manually.

**Disclaimer**

This project only generates QR codes from user-provided input. It does not scan, decode, or interact with QR codes in any way. Please ensure you have the right to encode any content you use with this tool.

**License**

This project is open source. Feel free to modify, improve, and share it.
