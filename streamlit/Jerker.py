import streamlit as st

st.set_page_config(page_title="Jerker", page_icon = '🏋🏻‍♂️')

navigation_menu = """
    <style>
        .menu-container {
            display: flex;
            justify-content: space-around;
            padding: 1em;
            background-color: #ffffff;
        }
        .menu-item {
            cursor: pointer;
        }
    </style>
    <div class="menu-container">
        <div <a href="http://localhost:8501">The Jerker<a/></div>
        <div <a href="http://192.168.0.25:8501/Bar_Trajectory">Bar Trajectory<a/></div>
        <div <a href="http://localhost:8501/Triple_Extension_Checker">Triple Extension<a/></div>
        <div <a href="http://localhost:8501/Bar_Trajectory">NO Half Reps!<a/></div>
        <div <a href="http://localhost:8501/Rep_Max_Calculator">1-Rep Max Calculator<a/></div>
    </div>
"""

st.markdown(navigation_menu, unsafe_allow_html=True)

### TITLE
st.markdown("<h1 style='text-align: center; color: #FF4619'> THE JERKER </h1>", unsafe_allow_html=True)

### IMAGE
st.markdown(f"<p style='text-align: center;'><img src='https://www.shutterstock.com/image-vector/black-white-illustration-barbell-isolated-600nw-1291006585.jpg' alt='Centered Image'></p>", unsafe_allow_html=True)

# jerker meaning
st.markdown("<p style='text-align: center;'><b>noun;</b> someone who gives a strong sudden pull; someone who applies force so as to cause motion toward herself or himself.</p>", unsafe_allow_html=True)

### ABOUT THE PROJECT
st.markdown("<h2 style='text-align: center; color: #000000;'> ABOUT THE PROJECT</h1>", unsafe_allow_html=True)

# about
st.markdown("<p style='text-align: center;'>Web APP focused on Olympic Weightlifting with the goal of optimizing technique efficiency by analyzing it's indicators using unsupervised Machine Learning models.</p>", unsafe_allow_html=True)

## what why how
st.markdown("<h3 style='text-align: center; color: #000000;'> WHY? HOW?</h1>", unsafe_allow_html=True)

# what why how
st.markdown("""
            <p style='text-align: center;'> The main reason to do this is because I love the sport of Olympic Weightlifting and decided that was the perfect subject to work on for my final project in <b> Ironhack's Data Analytics Bootcamp </b> </p>
            
            <p style='text-align: center;'> The main objective was to draw the bar trajectory, or bar path, and the triple extension to analyzing technique's efficiency and if there is any technique specific work to do.</p>
            
            <p style='text-align: center;'> Used open-source frameworks: <b>YOLOv8</b> for object detection and tracking and <b>MediaPipe</b> for pose estimations and recognition.</p>""", unsafe_allow_html=True)

## future improvements
st.markdown("<h3 style='text-align: center; color: #000000;'> FUTURE IMPROVMENTS </h1>", unsafe_allow_html=True)

# improvements
st.markdown("""
            <p style='text-align: center;'> Train my own models to identify with more accuracy the barbell plates on YOLO. On MediaPipe as well, even though it worked fine in the majority of the videos, depending on the angle which was recorded and the video quality.</b> </p>
            
            <p style='text-align: center;'> In Streamlit, when the user upload the video as an input, run the function on the video and get as an output the video with bar path analysis or extension checker.</p>""", unsafe_allow_html=True)


st.markdown("<h3 style='text-align: center; color: #000000;'> CONTACTS </h1>", unsafe_allow_html=True)

navigation_menu = """
    <style>
        .menu-container {
            display: flex;
            justify-content: space-around;
            padding: 1em;
            background-color: #ffffff;
        }
        .menu-item {
            cursor: pointer;
        }
    </style>
    <div class="menu-container">
        <div <a href="http://localhost:8501">tapmateus@gmail.com<a/></div>
        <div <a href="http://192.168.0.25:8501/Bar_Trajectory">LinkedIn<a/></div>
        <div <a href="http://localhost:8501/Triple_Extension_Checker">GitHub<a/></div>
    </div>
"""

st.markdown(navigation_menu, unsafe_allow_html=True)



