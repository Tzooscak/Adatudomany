import streamlit as st

st.title("📊 5. Valószínűségi változó")
st.markdown("---")

tab1, tab2 = st.tabs(["📚 Tételek", "🧠 Fogalmak"])

with tab1:
    st.info("Ez a fejezet tartalmazza a legtöbb tételt (5.1 - 5.25) [cite: 1415-1441].")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("5.1 - 5.5 Alapok"):
            st.write("5.1 Valószínűségi változók és események [cite: 1417]")
            st.write("5.3 Diszkrét eloszlás összege [cite: 1419]")
            st.write("5.5 Eloszlásfüggvény tulajdonságai * [cite: 1421]")
        with st.expander("5.6 - 5.12 Folytonos változók"):
            st.write("5.9 {a ≤ ξ < b} és a sűrűségfüggvény [cite: 1425]")
            st.write("5.11 Sűrűségfüggvény integrálja [cite: 1427]")
    
    with col2:
        with st.expander("5.15 - 5.18 Várható érték és Szórás"):
            st.write("5.16 A várható érték tulajdonságai [cite: 1432]")
            st.write("5.18 A szórás tulajdonságai * [cite: 1434]")
        with st.expander("5.19 - 5.25 Kapcsolatok"):
            st.write("5.19 A kovariancia kiszámolása [cite: 1435]")
            st.write("5.20 Kovariancia és függetlenség [cite: 1436]")
            st.write("5.25 Korreláció és függőség * [cite: 1441]")

with tab2:
    st.markdown("### Kulcsfogalmak [cite: 1442-1443]")
    st.write("- Diszkrét vs Abszolút folytonos változók")
    st.write("- CDF (Eloszlásfüggvény) és PDF (Sűrűségfüggvény)")
    st.write("- Momentumok, Variancia, Kovariancia, Korreláció")
    st.write("- Standardizált változó")