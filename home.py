import streamlit as st

st.set_page_config(
    page_title="Ludus",
    page_icon="🏛️",
    layout="wide"
)

# --- 1. MEMORIA DEL GIOCO (SESSION STATE) ---
if 'pagina_corrente' not in st.session_state:
    st.session_state.pagina_corrente = 'lobby'
if 'gladiator_sbloccato' not in st.session_state:
    st.session_state.gladiator_sbloccato = False
if 'imperator_sbloccato' not in st.session_state:
    st.session_state.imperator_sbloccato = False

# Strutture dati per il Quiz di Discipulus
if 'risposte_utente' not in st.session_state:
    st.session_state.risposte_utente = {}
if 'quiz_inviato' not in st.session_state:
    st.session_state.quiz_inviato = False

# --- DOMANDE DEL TEST DISCIPVLVS ---
DOMANDE_DISCIPULUS = [
    {"id": 1, "domanda": "Chi fu il primo imperatore romano?", "opzioni": ["Giulio Cesare", "Augusto", "Nerone", "Romolo"], "corretta": "Augusto"},
    {"id": 2, "domanda": "In quale anno fu fondata Roma secondo la tradizione?", "opzioni": ["753 a.C.", "509 a.C.", "476 d.C.", "27 a.C."], "corretta": "753 a.C."},
    {"id": 3, "domanda": "Quale fiume attraversa la città di Roma?", "opzioni": ["Po", "Arno", "Tevere", "Rubicone"], "corretta": "Tevere"},
    {"id": 4, "domanda": "Come si chiamava l'anfiteatro più famoso di Roma?", "opzioni": ["Circo Massimo", "Pantheon", "Colosseo", "Foro Romano"], "corretta": "Colosseo"},
    {"id": 5, "domanda": "Quale divinità romana corrisponde alla greca Atena?", "opzioni": ["Venere", "Minerva", "Giunone", "Diana"], "corretta": "Minerva"},
    {"id": 6, "domanda": "Chi vinse le guerre puniche?", "opzioni": ["Cartagine", "I Galli", "Roma", "I Greci"], "corretta": "Roma"},
    {"id": 7, "domanda": "Cosa significava la sigla S.P.Q.R.?", "opzioni": ["Senatus Populusque Romanus", "Salus Populi Romani", "Soli Populo Que Romano", "Spazio Pubblico Quotidiano Romano"], "corretta": "Senatus Populusque Romanus"},
    {"id": 8, "domanda": "Quale famoso generale pronunciò la frase 'Alea iacta est'?", "opzioni": ["Marco Antonio", "Giulio Cesare", "Scipione l'Africano", "Silla"], "corretta": "Giulio Cesare"},
    {"id": 9, "domanda": "Chi erano i soldati scelti che proteggevano l'imperatore?", "opzioni": ["Gladiatori", "Pretoriani", "Centurioni", "Legionari"], "corretta": "Pretoriani"},
    {"id": 10, "domanda": "In quanti colli principali sorgeva l'antica Roma?", "opzioni": ["3", "5", "7", "9"], "corretta": "7"}
]

# --- 2. STILI CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

header, footer, #MainMenu { visibility:hidden; }

