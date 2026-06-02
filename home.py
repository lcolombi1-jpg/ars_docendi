import streamlit as st

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(
    page_title="LVDVS",
    page_icon="🏛️",
    layout="wide"
)

# --- 2. SESSION STATE ---
if 'pagina_corrente' not in st.session_state:
    st.session_state.pagina_corrente = 'lobby'
if 'gladiator_sbloccato' not in st.session_state:
    st.session_state.gladiator_sbloccato = False
if 'imperator_sbloccato' not in st.session_state:
    st.session_state.imperator_sbloccato = False

# --- 3. CSS "STRICT" PER CENTRATURA E DIMENSIONI ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

/* Rimuove spazi bianchi di Streamlit e blocca lo scroll */
header, footer, #MainMenu { visibility:hidden; }
.stApp {
    background: radial-gradient(circle at center, #19002f 0%, #0a0015 50%, #020004 100%);
    overflow: hidden;
}
.block-container { 
    max-width: 100%; 
    padding: 0 !important; 
    display: flex;
    justify-content: center;
}

/* CONTENITORE UNIVERSALE CENTRATO */
.viewport-center {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 90vh; /* Usa quasi tutta l'altezza ma non tutta per sicurezza */
    width: 100vw;
}

/* TITOLO E SOTTOTITOLO */
.title-box { text-align: center; margin-bottom: 20px; }
.title-box h1 {
    font-family: 'Cinzel', serif;
    font-size: clamp(3rem, 10vw, 6rem);
    color: white;
    letter-spacing: 15px;
    text-shadow: 0 0 20px #ff00ff;
    margin: 0;
}
.subtitle-box {
    color: #00f0ff;
    font-family: 'Montserrat', sans-serif;
    letter-spacing: 8px;
    font-size: 1rem;
    text-transform: uppercase;
    margin-top: 10px;
}

/* LE ARCATE - RIDOTTE PER STARE NELLO SCHERMO */
.gates-container { 
    display: flex; 
    justify-content: center; 
    align-items: center;
    gap: 30px; 
    flex-wrap: nowrap; /* Impedisce di andare a capo */
    margin-top: 30px;
}

.gate {
    width: 220px; /* Più strette */
    height: 380px; /* Più basse per non uscire dallo schermo */
    border-radius: 110px 110px 10px 10px;
    text-decoration: none !important;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    transition: all 0.4s ease;
}

.gate-title { font-family: 'Cinzel', serif; font-size: 1.2rem; color: inherit; }
.gate-sub { font-size: 0.7rem; letter-spacing: 3px; opacity: 0.6; color: white; margin-top: 10px; }

.cyan { border: 3px solid #00f0ff; box-shadow: 0 0 15px #00f0ff; color: #00f0ff !important; }
.violet { border: 3px solid #d64dff; box-shadow: 0 0 15px #d64dff; color: #d64dff !important; }
.pink { border: 3px solid #ff0077; box-shadow: 0 0 15px #ff0077; color: #ff0077 !important; }

.locked { border: 3px solid #333 !important; background: rgba(0,0,0,0.4); opacity: 0.5; cursor: not-allowed; }
.locked .gate-title { color: #555 !important; }

/* IL BOTTONE - CENTRATURA FORZATA */
[data-testid="stElementContainer"] {
    display: flex !important;
    justify-content: center !important;
}

div.stButton > button {
    font-family: 'Cinzel', serif;
    background: transparent;
    color: #00f0ff !important;
    border: 1px solid #00f0ff !important;
    padding: 10px 40px !important;
    letter-spacing: 4px !important;
    margin-top: 40px !important;
}
div.stButton > button:hover {
    background: rgba(0, 240, 255, 0.1) !important;
    box-shadow: 0 0 20px #00f0ff;
}
</style>
""", unsafe_allow_html=True)

# --- 4. LOGICA PAGINE ---

if st.session_state.pagina_corrente == 'lobby':
    # Tutto dentro un unico div centrato
    st.markdown("""
    <div class="viewport-center">
        <div class="title-box">
            <h1>LVDVS</h1>
            <div class="subtitle-box">Scegli il tuo destino</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.button("AD MAIORA", on_click=vai_ai_livelli)

elif st.session_state.pagina_corrente == 'archi':
    # Costruzione HTML per gli archi
    arc_1 = '<a class="gate cyan" href="./01_discipulus" target="_self"><div class="gate-title">DISCIPVLVS</div><div class="gate-sub">BEGINNER</div></a>'
    
    if st.session_state.gladiator_sbloccato:
        arc_2 = '<a class="gate violet" href="./02_gladiator" target="_self"><div class="gate-title">GLADIATOR</div><div class="gate-sub">INTERMEDIATE</div></a>'
    else:
        arc_2 = '<div class="gate locked"><div class="gate-title">GLADIATOR 🔒</div><div class="gate-sub">BLOCCATO</div></div>'
        
    if st.session_state.imperator_sbloccato:
        arc_3 = '<a class="gate pink" href="./03_imperator" target="_self"><div class="gate-title">IMPERATOR</div><div class="gate-sub">PRO</div></a>'
    else:
        arc_3 = '<div class="gate locked"><div class="gate-title">IMPERATOR 🔒</div><div class="gate-sub">BLOCCATO</div></div>'

    st.markdown(f"""
    <div class="viewport-center">
        <div class="title-box">
            <h1>LVDVS</h1>
        </div>
        <div class="gates-container">
            {arc_1}
            {arc_2}
            {arc_3}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.button("TORNA ALLA LOBBY", on_click=lambda: st.session_state.update(pagina_corrente='lobby'))
