import streamlit as st

st.set_page_config(page_title="Adattudomány 2025", page_icon="🚀", layout="wide")

kereso_adatbazis = {
    "Elemi és összetett események": "pages/01_Valoszinuseg.py",
    "Eseményalgebra (Unió, Metszet)": "pages/01_Valoszinuseg.py",
    "Relatív gyakoriság": "pages/01_Valoszinuseg.py",
    "Szigma-algebra (σ-algebra)": "pages/01_Valoszinuseg.py",
    "Kolmogorov axiómák (K1, K2, K3)": "pages/02_Axiomak.py",
    "Szita-formula": "pages/02_Axiomak.py",
    "Klasszikus valószínűségi mező": "pages/02_Axiomak.py",
    "Geometriai valószínűségi mező": "pages/02_Axiomak.py",
    "Feltételes valószínűség": "pages/03_Felteteles.py",
    "Szorzástétel": "pages/03_Felteteles.py",
    "Teljes valószínűség tétele": "pages/03_Felteteles.py",
    "Bayes-tétel": "pages/03_Felteteles.py",
    "Kizárás és függetlenség 1. alak": "pages/04_Fuggetlenseg.py",
    "Kizárás és függetlenség 2. alak": "pages/04_Fuggetlenseg.py",
    "Eseményrendszerek teljes függetlensége": "pages/04_Fuggetlenseg.py"
}

st.sidebar.markdown("### 🔍 Gyorskereső")
kivalasztott_tema = st.sidebar.selectbox("Ugrás a tételre:", ["-- Válassz --"] + list(kereso_adatbazis.keys()))

if kivalasztott_tema != "-- Válassz --":
    cel_oldal = kereso_adatbazis[kivalasztott_tema]
    if st.sidebar.button(f"🚀 Ugrás: {kivalasztott_tema}", use_container_width=True):
        st.switch_page(cel_oldal)

st.sidebar.markdown("---")

pages = {
    "Áttekintés": [
        st.Page("pages/00_Kezdolap.py", title="Kezdőlap", icon="🏠"),
    ],
    "1. Rész: Alapok": [
        st.Page("pages/01_Valoszinuseg.py", title="1. A valószínűség bevezetése", icon="🎲"),
        st.Page("pages/02_Axiomak.py", title="2. Kolmogorov axiómái", icon="📐"),
    ],
    "2. Rész: Haladó Valószínűségszámítás": [
        st.Page("pages/03_Felteteles.py", title="3. Feltételes valószínűség", icon="🔗"),
        st.Page("pages/04_Fuggetlenseg.py", title="4. Események függetlensége", icon="⚡"),
    ],
    "3. Rész: Változók és Eloszlások": [
        st.Page("pages/05_Valtozok.py", title="5. Valószínűségi változó", icon="📊"),
        st.Page("pages/06_Eloszlasok.py", title="6. Nevezetes Eloszlások", icon="📈"),
    ],
    "Gyakorlás": [
        st.Page("pages/99_Gyakorlas.py", title="Vizsga Szimulátor", icon="🎓"),
    ]
}

pg = st.navigation(pages)
pg.run()