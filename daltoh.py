import streamlit as st
from PIL import Image

st.set_page_config(page_title="Los guanacos en el exilio", layout="wide")

if "bg_color" not in st.session_state:
    st.session_state["bg_color"] = "#647587"  # Initial color
if "show_outline" not in st.session_state:
    st.session_state["show_outline"] = False

def scroll_to_outline():
    st.session_state["bg_color"] = "#877664"
    st.session_state["show_outline"] = True

def reset_bg():
    st.session_state["bg_color"] = "#647587"
    st.session_state["show_outline"] = False

# Dynamic CSS injects current bg color and all previous style
custom_css = f"""
<style>
body, [data-testid="stAppViewContainer"] {{
    background: {st.session_state['bg_color']} !important;
    font-family: 'Inter', Arial, sans-serif;
    transition: background 0.8s cubic-bezier(.61,.01,.11,.99);
}}
.stApp > header {{
    position: sticky !important;
    top: 0;
    z-index: 99;
    background: #D8D8F6 !important;
    box-shadow: 0 1.5px 10px #97889722;
}}
.lg-text {{
    font-family: 'Inter', Arial, sans-serif;
    font-size: 2.7rem!important;
    font-weight: 800;
    color: #dbdbeb;
    margin-bottom: 2.2rem;
}}
h2, h3 {{
    font-family: 'Inter';
    color: #d6d3e8;
    font-weight: 700;
}}
p, li, .section {{
    font-family: 'Inter';
    color: #d6d3e8;
    font-size: 1.13rem;
    line-height: 1.7;
}}
.section {{
    background: #B18FCF;
    border-radius: 16px;
    padding: 1.9em 2em;
    margin-bottom: 2rem;
    box-shadow: 0 2px 18px #49485040;
    font-family: 'Inter';
    color: #2C2C34;
}}
.section-alt {{
    background: #978897;
    border-radius: 18px;
    padding: 2em 2em;
    margin-bottom: 2rem;
    box-shadow: 0 1.5px 14px #49485030;
    font-family: 'Inter';
    color: #2C2C34;
}}
.final-idea {{
    background: #2C2C34;
    color: #D8D8F6;
    border-radius: 26px;
    padding: 3em 2em;
    margin-top: 1.2em;
    animation: fadeInUp 1.1s cubic-bezier(.31,.16,.47,.97);
    box-shadow: 0 6px 44px #97889799;
    font-family: 'Inter';
}}
@keyframes fadeInUp {{
    0% {{opacity: 0; transform: translateY(40px);}}
    100% {{opacity: 1; transform: translateY(0);}}
}}
.footer {{
    margin-top: 4rem;
    background: #B18FCF;
    color: #2C2C34;
    padding: 2rem;
    border-radius: 18px;
    font-size: 1.04rem;
    text-align: center;
    font-family: 'Inter';
}}
hr {{
    border: none;
    background: #B18FCF;
    height: 2px;
    margin: 3rem 0;
}}
img {{
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: 0px 8px 24px #49485023;
}}
.stButton > button {{
    background: #978897;
    color: #fff;
    border-radius: 12px;
    font-family: 'Inter';
    font-size: 1.17rem;
    padding: 0.7em 2em;
    box-shadow: 0 3px 16px #49485032;
    border: none;
}}
.stButton > button:hover {{
    background: #f2dfdf;
    color: #D8D8F6;
    box-shadow: 0 7px 28px #2C2C3466;
}}
@media (max-width:900px){{
    .section, .footer, .hero-img {{padding:1em;}}
    .lg-text {{font-size: 1.45rem!important;}}
    .final-idea {{padding: 1.2em 1em;}}
}}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

st.markdown('<div class="lg-text">Los Guanacos En El Exilio<br>Contexto y resistencia en ‘Poema de Amor’ de Roque Dalton</div>', unsafe_allow_html=True)
st.write("SPA 70 | Diego Ramirez | Profesora Martinez<br> 21 de Noviembre de 2025", unsafe_allow_html=True)

try:
    dalton_img = Image.open("roque Dalton.jpg")
    st.image(dalton_img, use_container_width=True)
except Exception:
    st.warning("check jpg bruh")

st.markdown("""
<div class="section">
<h2>Un Trauma Nacional</h2>
<p>
El Salvador venía arrastrando la herida de la Matanza de 1932, dictaduras, migración y exclusión. Dalton expresa la ansiedad, la resiliencia y la lucha histórica de los guanacos a través del exilio y la poesía testimonial.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-alt">
<h2>La Migración, Los Trabajo, y La Resistencia</h2>
<p>
Los migrantes enfrentaron marginación en ‘silver roll’ y ‘golden roll’, murieron en bananeras y canales, y forjaron nuevas identidades a partir del trauma y la desigualdad. Dalton dignifica y universaliza su experiencia.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
<h2>Militancia y testimonio literario</h2>
<p>
Dalton no solo narra, sino integra su vida de exilio, resistencia política y creación literaria. ‘Poema de Amor’ y su obra transforman sufrimiento en memoria y signo de dignidad latinoamericana.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)

# Button row always present, changes state/calls rerun
colA, colB = st.columns([1,1])
with colA:
    if st.button("Como Planeo Estructurar Mi Ensayo?"):
        scroll_to_outline()
       
with colB:
    if st.button("Cambiar el color del fondo :D"):
        reset_bg()
        

# Show outline only if requested
if st.session_state.get("show_outline", False):
    st.markdown("""
    <div class="final-idea">
        <h2>La Conexión Final</h2>
        <ul>
            <li><b>Ansiedad central:</b> Miedo al olvido de la memoria colectiva, dolor del exilio y la marginación socioeconómica.</li>
            <li><b>Estructura :</b>
                <ul>
                    <li>Centro: ‘Poema de Amor’ y la ansiedad universal</li>
                    <li>Rama 1: Trauma de 1932 (Mosquera, Harlow)</li>
                    <li>Rama 2: Explotación migrante (Shragai, O’Sullivan)</li>
                    <li>Rama 3: Testimonio y militancia (Rodríguez Gutiérrez)</li>
                    <li>Rama 4: Identidad y creación cultural (Dalton)</li>
                    <li>Todos vuelven a:<b> Memoria y dignidad latinoamericana universalizada por Dalton</b></li>
                </ul>
            </li>
            <li><b>¿Que Ansiedad Se Revela?</b>
                <ul>
                    <li>El trauma, la invisibilidad y la fuerza colectiva del exilio</li>
                </ul>
            <li><b> ¿Cómo conecta con la historia latinoamericana? </b> 
                <ul>
                    <li>Dalton convierte lo personal en símbolo universal de la lucha por la memoria</li>
                </ul>
            </li>
            <li><b>Bibliografía clave:</b> Mosquera, Harlow, Rodríguez Gutiérrez, Shragai, O'Sullivan</li>
        </ul>
        <p style="margin-top:2.2em; font-size:1.17rem;">Dalton universaliza el destino del migrante salvadoreño y su ansiedad histórica, transformando el sufrimiento en testimonio revolucionario.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
<b>Bibliografía académica:</b><br>
Mosquera, Juan Góngora (1991) · Harlow, Barbara (1991) · Rodríguez Gutiérrez, Milena (2023)<br>
Shragai, Atalia (2011) · O’Sullivan, Kevin (2021)
<hr>
 Semester Project 3: Outline · Diego Ramirez  · Espero Que Le Gusten Me Tarde Mucho Haciendo Esto
</div>
""", unsafe_allow_html=True)
