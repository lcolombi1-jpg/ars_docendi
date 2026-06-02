import streamlit as st

st.set_page_config(
    page_title="Discipulus",
    page_icon="🏛️",
    layout="wide"
)

st.title("DISCIPVLVS")

st.write("Quiz livello Beginner")

domanda = st.radio(
    "Traduci 'puella'",
    ["ragazza", "guerra", "cavallo"]
)

if st.button("Verifica"):

    if domanda == "ragazza":
        st.success("Corretto!")
    else:
        st.error("Riprova")
