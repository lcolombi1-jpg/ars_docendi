import streamlit as st

# --- 1. SETUP (Deve essere la prima riga) ---
st.set_page_config(
    page_title="LVDVS",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. FUNZIONI DI NAVIGAZIONE ---
def vai_ai_livelli():
    st.session_state.pagina_corrente = 'archi'

def torna_alla_lobby():
    st.session_state.pagina_corrente = 'lobby'

# --- 3. SESSION STATE (Persistente tra le pagine) ---
if 'pagina_corrente' not in st.session_state:
    st.session_state.pagina_corrente = 'lobby'
if 'gladiator_sbloccato' not in st.session_state:
    st.session_state.gladiator_sbloccato = False
if 'imperator_sbloccato' not in st.session_state:
    st.session_state.imperator_sbloccato = False

# --- 4. CSS OTTIMIZZATO ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

header, footer, .stDeployButton { visibility: hidden; }

.stApp {
    background: radial-gradient(circle at center, #19002f 0%, #0a0015 50%, #020004 100%);
}

.hero-container {
    text-align: center;
    padding-top: 5vh;
}

.hero-title {
    font-family: 'Cinzel', serif;
    font-size: clamp(3rem, 10vw, 6rem);
    color: white;
    letter-spacing: 12px;
    text-shadow: 0 0 20px #ff00ff;
    margin: 0;
}

.hero-subtitle {
    font-family: 'Montserrat', sans-serif;
    color: #00f0ff;
    letter-spacing: 6px;
    font-size: 1rem;
    text-transform: uppercase;
    margin-bottom: 20px;
}

/* Stile Archi (Solo visuale ora, senza <a>) */
.gate {
    width: 100%;
    height: 320px;
    border-radius: 100px 100px 10px 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: rgba(0, 0, 0, 0.4);
    margin-bottom: 15px;
}

.gate-title { font-family: 'Cinzel', serif; font-size: 1.2rem; margin-bottom: 5px;}
.gate-sub { font-family: 'Montserrat', sans-serif; font-size: 0.6rem; letter-spacing: 2px; color: rgba(255,255,255,0.6); }

.cyan { border: 3px solid #00f0ff; box-shadow: 0 0 15px #00f0ff; color: #00f0ff; }
.violet { border: 3px solid #d64dff; box-shadow: 0 0 15px #d64dff; color: #d64dff; }
.pink { border: 3px solid #ff0077; box-shadow: 0 0 15px #ff0077; color: #ff0077; }
.locked { border: 3px solid #333; opacity: 0.4; }

/* Centratura Bottoni Streamlit */
div.stButton, div.stPageLink {
    display: flex;
    justify-content: center;
    width: 100%;
}

/* Stile per i bottoni page_link (quelli sotto gli archi) */
[data-testid="stPageLink-NavLink"] {
    background-color: transparent !important;
    border: 1px solid #00f0ff !important;
    color: #00f0ff !important;
    font-family: 'Cinzel', serif !important;
    transition: all 0.3s ease !important;
}

[data-testid="stPageLink-NavLink"]:hover {
    background-color: rgba(0, 240, 255, 0.2) !important;
    box-shadow: 0 0 10px #00f0ff !important;
}
</style>
""", unsafe_allow_html=True)

# --- 5. LOGICA PAGINE ---

if st.session_state.pagina_corrente == 'lobby':
    st.markdown('<div class="hero-container"><h1 class="hero-title">LVDVS</h1><p class="hero-subtitle">Scegli il tuo destino</p></div>', unsafe_allow_html=True)
    st.button("AD MAIORA", on_click=vai_ai_livelli)

elif st.session_state.pagina_corrente == 'archi':
    st.markdown('<div class="hero-container"><h1 class="hero-title" style="font-size:3rem;">ARCHI DI GLORIA</h1></div>', unsafe_allow_html=True)
    
    # Usiamo le colonne di Streamlit per posizionare gli archi e i link
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="gate cyan"><div class="gate-title">DISCIPVLVS</div><div class="gate-sub">BEGINNER</div></div>', unsafe_allow_html=True)
        # IL SEGRETO: st.page_link mantiene la sessione attiva!
        st.page_link("pages/01_discipulus.py", label="ENTRA NEL TEST", icon="⚔️")

    with col2:
        if st.session_state.gladiator_sbloccato:
            st.markdown('<div class="gate violet"><div class="gate-title">GLADIATOR</div><div class="gate-sub">INTERMEDIATE</div></div>', unsafe_allow_html=True)
            st.page_link("pages/02_gladiator.py", label="ENTRA NEL TEST", icon="🛡️")
        else:
            st.markdown('<div class="gate locked"><div class="gate-title">GLADIATOR</div><div class="gate-sub">BLOCCATO 🔒</div></div>', unsafe_allow_html=True)

    with col3:
        if st.session_state.imperator_sbloccato:
            st.markdown('<div class="gate pink"><div class="gate-title">IMPERATOR</div><div class="gate-sub">PRO</div></div>', unsafe_allow_html=True)
            st.page_link("pages/03_imperator.py", label="ENTRA NEL TEST", icon="👑")
        else:
            st.markdown('<div class="gate locked"><div class="gate-title">IMPERATOR</div><div class="gate-sub">BLOCCATO 🔒</div></div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.button("TORNA ALLA LOBBY", on_click=torna_alla_lobby)
