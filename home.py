import streamlit as st

st.title("LUDUS")

st.write("Test navigazione")

st.page_link(
    "pages/01_discipulus.py",
    label="DISCIPVLVS"
)

st.page_link(
    "pages/02_gladiator.py",
    label="GLADIATOR"
)

st.page_link(
    "pages/03_imperator.py",
    label="IMPERATOR"
)
