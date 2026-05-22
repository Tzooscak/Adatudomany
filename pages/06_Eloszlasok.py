import streamlit as st
import numpy as np
import pandas as pd

st.title("📈 6. Nevezetes Eloszlások")
st.markdown("---")

tab1, tab2 = st.tabs(["📚 Tételek & Bizonyítások", "🧠 Fogalmak & Szimulációk"])

with tab1:
    # ==========================================================================
    # LEMMA: AZ INDIKÁTORVÁLTOZÓ IS VALÓSZÍNŰSÉGI VÁLTOZÓ
    # ==========================================================================
    with st.expander("Lemma: Az indikátorváltozó is valószínűségi változó"):
        st.write(r"**Állítás:** Az $I_A$ indikátorfüggvény nem csak egy egyszerű halmazelméleti leképezés, hanem a valószínűségszámítás szabályai szerint egy teljes értékű **valószínűségi változó**.")
        st.write(r"Eloszlása (más néven súlyfüggvénye) a következő két diszkrét értéket veheti fel:")
        st.latex(r"P(I_A = 1) = P(A) \quad \text{és} \quad P(I_A = 0) = P(\overline{A}) = 1 - P(A)")
        
        # Többirányú magyarázat blokkok
        col_view1, col_view2 = st.columns(2)
        with col_view1:
            st.info("🎯 **1. Intuitív irány (A Detektor)**\n\nGondolj az indikátorváltozóra úgy, mint egy digitális szenzorra vagy biztonsági riasztóra. Az egyetlen feladata, hogy 'figyelje' az $A$ eseményt. Ha az esemény megtörténik, a szenzor bekapcsol ($1$), ha nem történik meg, kikapcsolva marad ($0$).")
        with col_view2:
            st.warning("💻 **2. Adattudományi irány (One-Hot Encoding)**\n\nEz a tétel az adattudományban használt **Dummy Variable** (fiktív változó) vagy a **One-Hot Encoding** matematikai alapja! Amikor a kategorikus adatokat (pl. 'Férfi'/'Nő' vagy 'Igen'/'Nem') átalakítod $1$-esekké és $0$-kká a gépi tanulási modell számára, pontosan ezt a lemmát használod.")

        if st.checkbox("🔍 Részletes matematikai bizonyítás (Mérhetőség)", key="biz_indikator"):
            st.markdown("##### Miért kell ezt egyáltalán bizonyítani?")
            st.write(r"Ahhoz, hogy egy függvényt *valószínűségi változónak* nevezhessünk, teljesülnie kell a **mérhetőségi feltételnek**. Ez azt jelenti, hogy ha kijelölünk egy tetszőleges valós $x$ korlátot, az $\{I_A < x\}$ halmaznak egy érvényes, mérhető eseménynek kell lennie az $\mathcal{F}$ eseményalgebrában. Bontsuk fel a valós számegyenest 3 logikus szakaszra $x$ értéke alapján:")
            
            st.latex(r"\{I_A < x\} = \begin{cases} \emptyset, & \text{ha } x \le 0 \quad \text{(Mivel az } I_A \text{ sosem negatív, az esemény lehetetlen.)} \\ \overline{A}, & \text{ha } 0 < x \le 1 \quad \text{(Csak a 0 kisebb náluk, vagyis az } A \text{ ellentettje.)} \\ \Omega, & \text{ha } x > 1 \quad \text{(A 0 és az 1 is kisebb nála, ez a biztos esemény.)} \end{cases}")
            
            st.write(r"**Konklúzió:** Mivel az eseményalgebra ($\mathcal{F}$) definíció szerint tartalmazza a lehetetlen eseményt ($\emptyset$), a biztos eseményt ($\Omega$), és zárt a komplementerképzésre ($\overline{A} \in \mathcal{F}$), így az $\{I_A < x\}$ kifejezés minden létező $x$ esetén egy érvényes eseményt ad ki. A függvény tehát mérhető, vagyis **valóban valószínűségi változó**.")
            st.success("A bizonyítás kész! 🎉")

    # ==========================================================================
    # 6.1 TÉTEL: INDIKÁTORVÁLTOZÓ VÁRHATÓ ÉRTÉKE ÉS VARIANCIÁJA
    # ==========================================================================
    with st.expander("6.1 Tétel: Az indikátorváltozó várható értéke és varianciája"):
        st.write(r"**6.1 Tétel:** Legyen $(\Omega, \mathcal{F}, P)$ valószínűségi mező és $I_A$ az $A$ esemény indikátorváltozója. Ekkor a változó karakterisztikus számai:")
        st.latex(r"E(I_A) = P(A) \quad \text{és} \quad D^2(I_A) = P(A)(1 - P(A))")
        
        st.markdown("#### 🧠 A tétel megértése két irányból:")
        
        tab_e, tab_v = st.tabs(["🎯 A Várható érték mögöttes logikája", "⚖️ A Variancia mögöttes logikája"])
        
        with tab_e:
            st.write(r"**Miért pontosan a valószínűség ($p$) a várható érték?**")
            st.write(r"Gondolj a *Nagy Számok Törvényére*. Ha egy kísérletet (pl. kosárra dobás) nagyon sokszor megismételsz, és minden találatnál felírsz egy $1$-est, minden mellédobásnál egy $0$-st, akkor ezeknek a számoknak az átlaga pontosan a **találati arányod** (relatív gyakoriság) lesz. Hosszú távon ez az átlag beáll a kísérlet elméleti valószínűségére ($p$). Ezért a digitális kapcsoló várható értéke maga a valószínűség!")
            
        with tab_v:
            st.write(r"**Miért $p(1-p)$ a szórásnégyzet?**")
            st.write(r"A variancia a **bizonytalanságot** (kockázatot) méri. Nézzük meg a két szélsőséget:")
            st.write(r"- Ha egy esemény biztosan bekövetkezik ($p=1$), vagy biztosan lehetetlen ($p=0$), akkor a variancia $1 \cdot 0 = 0$ vagy $0 \cdot 1 = 0$. Nincs bizonytalanság, pontosan tudjuk az eredményt!")
            st.write(r"- Mikor a legnagyobb a bizonytalanság? Amikor egy érme tökéletesen igazságos ($p=0.5$). Ekkor a variancia eléri a maximumát: $0.5 \cdot 0.5 = 0.25$.")

        if st.checkbox("🔍 Részletes matematikai bizonyítás", key="biz_6_1"):
            st.write(r"Vezessük be a rövidebb $P(A) = p$ jelölést. Ekkor $P(I_A=1)=p$ és $P(I_A=0)=1-p$.")
            
            st.markdown("**1. A Várható érték ($E$) levezetése:**")
            st.write("A diszkrét várható érték definíciója szerint az értékeket megszorozzuk a hozzátartozó valószínűségekkel, majd összeadjuk:")
            st.latex(r"E(I_A) = \sum x_k \cdot P(I_A = x_k) = 1 \cdot p + 0 \cdot (1 - p) = \mathbf{p}")
            
            st.markdown("**2. A Variancia ($D^2$) levezetése:**")
            st.write("Alkalmazzuk a korábban tanult 5.17-es számolási kiskaput: $D^2(\xi) = E(\xi^2) - E^2(\xi)$. Ehhez először ki kell számolnunk a négyzetek várható értékét ($E(I_A^2)$):")
            st.latex(r"E(I_A^2) = 1^2 \cdot p + 0^2 \cdot (1 - p) = p")
            st.write("Most helyettesítsük be ezt és a korábban kapott várható értéket a főképletbe:")
            st.latex(r"D^2(I_A) = E(I_A^2) - E^2(I_A) = p - p^2 = \mathbf{p(1 - p)}")
            st.success("A levezetés matematikai szempontból hibátlan. ✅")

        # --- VIZUÁLIS ELEM: VARIANCE PARABOLA ---
        st.markdown("##### 📊 Vizuális bizonyíték: A bizonytalansági parabola")
        st.write("Az alábbi grafikon a varianciát ($y = p(1-p)$) ábrázolja a siker valószínűségének ($p$) függvényében. Figyeld meg, hogyan csúcsosodik ki pontosan középen!")
        
        # Generálunk egy szép parabola ívet pandas-ban
        p_axis = np.linspace(0.0, 1.0, 100)
        var_axis = p_axis * (1.0 - p_axis)
        df_parabola = pd.DataFrame({"Siker esélye (p)": p_axis, "Variancia / Bizonytalanság (D²)": var_axis})
        
        st.line_chart(df_parabola.set_index("Siker esélye (p)"), color="#ff4b4b")
        st.caption("A grafikon tökéletesen szemlélteti, hogy a bizonytalanság egy Bernoulli-kísérletben szimmetrikus, és 0.5-nél éri el a csúcspontját.")

    # ==========================================================================
    # HELYHETESÍTŐK A KÖVETKEZŐ TÉTELEKNEK
    # ==========================================================================
    with st.expander("6.2 Binomiális eloszlású vv várható értéke és varianciája"):
        st.write("Kidolgozandó...")
        
    with st.expander("6.3 A binomiális eloszlás határeloszlása *"):
        st.write("Kidolgozandó...")
        
    with st.expander("6.4 Poisson-eloszlású vv várható értéke és varianciája *"):
        st.write("Kidolgozandó...")

