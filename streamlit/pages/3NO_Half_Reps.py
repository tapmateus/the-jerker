import numpy as np
import streamlit as st

#############

st.set_page_config(page_title="NO Half Reps!")

st.markdown("<h1 style='text-align: center; color: #FF4619;'> NO Half Reps! </h1>", unsafe_allow_html=True)

st.subheader("Turn your camera on and let's see if your squat is as deep as it should. Make your butt kiss the floor!")

st.write("Criteria to score a rep - good, deep squat - is to 'break the parrelel', so, to have angle on your knees below 90 degrees.")

tab1 = st.tabs(['Camera'])
st.camera_input("")

st.video("reps.mp4")