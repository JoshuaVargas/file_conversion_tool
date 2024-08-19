# File Conversion Tool

## Overview

The File Conversion Tool is a Python-based application designed to handle various file conversions. Currently, it supports:

- **CSV to JSON/XML conversion**
- **PDF to text extraction**
- **Image format conversion and resizing**
- **Audio/Video format conversion**

This tool is structured into modules and includes unit tests for validating the functionality of each module.

## Project Structure
```
file_conversion_tool/
│
├── README.md
├── requirements.txt
├── main.py
│
├── config/
│ └── settings.py
│
├── src/
│ ├── init.py
│ ├── image_converter.py
│ ├── pdf_converter.py
│ ├── csv_converter.py
│ └── media_converter.py
│
├── tests/
│ ├── init.py
│ ├── test_image.py
│ ├── test_pdf.py
│ ├── test_csv.py
│ └── test_media.py
│
├── utils/
│ ├── init.py
│ ├── file_utils.py
│ └── logging_utils.py
│
├── input/
│ ├── images/
│ ├── pdfs/
│ ├── csvs/
│ └── media/
│
└── output/
├── images/
├── texts/
├── jsons/
└── media/
```

## Current Status

- **Completed**: The `src` directory with all the conversion modules (`image_converter.py`, `pdf_converter.py`, `csv_converter.py`, `media_converter.py`), and the `tests` directory with all unit tests for these modules.
- **In Progress**: The `main.py` script for orchestrating the tool's execution. This is yet to be implemented.

## Future Plans

The project is planned to transition into a Flask application. This will enable a web interface for file conversion, enhancing usability and accessibility.
