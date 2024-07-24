import streamlit as st
from pytube import YouTube
import random
import os
from zipfile import ZipFile


emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"]
def random_emoji():
    st.session_state.emoji = random.choice(emojis)
    return st.session_state.emoji

def zip_csv(directory_name, zip_file_name, filter):
   # Create object of ZipFile
   with ZipFile(zip_file_name, 'w') as zip_object:
   # Traverse all files in directory
    for folder_name, sub_folders, file_names in os.walk(directory_name):
      for filename in file_names:
      # Filter for csv files
       if filter(filename):
         # Create filepath of files in directory
         file_path = os.path.join(folder_name, filename)
         # Add files to zip file
         zip_object.write(file_path, os.path.basename(file_path))

def clean_mp4(filter):
   for folder_name, sub_folders, file_names in os.walk('./'):
      for filename in file_names:
         if filter(filename):
            os.remove(filename)
with st.sidebar:
    choice= st.radio("Navigation",["Provide Url",'download'])
"""
# Youtube Video Downloader
"""
if choice == 'Provide Url':
    url = st.text_input('Please enter Video URL')
    st.write('Your entered URL', url)
    if url:
        video=YouTube(url)
        stream=video.streams.get_highest_resolution()
        st.write('downloading..please wait!',random_emoji())
        stream.download()
        zip_csv('./', './Zipped file.zip', lambda name: 'mp4' in name)
        st.write('Success!',random_emoji())

if choice == 'download':
    if os.path.exists('./Zipped file.zip'):
        with open("Zipped file.zip",'rb') as f:
            st.download_button('download_video',f,file_name="Zipped file.zip")
            clean_mp4(lambda name: 'mp4' in name)
            clean_mp4(lambda name: 'zip' in name)

    else:
       st.write('Go to provide Url button')