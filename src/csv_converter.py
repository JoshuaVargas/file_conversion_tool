import pandas as pd
import os

def convert_csv(input_folder, output_folder, output_format='json'):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            df = pd.read_csv(os.path.join(input_folder, filename))
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + f'.{output_format}')
            
            if output_format == 'json':
                df.to_json(output_file, orient='records', lines=True)
            elif output_format == 'xml':
                df.to_xml(output_file)
            print(f'Converted {filename} to {output_format} and saved as {output_file}')