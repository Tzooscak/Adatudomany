import streamlit as st
import time

# Alapvető oldalbeállítások
st.set_page_config(page_title="Adattudomány 2025", page_icon="🚀", layout="wide")


if "xp" not in st.session_state:
    st.session_state.xp = 120
if "streak" not in st.session_state:
    st.session_state.streak = 3 
if "puska" not in st.session_state:
    st.session_state.puska = []
if "level" not in st.session_state:
    st.session_state.level = 1

st.session_state.level = (st.session_state.xp // 200) + 1
xp_ebben_a_szintben = st.session_state.xp % 200

if st.session_state.level == 1:
    rang = "Kezdő Kockadobó 🎲"
elif st.session_state.level == 2:
    rang = "Bayes-Mester 🧠"
elif st.session_state.level == 3:
    rang = "Kvantum-Guru 🔮"
else:
    rang = "Valószínűség Istene ⚡"

# ==============================================================================
# 2. FEJEZET: OLDALSÁV (SIDEBAR) WIDGETEK - XP PROFIL, POMODORO, PUSKA
# ==============================================================================

# --- FEATURE 1: TANULÓI PROFIL & XP ---
st.sidebar.markdown("## 🏆 Tanulói Profil")
st.sidebar.markdown(f"**Rang:** `{rang}`")
st.sidebar.markdown(f"**Szint:** `{st.session_state.level}`")

# Szintlépési haladási sáv (Progress Bar)
progress_szazalek = min(xp_ebben_a_szintben / 200.0, 1.0)
st.sidebar.progress(progress_szazalek)
st.sidebar.caption(f"✨ {xp_ebben_a_szintben} / 200 XP a következő szintig (Összesen: {st.session_state.xp} XP)")
st.sidebar.markdown(f"🔥 **Napi sorozat:** `{st.session_state.streak} nap`")

st.sidebar.markdown("---")

# --- FEATURE 2: BEÉPÍTETT POMODORO IDŐZÍTŐ ---
st.sidebar.markdown("### 🍅 Pomodoro Fókusz")
pomo_tipus = st.sidebar.radio("Időzítő mód:", ["📚 Tanulás (25 perc)", "☕ Szünet (5 perc)"], label_visibility="collapsed")

if st.sidebar.button("⏱️ Fókusz Blokk Indítása", use_container_width=True):
    st.toast("Fókuszálás elindult! Ne válts oldalt, amíg a csík be nem telik!")
    pomo_bar = st.sidebar.progress(0)
    
    # Szimulált visszaszámlálás látványos vizuális visszajelzéssel
    for i in range(100):
        time.sleep(0.04)  # Tanulási fókuszidő gyorsított szimulációja
        pomo_bar.progress(i + 1)
        
    # Siker és XP jutalom!
    st.session_state.xp += 50
    st.sidebar.success("🎉 +50 XP! Sikeres fókusz blokk!")
    st.balloons()
    st.rerun()

st.sidebar.markdown("---")

# --- FEATURE 3: 📌 SAJÁT PUSKÁM (KÖNYVJELZŐ GYŰJTŐ) ---
st.sidebar.markdown("### 📌 Saját Puskám")
if not st.session_state.puska:
    st.sidebar.caption("Üres a puskád. Kattints a tételeknél lévő 📌 gombokra a mentéshez!")
else:
    for mentett_tetel in st.session_state.puska:
        st.sidebar.markdown(f"- {mentett_tetel}")
        
    if st.sidebar.button("🗑️ Puska kiürítése", use_container_width=True):
        st.session_state.puska = []
        st.toast("Puska sikeresen törölve!")
        st.rerun()

st.sidebar.markdown("---")

# ==============================================================================
# 3. FEJEZET: GYORSKERESŐ ADATBÁZIS ÉS NAVIGÁCIÓ (Eredeti kódod integrálása)
# ==============================================================================
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

# Alkalmazás struktúra oldalai
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