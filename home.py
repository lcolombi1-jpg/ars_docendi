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

.block-container{ max-width:100%; padding-top:0rem; }

.title{ text-align:center; margin-top:20px; }
.title h1{
    font-family:'Cinzel', serif;
    font-size:clamp(3rem,8vw,6rem);
    color:white;
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

.gates{ 
    display:flex; 
    justify-content:center; 
    gap:40px; 
    flex-wrap: wrap;
    padding: 20px;
}

.gate{
    width: 260px;
    height: 480px;
    border-radius: 130px 130px 10px 10px;
    text-decoration:none !important;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    transition: all 0.4s ease;
}

.gate-title{
    font-family:'Cinzel', serif;
    font-size: 1.5rem;
    letter-spacing:1px;
    text-align:center;
}

.gate-sub{
    margin-top:16px;
    font-size: 0.8rem;
    letter-spacing:4px;
    color:rgba(255,255,255,.4);
}

.cyan { border:4px solid #00f0ff; box-shadow: 0 0 20px #00f0ff; color:#00f0ff !important; }
.violet { border:4px solid #d64dff; box-shadow: 0 0 20px #d64dff; color:#d64dff !important; }
.pink { border:4px solid #ff0077; box-shadow: 0 0 20px #ff0077; color:#ff0077 !important; }

.gate:hover:not(.locked) { transform: scale(1.05); filter: brightness(1.2); }

.locked {
    border: 4px solid #333 !important;
    background: rgba(0,0,0,0.4);
    cursor: not-allowed;
    opacity: 0.6;
}
.locked .gate-title, .locked .gate-sub { color: #666 !important; }

div.stButton > button {
    font-family: 'Cinzel', serif;
    background-color: transparent;
    color: #00f0ff;
    border: 2px solid #00f0ff;
    padding: 15px 40px;
    font-size: 1.8rem;
    letter-spacing: 5px;
    box-shadow: 0 0 15px #00f0ff;
    display: block;
    margin: 0 auto;
}
div.stButton > button:hover {
    background-color: #00f0ff;
    color: #0a0015;
    box-shadow: 0 0 20px #00f0ff, 0 0 40px #00f0ff;
}
/* Questo centra perfettamente il contenitore del bottone in Streamlit */
div.stButton {
    display: flex;
    justify-content: center;
    width: 100%;
    margin-top: -30px; /* Usa questo per avvicinarlo o allontanarlo dal titolo */
}

div.stButton > button {
    font-family: 'Cinzel', serif;
    background-color: transparent;
    color: #00f0ff;
    border: 2px solid #00f0ff;
    padding: 15px 40px;
    font-size: 1.8rem;
    letter-spacing: 5px;
    box-shadow: 0 0 15px #00f0ff;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background-color: #00f0ff;
    color: #0a0015;
    box-shadow: 0 0 20px #00f0ff, 0 0 40px #00f0ff;
}
</style>
""", unsafe_allow_html=True)

# --- 3. LOGICA DELLE PAGINE ---

if st.session_state.pagina_corrente == 'lobby':
    st.markdown('<div class="title"><h1>LVDVS</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Benvenuto nel tempio</div>', unsafe_allow_html=True)
    st.write("") 
    st.button("AD MAIORA", on_click=vai_ai_livelli)

else:
    st.markdown('<div class="title"><h1>LVDVS</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Scegli il tuo destino</div>', unsafe_allow_html=True)

    # --- COSTRUZIONE HTML SICURA (senza indentazioni problematiche) ---
    html_content = '<div class="gates">'
    
    # Arco 1: DISCIPVLVS (Sempre aperto)
    html_content += '<a class="gate cyan" href="./01_discipulus" target="_self">'
    html_content += '<div class="gate-title">DISCIPVLVS</div>'
    html_content += '<div class="gate-sub">BEGINNER</div>'
    html_content += '</a>'

    # Arco 2: GLADIATOR (Si apre se sbloccato)
    if st.session_state.gladiator_sbloccato:
        html_content += '<a class="gate violet" href="./02_gladiator" target="_self">'
        html_content += '<div class="gate-title">GLADIATOR</div>'
        html_content += '<div class="gate-sub">INTERMEDIATE</div>'
        html_content += '</a>'
    else:
        html_content += '<div class="gate locked">'
        html_content += '<div class="gate-title">GLADIATOR 🔒</div>'
        html_content += '<div class="gate-sub">BLOCCATO</div>'
        html_content += '</div>'

    # Arco 3: IMPERATOR (Si apre se sbloccato)
    if st.session_state.imperator_sbloccato:
        html_content += '<a class="gate pink" href="./03_imperator" target="_self">'
        html_content += '<div class="gate-title">IMPERATOR</div>'
        html_content += '<div class="gate-sub">PRO</div>'
        html_content += '</a>'
    else:
        html_content += '<div class="gate locked">'
        html_content += '<div class="gate-title">IMPERATOR 🔒</div>'
        html_content += '<div class="gate-sub">BLOCCATO</div>'
        html_content += '</div>'

    html_content += '</div>'

    # Stampiamo tutto a schermo in una volta sola
    st.markdown(html_content, unsafe_allow_html=True)

    # Pulsante per tornare indietro
    st.write("")
    if st.button("Torna alla Lobby"):
        st.session_state.pagina_corrente = 'lobby'
        st.rerun()
