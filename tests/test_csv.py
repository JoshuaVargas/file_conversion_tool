import os
import pandas as pd
import pytest
from unittest.mock import patch
from src.csv_converter import convert_csv

@pytest.fixture
def setup_folders(tmpdir):
    # Create temporary directories for input and output
    input_folder = tmpdir.mkdir("input_csvs")
    output_folder = tmpdir.mkdir("output_jsons")
    return str(input_folder), str(output_folder)

@pytest.fixture
def sample_csv(setup_folders):
    input_folder, _ = setup_folders
    # Create a sample CSV file
    data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(input_folder, "test.csv"), index=False)

def test_convert_csv_to_json(setup_folders, sample_csv):
    input_folder, output_folder = setup_folders
    
    convert_csv(input_folder, output_folder, 'json')
    
    output_file = os.path.join(output_folder, 'test.json')
    assert os.path.exists(output_file), "JSON file was not created"
    
    # Check if the JSON file contains the expected data
    df = pd.read_json(output_file, orient='records', lines=True)
    assert len(df) == 2, "JSON file does not contain the expected number of records"

def test_convert_csv_to_xml(setup_folders, sample_csv):
    input_folder, output_folder = setup_folders
    
    convert_csv(input_folder, output_folder, 'xml')
    
    output_file = os.path.join(output_folder, 'test.xml')
    assert os.path.exists(output_file), "XML file was not created"
    
    # Read and check the XML file content
    with open(output_file, 'r') as file:
        content = file.read()
    
    # Debug output to understand the XML structure
    print("XML Content:", content)
    
    # Modify these checks based on the actual XML structure
    assert '<name>Alice</name>' in content, "XML file does not contain expected data for Alice"
    assert '<age>25</age>' in content, "XML file does not contain expected data for age 25"

def test_create_output_folder(setup_folders, sample_csv):
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
    
    convert_csv(input_folder, temp_output_folder, 'json')
    
    assert os.path.exists(temp_output_folder), "Output folder was not created"
    
    # Clean up
    for root, dirs, files in os.walk(temp_output_folder, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(temp_output_folder)