.stApp{
    background: radial-gradient(circle at center, #19002f 0%, #0a0015 50%, #020004 100%);
}

.title h1{
    font-family:'Cinzel', serif;
    font-size:clamp(3rem,8vw,6rem);
    color:white;
    text-align:center;
    letter-spacing:10px;
    text-shadow: 0 0 10px #ff00ff, 0 0 40px #ff00ff;
}

.subtitle{
    color:#00f0ff;
    text-align:center;
    font-family: 'Montserrat', sans-serif;
    letter-spacing:8px;
    margin-bottom:50px;
    text-transform: uppercase;
}

/* Stile per i bottoni ad ARCO */
div.stButton > button {
    font-family: 'Cinzel', serif;
    background-color: transparent;
    border-radius: 130px 130px 10px 10px !important;
    height: 420px !important;
    width: 100% !important;
    font-size: 1.4rem !important;
    letter-spacing: 2px !important;
    transition: all 0.4s ease;
    display: flex;
    flex-direction: column;
    justify-content: center;
    white-space: normal;
}

/* Colori degli Archi */
.st-key-btn_discipulus button { color: #00f0ff !important; border: 4px solid #00f0ff !important; box-shadow: 0 0 20px #00f0ff; }
.st-key-btn_discipulus button:hover { box-shadow: 0 0 40px #00f0ff; background-color: rgba(0, 240, 255, 0.1) !important; }

.st-key-btn_gladiator button { color: #d64dff !important; border: 4px solid #d64dff !important; box-shadow: 0 0 20px #d64dff; }
.st-key-btn_gladiator button:hover { box-shadow: 0 0 40px #d64dff; background-color: rgba(214, 77, 255, 0.1) !important; }

.st-key-btn_imperator button { color: #ff0077 !important; border: 4px solid #ff0077 !important; box-shadow: 0 0 20px #ff0077; }
.st-key-btn_imperator button:hover { box-shadow: 0 0 40px #ff0077; background-color: rgba(255, 0, 119, 0.1) !important; }

/* Ad Maiora e bottoni normali del quiz */
.st-key-ad_maiora_btn button, .st-key-submit_quiz button, .st-key-action_btn button {
    height: auto !important; border-radius: 10px !important; padding: 15px 40px !important; font-size: 1.5rem !important;
    color: #00f0ff !important; border: 2px solid #00f0ff !important; box-shadow: 0 0 15px #00f0ff; margin: 0 auto !important;
}

.st-key-back button { height: auto !important; border-radius: 5px !important; width: auto !important; }

/* Testo delle domande stile romano neon */
.quiz-question {
    font-family: 'Montserrat', sans-serif;
    color: #ffffff;
    font-size: 1.2rem;
    margin-top: 20px;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DELLE PAGINE ---

# PAGINA: LOBBY
if st.session_state.pagina_corrente == 'lobby':
    st.markdown('<div class="title"><h1>LVDVS</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">SCEGLI IL TUO DESTINO</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if st.button("AD MAIORA", key="ad_maiora_btn", use_container_width=True):
            st.session_state.pagina_corrente = 'archi'
            st.rerun()

# PAGINA: ARCHI
elif st.session_state.pagina_corrente == 'archi':
    st.markdown('<div class="title"><h1>LVDVS</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Scegli il tuo livello</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("DISCIPVLVS\n\nBEGINNER", key="btn_discipulus"):
            st.session_state.pagina_corrente = 'test_discipulus'
            st.rerun()

    with col2:
        if st.session_state.gladiator_sbloccato:
            if st.button("GLADIATOR\n\nINTERMEDIATE", key="btn_gladiator"):
                st.session_state.pagina_corrente = 'test_gladiator'
                st.rerun()
        else:
            st.button("GLADIATOR\n\n🔒 BLOCCATO", disabled=True, key="lock1")

    with col3:
        if st.session_state.imperator_sbloccato:
            if st.button("IMPERATOR\n\nPRO", key="btn_imperator"):
                st.session_state.pagina_corrente = 'test_imperator'
                st.rerun()
        else:
            st.button("IMPERATOR\n\n🔒 BLOCCATO", disabled=True, key="lock2")

    st.markdown("<br><br>", unsafe_allow_html=True)
    _, col_back, _ = st.columns([2, 1, 2])
    with col_back:
        if st.button("Torna alla Lobby", key="back", use_container_width=True):
            st.session_state.pagina_corrente = 'lobby'
            st.rerun()

# PAGINA: VERO TEST DISCIPVLVS (QUIZ ALLIEVO)
elif st.session_state.pagina_corrente == 'test_discipulus':
    st.markdown('<div class="title"><h1>DISCIPVLVS</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">PROVA DI AMMISSIONE AL GLADIATOR</div>', unsafe_allow_html=True)
    
    st.markdown("> *Rispondi correttamente ad almeno 8 domande su 10 per dimostrare il tuo valore e sbloccare l'arena dei Gladiatori.*")
    st.write("---")

    # Mostriamo le domande
    for q in DOMANDE_DISCIPULUS:
        st.markdown(f'<p class="quiz-question">Domanda {q["id"]}: {q["domanda"]}</p>', unsafe_allow_html=True)
        
        # Gestiamo l'indice di default per non pre-selezionare la risposta corretta
        opzioni_con_default = ["Seleziona una risposta..."] + q["opzioni"]
        
        scelta = st.radio(
            f"Opzioni per domanda {q['id']}", 
            opzioni_con_default, 
            key=f"q_{q['id']}", 
            label_visibility="collapsed",
            disabled=st.session_state.quiz_inviato
        )
        if scelta != "Seleziona una risposta...":
            st.session_state.risposte_utente[q["id"]] = scelta

    st.write("---")

    # Calcolo dei Risultati
    if not st.session_state.quiz_inviato:
        if st.button("CONSEGNA IL TEST", key="submit_quiz"):
            # Controlliamo che l'utente abbia risposto a tutto
            if len(st.session_state.risposte_utente) < 10:
                st.warning("⚠️ Per favore, rispondi a tutte e 10 le domande prima di consegnare!")
            else:
                st.session_state.quiz_inviato = True
                st.rerun()
    else:
        # Correzione del Quiz
        punteggio = 0
        for q in DOMANDE_DISCIPULUS:
            if st.session_state.risposte_utente.get(q["id"]) == q["corretta"]:
                punteggio += 1
        
        st.subheader(f"Risultato: {punteggio} / 10 risposte corrette")
        
        if punteggio >= 8:
            st.success("🎉 ECCELLENTE! Hai dimostrato di avere la stoffa del guerriero. Il grado GLADIATOR è sbloccato!")
            st.session_state.gladiator_sbloccato = True
        else:
            st.error("❌ Non hai raggiunto il punteggio minimo (8/10). Studia ancora le antiche pergamene e riprova!")
        
        # Bottoni di uscita dopo aver visto il risultato
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            if st.button("Torna alla Mappa", key="action_btn"):
                # Resettiamo lo stato del quiz per poterlo rifare se si ha fallito
                st.session_state.quiz_inviato = False
                st.session_state.risposte_utente = {}
                st.session_state.pagina_corrente = 'archi'
                st.rerun()
        with col_res2:
            if not st.session_state.gladiator_sbloccato:
                if st.button("Riprova il Test", key="action_btn_2"):
                    st.session_state.quiz_inviato = False
                    st.session_state.risposte_utente = {}
                    st.rerun()

    # Bottone per uscire senza consegnare
    if tyrannical_condition := (not st.session_state.quiz_inviato):
        if st.button("Abbandona il Test e torna alla mappa", key="back_map"):
            st.session_state.pagina_corrente = 'archi'
            st.rerun()
