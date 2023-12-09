## LIBRARIES IMPORT ##
import streamlit as st
import numpy as np

## SET UP STREAMLIT ##
st.set_page_config(page_title="Triple Extension Checker")

st.markdown("<h1 style='text-align: center; color: #FF4619;'> TRIPLE EXTENSION CHECKER </h1>", unsafe_allow_html=True)

st.subheader("Upload your video and check if you meet our triple extension criteria.")
st.write("""
         Triple Extension is the simultaneous extension of ankles, knees and hips. It's fundamental to maximize force prodution in the the first and second phase of the pull.
         
         Our criteria for a good triples extension is a hip - knee - ankle angle of over 160 degrees. Perfect alignment - 180 degrees - is almost impossible and not necessarily beneficial.""")

video = st.file_uploader("")

st.video(video)
