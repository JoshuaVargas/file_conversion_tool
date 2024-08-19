import os
from PIL import Image
import pytest
from src.image_converter import convert_images

@pytest.fixture
def setup_folders(tmpdir):
    # Create temporary directories for input and output
    input_folder = tmpdir.mkdir("input_images")
    output_folder = tmpdir.mkdir("output_images")
    return str(input_folder), str(output_folder)

@pytest.fixture
def sample_image(setup_folders):
    input_folder, _ = setup_folders
    # Create a sample image file
    image = Image.new('RGB', (100, 100), color='red')
    image.save(os.path.join(input_folder, "test_image.png"))

def test_convert_image_to_jpg(setup_folders, sample_image):
    input_folder, output_folder = setup_folders
    
    convert_images(input_folder, output_folder, 'jpg')
    
    output_file = os.path.join(output_folder, 'test_image.jpeg')  # Updated extension to .jpeg
    print(f'Checking for file: {output_file}')
    assert os.path.exists(output_file), "JPEG file was not created"
    
    # Verify the image file is valid
    with Image.open(output_file) as img:
        assert img.format == 'JPEG', "Converted image is not in JPG format"

def test_convert_image_with_resize(setup_folders, sample_image):
    input_folder, output_folder = setup_folders
    
    convert_images(input_folder, output_folder, 'jpg', resize=(50, 50))
    
    output_file = os.path.join(output_folder, 'test_image.jpeg')  # Updated extension to .jpeg
    print(f'Checking for file: {output_file}')
    assert os.path.exists(output_file), "JPEG file was not created"
    
    # Verify the image file is valid and resized
    with Image.open(output_file) as img:
        assert img.format == 'JPEG', "Converted image is not in JPG format"
        assert img.size == (50, 50), "Image was not resized correctly"

def test_convert_image_to_bmp(setup_folders, sample_image):
    input_folder, output_folder = setup_folders
    
    convert_images(input_folder, output_folder, 'bmp')
    
    output_file = os.path.join(output_folder, 'test_image.bmp')
    print(f'Checking for file: {output_file}')
    assert os.path.exists(output_file), "BMP file was not created"
    
    # Verify the image file is valid
    with Image.open(output_file) as img:
        assert img.format == 'BMP', "Converted image is not in BMP format"

def test_create_output_folder(setup_folders, sample_image):
    input_folder, _ = setup_folders
    temp_output_folder = "temp_output_folder"
    
    # Ensure the folder does not exist
    if os.path.exists(temp_output_folder):
        # Remove all files and subdirectories first
        for root, dirs, files in os.walk(temp_output_folder, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(temp_output_folder)
    
    convert_images(input_folder, temp_output_folder, 'jpg')
    
    assert os.path.exists(temp_output_folder), "Output folder was not created"
    
    # Clean up
    for root, dirs, files in os.walk(temp_output_folder, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(temp_output_folder)