with tab2:
    # ==========================================================================
    # KULCSFOGALOM: INDIKÁTORVÁLTOZÓ ÉS BERNOULLI-ELOSZLÁS DEFINÍCIÓJA
    # ==========================================================================
    st.markdown("### 1. Az Indikátorváltozó és a Bernoulli-eloszlás")
    st.write(r"Legyen $(\Omega, \mathcal{F}, P)$ valószínűségi mező és $A \in \mathcal{F}$ egy tetszőleges esemény. Az $A$ esemény **indikátorváltozójának** nevezzük a következő függvényt:")
    
    st.latex(r"I_A : \Omega \rightarrow \mathbb{R}, \quad I_A(\omega) = \begin{cases} 1, & \text{ha } \omega \in A, \\ 0, & \text{ha } \omega \notin A. \end{cases}")
    
    st.write(r"Ha egy valószínűségi változó kizárólag ezt az eloszlást követi, akkor azt **Bernoulli-eloszlásnak** nevezzük, melynek egyetlen paramétere a $p = P(A)$ (a siker valószínűsége).")
    
    st.markdown("---")
    
    # ==========================================================================
    # INTERAKTÍV JÁTÉKOS SZIMULÁCIÓ
    # ==========================================================================
    st.markdown("##### 🪙 Interaktív Szimulátor: Teszteld a Bernoulli-eloszlást!")
    st.write("Állíts be egy tetszőleges siker-valószínűséget (pl. egy hamisított érme vagy egy kosárra dobás esélyét), és indíts el egy gombnyomással egy valódi kísérletet a háttérben!")
    
    p_sim = st.slider("Siker valószínűsége (p) a szimulációban:", 0.0, 1.0, 0.7, 0.05)
    
    if st.button("🎲 Kísérlet elindítása!", use_container_width=True):
        import random
        # Generálunk egy véletlen számot 0 és 1 között
        veletlen = random.random()
        
        st.write(f"A generált háttér-valószínűség: `{veletlen:.4f}`")
        
        if veletlen <= p_sim:
            st.success(f"🎉 **SIKER!** Mivel a véletlen szám kisebb vagy egyenlő, mint {p_sim}, az esemény bekövetkezett ($\omega \in A$). Az indikátorváltozó értéke: **$I_A = 1$**")
        else:
            st.error(f"❌ **KUDARC!** Mivel a véletlen szám nagyobb, mint {p_sim}, az esemény nem következett be ($\omega \notin A$). Az indikátorváltozó értéke: **$I_A = 0$**")

    st.markdown("---")
    st.markdown("### További kulcsfogalmak ebben a fejezetben")
    st.write("- **Binomiális eloszlás:** Amikor nem egy, hanem $n$ darab teljesen független Bernoulli-kísérletet végzünk el egymás után, és számoljuk a sikerek számát (Kidolgozandó...).")
    st.write("- **Poisson-eloszlás:** Ritka események száma adott időintervallum vagy térfogat alatt, a binomiális eloszlás határeloszlása (Kidolgozandó...).")