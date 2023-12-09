import numpy as np
import streamlit as st

## streamlit

st.set_page_config(page_title="Bar Trajectory")

st.markdown("<h1 style='text-align: center; color: #FF4619;'> BAR TRAJECTORY </h1>", unsafe_allow_html=True)

#st.markdown(f"<p style='text-align: center;'><img src='####' alt='Centered Image'></p>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: left; color: #000000;'> Upload your video and let's take a look at the bar path on your movement. </h1>", unsafe_allow_html=True)
st.write("""
        The bar path is a great indicator of good technique and, as a consequence, optimal power transfer.
        
         It's a useful tool also for other movements / exercises such as: back or front squat, deadlift and bench press (among others).""")

video = st.file_uploader("")

st.video(video)