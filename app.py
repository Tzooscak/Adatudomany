import streamlit as st

# Ez kötelezően az első parancs kell legyen!
st.set_page_config(page_title="Adattudomány 2025", page_icon="🚀", layout="wide")

# Modern navigációs struktúra felépítése
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
    ]
}

# Navigáció indítása
pg = st.navigation(pages)
pg.run()