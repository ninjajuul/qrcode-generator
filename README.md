**QR Code Generator**

A simple Python script that generates QR codes from any text or URL. Just type or paste your input, and the script creates a scannable QR code, displays an ASCII preview directly in your terminal, and saves it as a PNG file for later use.

**Features**

* Generate QR codes from any text or URL.
* Displays the complete QR code as ASCII art in the terminal.
* Automatically names the saved file after the website domain.
* Saves the PNG in the same folder as the script, no matter where it's run from.
* Simple and lightweight.
* Easy to modify or integrate into other projects.

**Requirements**

* Python 3.7 or newer
* `qrcode`

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

The script will display an ASCII preview of the QR code and save a PNG version in the same folder.

**Supported Input**

* Standard URLs (`https://example.com`)
* Short URLs (`youtu.be`, `t.co`, etc.)
* Plain text of any kind

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

Simply scan the terminal preview with your phone, or open the saved PNG file directly.

**Limitations**

* Very long text or URLs may require a higher QR code version to encode properly.
* Terminal rendering may look slightly distorted depending on font and window size — the saved PNG is always accurate regardless.
* Generating multiple QR codes for the same domain will overwrite the previous file unless renamed manually.

**Possible Improvements**

* Automatically detect and prevent filename collisions.
* Add support for custom colors and embedded logos.
* Build a simple graphical user interface (GUI).
* Batch generate QR codes from a list of URLs.
* Add adjustable error correction levels for damaged or dirty codes.

**Disclaimer**

This project only generates QR codes from user-provided input. It does not scan, decode, or interact with existing QR codes in any way. Please ensure you have the right to encode any content you use with this tool.

**License**

This project is open source. Feel free to modify, improve, and share it.
