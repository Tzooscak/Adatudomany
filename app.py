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

# Szint és Rang kiszámítása dinamikusan az XP alapján (Minden 200 XP egy szint)
st.session_state.level = (st.session_state.xp // 200) + 1
xp_ebben_a_szintben = st.session_state.xp % 200

# 50+ Szintből álló rangrendszer (Dictionary alapú leképezés)
rangok = {
    1: "Kezdő Kockadobó 🎲",
    2: "Érmefeldobó Tanonc 🪙",
    3: "Relatív Gyakoriság Lovagja 🏇",
    4: "Eseménytér Felfedezője 🔭",
    5: "Szigma-Algebra Újonc 🔰",
    6: "Halmazelméleti Padavan 🤺",
    7: "Metszet-Mágus ⚔️",
    8: "Unió-Uraság 🤝",
    9: "Komplementer Kapitány 🏴‍☠️",
    10: "Kolmogorov Kegyeltje 📜",
    11: "Klasszikus Valószínűség Látnoka 👁️",
    12: "Geometriai Valószínűség Geometre 📐",
    13: "Feltételes Valószínűség Felfedező 🔗",
    14: "Szorzástétel Szamuráj 🥷",
    15: "Teljes Valószínűség Taktikusa 🗺️",
    16: "Bayes-Tanonc 🕵️",
    17: "Bayes-Mester 🧠",
    18: "Függetlenség Harcosa 🦅",
    19: "Diszkrét Változók Bajnoka 📊",
    20: "Folytonos Változók Főpapja 🌊",
    21: "Eloszlásfüggvény Építész 🏗️",
    22: "Sűrűségfüggvény Suttogó 🌬️",
    23: "Integrál Mágus 🪄",
    24: "Várható Érték Vadász 🎯",
    25: "Szórás-Szamuráj 🌪️",
    26: "Kovariancia Kapitány ⚓",
    27: "Korreláció Király/Királynő 👑",
    28: "Binomiális Báró 🎩",
    29: "Poisson Próféta 🕰️",
    30: "Hipergeometriai Herceg 🏰",
    31: "Geometriai Eloszlás Grófja 💎",
    32: "Egyenletes Eloszlás Egyensúlyozója ⚖️",
    33: "Normális Eloszlás Nindzsa 🥷",
    34: "Haranggörbe Huszár 🔔",
    35: "Exponenciális Emisszárius 🚀",
    36: "Markov-Egyenlőtlenség Mágusa 🧙",
    37: "Csebisev Lovagrend Vezére 🛡️",
    38: "Nagy Számok Törvényének Tudósa 📜",
    39: "Centrális Határeloszlás Császára 🏛️",
    40: "Generátorfüggvény Géniusz 🧬",
    41: "Karakterisztikus Függvény Khán ⛺",
    42: "Sztochasztikus Szelídítő 🦁",
    43: "Kvantum-Guru 🔮",
    44: "Valószínűségi Változók Varázslója 🪄",
    45: "Entrópia Ellenőr 🌌",
    46: "Káoszelmélet Kutató 🌀",
    47: "Valószínűségi Tér Tervezője 🌌",
    48: "Sztochasztikus Folyamatok Fantomja 👻",
    49: "Matematikai Statisztika Mestere 📈",
    50: "Adattudomány Félistene 🧬",
    51: "Sztochasztikus Szupernóva 💥"
}

# A rang kiválasztása: ha túllépi az 51-es szintet, alapértelmezetten a legmagasabbat kapja
rang = rangok.get(st.session_state.level, "Valószínűség Istene ⚡")

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