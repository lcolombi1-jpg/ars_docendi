import streamlit as st

# --- 1. CONFIGURAZIONE PAGINA (Deve essere la prima istruzione) ---
st.set_page_config(
    page_title="LVDVS",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. FUNZIONI DI NAVIGAZIONE (Definite prima dell'uso) ---
def vai_ai_livelli():
    st.session_state.pagina_corrente = 'archi'

def torna_alla_lobby():
    st.session_state.pagina_corrente = 'lobby'

# --- 3. INIZIALIZZAZIONE SESSION STATE ---
if 'pagina_corrente' not in st.session_state:
    st.session_state.pagina_corrente = 'lobby'
if 'gladiator_sbloccato' not in st.session_state:
    st.session_state.gladiator_sbloccato = False
if 'imperator_sbloccato' not in st.session_state:
    st.session_state.imperator_sbloccato = False

# --- 4. CSS TOTALE (Layout, Centratura e Archi) ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

/* Nasconde elementi superflui */
header, footer, #MainMenu { visibility:hidden; }

/* Sfondo e Overflow */
.stApp {
    background: radial-gradient(circle at center, #19002f 0%, #0a0015 50%, #020004 100%);
    overflow: hidden;
}

/* Contenitore principale Streamlit */
.block-container {
    padding: 0 !important;
    max-width: 100%;
}

/* Wrapper per centrare tutto verticalmente */
.page-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 85vh;
    text-align: center;
    width: 100%;
}

/* Titolo e Sottotitolo */
.hero-title {
    font-family: 'Cinzel', serif;
    font-size: clamp(3.5rem, 12vw, 7.5rem);
    color: white;
    letter-spacing: 12px;
    text-shadow: 0 0 15px #ff00ff, 0 0 40px #ff00ff;
    margin: 0;
}

.hero-subtitle {
    color: #00f0ff;
    font-family: 'Montserrat', sans-serif;
    letter-spacing: 6px;
    font-size: clamp(0.8rem, 2vw, 1.2rem);
    text-transform: uppercase;
    margin-bottom: 30px;
}

/* Griglia delle Arcate */
.gates-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 25px;
    margin-top: 20px;
}

.gate {
    width: 200px;
    height: 350px; /* Altezza ridotta per sicurezza */
    border-radius: 100px 100px 10px 10px;
    text-decoration: none !important;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.gate-title { font-family: 'Cinzel', serif; font-size: 1.1rem; }
.gate-sub { font-size: 0.6rem; letter-spacing: 2px; opacity: 0.7; color: white; margin-top: 8px; }

.cyan { border: 3px solid #00f0ff; box-shadow: 0 0 15px #00f0ff; color: #00f0ff !important; }
.violet { border: 3px solid #d64dff; box-shadow: 0 0 15px #d64dff; color: #d64dff !important; }
.pink { border: 3px solid #ff0077; box-shadow: 0 0 15px #ff0077; color: #ff0077 !important; }

.gate:hover:not(.locked) { transform: scale(1.08); filter: brightness(1.2); }

.locked { border: 3px solid #333 !important; background: rgba(0,0,0,0.5); opacity: 0.6; cursor: not-allowed; }
.locked .gate-title { color: #666 !important; }

/* Centratura forzata del Bottone Streamlit */
[data-testid="stElementContainer"] {
    display: flex;
    justify-content: center;
    width: 100%;
}

div.stButton > button {
    font-family: 'Cinzel', serif;
    background-color: transparent;
    color: #00f0ff !important;
    border: 1px solid #00f0ff !important;
    padding: 12px 40px !important;
    font-size: 1.1rem !important;
    letter-spacing: 4px !important;
    transition: all 0.3s ease;
    margin-top: 20px;
}

div.stButton > button:hover {
    background-color: rgba(0, 240, 255, 0.1) !important;
    box-shadow: 0 0 20px #00f0ff;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# --- 5. LOGICA DELLE PAGINE ---

# --- PAGINA: LOBBY ---
if st.session_state.pagina_corrente == 'lobby':
    st.markdown("""
        <div class="page-wrapper">
            <h1 class="hero-title">LVDVS</h1>
            <p class="hero-subtitle">Scegli il tuo destino</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Bottone centrato dal CSS
    st.button("AD MAIORA", on_click=vai_ai_livelli)

# --- PAGINA: ARCHI ---
else:
    # Preparazione Archi
    arc_1 = """
    <a class="gate cyan" href="./01_discipulus" target="_self">
        <div class="gate-title">DISCIPVLVS</div>
        <div class="gate-sub">BEGINNER</div>
    </a>"""

    if st.session_state.gladiator_sbloccato:
        arc_2 = """
        <a class="gate violet" href="./02_gladiator" target="_self">
            <div class="gate-title">GLADIATOR</div>
            <div class="gate-sub">INTERMEDIATE</div>
        </a>"""
    else:
        arc_2 = """
        <div class="gate locked">
            <div class="gate-title">GLADIATOR 🔒</div>
            <div class="gate-sub">BLOCCATO</div>
        </div>"""

    if st.session_state.imperator_sbloccato:
        arc_3 = """
        <a class="gate pink" href="./03_imperator" target="_self">
            <div class="gate-title">IMPERATOR</div>
            <div class="gate-sub">PRO</div>
        </a>"""
    else:
        arc_3 = """
        <div class="gate locked">
            <div class="gate-title">IMPERATOR 🔒</div>
            <div class="gate-sub">BLOCCATO</div>
        </div>"""

    st.markdown(f"""
        <div class="page-wrapper">
            <h1 class="hero-title" style="font-size: 4rem;">LVDVS</h1>
            <div class="gates-container">
                {arc_1}
                {arc_2}
                {arc_3}
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Bottone per tornare indietro
    st.button("TORNA ALLA LOBBY", on_click=torna_alla_lobby)
