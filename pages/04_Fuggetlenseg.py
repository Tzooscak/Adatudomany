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
    st.markdown("### Kulcsfogalmak")
    st.write("- **Események függetlensége:** Két esemény független, ha együttes bekövetkezésük (metszetük) valószínűsége egyenlő a valószínűségeik szorzatával: $P(AB) = P(A)P(B)$.")
    st.write("- **Eseményrendszerek (teljes) függetlensége:** Nem elég, ha páronként függetlenek! Egy rendszer akkor teljesen független, ha bármely részhalmazukra igaz, hogy a metszetük valószínűsége a valószínűségek szorzata.")