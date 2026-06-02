import streamlit as st

# --- 1. CONFIGURAZIONE PAGINA ---
st.set_page_config(
    page_title="LVDVS",
    page_icon="🏛️",
    layout="wide"
)

# --- 2. INIZIALIZZAZIONE MEMORIA (Session State) ---
if 'pagina_corrente' not in st.session_state:
    st.session_state.pagina_corrente = 'lobby'
if 'gladiator_sbloccato' not in st.session_state:
    st.session_state.gladiator_sbloccato = False
if 'imperator_sbloccato' not in st.session_state:
    st.session_state.imperator_sbloccato = False

def vai_ai_livelli():
    st.session_state.pagina_corrente = 'archi'

def torna_home():
    st.session_state.pagina_corrente = 'lobby'

# --- 3. CSS COMPLETO E OTTIMIZZATO ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

/* Nasconde menu e footer */
header, footer, #MainMenu { visibility:hidden; }

.stApp {
    background: radial-gradient(circle at center, #19002f 0%, #0a0015 50%, #020004 100%);
}

.block-container { max-width:100%; padding-top:2rem; }

/* CONTENITORE LOBBY CENTRATA */
.main-lobby {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    margin-top: 10vh;
}

.title h1 {
    font-family: 'Cinzel', serif;
    font-size: clamp(4rem, 12vw, 8rem);
    color: white;
    letter-spacing: 15px;
    text-shadow: 0 0 10px #ff00ff, 0 0 40px #ff00ff;
    margin-bottom: 0px;
}

.subtitle {
    color: #00f0ff;
    font-family: 'Montserrat', sans-serif;
    letter-spacing: 8px;
    font-size: clamp(1rem, 2vw, 1.5rem);
    margin-bottom: 50px;
    text-transform: uppercase;
}

/* ARCHI (PAGINA LIVELLI) */
.gates { 
    display: flex; 
    justify-content: center; 
    gap: 40px; 
    flex-wrap: wrap;
    padding: 20px;
}

.gate {
    width: 260px;
    height: 480px;
    border-radius: 130px 130px 10px 10px;
    text-decoration: none !important;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    transition: all 0.4s ease;
}

.gate-title {
    font-family: 'Cinzel', serif;
    font-size: 1.5rem;
    letter-spacing: 1px;
    text-align: center;
}

.gate-sub {
    margin-top: 16px;
    font-size: 0.8rem;
    letter-spacing: 4px;
    color: rgba(255,255,255,0.4);
}

.cyan { border: 4px solid #00f0ff; box-shadow: 0 0 20px #00f0ff; color: #00f0ff !important; }
.violet { border: 4px solid #d64dff; box-shadow: 0 0 20px #d64dff; color: #d64dff !important; }
.pink { border: 4px solid #ff0077; box-shadow: 0 0 20px #ff0077; color: #ff0077 !important; }

.gate:hover:not(.locked) { transform: scale(1.05); filter: brightness(1.2); }

.locked {
    border: 4px solid #333 !important;
    background: rgba(0,0,0,0.4);
    cursor: not-allowed;
    opacity: 0.6;
}
.locked .gate-title, .locked .gate-sub { color: #666 !important; }

/* FIX CENTRATURA BOTTONE STREAMLIT */
[data-testid="stElementContainer"] {
    display: flex;
    justify-content: center;
    width: 100% !important;
}

div.stButton > button {
    font-family: 'Cinzel', serif;
    background-color: transparent;
    color: #00f0ff !important;
    border: 1px solid #00f0ff !important;
    padding: 12px 35px !important;
    font-size: 1.2rem !important;
    letter-spacing: 4px !important;
    box-shadow: 0 0 10px #00f0ff;
    transition: all 0.3s ease;
    border-radius: 4px;
    width: auto !important;
    margin-top: 20px;
}

div.stButton > button:hover {
    background-color: #00f0ff !important;
    color: #0a0015 !important;
    box-shadow: 0 0 25px #00f0ff;
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# --- 4. LOGICA DI NAVIGAZIONE ---

# --- PAGINA: LOBBY ---
if st.session_state.pagina_corrente == 'lobby':
    st.markdown("""
    <div class="main-lobby">
        <div class="title"><h1>LVDVS</h1></div>
        <div class="subtitle">Scegli il tuo destino</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Il bottone apparirà centrato e piccolo grazie al CSS sopra
    st.button("AD MAIORA", on_click=vai_ai_livelli)

# --- PAGINA: ARCHI (SCELTA LIVELLO) ---
elif st.session_state.pagina_corrente == 'archi':
    st.markdown('<div class="title" style="margin-bottom:40px;"><h1>LVDVS</h1></div>', unsafe_allow_html=True)
    
    # Costruzione dinamica degli archi
    html_archi = '<div class="gates">'
    
    # 1. DISCIPVLVS (Sempre Sbloccato)
    html_archi += """
    <a class="gate cyan" href="./01_discipulus" target="_self">
        <div class="gate-title">DISCIPVLVS</div>
        <div class="gate-sub">BEGINNER</div>
    </a>"""
    
    # 2. GLADIATOR
    if st.session_state.gladiator_sbloccato:
        html_archi += """
        <a class="gate violet" href="./02_gladiator" target="_self">
            <div class="gate-title">GLADIATOR</div>
            <div class="gate-sub">INTERMEDIATE</div>
        </a>"""
    else:
        html_archi += """
        <div class="gate locked">
            <div class="gate-title">GLADIATOR 🔒</div>
            <div class="gate-sub">BLOCCATO</div>
        </div>"""
        
    # 3. IMPERATOR
    if st.session_state.imperator_sbloccato:
        html_archi += """
        <a class="gate pink" href="./03_imperator" target="_self">
            <div class="gate-title">IMPERATOR</div>
            <div class="gate-sub">PRO</div>
        </a>"""
    else:
        html_archi += """
        <div class="gate locked">
            <div class="gate-title">IMPERATOR 🔒</div>
            <div class="gate-sub">BLOCCATO</div>
        </div>"""
        
    html_archi += '</div>'
    
    st.markdown(html_archi, unsafe_allow_html=True)
    
    # Pulsante per tornare indietro (opzionale)
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.button("TORNA ALLA LOBBY", on_click=torna_home)
