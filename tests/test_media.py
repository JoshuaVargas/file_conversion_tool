import os
import pytest
from moviepy.editor import ColorClip
from pydub import AudioSegment
from src.media_converter import convert_media

@pytest.fixture
def setup_folders(tmpdir):
    # Create temporary directories for input and output
    input_folder = tmpdir.mkdir("input_media")
    output_folder = tmpdir.mkdir("output_media")
    return str(input_folder), str(output_folder)

@pytest.fixture
def create_test_media_files(setup_folders):
    input_folder, _ = setup_folders
    # Create a simple video
    video_file = os.path.join(input_folder, "test_video.mp4")
    clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)  # 5-second red video
    clip.write_videofile(video_file, fps=24)
    
    # Create a simple audio file
    audio_file = os.path.join(input_folder, "test_audio.mp3")
    # Generate a 5-second silent audio file for testing
    silent_audio = AudioSegment.silent(duration=5000)  # 5 seconds of silence
    silent_audio.export(audio_file, format="mp3")

def test_convert_audio_to_wav(setup_folders, create_test_media_files):
    input_folder, output_folder = setup_folders
    convert_media(input_folder, output_folder, 'wav')
    output_file = os.path.join(output_folder, 'test_audio.wav')
    assert os.path.isfile(output_file), f'WAV file was not created: {output_file}'

def test_convert_video_to_avi(setup_folders, create_test_media_files):
    input_folder, output_folder = setup_folders
    convert_media(input_folder, output_folder, 'avi')
    output_file = os.path.join(output_folder, 'test_video.avi')
    assert os.path.isfile(output_file), f'AVI file was not created: {output_file}'

def test_create_output_folder(setup_folders, create_test_media_files):
    input_folder, _ = setup_folders
    temp_output_folder = os.path.join(os.getcwd(), "temp_output_folder")
    
    # Ensure the folder does not exist
    if os.path.exists(temp_output_folder):
        # Remove all files and subdirectories first
        for root, dirs, files in os.walk(temp_output_folder, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(temp_output_folder)
    
    convert_media(input_folder, temp_output_folder, 'wav')
    
    assert os.path.exists(temp_output_folder), "Output folder was not created"
    
    # Clean up
    for root, dirs, files in os.walk(temp_output_folder, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(temp_output_folder)