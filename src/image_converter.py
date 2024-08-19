from PIL import Image
import os

def convert_images(input_folder, output_folder, target_format, resize=None):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    target_format = target_format.upper()  # Ensure format is uppercase
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            img = Image.open(os.path.join(input_folder, filename))
            if resize:
                img = img.resize(resize)
            # Convert 'JPG' to 'JPEG' for saving
            if target_format == 'JPG':
                target_format = 'JPEG'
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + f'.{target_format.lower()}')
            img.save(output_file, target_format)
            print(f'Converted {filename} to {target_format.lower()} and saved as {output_file}')