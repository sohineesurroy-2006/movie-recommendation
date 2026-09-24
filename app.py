import streamlit as st
import joblib
import random

model = joblib.load("model.pkl")

movie_library = {
    "Action": [
        "John Wick",
        "Mad Max",
        "Avengers",
        "Mission Impossible",
        "The Dark Knight"
    ],

    "Comedy": [
        "The Hangover",
        "Jumanji",
        "Free Guy",
        "Home Alone",
        "Yes Man"
    ],

    "Drama": [
        "The Shawshank Redemption",
        "The Godfather",
        "Forrest Gump",
        "Oppenheimer",
        "A Beautiful Mind"
    ],

    "Action Comedy": [
        "Deadpool",
        "Rush Hour",
        "Guardians of the Galaxy",
        "Men in Black",
        "21 Jump Street"
    ]
}

st.title("ðŸŽ¬ Movie Genre Recommendation")

age = st.slider("Age", 10, 70, 22)

action = st.checkbox("I Like Action Movies")

comedy = st.checkbox("I Like Comedy Movies")

if st.button("Recommend Movies"):

    prediction = model.predict([[age, int(action), int(comedy)]])[0]

    st.success(f"Recommended Genre : {prediction}")

    st.subheader("Movies You Should Watch")

    for movie in random.sample(movie_library[prediction], 3):
        st.write("ðŸŽ¥", movie)