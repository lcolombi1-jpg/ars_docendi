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

# Stati separati per ogni quiz per non accavallare i salvataggi
if 'quiz_inviato_disc' not in st.session_state:
    st.session_state.quiz_inviato_disc = False
if 'risposte_disc' not in st.session_state:
    st.session_state.risposte_disc = {}

if 'quiz_inviato_glad' not in st.session_state:
    st.session_state.quiz_inviato_glad = False
if 'risposte_glad' not in st.session_state:
    st.session_state.risposte_glad = {}

if 'quiz_inviato_imp' not in st.session_state:
    st.session_state.quiz_inviato_imp = False
if 'risposte_imp' not in st.session_state:
    st.session_state.risposte_imp = {}

# Aggiungi queste righe sotto alle altre variabili di stato
if 'indice_disc' not in st.session_state:
    st.session_state.indice_disc = 0
if 'indice_glad' not in st.session_state:
    st.session_state.indice_glad = 0
if 'indice_imp' not in st.session_state:
    st.session_state.indice_imp = 0

# --- DOMANDE DEI TEST ---
DOMANDE_DISCIPULUS = [
    {"id": 1, "domanda": "Barbari _______________ veniunt", "opzioni": ["Romae", "ad Romam", "Romam", "Romā"], "corretta": "Romam"},
    {"id": 2, "domanda": "Nautae _______________ non terrentur", "opzioni": ["saevis procellis", "saevas procellas", "saeva procella", "saevae procellae"], "corretta": "saevis procellis"},
    {"id": 3, "domanda": "_________ Syracusas cum liberis meis veniam", "opzioni": ["proximus annus", "proximi anni", "proximorum annorum", "proximo anno"], "corretta": "proximo anno"},
    {"id": 4, "domanda": "Romanorum oppida ______________ a Germani oppugnabantur", "opzioni": ["magnā cum ferociā", "magnam ferociam", "ex magnis ferocis", "magnae ferociae"], "corretta": "magnā cum ferociā"},
    {"id": 5, "domanda": "Persarum __________ longae hastae et acutae sagittae erant", "opzioni": ["copias", "copiarum", "copiis", "copiae"], "corretta": "copiis"},
    {"id": 6, "domanda": "Milites antiquis temporibus __________ pugnabant", "opzioni": ["cum gladiis", "per gladium", "gladium", "gladiis"], "corretta": "gladiis"},
    {"id": 8, "domanda": "___________ tenebrae solis luce pelluntur", "opzioni": ["nocti", "nox", "noctium", "noctem"], "corretta": "noctium"},
    {"id": 7, "domanda": "Petronius a Romanis elegantiae ___________ appellabitur", "opzioni": ["arbitri", "arbiter", "arbitrum", "arbitro"], "corretta": "arbiter"},
    {"id": 9, "domanda": "_______________ auxiliorum dux equites nostros in hibernis detinebat", "opzioni": ["propter moram", "morā", "prae moram", "morarum"], "corretta": "propter moram"},
    {"id": 10, "domanda": "Macedonum legati Athenas _______________ venient", "opzioni": ["paci causā", "pace", "pacis causā", "ob pacem"], "corretta": "pacis causā"}
]

