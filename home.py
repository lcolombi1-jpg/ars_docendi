import streamlit as st

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="LVDVS",
    page_icon="🏛️",
    layout="wide"
)

# ==================================================
# SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "intro"

if "gladiator_unlocked" not in st.session_state:
    st.session_state.gladiator_unlocked = False

if "imperator_unlocked" not in st.session_state:
    st.session_state.imperator_unlocked = False

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Montserrat:wght@300;400;500&display=swap');

header, footer, #MainMenu{
    visibility:hidden;
}

.stApp{
    background:
    radial-gradient(
        circle at center,
        #19002f 0%,
        #0a0015 50%,
        #020004 100%
    );
}

.block-container{
    padding-top:1rem;
    max-width:1200px;
}

html{
    font-size:clamp(14px,1vw,18px);
}

.title{
    text-align:center;
    margin-top:40px;
}

.title h1{
    font-family:'Cinzel', serif;
    font-size:clamp(3rem,8vw,6rem);
    color:white;
    letter-spacing:10px;

    text-shadow:
        0 0 10px #ff00ff,
        0 0 40px #ff00ff;
}

.subtitle{
    text-align:center;
    color:#00f0ff;
    letter-spacing:5px;
    margin-top:-10px;
    margin-bottom:40px;

    text-shadow:
        0 0 10px #00f0ff;
}

.center-button{
    display:flex;
    justify-content:center;
    margin-top:40px;
}

.locked{
    opacity:0.35;
}

.big-space{
    height:20px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# INTRO
# ==================================================

if st.session_state.page == "intro":

    st.markdown("""
    <div class="title">
        <h1>LVDVS</h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subtitle">
        AVDACES FORTVNA IVVAT
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.write("")

    c1, c2, c3 = st.columns([2,1,2])

    with c2:
        if st.button("AD MAIORA", use_container_width=True):
            st.session_state.page = "lobby"
            st.rerun()

# ==================================================
# LOBBY
# ==================================================

elif st.session_state.page == "lobby":

    st.markdown("""
    <div class="title">
        <h1>LVDVS</h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subtitle">
        SCEGLI IL TVO DESTINO
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns(3)

    # =====================================
    # DISCIPVLVS
    # =====================================

    with col1:

        st.markdown("""
        <div style="
        height:420px;
        border-radius:220px 220px 10px 10px;
        border:4px solid #00f0ff;
        box-shadow:
        0 0 15px #00f0ff,
        0 0 50px #00f0ff,
        0 0 100px rgba(0,240,255,.5);
        display:flex;
        align-items:center;
        justify-content:center;
        flex-direction:column;
        ">
        <h2 style="
        color:#00f0ff;
        font-family:Cinzel;
        ">
        DISCIPVLVS
        </h2>
        <p style="color:white;">
        BEGINNER
        </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("ENTRA", key="discipulus"):
            st.session_state.page = "discipulus"
            st.rerun()

    # =====================================
    # GLADIATOR
    # =====================================

    with col2:

        st.markdown("""
        <div class="locked" style="
        height:420px;
        border-radius:220px 220px 10px 10px;
        border:4px solid #d64dff;
        box-shadow:
        0 0 15px #d64dff,
        0 0 50px #d64dff;
        display:flex;
        align-items:center;
        justify-content:center;
        flex-direction:column;
        ">
        <h2 style="
        color:#d64dff;
        font-family:Cinzel;
        ">
        GLADIATOR
        </h2>
        <p style="color:white;">
        🔒 BLOCCATO
        </p>
        </div>
        """, unsafe_allow_html=True)

    # =====================================
    # IMPERATOR
    # =====================================

    with col3:

        st.markdown("""
        <div class="locked" style="
        height:420px;
        border-radius:220px 220px 10px 10px;
        border:4px solid #ff0077;
        box-shadow:
        0 0 15px #ff0077,
        0 0 50px #ff0077;
        display:flex;
        align-items:center;
        justify-content:center;
        flex-direction:column;
        ">
        <h2 style="
        color:#ff0077;
        font-family:Cinzel;
        ">
        IMPERATOR
        </h2>
        <p style="color:white;">
        🔒 BLOCCATO
        </p>
        </div>
        """, unsafe_allow_html=True)

# ==================================================
# DISCIPVLVS
# ==================================================

elif st.session_state.page == "discipulus":

    st.markdown("""
    <div class="title">
        <h1>DISCIPVLVS</h1>
    </div>
    """, unsafe_allow_html=True)

    st.info("Qui inseriremo il quiz DISCIPVLVS.")

    st.write("")
    st.write("")

    if st.button("← TORNA AL LVDVS"):
        st.session_state.page = "lobby"
        st.rerun()
