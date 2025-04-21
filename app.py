import streamlit as st
import random

st.title("Guessing Game")

# Initialise the secret number once
if "secret_number" not in st.session_state:
  st.session_state.secret_number = random.randint(1, 10)

guess = st.number_input("Guess a number between 1 and 10", min_value=1, max_value=10, step=1)

if st.button("Submit"):
  if guess == st.session_state.secret_number:
    st.sucess("You got it! Well done.")
    st.session_state.secret_number = random.randint(1,10) # Reset secret number
    st.info("A new number has been generated.")
elif guess < st.session_state.secret_number:
  st.warning("Too low. Try again.")
else: 
  st.warning("Too high. Try again.")
