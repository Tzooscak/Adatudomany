import streamlit as st

st.title("⚡ 4. Események függetlensége")
st.markdown("---")

tab1, tab2 = st.tabs(["📚 Tételek", "🧠 Fogalmak"])

with tab1:
    with st.expander("4.1 Kizárás és függetlenség 1. alak"):
        # ==========================================
        # 4.1 TÉTEL: KIZÁRÁS ÉS FÜGGETLENSÉG 1. ALAK
        # ==========================================
        st.write(r"Legyen $(\Omega, \mathcal{F}, P)$ valószínűségi mező, $A, B \in \mathcal{F}$ és $P(A)P(B) \neq 0$.")
        st.write("Ha $A$ és $B$ egymást kizáróak, akkor **nem függetlenek**.")

        st.markdown("**Részletes magyarázat:**")
        st.write("A mindennapi nyelvben a 'kizárják egymást' és a 'függetlenek' szavakat gyakran rokon értelműként használjuk, de a matematikában a kettő pont a szöges ellentéte egymásnak! Ha két esemény kizárja egymást, akkor a legnagyobb mértékben *függenek* egymástól: ha tudom, hogy az egyik megtörtént, abból 100%-os biztonsággal tudom, hogy a másik nem történhetett meg.")

        if st.checkbox("💡 Részletes Bizonyítás (4.1)", key="biz4_1"):
            st.info("A bizonyítás nagyon egyszerű, csak a függetlenség definícióját és az üres halmaz valószínűségét kell használni.")
            st.write("1. Mivel $A$ és $B$ egymást kizáróak, a metszetük üres halmaz ($AB = \emptyset$).")
            st.write("2. A (K1) axióma értelmében a lehetetlen esemény valószínűsége nulla:")
            st.latex(r"P(AB) = P(\emptyset) = 0")
            st.write("3. A feltétel szerint $P(A) \neq 0$ és $P(B) \neq 0$, tehát a szorzatuk sem lehet nulla:")
            st.latex(r"P(A)P(B) \neq 0")
            st.write("4. Mivel a két oldal nem egyenlő, az események definíció szerint nem lehetnek függetlenek:")
            st.latex(r"P(AB) \neq P(A)P(B)")

        st.markdown("##### 🪙 Szimuláció 4.1: A Pénzfeldobás")
        st.write("Dobjunk fel egy pénzérmét. Legyen az $A$ esemény a Fej, a $B$ esemény az Írás. Kizárják egymást? Igen. Függetlenek? Számoljunk!")
        
        p_fej = 0.5
        p_iras = 0.5
        
        st.latex(rf"P(\text{{Fej}}) \cdot P(\text{{Írás}}) = {p_fej} \cdot {p_iras} = \mathbf{{{p_fej*p_iras}}}")
        st.latex(rf"P(\text{{Fej ÉS Írás egyszerre}}) = P(\emptyset) = \mathbf{{0}}")
        st.error(f"**Eredmény:** Mivel $0 \neq 0.25$, a Fej és az Írás dobása matematikai értelemben **NEM független** események (hiszen erősen függenek egymástól: ha az egyik bejön, a másik biztosan nem)!")

    with st.expander("4.2 Kizárás és függetlenség 2. alak"):
        # ==========================================
        # 4.2 TÉTEL: KIZÁRÁS ÉS FÜGGETLENSÉG 2. ALAK
        # ==========================================
        st.write(r"Legyen $(\Omega, \mathcal{F}, P)$ valószínűségi mező, $A, B \in \mathcal{F}$ és $P(A)P(B) \neq 0$.")
        st.write("Ha $A$ és $B$ függetlenek, akkor **nem egymást kizáróak**.")

        st.markdown("**Részletes magyarázat:**")
        st.write("Ez a tétel pontosan az előző (4.1) tétel logikai megfordítása (úgynevezett kontrapozíciója). Ha két esemény valóban független egymástól, akkor lennie kell egy olyan 'metszetnek', ahol mindkettő egyszerre is be tud következni.")

        if st.checkbox("💡 Részletes Bizonyítás (4.2)", key="biz4_2"):
            st.info("Nincs szükség új matematikai levezetésre, az állítás pusztán az előző tétel logikai kontrapozíciójából (Ha P, akkor Q $\implies$ Ha nem Q, akkor nem P) adódik:")
            st.latex(r"(A \cap B = \emptyset) \implies (P(AB) \neq P(A)P(B))")
            st.write("Ennek a logikai megfordítása:")
            st.latex(r"(P(AB) = P(A)P(B)) \implies (A \cap B \neq \emptyset)")

        st.markdown("##### 🃏 Szimuláció 4.2: Független, de nem kizáró események")
        st.write("Húzzunk egy véletlenszerű lapot egy 52 lapos francia kártyapakliból.")
        st.write("* $A$ esemény: A húzott lap **Pikk** (13 lap).")
        st.write("* $B$ esemény: A húzott lap **Király** (4 lap).")

        st.write("Számoljuk ki a valószínűségek szorzatát:")
        st.latex(r"P(\text{Pikk}) \cdot P(\text{Király}) = \frac{13}{52} \cdot \frac{4}{52} = \frac{1}{4} \cdot \frac{1}{13} = \mathbf{\frac{1}{52}}")
        
        st.write("Mivel pontosan **1 db Pikk Király** van a pakliban, a metszet (Pikk ÉS Király) valószínűsége:")
        st.latex(r"P(\text{Pikk} \cap \text{Király}) = \mathbf{\frac{1}{52}}")

        st.success("**Eredmény:** Látod? A két érték tökéletesen megegyezik ($1/52 = 1/52$), tehát a 'Pikk húzása' és a 'Király húzása' **független** események. És mivel van közös lapjuk (a metszetük nem üres), a tételnek megfelelően **NEM zárják ki egymást**!")

