import streamlit as st
import random

st.title("🎓 Vizsga Szimulátor (1-4. Fejezet)")
st.markdown("Minden indításkor egy új, véletlenszerűen generált 5 kérdéses tesztet kapsz az eddigi anyagokból!")
st.markdown("---")

# ==========================================
# BEÉPÍTETT KÉRDÉSBANK (Neked nem kell írni semmit!)
# ==========================================
NAGY_KERDESBANK = [
    {
        "kerdes": "Mit mond ki Kolmogorov 1. axiómája (K1)?", 
        "valaszok": ["Minden esemény valószínűsége 0 és 1 között van.", "A biztos esemény valószínűsége 1.", "Bármely A esemény valószínűsége nemnegatív: P(A) ≥ 0.", "A lehetetlen esemény valószínűsége 0."], 
        "helyes": 2
    },
    {
        "kerdes": "A 4.1-es tétel szerint, ha két esemény (A és B) P(A)P(B) ≠ 0 mellett egymást kizáróak, akkor...", 
        "valaszok": ["Garantáltan függetlenek is.", "Teljes eseményrendszert alkotnak.", "Biztosan NEM függetlenek.", "A metszetük valószínűsége 1."], 
        "helyes": 2
    },
    {
        "kerdes": "Mi a klasszikus valószínűségi mező alapképlete tetszőleges A eseményre?", 
        "valaszok": ["P(A) = Kedvező esetek / Összes eset", "P(A) = Terület(A) / Terület(Ω)", "P(A) = 1 - P(B)", "P(A|B) * P(B)"], 
        "helyes": 0
    },
    {
        "kerdes": "Mire ad választ a Bayes-tétel a gyakorlatban?", 
        "valaszok": ["A geometriai alakzatok területére.", "Az 'okok' (kiinduló feltételek) valószínűségének visszaszámolására.", "A végtelen additivitás bizonyítására.", "Kizáró események összeadására."], 
        "helyes": 1
    },
    {
        "kerdes": "Mit jelent a szigma-additivitás (K3 axióma)?", 
        "valaszok": ["Egymást páronként kizáró események uniójának valószínűsége megegyezik a valószínűségeik összegével.", "Minden esemény független egymástól.", "A teljes eseményrendszer összege 1.", "A metszet valószínűsége a valószínűségek szorzata."], 
        "helyes": 0
    },
    {
        "kerdes": "A geometriai valószínűségi mezőnél hogyan számoljuk P(A)-t?", 
        "valaszok": ["Kedvező esetek száma / Összes eset száma", "λ(A) / λ(Ω) (ahol λ a mérték, pl. terület)", "P(A|B) / P(B)", "A derivált segítségével."], 
        "helyes": 1
    },
    {
        "kerdes": "A Feltételes valószínűség tulajdonságai (3.3 tétel) alapján mennyi P(A|B), ha B részhalmaza A-nak (B ⊆ A)?", 
        "valaszok": ["0", "P(B) - P(A)", "1", "0.5"], 
        "helyes": 2
    },
    {
        "kerdes": "Hogyan szól a Szorzástétel (3.1 tétel)?", 
        "valaszok": ["P(AB) = P(A) + P(B)", "P(AB) = P(A|B) * P(B)", "P(A|B) = P(AB) / P(A)", "P(A+B) = P(A)P(B)"], 
        "helyes": 1
    },
    {
        "kerdes": "Mit értünk 'Triviális σ-algebra' alatt?", 
        "valaszok": ["Csak az üres halmazt tartalmazza.", "A teljes hatványhalmazt.", "Az {∅, Ω} halmazt.", "Kizárólag az elemi eseményeket tartalmazza."], 
        "helyes": 2
    },
    {
        "kerdes": "A Szita-formula alapján mennyi P(A+B)?", 
        "valaszok": ["P(A) + P(B)", "P(A) * P(B)", "P(A) + P(B) + P(AB)", "P(A) + P(B) - P(AB)"], 
        "helyes": 3
    }
]

# ==========================================
# KVÍZ GENERÁTOR LOGIKA (Session State)
# ==========================================
# Csak az első betöltéskor sorsolunk 5 random kérdést
if "aktualis_kviz" not in st.session_state:
    st.session_state.aktualis_kviz = random.sample(NAGY_KERDESBANK, 5)
    st.session_state.kviz_index = 0
    st.session_state.pontszam = 0
    st.session_state.kviz_vege = False

if not st.session_state.kviz_vege:
    aktualis_kerdes = st.session_state.aktualis_kviz[st.session_state.kviz_index]
    
    st.markdown(f"### {st.session_state.kviz_index + 1}. Kérdés (5-ből)")
    st.write(f"**{aktualis_kerdes['kerdes']}**")
    
    valasz = st.radio("Válaszd ki a helyes megfejtést:", aktualis_kerdes["valaszok"], index=None)
    
    if st.button("Válasz beküldése", type="primary"):
        if valasz is None:
            st.warning("Kérlek válassz ki egy választ a beküldés előtt!")
        else:
            helyes_valasz_szoveg = aktualis_kerdes["valaszok"][aktualis_kerdes["helyes"]]
            if valasz == helyes_valasz_szoveg:
                st.success("✅ Helyes válasz! Szép munka.")
                st.session_state.pontszam += 1
            else:
                st.error(f"❌ Helytelen. A helyes válasz: {helyes_valasz_szoveg}")
            
            if st.session_state.kviz_index < 4:
                st.session_state.kviz_index += 1
                st.rerun() 
            else:
                st.session_state.kviz_vege = True
                st.rerun()
                
else:
    # Eredményhirdetés
    st.balloons()
    st.success(f"🎉 Kvíz vége! Elért pontszám: **{st.session_state.pontszam} / 5**")
    
    # Újrageneráló gomb
    if st.button("🔄 Új kvíz generálása (Másik 5 kérdés)"):
        st.session_state.aktualis_kviz = random.sample(NAGY_KERDESBANK, 5)
        st.session_state.kviz_index = 0
        st.session_state.pontszam = 0
        st.session_state.kviz_vege = False
        st.rerun()