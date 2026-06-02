import streamlit as st

# --- 1. SETUP (Deve essere assolutamente la prima riga di codice Streamlit!) ---
st.set_page_config(
    page_title="LVDVS",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. FUNZIONI DI NAVIGAZIONE ---
# Vengono lette dal sistema PRIMA di essere collegate ai bottoni
def vai_ai_livelli():
    st.session_state.pagina_corrente = 'archi'

def torna_alla_lobby():
    st.session_state.pagina_corrente = 'lobby'

# --- 3. INIZIALIZZAZIONE DELLA MEMORIA (Session State) ---
if 'pagina_corrente' not in st.session_state:
    st.session_state.pagina_corrente = 'lobby'
if 'gladiator_sbloccato' not in st.session_state:
    st.session_state.gladiator_sbloccato = False
if 'imperator_sbloccato' not in st.session_state:
    st.session_state.imperator_sbloccato = False

# --- 4. CSS PULITO E SICURO ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

/* Nascondiamo header, footer e menu di base per pulire la grafica */
header, footer, .stDeployButton { visibility: hidden; }

/* Sfondo della pagina */
.stApp {
    background: radial-gradient(circle at center, #19002f 0%, #0a0015 50%, #020004 100%);
}

/* --- STILI TESTI --- */
.hero-container {
    text-align: center;
    padding-top: 5vh;
}

.hero-title {
    font-family: 'Cinzel', serif;
    font-size: clamp(3rem, 10vw, 7rem);
    color: white;
    letter-spacing: 12px;
    text-shadow: 0 0 20px #ff00ff;
    margin: 0;
    line-height: 1.2;
}

.hero-subtitle {
    font-family: 'Montserrat', sans-serif;
    color: #00f0ff;
    letter-spacing: 6px;
    font-size: 1.2rem;
    text-transform: uppercase;
    margin-bottom: 30px;
}

/* --- STILE BOTTONI STREAMLIT --- */
/* Centra i bottoni di Streamlit in modo sicuro e li abbellisce */
div.stButton {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

div.stButton > button {
    font-family: 'Cinzel', serif !important;
    background-color: transparent !important;
    color: #00f0ff !important;
    border: 2px solid #00f0ff !important;
    padding: 10px 40px !important;
    font-size: 1.2rem !important;
    letter-spacing: 3px !important;
    transition: all 0.3s ease !important;
    border-radius: 5px !important;
}

div.stButton > button:hover {
    background-color: #00f0ff !important;
    color: #0a0015 !important;
    box-shadow: 0 0 20px #00f0ff;
    transform: scale(1.05);
}

/* --- STILE ARCATE --- */
.gates-container {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin-top: 30px;
    flex-wrap: wrap; /* Se lo schermo è piccolo, vanno a capo invece di uscire fuori */
}

.gate {
    width: 220px;
    height: 380px;
    border-radius: 110px 110px 10px 10px;
    text-decoration: none !important;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    transition: all 0.4s ease;
    background: rgba(0, 0, 0, 0.4); /* Sfondo leggero per far risaltare l'arco */
}

.gate-title {
    font-family: 'Cinzel', serif;
    font-size: 1.3rem;
    margin-bottom: 10px;
}

.gate-sub {
    font-family: 'Montserrat', sans-serif;
    font-size: 0.7rem;
    letter-spacing: 3px;
    color: rgba(255,255,255,0.6);
}

/* Colori e bagliori degli archi */
.cyan { border: 3px solid #00f0ff; box-shadow: 0 0 15px #00f0ff; color: #00f0ff !important; }
.violet { border: 3px solid #d64dff; box-shadow: 0 0 15px #d64dff; color: #d64dff !important; }
.pink { border: 3px solid #ff0077; box-shadow: 0 0 15px #ff0077; color: #ff0077 !important; }

/* Animazione al passaggio del mouse */
.gate:hover:not(.locked) { transform: scale(1.05); filter: brightness(1.2); }

/* Stile per gli archi chiusi */
.locked { border: 3px solid #333 !important; box-shadow: none; opacity: 0.5; cursor: not-allowed; }
.locked .gate-title, .locked .gate-sub { color: #666 !important; }

</style>
""", unsafe_allow_html=True)


# --- 5. COSTRUZIONE DELLE PAGINE ---

if st.session_state.pagina_corrente == 'lobby':
    # Disegniamo Titolo e Sottotitolo
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">LVDVS</h1>
            <p class="hero-subtitle">Scegli il tuo destino</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Inseriamo il bottone subito sotto (sarà centrato dal CSS)
    st.button("AD MAIORA", on_click=vai_ai_livelli)

elif st.session_state.pagina_corrente == 'archi':
    
    # 1. DISCIPVLVS
    html_arc_1 = """
    <a class="gate cyan" href="./01_discipulus" target="_self">
        <div class="gate-title">DISCIPVLVS</div>
        <div class="gate-sub">BEGINNER</div>
    </a>"""
    
    # 2. GLADIATOR
    if st.session_state.gladiator_sbloccato:
        html_arc_2 = """
        <a class="gate violet" href="./02_gladiator" target="_self">
            <div class="gate-title">GLADIATOR</div>
            <div class="gate-sub">INTERMEDIATE</div>
        </a>"""
    else:
        html_arc_2 = """
        <div class="gate locked">
            <div class="gate-title">GLADIATOR 🔒</div>
            <div class="gate-sub">BLOCCATO</div>
        </div>"""
        
    # 3. IMPERATOR
    if st.session_state.imperator_sbloccato:
        html_arc_3 = """
        <a class="gate pink" href="./03_imperator" target="_self">
            <div class="gate-title">IMPERATOR</div>
            <div class="gate-sub">PRO</div>
        </a>"""
    else:
        html_arc_3 = """
        <div class="gate locked">
            <div class="gate-title">IMPERATOR 🔒</div>
            <div class="gate-sub">BLOCCATO</div>
        </div>"""

    # Disegniamo la schermata dei livelli
    st.markdown(f"""
        <div class="hero-container" style="padding-top: 2vh;">
            <h1 class="hero-title" style="font-size: 4rem;">LVDVS</h1>
            <div class="gates-container">
                {html_arc_1}
                {html_arc_2}
                {html_arc_3}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Bottone Indietro (centrato)
    st.button("TORNA ALLA LOBBY", on_click=torna_alla_lobby)
