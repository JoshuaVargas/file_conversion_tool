import os
import pytest
from fpdf import FPDF
from src.pdf_converter import pdf_to_text

@pytest.fixture
def setup_folders(tmpdir):
    input_folder = tmpdir.mkdir("input_pdfs")
    output_folder = tmpdir.mkdir("output_texts")
    return str(input_folder), str(output_folder)

@pytest.fixture
def sample_pdf(setup_folders):
    input_folder, _ = setup_folders
    
    # Create a sample PDF file with some text
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Hello World", ln=True, align='C')
    pdf_output_path = os.path.join(input_folder, "sample.pdf")
    pdf.output(pdf_output_path)

def test_pdf_to_text_conversion(setup_folders, sample_pdf):
    input_folder, output_folder = setup_folders

    pdf_to_text(input_folder, output_folder)

    output_file = os.path.join(output_folder, 'sample.txt')
    assert os.path.isfile(output_file), "Text file was not created"

    with open(output_file, 'r') as file:
        content = file.read()

    assert "Hello World" in content, "Text file does not contain the expected text"

def test_pdf_to_text_output_folder_creation(setup_folders, sample_pdf):
    input_folder, _ = setup_folders
    temp_output_folder = "temp_output_folder"

    # Ensure the folder does not exist
    if os.path.exists(temp_output_folder):
        for root, dirs, files in os.walk(temp_output_folder, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(temp_output_folder)

    pdf_to_text(input_folder, temp_output_folder)

    assert os.path.exists(temp_output_folder), "Output folder was not created"

    # Clean up
    for root, dirs, files in os.walk(temp_output_folder, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(temp_output_folder)
