import streamlit as st

st.set_page_config(
    page_title="Ludus",
    page_icon="🏛️",
    layout="wide"
)

# --- 1. MEMORIA DEL GIOCO ---
if 'pagina_corrente' not in st.session_state:
    st.session_state.pagina_corrente = 'lobby'
if 'gladiator_sbloccato' not in st.session_state:
    st.session_state.gladiator_sbloccato = False
if 'imperator_sbloccato' not in st.session_state:
    st.session_state.imperator_sbloccato = False

def vai_ai_livelli():
    st.session_state.pagina_corrente = 'archi'

def vai_alla_lobby():
    st.session_state.pagina_corrente = 'lobby'

# --- 2. STILI CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

header, footer, #MainMenu { visibility:hidden; }

.stApp{
    background: radial-gradient(circle at center, #19002f 0%, #0a0015 50%, #020004 100%);
}

/* Stile per i bottoni-arco */
div.stButton > button {
    font-family: 'Cinzel', serif;
    background-color: transparent;
    color: #00f0ff;
    border: 4px solid #00f0ff !important;
    border-radius: 130px 130px 10px 10px !important; /* Forma ad arco */
    height: 400px !important;
    width: 220px !important;
    font-size: 1.5rem !important;
    letter-spacing: 2px !important;
    box-shadow: 0 0 20px #00f0ff;
    transition: all 0.4s ease;
    display: flex;
    flex-direction: column;
    justify-content: center;
    white-space: normal;
}

div.stButton > button:hover {
    transform: scale(1.05);
    background-color: rgba(0, 240, 255, 0.1) !important;
    box-shadow: 0 0 40px #00f0ff;
    color: white !important;
}

/* Colori diversi per i bottoni */
[data-testid="stBaseButton-secondary"] { /* Questo è il default se non cambi */ }

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

.centered-container {
    display: flex;
    justify-content: center;
    gap: 20px;
}
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DELLE PAGINE ---

# SCHERMATA: LOBBY
if st.session_state.pagina_corrente == 'lobby':
    st.markdown('<div class="title"><h1>LVDVS</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">SCEGLI IL TUO DESTINO</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("AD MAIORA", use_container_width=True):
            vai_ai_livelli()
            st.rerun()

# SCHERMATA: ARCHI (LIVELLI)
elif st.session_state.pagina_corrente == 'archi':
    st.markdown('<div class="title"><h1>LVDVS</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Scegli il tuo livello</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        # ARCO DISCIPVLVS
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

    st.write("")
    if st.button("Torna alla Lobby", key="back"):
        vai_alla_lobby()
        st.rerun()

# SCHERMATA: TEST DISCIPULUS
elif st.session_state.pagina_corrente == 'test_discipulus':
    st.markdown('<div class="title"><h1>DISCIPVLVS</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">IL TEST HA INIZIO</div>', unsafe_allow_html=True)
    
    st.info("Benvenuto, giovane allievo. Rispondi correttamente alle domande per sbloccare il livello Gladiator.")
    
    # Esempio di logica per sbloccare il prossimo livello
    if st.button("Completa Test (Simulazione)"):
        st.session_state.gladiator_sbloccato = True
        st.success("Complimenti! Hai sbloccato il grado di GLADIATOR!")
        if st.button("Torna ai livelli"):
            st.session_state.pagina_corrente = 'archi'
            st.rerun()
    
    if st.button("Abbandona"):
        st.session_state.pagina_corrente = 'archi'
        st.rerun()
