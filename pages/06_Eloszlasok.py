import streamlit as st

st.title("📈 6. Nevezetes Eloszlások")
st.markdown("---")

tab1, tab2 = st.tabs(["📚 Tételek", "🧠 Fogalmak"])

with tab1:
    with st.expander("Indikátorváltozó (lemma)"):
        st.write("Kidolgozandó... [cite: 1446]")
    with st.expander("6.1 Indikátorváltozó várható értéke és varianciája"):
        st.write("Kidolgozandó... [cite: 1447]")
    with st.expander("6.2 Binomiális eloszlású vv várható értéke és varianciája"):
        st.write("Kidolgozandó... [cite: 1448]")
    with st.expander("6.3 A binomiális eloszlás határeloszlása *"):
        st.write("Kidolgozandó... [cite: 1449]")
    with st.expander("6.4 Poisson-eloszlású vv várható értéke és varianciája *"):
        st.write("Kidolgozandó... [cite: 1450]")

with tab2:
    st.markdown("### Kulcsfogalmak [cite: 1451-1452]")
    st.write("- Bernoulli-eloszlás")
    st.write("- Binomiális eloszlás")
    st.write("- Poisson-eloszlás")