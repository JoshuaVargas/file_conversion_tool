import os
from pypdf import PdfReader

def pdf_to_text(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            with open(os.path.join(input_folder, filename), 'rb') as pdf_file:
                reader = PdfReader(pdf_file)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() or ''  # Handle the case where extract_text() might return None
                output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.txt')
                with open(output_file, 'w') as text_file:
                    text_file.write(text)
                print(f'Converted {filename} to text and saved as {output_file}')