DOMANDE_GLADIATOR = [
    {"id": 1, "domanda": "Seleziona il paradigma corretto:", "opzioni": ["lego, legis, lexi, lectum, legere", "fero, fers, tuli, latum, ferre", "moneo, mones, moni, monitum, monere", "ago, agis, agi, actum, agere"], "corretta": "fero, fers, tuli, latum, ferre"},
    {"id": 2, "domanda": "Nella frase "dum haec in his locis geruntur", la congiunzione "dum" significa:", "opzioni": ["dopo che", "prima che", "mentre", "non appena"], "corretta": "mentre"},
    {"id": 3, "domanda": "Traduci in latino la seguente frase: Marco ha molti amici", "opzioni": ["Marcus multos amicos habet", "Marco multi amici erant", "Marcus multos amicos habebat", "Marco multi amici sunt"], "corretta": "Marco multi amici sunt"},
    {"id": 4, "domanda": "Roboris è...", "opzioni": ["il dativo/ablativo plurale di vir", "il genitivo singolare di vis", "il dativo/ablativo plurale di virus", "nessuna delle precedenti"], "corretta": "il genitivo singolare di vis"},
    {"id": 5, "domanda": "Tela saxaque de summo monte in hostes __________", "opzioni": ["coniecti sunt", "coniecerunt", "coniciunt", "coniecta sunt"], "corretta": "coniecta sunt"},
    {"id": 8, "domanda": "Seleziona il paradigma corretto:", "opzioni": ["tango, tangis, tetigi, tactum, tangere", "volo, volis, volui, velle", "trado, tradis, tradi, traditum, tradere", "vinco, vincis, vinxi, vinctum, vincere"], "corretta": "tango, tangis, tetigi, tactum, tangere"},

for i in range(1, 21)]
DOMANDE_IMPERATOR = [{"id": i, "domanda": f"Quesito strategico Imperator numero {i}?", "opzioni": ["Opzione Alfa", "Opzione Beta", "Opzione Gamma", "Opzione Delta"], "corretta": "Opzione Alfa"} for i in range(1, 31)]

# --- 2. STILI CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;400;500;600&display=swap');

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

/* Animazioni globali */
@keyframes fadeInBanner {
    from { opacity: 0; transform: scale(0.9); }
    to { opacity: 1; transform: scale(1); }
}

/* --- LOBBY --- */
.lobby-wrapper {
    margin-top: 15vh; 
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.lobby-title h1 {
    font-family:'Cinzel', serif;
    font-size:clamp(5rem, 15vw, 10rem); 
    color:white;
    letter-spacing:15px;
    text-shadow: 0 0 15px #ff00ff, 0 0 60px #ff00ff;
    margin-bottom: 0;
    text-align: center;
    line-height: 1;
}
.lobby-subtitle {
    color:#00f0ff;
    text-align:center;
    letter-spacing:12px;
    font-size: clamp(1.2rem, 3vw, 2.5rem); 
    margin-top: 10px;
    margin-bottom: 60px; 
    font-family: 'Montserrat', sans-serif;
    text-transform: uppercase;
}

/* --- TITOLI PAGINE TEST --- */
.title{ text-align:center; margin-top:20px; }
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
    margin-bottom:20px;
    font-family: 'Montserrat', sans-serif;
    text-transform: uppercase;
}

/* --- STILE CITAZIONI (Molto più visibili e centrate) --- */
blockquote {
    background-color: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    padding: 20px 30px;
    margin: 10px auto 40px auto;
    width: 80%;
    color: #ffffff !important;
    font-size: 1.25rem !important;
    text-align: center !important;
    font-family: 'Montserrat', sans-serif;
    text-shadow: 0 0 8px rgba(255,255,255,0.4);
    box-shadow: 0 0 15px rgba(0,0,0,0.5);
}

/* --- STILE ARCATE --- */
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
    letter-spacing: 1px !important;
    transition: all 0.4s ease;
    white-space: pre-wrap !important;
}

/* Formattazione Testo Arcate: Nome grande, Traduzione piccola */
.st-key-btn_discipulus button p,
.st-key-btn_gladiator button p,
.st-key-btn_imperator button p {
    font-size: 1rem !important;
    letter-spacing: 3px;
    text-align: center;
}
.st-key-btn_discipulus button p::first-line,
.st-key-btn_gladiator button p::first-line,
.st-key-btn_imperator button p::first-line {
    font-size: 2.2rem !important;
    line-height: 1.8;
}

/* 1. DISCIPVLVS (CYAN) */
.st-key-btn_discipulus button {
    border: 4px solid #00f0ff !important;
    color: #00f0ff !important;
    box-shadow: 0 0 15px #00f0ff, 0 0 50px #00f0ff, 0 0 100px rgba(0,240,255,.5) !important;
}
.st-key-btn_discipulus button:hover { transform: scale(1.05); background-color: rgba(0, 240, 255, 0.1) !important; }

/* 2. GLADIATOR (VIOLET) */
.st-key-btn_gladiator button {
    border: 4px solid #d64dff !important;
    color: #d64dff !important;
    box-shadow: 0 0 15px #d64dff, 0 0 50px #d64dff, 0 0 100px rgba(214,77,255,.5) !important;
}
.st-key-btn_gladiator button:hover:not(:disabled) { transform: scale(1.05); background-color: rgba(214, 77, 255, 0.1) !important; }

