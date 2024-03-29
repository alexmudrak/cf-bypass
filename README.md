# CF-Bypass Tool

This Python script allows you to take a screenshot of a webpage, even if it is protected by Cloudflare's "Just a moment" screen.

## Features

- Bypass Cloudflare's "Just a moment" screen.
- Take a screenshot of the webpage.
- Run in headless mode for automation.

## Requirements

- Python 3.6+
- Selenium
- Pillow
- Colorama
- SeleniumBase

## Installation

Before running the script, ensure you have the required packages installed:

```bash
poetry install
```

You will also need to have ChromeDriver installed and available in your system's PATH.

## Usage

To use the script, run it from the command line and pass the URL of the webpage as an argument:

```bash
python screenshot.py <URL>
```

Replace `<URL>` with the actual URL of the webpage you want to capture.

## Troubleshooting

If you encounter issues with Cloudflare bypass, you may need to adjust the `TRY_COUNT` variable to attempt more retries.

## License

This project is open-source and available under the MIT License.
