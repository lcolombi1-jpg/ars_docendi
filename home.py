import streamlit as st

st.set_page_config(
    page_title="Ludus",
    page_icon="🏛️",
    layout="wide"
)

# --- 1. INIZIALIZZAZIONE DELLA MEMORIA (SESSION STATE) ---
if 'pagina_corrente' not in st.session_state:
    st.session_state.pagina_corrente = 'lobby'
if 'gladiator_sbloccato' not in st.session_state:
    st.session_state.gladiator_sbloccato = False
if 'imperator_sbloccato' not in st.session_state:
    st.session_state.imperator_sbloccato = False

def vai_ai_livelli():
    st.session_state.pagina_corrente = 'archi'

# --- 2. CSS CUSTOM ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

header, footer, #MainMenu { visibility:hidden; }

.stApp{
    background: radial-gradient(circle at center, #19002f 0%, #0a0015 50%, #020004 100%);
}

.block-container{ max-width:100%; padding-top:0rem; }
html{ font-size:clamp(14px,1vw,18px); }

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
    letter-spacing:8px;
    margin-bottom:50px;
}

.gates{ display:flex; justify-content:center; gap:80px; }

.gate{
    width:min(260px,28vw);
    height:min(520px,60vh);
    border-radius: 130px 130px 10px 10px;
    text-decoration:none;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    background:transparent;
    transition: transform 0.3s ease;
}

.gate:hover { transform: translateY(-10px); }

.gate-title{
    font-family:'Cinzel', serif;
    font-size:clamp(1rem,2vw,1.8rem);
    letter-spacing:1px;
    text-align:center;
}

.gate-sub{
    margin-top:16px;
    font-size:clamp(.7rem,1vw,.9rem);
    letter-spacing:4px;
    color:rgba(255,255,255,.4);
}

/* Stili per i gate sbloccati */
.cyan{
    border:4px solid #00f0ff;
    box-shadow: 0 0 15px #00f0ff, 0 0 50px #00f0ff, 0 0 100px rgba(0,240,255,.5);
}
.cyan .gate-title{ color:#00f0ff; }

.violet{
    border:4px solid #d64dff;
    box-shadow: 0 0 15px #d64dff, 0 0 50px #d64dff, 0 0 100px rgba(214,77,255,.5);
}
.violet .gate-title{ color:#d64dff; }

.pink{
    border:4px solid #ff0077;
    box-shadow: 0 0 15px #ff0077, 0 0 50px #ff0077, 0 0 100px rgba(255,0,119,.5);
}
.pink .gate-title{ color:#ff0077; }

/* Stile per i gate bloccati */
.locked{
    border:4px solid #333333;
    box-shadow: none;
    cursor: not-allowed;
    background: rgba(255,255,255,0.05);
}
.locked .gate-title{ color: #666666; }
.locked:hover { transform: none; }

/* Stile per il bottone AD MAIORA di Streamlit */
div.stButton > button {
    font-family: 'Cinzel', serif;
    background-color: transparent;
    color: #00f0ff;
    border: 2px solid #00f0ff;
    border-radius: 10px;
    padding: 15px 30px;
    font-size: 1.5rem;
    letter-spacing: 5px;
    box-shadow: 0 0 10px #00f0ff;
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

# PAGINA 1: LOBBY
if st.session_state.pagina_corrente == 'lobby':
    st.markdown("""
    <div class="title"><h1>LVDVS</h1></div>
    <div class="subtitle">scegli il tuo destino</div>
    <br><br>
    """, unsafe_allow_html=True)
    
    # Creiamo 3 colonne per centrare il bottone
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.button("AD MAIORA", use_container_width=True, on_click=vai_ai_livelli)

# PAGINA 2: SCELTA DEGLI ARCHI
elif st.session_state.pagina_corrente == 'archi':
    st.markdown("""
    <div class="title"><h1>LVDVS</h1></div>
    <div class="subtitle">I TRE ARCHI</div>
    """, unsafe_allow_html=True)

    # Iniziamo a costruire l'HTML dei gate dinamicamente in base a cosa è sbloccato
    html_gates = '<div class="gates">'
    
    # 1. DISCIPVLVS (Sempre aperto)
    html_gates += """
    <a class="gate cyan" href="./01_discipulus" target="_self">
        <div class="gate-title">DISCIPVLVS</div>
        <div class="gate-sub">BEGINNER</div>
    </a>
    """
    
    # 2. GLADIATOR
    if st.session_state.gladiator_sbloccato:
        html_gates += """
        <a class="gate violet" href="./02_gladiator" target="_self">
            <div class="gate-title">GLADIATOR</div>
            <div class="gate-sub">INTERMEDIATE</div>
        </a>
        """
    else:
        html_gates += """
        <div class="gate locked">
            <div class="gate-title">GLADIATOR 🔒</div>
            <div class="gate-sub">BLOCCATO</div>
        </div>
        """
        
    # 3. IMPERATOR
    if st.session_state.imperator_sbloccato:
        html_gates += """
        <a class="gate pink" href="./03_imperator" target="_self">
            <div class="gate-title">IMPERATOR</div>
            <div class="gate-sub">PRO</div>
        </a>
        """
    else:
        html_gates += """
        <div class="gate locked">
            <div class="gate-title">IMPERATOR 🔒</div>
            <div class="gate-sub">BLOCCATO</div>
        </div>
        """
        
    html_gates += '</div>'
    
    # Stampiamo gli archi a schermo
    st.markdown(html_gates, unsafe_allow_html=True)
    
    # Tasto opzionale per tornare alla lobby
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Torna alla Lobby"):
        st.session_state.pagina_corrente = 'lobby'
        st.rerun()