/* 3. IMPERATOR (PINK) */
.st-key-btn_imperator button {
    border: 4px solid #ff0077 !important;
    color: #ff0077 !important;
    box-shadow: 0 0 15px #ff0077, 0 0 50px #ff0077, 0 0 100px rgba(255,0,119,.5) !important;
}
.st-key-btn_imperator button:hover:not(:disabled) { transform: scale(1.05); background-color: rgba(255, 0, 119, 0.1) !important; }

/* ARCATE BLOCCATE */
div.stButton > button:disabled {
    cursor: not-allowed !important;
    transform: none !important;
    opacity: 0.65 !important;
}

/* --- BOTTONI RETTANGOLARI --- */
.st-key-ad_maiora_btn, .st-key-back_btn, .st-key-back_map {
    display: flex !important; justify-content: center !important; width: 100% !important;
}
.st-key-ad_maiora_btn button, .st-key-back_btn button, .st-key-submit_quiz button, 
.st-key-action_btn button, .st-key-action_btn_2 button, .st-key-back_map button,
.st-key-action_btn_d1 button, .st-key-action_btn_d2 button,
.st-key-action_btn_g1 button, .st-key-action_btn_g2 button,
.st-key-action_btn_i1 button, .st-key-action_btn_i2 button,
.st-key-submit_quiz_disc button, .st-key-submit_quiz_glad button, .st-key-submit_quiz_imp button,
.st-key-prev_disc button, .st-key-next_disc button,
.st-key-back_map_d button, .st-key-back_map_g button, .st-key-back_map_i button {
    height: auto !important; width: auto !important; padding: 10px 25px !important; 
    border-radius: 4px !important; font-size: 1.1rem !important; 
    font-family: 'Cinzel', serif !important; color: #00f0ff !important; 
    border: 1px solid #00f0ff !important; box-shadow: 0 0 10px rgba(0, 240, 255, 0.5) !important; 
    background: transparent !important; margin: 0 auto !important; display: block !important; transition: all 0.3s ease;
}
.st-key-ad_maiora_btn button:hover, .st-key-back_btn button:hover, .st-key-submit_quiz button:hover, .st-key-back_map button:hover,
.st-key-action_btn_d1 button:hover, .st-key-action_btn_d2 button:hover,
.st-key-action_btn_g1 button:hover, .st-key-action_btn_g2 button:hover,
.st-key-action_btn_i1 button:hover, .st-key-action_btn_i2 button:hover,
.st-key-submit_quiz_disc button:hover, .st-key-submit_quiz_glad button:hover, .st-key-submit_quiz_imp button:hover,
.st-key-prev_disc button:hover, .st-key-next_disc button:hover,
.st-key-back_map_d button:hover, .st-key-back_map_g button:hover, .st-key-back_map_i button:hover {
    background-color: rgba(0, 240, 255, 0.2) !important; box-shadow: 0 0 20px #00f0ff !important;
}

/* --- STILI TEST / QUIZ CENTRATI --- */
.quiz-counter {
    font-family: 'Montserrat', sans-serif;
    color: #ffffff;
    font-size: 1.2rem;
    font-weight: 500;
    text-align: center;
    margin-top: 45px;      
    margin-bottom: 20px;   
    letter-spacing: 1px;
    opacity: 0.9;
}

.quiz-text {
    font-family: 'Montserrat', sans-serif;
    color: #00f0ff;
    font-size: 2.2rem !important;  /* <--- Aggiunto !important */
    font-weight: 600;
    text-align: center;
    margin-bottom: 30px;
    text-shadow: 0 0 10px rgba(0,240,255,0.4); 
}