with tab2:
    st.header("🧠 Fogalmak definíciói")
    st.write("A 4. fejezethez (Események függetlensége) tartozó hivatalos definíciók:")

    # ==========================================
    # 1. KÉT ESEMÉNY FÜGGETLENSÉGE
    # ==========================================
    st.markdown("### 1. Két esemény függetlensége")
    st.write(r"Legyen $(\Omega, \mathcal{F}, P)$ valószínűségi mező és $A, B \in \mathcal{F}$.")
    st.write("Ekkor azt mondjuk, hogy az $A$ esemény **független** a $B$-től, ha:")
    st.latex(r"P(AB) = P(A) \cdot P(B)")

    st.markdown("### 2. Eseményrendszerek (teljes) függetlensége")
    st.write(r"Legyen $(\Omega, \mathcal{F}, P)$ valószínűségi mező és $\mathcal{F} \supseteq \mathcal{H} := \{A_i \in \mathcal{F} : i = 1, 2, \dots, n\}$.")
    st.write(r"Ekkor $\mathcal{H}$ eseményrendszer elemeit **(teljesen) függetlennek nevezzük**, ha bármely $\mathcal{G} \subseteq \mathcal{H}$ esetén:")
    st.latex(r"P\left(\prod_{A_i \in \mathcal{G}} A_i\right) = \prod_{A_i \in \mathcal{G}} P(A_i)")
    st.write(r"Ha $\mathcal{H}$ végtelen, akkor elemei függetlenek, ha bármely véges részrendszere független.")
    
    st.info("💡 **Magyarázat a képlethez:** A nagy $\prod$ szorzatjel azt jelenti, hogy nem elég, ha az eseményeket kettesével (páronként) vizsgáljuk! A rendszerből BÁRMENNYI (három, négy, stb.) eseményt is választunk ki, a közös metszetük valószínűsége meg kell hogy egyezzen a valószínűségek szorzatával.")

    st.markdown("---")

    # ==========================================
    # INTERAKTÍV TESZTELŐ: PÁRONKÉNT VS TELJESEN FÜGGETLEN
    # ==========================================
    st.markdown("### 🪙 Interaktív tesztelő: A nagy 'függetlenség' beugrató!")
    st.write("Dobjunk fel 2 darab pénzérmét (kimenetelek: FF, FÍ, ÍF, ÍÍ - mindegyik esélye 1/4 = 0.25).")
    st.write("Vizsgáljuk meg a következő 3 eseményt:")
    st.write("- **A esemény:** Az 1. érme FEJ $\implies$ {FF, FÍ} $\implies P(A) = 0.5$")
    st.write("- **B esemény:** A 2. érme FEJ $\implies$ {FF, ÍF} $\implies P(B) = 0.5$")
    st.write("- **C esemény:** A két érme KÜLÖNBÖZŐ $\implies$ {FÍ, ÍF} $\implies P(C) = 0.5$")

    if st.button("1. Lépés: Nézzük meg a páronkénti függetlenséget!"):
        st.success("**Vizsgáljuk meg az eseményeket kettesével (páronként):**")
        
        st.write("**A és B:** Metszetük az {FF}. Esélye $0.25$.")
        st.latex(r"P(AB) = 0.25 \quad \text{és} \quad P(A)P(B) = 0.5 \cdot 0.5 = 0.25 \implies \text{Függetlenek!}")
        
        st.write("**A és C:** Metszetük az {FÍ}. Esélye $0.25$.")
        st.latex(r"P(AC) = 0.25 \quad \text{és} \quad P(A)P(C) = 0.5 \cdot 0.5 = 0.25 \implies \text{Függetlenek!}")
        
        st.write("**B és C:** Metszetük az {ÍF}. Esélye $0.25$.")
        st.latex(r"P(BC) = 0.25 \quad \text{és} \quad P(B)P(C) = 0.5 \cdot 0.5 = 0.25 \implies \text{Függetlenek!}")
        
        st.info("Úgy tűnik, mindenki független mindenkivel! Akkor ez egy teljesen független eseményrendszer, igaz? **Kattints a 2. gombra!**")

    if st.button("2. Lépés: Nézzük meg a TELJES függetlenséget (Definíció tesztje)!"):
        st.warning("**Most vizsgáljuk meg mind a HÁRMAT egyszerre (ahogy a definíció nagy szorzatjele kéri):**")
        st.write("Mekkora az esélye annak, hogy az 1. érme FEJ (A), a 2. érme FEJ (B), ÉS a két érme KÜLÖNBÖZŐ (C)?")
        
        st.write("Mivel ez lehetetlen (ha mindkettő Fej, akkor nem lehetnek különbözőek), a metszet üres halmaz, esélye 0!")
        st.latex(r"P(ABC) = P(\emptyset) = \mathbf{0}")
        
        st.write("Ezzel szemben a valószínűségeik szorzata:")
        st.latex(r"P(A) \cdot P(B) \cdot P(C) = 0.5 \cdot 0.5 \cdot 0.5 = \mathbf{0.125}")
        
        st.error(r"**Végeredmény:** Mivel $0 \neq 0.125$, az $A, B, C$ események **NEM teljesen függetlenek!** Bár páronként függetlenek voltak, a teljes rendszer elbukott a hivatalos definíció tesztjén.")