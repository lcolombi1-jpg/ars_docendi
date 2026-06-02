import streamlit as st

st.set_page_config(
    page_title="Ludus",
    page_icon="🏛️",
    layout="wide"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Montserrat:wght@300;500&display=swap');

header, footer, #MainMenu {
    visibility:hidden;
}

.stApp{
    background:
    radial-gradient(circle at center,
    #19002f 0%,
    #0a0015 50%,
    #020004 100%);
}

.block-container{
    max-width:100%;
    padding-top:0rem;
}

.title{
    text-align:center;
    margin-top:20px;
}

.title h1{
    font-family:'Cinzel', serif;
    font-size:6rem;
    color:white;
    letter-spacing:10px;

    text-shadow:
        0 0 10px #ff00ff,
        0 0 40px #ff00ff;
}

.subtitle{
    color:#00f0ff;
    text-align:center;
    letter-spacing:8px;
    margin-bottom:50px;
}

.gates{
    display:flex;
    justify-content:center;
    gap:80px;
}

.gate{
    width:260px;
    height:520px;

    border-radius:
        130px
        130px
        10px
        10px;

    text-decoration:none;

    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    background:transparent;
}

.gate-title{
    font-family:'Cinzel', serif;
    font-size:1.8rem;
    letter-spacing:1px;
    text-align:center;
}

.gate-sub{
    margin-top:16px;
    font-size:0.85rem;
    letter-spacing:4px;
    color:rgba(255,255,255,.4);
}

.cyan{
    border:4px solid #00f0ff;

    box-shadow:
        0 0 15px #00f0ff,
        0 0 50px #00f0ff,
        0 0 100px rgba(0,240,255,.5);
}

.cyan .gate-title{
    color:#00f0ff;
}

.violet{
    border:4px solid #d64dff;

    box-shadow:
        0 0 15px #d64dff,
        0 0 50px #d64dff,
        0 0 100px rgba(214,77,255,.5);
}

.violet .gate-title{
    color:#d64dff;
}

.pink{
    border:4px solid #ff0077;

    box-shadow:
        0 0 15px #ff0077,
        0 0 50px #ff0077,
        0 0 100px rgba(255,0,119,.5);
}

.pink .gate-title{
    color:#ff0077;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title">
<h1>LVDVS</h1>
</div>

<div class="subtitle">
scegli il tuo destino
</div>

<div class="gates">

<a class="gate cyan" href="/Discipulus">
<div class="gate-title">DISCIPVLVS</div>
<div class="gate-sub">BEGINNER</div>
</a>

<a class="gate violet" href="/Gladiator">
<div class="gate-title">GLADIATOR</div>
<div class="gate-sub">INTERMEDIATE</div>
</a>

<a class="gate pink" href="/Imperator">
<div class="gate-title">IMPERATOR</div>
<div class="gate-sub">PRO</div>
</a>

</div>
""", unsafe_allow_html=True)
