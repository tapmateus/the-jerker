## IMPORT LIBRARIES ##

import streamlit as st

## 1REP MAX CALCULATOR ##

def rep_max_calculator(weight, reps): 
    percentages = [1, 0.97, 0.94, 0.92, 0.89, 0.86, 0.83, 0.81, 0.78, 0.75, 0.73, 0.71, 0.70, 0.68, 0.67]
    return weight / percentages[reps-1]

## STREAMLIT CONFIGS, INPUTS AND OUTPUT ##

st.markdown("<h1 style='text-align: center; color: #FF4619'> 1-Rep Max Calculator </h1>", unsafe_allow_html=True)

st.write("""
         The reps considered have to be at maximum effort. That means that the RPE is 10 or close to. 
         
         RPE - Rate of Percieved Exertion - measures the difficulty of the exercise.""")

movement = st.selectbox("Which movement?", ["Snatch", "Clean", "Jerk", "Back Squat", "Front Squat"])

col1, col2 = st.columns(2)
units = col1.radio("Units", ["Kgs", "Lbs"])

reps = col2.slider("Number of reps:", 1, 15)

if units == 'Kgs':
    weight = st.slider("Weight lifted:", 0, 200)
else:
    weight = st.slider("Weight lifted:", 0, 400)


tab1 = st.tabs(['Estimation'])
st.write(f"Your estimated 1 Rep Max for {movement} is {round(rep_max_calculator(weight, reps), 2)} {units}.")