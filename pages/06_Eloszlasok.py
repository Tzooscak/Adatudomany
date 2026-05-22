import streamlit as st

st.title("📈 6. Nevezetes Eloszlások")
st.markdown("---")

tab1, tab2 = st.tabs(["📚 Tételek", "🧠 Fogalmak"])

with tab1:
    with st.expander("Lemma: Az indikátorváltozó is valószínűségi változó"):
        # ==========================================
        # LEMMA: INDIKÁTORVÁLTOZÓ
        # ==========================================
        st.write(r"**Lemma:** Az indikátorváltozó is valószínűségi változó.")
        st.write(r"Az $I_A$ eloszlása a következőképpen alakul:")
        st.latex(r"P(I_A = 1) = P(A) \quad \text{és} \quad P(I_A = 0) = P(\overline{A}) \quad \text{}")
        
        st.info(r"💡 **Konyhanyelven:** Ha az $A$ esemény mondjuk az, hogy 'Hatos dobunk', akkor az indikátorváltozó 1 lesz (aminek esélye $1/6$), ha pedig nem hatost dobunk, akkor 0 lesz (aminek esélye $5/6$).")

        if st.checkbox("💡 Bizonyítás mutatása", key="biz_indikator"):
            st.write(r"Azt kell látni, hogy bármely valós $x$-re az $\{I_A < x\}$ egy érvényes esemény. Bontsuk esetekre $x$ értéke alapján:")
            
            st.latex(r"\{I_A < x\} = \begin{cases} \emptyset, & \text{ha } x \le 0, \\ \overline{A}, & \text{ha } 0 < x \le 1, \\ \Omega, & \text{ha } x > 1. \end{cases} \quad \text{}")
            
            st.success(r"Mivel a lehetetlen esemény ($\emptyset$), a komplementer esemény ($\overline{A}$) és a biztos esemény ($\Omega$) mind elemei az eseményalgebrának, az állítás igaz.")

    with st.expander("6.1 Indikátorváltozó várható értéke és varianciája"):
        st.write("Kidolgozandó...")
        
    with st.expander("6.2 Binomiális eloszlású vv várható értéke és varianciája"):
        st.write("Kidolgozandó...")
        
    with st.expander("6.3 A binomiális eloszlás határeloszlása *"):
        st.write("Kidolgozandó...")
        
    with st.expander("6.4 Poisson-eloszlású vv várható értéke és varianciája *"):
        st.write("Kidolgozandó...")

with tab2:
    # ==========================================
    # 1. INDIKÁTORVÁLTOZÓ DEFINÍCIÓ
    # ==========================================
    st.markdown("### 1. Indikátorváltozó")
    st.write(r"Legyen $(\Omega, \mathcal{F}, P)$ valószínűségi mező és értelmezzük egy $A \in \mathcal{F}$ eseményre a következő függvényt:")
    
    st.latex(r"I_A : \Omega \rightarrow \mathbb{R}, \quad I_A(\omega) = \begin{cases} 1, & \text{ha } \omega \in A, \\ 0, & \text{ha } \omega \notin A. \end{cases} \quad \text{}")
    
    st.write(r"Ezt az $I_A$ függvényt az $A$ esemény **indikátorváltozójának** nevezzük.")
    
    st.markdown("---")
    st.markdown("##### 🪙 Szimuláció: Pénzfeldobás indikátora")
    st.write(r"Legyen a kísérlet egy pénzfeldobás, az $A$ esemény pedig az, hogy **Fejet** dobunk. Az $I_A$ indikátorváltozó értéke 1 lesz, ha Fej, és 0, ha Írás.")
    
    if st.button("🎲 Pénzfeldobás szimulálása", use_container_width=True):
        import random
        eredmeny = random.choice(["Fej", "Írás"])
        
        if eredmeny == "Fej":
            st.success(rf"**Eredmény: {eredmeny}** $\implies \omega \in A$, ezért az indikátorváltozó értéke: $\mathbf{{I_A = 1}}$")
        else:
            st.error(rf"**Eredmény: {eredmeny}** $\implies \omega \notin A$, ezért az indikátorváltozó értéke: $\mathbf{{I_A = 0}}$")

    st.markdown("---")
    st.markdown("### További kulcsfogalmak")
    st.write("- Bernoulli-eloszlás (Kidolgozandó...)")
    st.write("- Binomiális eloszlás (Kidolgozandó...)")
    st.write("- Poisson-eloszlás (Kidolgozandó...)")