/* Il box delle risposte vero e proprio */
div[role="radiogroup"] {
    background-color: rgba(255, 255, 255, 0.05); 
    padding: 35px 55px !important; 
    border-radius: 12px;
    border: 1px solid rgba(255, 255, 255, 0.2); 
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

label[data-baseweb="radio"] {
    margin-bottom: 14px !important; 
}
label[data-baseweb="radio"]:last-child {
    margin-bottom: 0px !important;
}

div[role="radiogroup"] p {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.25rem !important;
    color: #ffffff !important; 
    font-weight: 500;
    margin-bottom: 0px;
}
</style>
""", unsafe_allow_html=True)


# --- 3. LOGICA DELLE PAGINE ---

# ================================
# PAGINA: LOBBY
# ================================
if st.session_state.pagina_corrente == 'lobby':
    st.markdown('''
    <div class="lobby-wrapper">
        <div class="lobby-title"><h1>LVDVS</h1></div>
        <div class="lobby-subtitle">SCEGLI IL TUO DESTINO</div>
    </div>
    ''', unsafe_allow_html=True)
    
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
            st.button("GLADIATOR 🔒\n\nINTERMEDIATE", disabled=True, key="btn_gladiator")

    with col3:
        if st.session_state.imperator_sbloccato:
            if st.button("IMPERATOR\n\nPRO", key="btn_imperator"):
                st.session_state.pagina_corrente = 'test_imperator'
                st.rerun()
        else:
            st.button("IMPERATOR 🔒\n\nPRO", disabled=True, key="btn_imperator")

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
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

    if not st.session_state.quiz_inviato_disc:
        
        # --- BARRA DI PROGRESSO ESTETICA ---
        progresso = st.session_state.indice_disc / (len(DOMANDE_DISCIPULUS) - 1)
        st.progress(progresso)
        
        # --- PESCHIAMO LA DOMANDA CORRENTE ---
        q = DOMANDE_DISCIPULUS[st.session_state.indice_disc]
        
        st.markdown(f'<p class="quiz-counter">Domanda {st.session_state.indice_disc + 1} di {len(DOMANDE_DISCIPULUS)}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="quiz-text">{q["domanda"]}</p>', unsafe_allow_html=True)
        
        # COLONNE PER CENTRARE IL BOX RISPOSTE
        col_vuota_sx, col_centrale, col_vuota_dx = st.columns([1, 2, 1])
        with col_centrale:
            opzioni_con_default = ["Seleziona una risposta..."] + q["opzioni"]
            
            default_index = 0
            if q["id"] in st.session_state.risposte_disc:
                risposta_salvata = st.session_state.risposte_disc[q["id"]]
                if risposta_salvata in opzioni_con_default:
                    default_index = opzioni_con_default.index(risposta_salvata)

            scelta = st.radio(
                f"Opzioni per domanda {q['id']}", 
                opzioni_con_default, 
                index=default_index, 
                key=f"d_q_{q['id']}", 
                label_visibility="collapsed"
            )
            if scelta != "Seleziona una risposta...":
                st.session_state.risposte_disc[q["id"]] = scelta

        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.write("---")

        # --- BOTTONI DI NAVIGAZIONE ---
        col_nav1, col_nav2, col_nav3 = st.columns([1, 2, 1])
        
        with col_nav1:
            if st.session_state.indice_disc > 0:
                if st.button("⬅️ Indietro", key="prev_disc"):
                    st.session_state.indice_disc -= 1
                    st.rerun()
                    
        with col_nav3:
            if st.session_state.indice_disc < len(DOMANDE_DISCIPULUS) - 1:
                if st.button("Avanti ➡️", key="next_disc"):
                    st.session_state.indice_disc += 1
                    st.rerun()
            else:
                if st.button("CONSEGNA IL TEST", key="submit_quiz_disc"):
                    if len(st.session_state.risposte_disc) < len(DOMANDE_DISCIPULUS):
                        st.warning("⚠️ Per favore, rispondi a tutte le domande prima di consegnare!")
                    else:
                        st.session_state.quiz_inviato_disc = True
                        st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Torna indietro", key="back_map_d"):
            st.session_state.pagina_corrente = 'archi'
            st.rerun()

    else:
        # --- GESTIONE RISULTATI ---
        punteggio = sum(1 for q in DOMANDE_DISCIPULUS if st.session_state.risposte_disc.get(q["id"]) == q["corretta"])
        st.markdown(f"<h3 style='text-align: center; color: white;'>Risultato: {punteggio} / 10 risposte corrette</h3>", unsafe_allow_html=True)
        
        if punteggio >= 8:
            st.success("🎉 ECCELLENTE! Hai dimostrato di avere la stoffa del guerriero. Il grado GLADIATOR è sbloccato!")
            st.session_state.gladiator_sbloccato = True
        else:
            st.error("❌ Non hai raggiunto il punteggio minimo (8/10). Riprova!")
        
        col_res1, col_res2, _ = st.columns([1, 1, 2])
        with col_res1:
            if st.button("Torna alla Mappa", key="action_btn_d1"):
                st.session_state.quiz_inviato_disc = False
                st.session_state.risposte_disc = {}
                st.session_state.indice_disc = 0
                st.session_state.pagina_corrente = 'archi'
                st.rerun()
        with col_res2:
            if not st.session_state.gladiator_sbloccato:
                if st.button("Riprova il Test", key="action_btn_d2"):
                    st.session_state.quiz_inviato_disc = False
                    st.session_state.risposte_disc = {}
                    st.session_state.indice_disc = 0
                    st.rerun()


# ================================
# PAGINA: TEST GLADIATOR
# ================================
elif st.session_state.pagina_corrente == 'test_gladiator':
    st.markdown('<div class="title" style="text-shadow: 0 0 10px #d64dff, 0 0 40px #d64dff;"><h1 style="text-shadow: 0 0 10px #d64dff, 0 0 40px #d64dff;">GLADIATOR</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle" style="color:#d64dff;">L\'ARENA INTERMEDIA</div>', unsafe_allow_html=True)
    st.markdown("> *Rispondi correttamente ad almeno 17 domande su 20 per sbloccare l'arena IMPERATOR.*")
    st.write("---")

    for q in DOMANDE_GLADIATOR:
        st.markdown(f'<p class="quiz-text">Domanda {q["id"]}: {q["domanda"]}</p>', unsafe_allow_html=True)
        
        # CENTRATURA A 3 COLONNE ANCHE QUI
        col_sx, col_centrale, col_dx = st.columns([1, 2, 1])
        with col_centrale:
            opzioni_con_default = ["Seleziona una risposta..."] + q["opzioni"]
            scelta = st.radio(
                f"Opzioni per domanda {q['id']}", opzioni_con_default, key=f"g_q_{q['id']}", 
                label_visibility="collapsed", disabled=st.session_state.quiz_inviato_glad
            )
            if scelta != "Seleziona una risposta...":
                st.session_state.risposte_glad[q["id"]] = scelta
        st.write("---")

    if not st.session_state.quiz_inviato_glad:
        st.markdown("<div style='display: flex; justify-content: center; width: 100%;'>", unsafe_allow_html=True)
        if st.button("CONSEGNA IL TEST", key="submit_quiz_glad"):
            if len(st.session_state.risposte_glad) < 20:
                st.warning("⚠️ Per favore, rispondi a tutte le domande prima di consegnare!")
            else:
                st.session_state.quiz_inviato_glad = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        punteggio = sum(1 for q in DOMANDE_GLADIATOR if st.session_state.risposte_glad.get(q["id"]) == q["corretta"])
        st.markdown(f"<h3 style='text-align: center; color: white;'>Risultato: {punteggio} / 20 risposte corrette</h3>", unsafe_allow_html=True)
        
        if punteggio >= 17:
            st.success("⚔️ GLORIOSO! Il sangue dell'arena è tuo. Il grado IMPERATOR è sbloccato!")
            st.session_state.imperator_sbloccato = True
        else:
            st.error("❌ Non hai raggiunto il punteggio minimo (17/20). Affila la spada e riprova!")
        
        col_res1, col_res2, _ = st.columns([1, 1, 2])
        with col_res1:
            if st.button("Torna alla Mappa", key="action_btn_g1"):
                st.session_state.quiz_inviato_glad = False
                st.session_state.risposte_glad = {}
                st.session_state.pagina_corrente = 'archi'
                st.rerun()
        with col_res2:
            if not st.session_state.imperator_sbloccato:
                if st.button("Riprova il Test", key="action_btn_g2"):
                    st.session_state.quiz_inviato_glad = False
                    st.session_state.risposte_glad = {}
                    st.rerun()

    if not st.session_state.quiz_inviato_glad:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Torna indietro", key="back_map_g"):
            st.session_state.pagina_corrente = 'archi'
            st.rerun()


# ================================
# PAGINA: TEST IMPERATOR
# ================================
elif st.session_state.pagina_corrente == 'test_imperator':
    st.markdown('<div class="title" style="text-shadow: 0 0 10px #ff0077, 0 0 40px #ff0077;"><h1 style="text-shadow: 0 0 10px #ff0077, 0 0 40px #ff0077;">IMPERATOR</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle" style="color:#ff0077;">LA PROVA FINALE</div>', unsafe_allow_html=True)
    st.markdown("> *Rispondi correttamente ad almeno 25 domande su 30 per dominare l'Impero.*")
    st.write("---")

    for q in DOMANDE_IMPERATOR:
        st.markdown(f'<p class="quiz-text">Domanda {q["id"]}: {q["domanda"]}</p>', unsafe_allow_html=True)
        
        # CENTRATURA A 3 COLONNE ANCHE QUI
        col_sx, col_centrale, col_dx = st.columns([1, 2, 1])
        with col_centrale:
            opzioni_con_default = ["Seleziona una risposta..."] + q["opzioni"]
            scelta = st.radio(
                f"Opzioni per domanda {q['id']}", opzioni_con_default, key=f"i_q_{q['id']}", 
                label_visibility="collapsed", disabled=st.session_state.quiz_inviato_imp
            )
            if scelta != "Seleziona una risposta...":
                st.session_state.risposte_imp[q["id"]] = scelta
        st.write("---")

    if not st.session_state.quiz_inviato_imp:
        st.markdown("<div style='display: flex; justify-content: center; width: 100%;'>", unsafe_allow_html=True)
        if st.button("CONSEGNA IL TEST", key="submit_quiz_imp"):
            if len(st.session_state.risposte_imp) < 30:
                st.warning("⚠️ Per favore, rispondi a tutte le domande prima di consegnare!")
            else:
                st.session_state.quiz_inviato_imp = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        punteggio = sum(1 for q in DOMANDE_IMPERATOR if st.session_state.risposte_imp.get(q["id"]) == q["corretta"])
        st.markdown(f"<h3 style='text-align: center; color: white;'>Risultato: {punteggio} / 30 risposte corrette</h3>", unsafe_allow_html=True)
        
        if punteggio >= 25:
            st.balloons()
            # BANNER EPICO A TUTTO SCHERMO
            st.markdown("""
            <div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.92); z-index: 999999; display: flex; justify-content: center; align-items: center; flex-direction: column; animation: fadeInBanner 1.2s ease-in-out;">
                <h1 style="font-family: 'Cinzel', serif; font-size: clamp(4rem, 12vw, 10rem); color: #ff0077; text-shadow: 0 0 20px #ff0077, 0 0 50px #ff0077, 0 0 80px #ff0077; margin:0; text-align:center; line-height: 1;">VENI, VIDI, VICI!</h1>
                <p style="font-family: 'Montserrat', sans-serif; color: white; font-size: clamp(1.2rem, 3vw, 2rem); margin-top: 30px; text-transform: uppercase; letter-spacing: 5px; text-align:center;">Complimenti, soldato!<br>Nunc est bibendum!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Non hai raggiunto il punteggio minimo (25/30). L'Impero attende, riprova!")
        
        col_res1, col_res2, _ = st.columns([1, 1, 2])
        with col_res1:
            if st.button("Torna alla Mappa", key="action_btn_i1"):
                st.session_state.quiz_inviato_imp = False
                st.session_state.risposte_imp = {}
                st.session_state.pagina_corrente = 'archi'
                st.rerun()
        with col_res2:
            if punteggio < 25:
                if st.button("Riprova il Test", key="action_btn_i2"):
                    st.session_state.quiz_inviato_imp = False
                    st.session_state.risposte_imp = {}
                    st.rerun()

    if not st.session_state.quiz_inviato_imp:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Torna indietro", key="back_map_i"):
            st.session_state.pagina_corrente = 'archi'
            st.rerun()
