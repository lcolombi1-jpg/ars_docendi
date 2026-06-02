import streamlit as st

# ==================================================
# CONFIGURAZIONE PAGINA
# ==================================================

st.set_page_config(
    page_title="DISCIPVLVS",
    page_icon="🏛️",
    layout="wide"
)

# ==================================================
# SESSION STATE
# ==================================================

if "gladiator_unlocked" not in st.session_state:
    st.session_state.gladiator_unlocked = False

# ==================================================
# TITOLO
# ==================================================

st.title("DISCIPVLVS")
st.caption("Initium Sapientiae")

st.markdown("---")

# ==================================================
# DOMANDE
# ==================================================

domande = [

    {
        "domanda": "DOMANDA 1",
        "opzioni": [
            "Risposta A",
            "Risposta B",
            "Risposta C",
            "Risposta D"
        ],
        "corretta": "Risposta A"
    },

    {
        "domanda": "DOMANDA 2",
        "opzioni": [
            "Risposta A",
            "Risposta B",
            "Risposta C",
            "Risposta D"
        ],
        "corretta": "Risposta B"
    },

    {
        "domanda": "DOMANDA 3",
        "opzioni": [
            "Risposta A",
            "Risposta B",
            "Risposta C",
            "Risposta D"
        ],
        "corretta": "Risposta C"
    },

    {
        "domanda": "DOMANDA 4",
        "opzioni": [
            "Risposta A",
            "Risposta B",
            "Risposta C",
            "Risposta D"
        ],
        "corretta": "Risposta D"
    },

    {
        "domanda": "DOMANDA 5",
        "opzioni": [
            "Risposta A",
            "Risposta B",
            "Risposta C",
            "Risposta D"
        ],
        "corretta": "Risposta A"
    },

    {
        "domanda": "DOMANDA 6",
        "opzioni": [
            "Risposta A",
            "Risposta B",
            "Risposta C",
            "Risposta D"
        ],
        "corretta": "Risposta B"
    },

    {
        "domanda": "DOMANDA 7",
        "opzioni": [
            "Risposta A",
            "Risposta B",
            "Risposta C",
            "Risposta D"
        ],
        "corretta": "Risposta C"
    },

    {
        "domanda": "DOMANDA 8",
        "opzioni": [
            "Risposta A",
            "Risposta B",
            "Risposta C",
            "Risposta D"
        ],
        "corretta": "Risposta D"
    },

    {
        "domanda": "DOMANDA 9",
        "opzioni": [
            "Risposta A",
            "Risposta B",
            "Risposta C",
            "Risposta D"
        ],
        "corretta": "Risposta A"
    },

    {
        "domanda": "DOMANDA 10",
        "opzioni": [
            "Risposta A",
            "Risposta B",
            "Risposta C",
            "Risposta D"
        ],
        "corretta": "Risposta B"
    }

]

# ==================================================
# QUIZ
# ==================================================

risposte_utente = []

for i, domanda in enumerate(domande):

    risposta = st.radio(
        f"{i+1}. {domanda['domanda']}",
        domanda["opzioni"],
        key=f"q_{i}"
    )

    risposte_utente.append(risposta)

# ==================================================
# CORREZIONE
# ==================================================

st.markdown("---")

if st.button("CONSEGNA IL TEST"):

    punteggio = 0

    for risposta, domanda in zip(risposte_utente, domande):

        if risposta == domanda["corretta"]:
            punteggio += 1

    percentuale = punteggio * 10

    st.subheader("RISULTATO")

    st.write(f"**Punteggio:** {punteggio}/10")
    st.write(f"**Percentuale:** {percentuale}%")

    if punteggio >= 8:

        st.balloons()

        st.success(
            "Complimenti! Hai superato il livello DISCIPVLVS."
        )

        st.success(
            "Il livello GLADIATOR è stato sbloccato."
        )

        st.session_state.gladiator_unlocked = True

    else:

        st.error(
            "Non hai raggiunto la soglia minima di 8/10."
        )

        st.info(
            "Ripassa e riprova il test."
        )
