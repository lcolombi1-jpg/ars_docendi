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

.block-container{
    max-width:100%;
    padding-top:0rem;
}

html{
    font-size:clamp(14px,1vw,18px);
}

.title{
    text-align:center;
    margin-top:20px;
}

.title h1{
    font-family:'Cinzel', serif;
    font-size:clamp(3rem,8vw,6rem);
    color:white;
    letter-spacing:10px;
    text-shadow: 0 0 10px #ff00ff, 0 0 40px #ff00ff;
    margin-bottom: 0;
}

.subtitle{
    color:#00f0ff;
    text-align:center;
    letter-spacing:8px;
    margin-bottom:50px;
    font-family: 'Montserrat', sans-serif;
    text-transform: uppercase;
}

/* --- STILE ARCATE PRINCIPALI --- */
.st-key-btn_discipulus button, 
.st-key-btn_gladiator button, 
.st-key-btn_imperator button {
    width: min(260px,28vw) !important;
    height: min(520px,60vh) !important;
    border-radius: 130px 130px 10px 10px !important;
    background: transparent !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    margin: 0 auto !important;
    font-family: 'Cinzel', serif !important;
    font-size: clamp(1rem,2vw,1.8rem) !important;
    letter-spacing: 1px !important;
    transition: all 0.4s ease;
    white-space: pre-wrap !important;
}

/* 1. DISCIPVLVS (CYAN) */
.st-key-btn_discipulus button {
    border: 4px solid #00f0ff !important;
    color: #00f0ff !important;
    box-shadow: 0 0 15px #00f0ff, 0 0 50px #00f0ff, 0 0 100px rgba(0,240,255,.5) !important;
}
.st-key-btn_discipulus button:hover {
    transform: scale(1.05);
    background-color: rgba(0, 240, 255, 0.1) !important;
}

/* 2. GLADIATOR (VIOLET) - SEMPRE NEON */
.st-key-btn_gladiator button {
    border: 4px solid #d64dff !important;
    color: #d64dff !important;
    box-shadow: 0 0 15px #d64dff, 0 0 50px #d64dff, 0 0 100px rgba(214,77,255,.5) !important;
}
.st-key-btn_gladiator button:hover:not(:disabled) {
    transform: scale(1.05);
    background-color: rgba(214, 77, 255, 0.1) !important;
}

/* 3. IMPERATOR (PINK) - SEMPRE NEON */
.st-key-btn_imperator button {
    border: 4px solid #ff0077 !important;
    color: #ff0077 !important;
    box-shadow: 0 0 15px #ff0077, 0 0 50px #ff0077, 0 0 100px rgba(255,0,119,.5) !important;
}
.st-key-btn_imperator button:hover:not(:disabled) {
    transform: scale(1.05);
    background-color: rgba(255, 0, 119, 0.1) !important;
}

/* ARCATE BLOCCATE - Cursore disabilitato e leggermente opache ma mantengono il neon! */
div.stButton > button:disabled {
    cursor: not-allowed !important;
    transform: none !important;
    opacity: 0.65 !important;
}

/* --- CENTRATURA ASSOLUTA BOTTONI RETTANGOLARI --- */
.st-key-ad_maiora_btn, 
.st-key-back_btn,
.st-key-back_map {
    display: flex !important;
    justify-content: center !important;
    width: 100% !important;
}

.st-key-ad_maiora_btn button, 
.st-key-back_btn button,
.st-key-submit_quiz button, 
.st-key-action_btn button, 
.st-key-action_btn_2 button, 
.st-key-back_map button {
    height: auto !important; 
    width: auto !important;
    padding: 8px 20px !important; 
    border-radius: 4px !important; 
    font-size: 1rem !important; 
    font-family: 'Cinzel', serif !important;
    color: #00f0ff !important; 
    border: 1px solid #00f0ff !important; 
    box-shadow: 0 0 10px rgba(0, 240, 255, 0.5) !important; 
    background: transparent !important;
    margin: 0 auto !important; 
    display: block !important;
    transition: all 0.3s ease;
}

.st-key-ad_maiora_btn button:hover, 
.st-key-back_btn button:hover,
.st-key-submit_quiz button:hover,
.st-key-back_map button:hover {
    background-color: rgba(0, 240, 255, 0.2) !important;
    box-shadow: 0 0 20px #00f0ff !important;
}

/* Testo del test stile pulito */
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

# ================================
# PAGINA: LOBBY
# ================================
if st.session_state.pagina_corrente == 'lobby':
    st.markdown('<div class="title"><h1>LVDVS</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">SCEGLI IL TUO DESTINO</div>', unsafe_allow_html=True)
    
    # Ad Maiora è ora inserito senza colonne, e il CSS lo centra perfettamente!
    if st.button("AD MAIORA", key="ad_maiora_btn"):
        st.session_state.pagina_corrente = 'archi'
        st.rerun()


# ================================
# PAGINA: ARCHI
# ================================
elif st.session_state.pagina_corrente == 'archi':
    st.markdown('<div class="title"><h1>LVDVS</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">SELEZIONA L\'ARENA</div>', unsafe_allow_html=True)

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
            # Bottone bloccato ma che ora ha il neon Viola
            st.button("GLADIATOR 🔒\n\nINTERMEDIATE", disabled=True, key="btn_gladiator")

    with col3:
        if st.session_state.imperator_sbloccato:
            if st.button("IMPERATOR\n\nPRO", key="btn_imperator"):
                st.session_state.pagina_corrente = 'test_imperator'
                st.rerun()
        else:
            # Bottone bloccato ma che ora ha il neon Rosa
            st.button("IMPERATOR 🔒\n\nPRO", disabled=True, key="btn_imperator")

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # Torna alla Lobby inserito senza colonne, centrato perfettamente dal CSS
    if st.button("Torna alla Lobby", key="back_btn"):
        st.session_state.pagina_corrente = 'lobby'
        st.rerun()


# ================================
# PAGINA: TEST DISCIPVLVS
# ================================
elif st.session_state.pagina_corrente == 'test_discipulus':
    st.markdown('<div class="title"><h1>DISCIPVLVS</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">PROVA DI AMMISSIONE AL GLADIATOR</div>', unsafe_allow_html=True)
    
    st.markdown("> *Rispondi correttamente ad almeno 8 domande su 10 per dimostrare il tuo valore e sbloccare l'arena dei Gladiatori.*")
    st.write("---")

    for q in DOMANDE_DISCIPULUS:
        st.markdown(f'<p class="quiz-question">Domanda {q["id"]}: {q["domanda"]}</p>', unsafe_allow_html=True)
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

    if not st.session_state.quiz_inviato:
        # Centriamo il bottone di consegna test usando lo stesso principio
        st.markdown("<div style='display: flex; justify-content: center; width: 100%;'>", unsafe_allow_html=True)
        if st.button("CONSEGNA IL TEST", key="submit_quiz"):
            if len(st.session_state.risposte_utente) < 10:
                st.warning("⚠️ Per favore, rispondi a tutte e 10 le domande prima di consegnare!")
            else:
                st.session_state.quiz_inviato = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
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
        
        col_res1, col_res2, _ = st.columns([1, 1, 2])
        with col_res1:
            if st.button("Torna alla Mappa", key="action_btn"):
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

    if not st.session_state.quiz_inviato:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Torna indietro", key="back_map"):
            st.session_state.pagina_corrente = 'archi'
            st.rerun()
