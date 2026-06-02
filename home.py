import streamlit as st

# --- 1. CONFIGURAZIONE (Deve essere la prima cosa) ---
st.set_page_config(
    page_title="LVDVS",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. INIZIALIZZAZIONE SESSION STATE ---
if 'pagina_corrente' not in st.session_state:
    st.session_state.pagina_corrente = 'lobby'
if 'gladiator_sbloccato' not in st.session_state:
    st.session_state.gladiator_sbloccato = False
if 'imperator_sbloccato' not in st.session_state:
    st.session_state.imperator_sbloccato = False

# --- 3. CSS ESSENZIALE (Senza rompere il layout) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Montserrat:wght@400&display=swap');

/* Sfondo e font generale */
.stApp {
    background: radial-gradient(circle at center, #19002f 0%, #0a0015 50%, #020004 100%);
    color: white;
}

/* Nascondi elementi inutili */
header, footer, .stDeployButton { visibility: hidden; }

/* Centratura Titoli */
.main-title {
    font-family: 'Cinzel', serif;
    font-size: 5rem;
    text-align: center;
    color: white;
    text-shadow: 0 0 20px #ff00ff;
    margin-top: 50px;
}
.main-subtitle {
    font-family: 'Montserrat', sans-serif;
    text-align: center;
    color: #00f0ff;
    letter-spacing: 5px;
    margin-bottom: 50px;
}

/* BOX DELLE ARCATE */
.arc-box {
    border-radius: 80px 80px 10px 10px;
    padding: 40px 20px;
    text-align: center;
    margin-bottom: 20px;
    min-height: 250px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background: rgba(255, 255, 255, 0.05);
}
.cyan-arc { border: 3px solid #00f0ff; box-shadow: 0 0 15px #00f0ff; color: #00f0ff; }
.violet-arc { border: 3px solid #d64dff; box-shadow: 0 0 15px #d64dff; color: #d64dff; }
.pink-arc { border: 3px solid #ff0077; box-shadow: 0 0 15px #ff0077; color: #ff0077; }
.locked-arc { border: 3px solid #333; color: #666; opacity: 0.5; }

.arc-title { font-family: 'Cinzel', serif; font-size: 1.5rem; }
.arc-sub { font-family: 'Montserrat', sans-serif; font-size: 0.7rem; letter-spacing: 2px; }

/* Centratura bottoni nativi */
div.stButton > button {
    display: block;
    margin: 0 auto;
}
</style>
""", unsafe_allow_html=True)

# --- 4. LOGICA DI NAVIGAZIONE ---
def vai_archi():
    st.session_state.pagina_corrente = 'archi'

def vai_lobby():
    st.session_state.pagina_corrente = 'lobby'

# --- 5. SCHERMATA: LOBBY ---
if st.session_state.pagina_corrente == 'lobby':
    st.markdown('<h1 class="main-title">LVDVS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="main-subtitle">Scegli il tuo destino</p>', unsafe_allow_html=True)
    
    st.button("AD MAIORA", on_click=vai_archi)

# --- 6. SCHERMATA: ARCHI ---
else:
    st.markdown('<h1 class="main-title" style="font-size: 3rem;">ARCHI DI GLORIA</h1>', unsafe_allow_html=True)
    
    # Tre colonne per le tre arcate
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="arc-box cyan-arc"><div class="arc-title">DISCIPVLVS</div><div class="arc-sub">BEGINNER</div></div>', unsafe_allow_html=True)
        # Importante: st.page_link DEVE puntare correttamente al file nella cartella pages
        st.page_link("pages/01_discipulus.py", label="INIZIA IL TEST", icon="🛡️")

    with col2:
        if st.session_state.get('gladiator_sbloccato', False):
            st.markdown('<div class="arc-box violet-arc"><div class="arc-title">GLADIATOR</div><div class="arc-sub">INTERMEDIATE</div></div>', unsafe_allow_html=True)
            st.page_link("pages/02_gladiator.py", label="INIZIA IL TEST", icon="⚔️")
        else:
            st.markdown('<div class="arc-box locked-arc"><div class="arc-title">GLADIATOR</div><div class="arc-sub">BLOCCATO 🔒</div></div>', unsafe_allow_html=True)

    with col3:
        if st.session_state.get('imperator_sbloccato', False):
            st.markdown('<div class="arc-box pink-arc"><div class="arc-title">IMPERATOR</div><div class="arc-sub">PRO</div></div>', unsafe_allow_html=True)
            st.page_link("pages/03_imperator.py", label="INIZIA IL TEST", icon="👑")
        else:
            st.markdown('<div class="arc-box locked-arc"><div class="arc-title">IMPERATOR</div><div class="arc-sub">BLOCCATO 🔒</div></div>', unsafe_allow_html=True)

    st.write("---")
    st.button("TORNA ALLA LOBBY", on_click=vai_lobby)
