import streamlit as st

# --- 1. SETUP DELLA PAGINA ---
st.set_page_config(page_title="DISCIPVLVS - Il Test", page_icon="📜", layout="centered")

# --- CSS PER MANTENERE IL VIBE LVDVS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

.stApp { background: radial-gradient(circle at center, #19002f 0%, #0a0015 50%, #020004 100%); color: white; }
h1, h2, h3 { font-family: 'Cinzel', serif; color: #00f0ff; text-align: center; }
p, div, span, label { font-family: 'Montserrat', sans-serif; }
.stRadio > label { background: rgba(0, 240, 255, 0.05); padding: 15px; border-radius: 8px; border: 1px solid rgba(0, 240, 255, 0.2); }
.stButton > button { font-family: 'Cinzel', serif !important; color: #00f0ff !important; border: 1px solid #00f0ff !important; width: 100%; padding: 10px !important; margin-top: 20px;}
.stButton > button:hover { background-color: rgba(0, 240, 255, 0.1) !important; box-shadow: 0 0 15px #00f0ff; }
.success-text { color: #d64dff; font-size: 1.5rem; text-align: center; font-family: 'Cinzel', serif; margin-top: 20px; }
.fail-text { color: #ff0077; font-size: 1.5rem; text-align: center; font-family: 'Cinzel', serif; margin-top: 20px; }
</style>
""", unsafe_allow_html=True)

# --- 2. INIZIALIZZAZIONE DELLA MEMORIA ---
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'test_completato' not in st.session_state:
    st.session_state.test_completato = False
if 'gladiator_sbloccato' not in st.session_state:
    st.session_state.gladiator_sbloccato = False

# --- 3. IL DATABASE DELLE DOMANDE ---
# Qui inserirai le tue domande vere. Assicurati che 'corretta' sia IDENTICA a una delle opzioni.
domande = [
    {"testo": "Domanda 1: Quale fu il primo re di Roma?", "opzioni": ["Romolo", "Numa Pompilio", "Tulio Ostilio", "Anco Marzio"], "corretta": "Romolo"},
    {"testo": "Domanda 2: Inserisci il testo qui", "opzioni": ["Opzione A", "Opzione B", "Opzione C", "Opzione D"], "corretta": "Opzione A"},
    {"testo": "Domanda 3: Inserisci il testo qui", "opzioni": ["Opzione A", "Opzione B", "Opzione C", "Opzione D"], "corretta": "Opzione B"},
    {"testo": "Domanda 4: Inserisci il testo qui", "opzioni": ["Opzione A", "Opzione B", "Opzione C", "Opzione D"], "corretta": "Opzione C"},
    {"testo": "Domanda 5: Inserisci il testo qui", "opzioni": ["Opzione A", "Opzione B", "Opzione C", "Opzione D"], "corretta": "Opzione D"},
    {"testo": "Domanda 6: Inserisci il testo qui", "opzioni": ["Opzione A", "Opzione B", "Opzione C", "Opzione D"], "corretta": "Opzione A"},
    {"testo": "Domanda 7: Inserisci il testo qui", "opzioni": ["Opzione A", "Opzione B", "Opzione C", "Opzione D"], "corretta": "Opzione B"},
    {"testo": "Domanda 8: Inserisci il testo qui", "opzioni": ["Opzione A", "Opzione B", "Opzione C", "Opzione D"], "corretta": "Opzione C"},
    {"testo": "Domanda 9: Inserisci il testo qui", "opzioni": ["Opzione A", "Opzione B", "Opzione C", "Opzione D"], "corretta": "Opzione D"},
    {"testo": "Domanda 10: Inserisci il testo qui", "opzioni": ["Opzione A", "Opzione B", "Opzione C", "Opzione D"], "corretta": "Opzione A"},
]

# --- 4. FUNZIONI DI LOGICA ---
def elabora_risposta(risposta_selezionata, risposta_esatta):
    # Controlla se è giusta e assegna il punto
    if risposta_selezionata == risposta_esatta:
        st.session_state.score += 1
    
    # Passa alla prossima domanda
    st.session_state.q_index += 1
    
    # Controlla se abbiamo finito le 10 domande
    if st.session_state.q_index >= 10:
        st.session_state.test_completato = True

def riavvia_test():
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.test_completato = False

# --- 5. INTERFACCIA UTENTE ---
st.title("PROVA DI INIZIAZIONE")
st.markdown("<h3 style='font-size: 1rem; color: rgba(255,255,255,0.5);'>LIVELLO: DISCIPVLVS</h3>", unsafe_allow_html=True)
st.write("---")

# SE IL TEST È IN CORSO...
if not st.session_state.test_completato:
    indice = st.session_state.q_index
    domanda_attuale = domande[indice]
    
    # Barra di progresso
    progresso = indice / len(domande)
    st.progress(progresso)
    st.markdown(f"<p style='text-align: right; font-size: 0.8rem; color: #00f0ff;'>Domanda {indice + 1} di 10</p>", unsafe_allow_html=True)
    
    # Mostra la domanda
    st.markdown(f"### {domanda_attuale['testo']}")
    
    # Opzioni di risposta
    scelta_utente = st.radio("Seleziona la tua risposta:", domanda_attuale['opzioni'], key=f"radio_{indice}")
    
    # Tasto di conferma che innesca la funzione di calcolo
    st.button("CONFERMA E PROCEDI", on_click=elabora_risposta, args=(scelta_utente, domanda_attuale['corretta']))

# SE IL TEST È FINITO...
else:
    st.progress(1.0)
    st.header("TEST CONCLUSO")
    st.markdown(f"<p style='text-align: center; font-size: 1.5rem;'>Hai risposto correttamente a <b>{st.session_state.score}</b> domande su 10.</p>", unsafe_allow_html=True)
    
    if st.session_state.score >= 8:
        # SUPERATO
        st.session_state.gladiator_sbloccato = True
        st.markdown("<div class='success-text'>AD MAIORA! Hai sbloccato il livello GLADIATOR. ⚔️</div>", unsafe_allow_html=True)
        st.write("---")
        # Pulsante per tornare alla main page (presumendo che il tuo file principale si chiami home.py o app.py)
        st.page_link("home.py", label="TORNA ALLA LOBBY PER PROSEGUIRE", icon="🏛️")
    else:
        # FALLITO
        st.markdown("<div class='fail-text'>NON SEI ANCORA PRONTO. DEVI ALLENARTI DI PIÙ. 🩸</div>", unsafe_allow_html=True)
        st.write("---")
        col1, col2 = st.columns(2)
        with col1:
            st.button("RIPROVA IL TEST", on_click=riavvia_test)
        with col2:
            st.page_link("home.py", label="TORNA ALLA LOBBY", icon="🏛️")
