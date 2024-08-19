import ffmpeg
import os

def convert_media(input_folder, output_folder, output_format):
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    # Ensure input_folder and output_folder are valid directories
    if not os.path.isdir(input_folder):
        print(f"Error: Input folder does not exist: {input_folder}")
        return

    if not os.path.isdir(output_folder):
        print(f"Error: Output folder does not exist: {output_folder}")
        return

    for filename in os.listdir(input_folder):
        input_file = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]
        output_file = os.path.join(output_folder, f"{base_name}.{output_format}")

        if filename.endswith('.mp3') or filename.endswith('.wav'):
            # Convert audio files
            try:
                print(f"Converting: {input_file} to {output_file}")
                ffmpeg.input(input_file).output(output_file).run(overwrite_output=True)
                print(f"Conversion successful: {output_file}")
            except ffmpeg.Error as e:
                error_message = e.stderr.decode() if e.stderr else 'Unknown error'
                print(f"Error during conversion: {error_message}")

        elif filename.endswith('.mp4') or filename.endswith('.avi'):
            # Convert video files (adjust as needed based on your use case)
            try:
                print(f"Converting: {input_file} to {output_file}")
                ffmpeg.input(input_file).output(output_file).run(overwrite_output=True)
                print(f"Conversion successful: {output_file}")
            except ffmpeg.Error as e:
                error_message = e.stderr.decode() if e.stderr else 'Unknown error'
                print(f"Error during conversion: {error_message}")

        else:
            print(f"File type not supported: {filename}")