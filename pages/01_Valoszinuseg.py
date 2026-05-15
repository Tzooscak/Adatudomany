import streamlit as st

st.title("🎲 1. A valószínűség bevezetése")
st.markdown("---")

tab1, tab2 = st.tabs(["📚 Tételek", "🧠 Fogalmak"])

with tab1:
    with st.expander("1.1 Észrevételek tetszőleges σ-algebrában I. *"):
        # 1. A hivatalos tétel kiírása LaTeX formátumban
        st.write(r"Legyen $\Omega$ nemüres megszámlálható halmaz és $\mathcal{F} \subseteq \wp(\Omega)$ $\sigma$-algebra, ekkor:")
        
        st.latex(r"(1) \quad A, B \in \mathcal{F} \implies A \cap B \in \mathcal{F}")
        st.caption("Magyarázat: Ha két esemény (A és B) benne van a vizsgálható események halmazában, akkor a **metszetük** (mindkettő egyszerre teljesül) is egy érvényes esemény.")
        
        st.latex(r"(2) \quad A_1, A_2, \dots \in \mathcal{F} \implies A_1 \cap A_2 \cap \dots \in \mathcal{F}")
        st.caption("Magyarázat: Ez ugyanaz, mint az első, csak nem kettő, hanem akár végtelen sok eseményre is igaz.")
        
        st.latex(r"(3) \quad \text{Ha } A_i, A_j \in \mathcal{F} \, (i \neq j) \text{ elemi események, akkor } A_i \cap A_j = \emptyset")
        st.caption("Magyarázat: Két különböző elemi (tovább már nem bontható) esemény sosem történhet meg egyszerre. Kizárják egymást.")

        st.markdown("---")
        
        # 2. Interaktív vizualizáció (Kockadobás példa)
        st.markdown("### 🎲 Interaktív Példa: Próbáld ki!")
        st.write(r"Képzelj el egy normál dobókockát. $\Omega = \{1, 2, 3, 4, 5, 6\}$. Válassz elemeket az $A$ és $B$ eseményekhez!")
        
        col1, col2 = st.columns(2)
        with col1:
            # A felhasználó kiválaszthatja az A esemény kimeneteleit
            A_list = st.multiselect("A esemény (pl. páros számok):", [1, 2, 3, 4, 5, 6], default=[2, 4, 6])
            A = set(A_list)
            
        with col2:
            # A felhasználó kiválaszthatja a B esemény kimeneteleit
            B_list = st.multiselect("B esemény (pl. 3-nál nagyobbak):", [1, 2, 3, 4, 5, 6], default=[4, 5, 6])
            B = set(B_list)
            
        # Halmazművelet: Metszet kiszámolása a Python beépített set funkciójával
        metszet = A.intersection(B)
        
        # Eredmény megjelenítése
        if metszet:
            st.info(rf"**A $\cap$ B (Metszet):** {metszet} $\implies$ Látod? Ez is egy érvényes esemény az (1)-es pont alapján!")
        else:
            st.warning(r"**A $\cap$ B (Metszet):** $\emptyset$ (Üres halmaz) $\implies$ A két esemény kizárja egymást, nincs közös kimenetelük.")
            
        # A (3)-as tétel automatikus ellenőrzése és demonstrálása
        if len(A) == 1 and len(B) == 1 and A != B:
            st.success(r"💡 **A (3)-as tétel a gyakorlatban:** Mivel az $A$ és a $B$ is csak egyetlen elemből áll (tehát **elemi események**), és nem egyformák, a metszetük garantáltan $\emptyset$! Nem dobhatsz egyszerre két különböző számot.")
    with st.expander("1.2 Észrevételek tetszőleges σ-algebrában II. *"):
        # 1. A tétel elméleti része
        st.write("A folytatásban azt vizsgáljuk, mi történik, ha a lehetséges kimenetelek halmaza ($\\Omega$) **véges**.")
        
        st.latex(r"(4) \quad \text{Ha } \Omega \text{ véges és } B \in \mathcal{F} \text{ összetett esemény,}")
        st.latex(r"\text{akkor létezik olyan } A \in \mathcal{F} \text{ elemi esemény, amelyre } A \subset B.")
        st.caption("Magyarázat: Minden összetett esemény (ami több kimenetelt is magában foglal) biztosan 'tartalmaz' legalább egy elemi (tovább már nem bontható) eseményt.")
        
        st.latex(r"(5) \quad \text{Ha } \Omega \text{ véges, akkor minden nem lehetetlen } \mathcal{F}\text{-beli esemény}")
        st.latex(r"\text{sorrendre való tekintet nélkül egyértelműen előáll elemi események összegeként.}")
        st.caption("Magyarázat: A valószínűségszámítás 'legója'. Bármilyen bonyolult eseményt is találsz ki, az pontosan felépíthető az elemi események (kimenetelek) uniójából.")
        
        st.latex(r"(6) \quad \text{Ha } \Omega \text{ véges és } \mathcal{F}\text{-ben } n \text{ elemi esemény van, akkor } |\mathcal{F}| = 2^n.")
        st.caption("Magyarázat: Ha tudod, hányféle elemi kimenetel van (n), akkor a belőlük képezhető összes lehetséges események száma mindig pontosan kettő az n-ediken (ez a hatványhalmaz mérete).")

        st.markdown("---")

        # 2. Interaktív vizualizáció (Eseménytér építő)
        st.markdown(r"### 🧩 Interaktív Példa: Építsük fel a $\sigma$-algebrát!")
        st.write("Próbáljuk ki az (5)-ös és (6)-os tételt a gyakorlatban! Hány elemi kimenetele (pl. dobás eredménye) legyen a kísérletednek?")

        # Csúszka a kimenetelek számához
        n_elem = st.slider("Elemi események száma (n):", 1, 6, 3)

        import itertools

        # Elemi események generálása
        elemi_esemenyek = [f"e{i+1}" for i in range(n_elem)]
        st.write(f"**Alap elemi eseményeid ($\\Omega$):** `{elemi_esemenyek}`")

        st.info(f"A (6)-os tétel alapján az összes lehetséges esemény száma ($\\mathcal{{F}}$ mérete): **$2^{n_elem} = {2**n_elem}$** db.")

        # Összes kombináció (hatványhalmaz) legenerálása
        osszes_esemeny = []
        for r in range(n_elem + 1):
            for combo in itertools.combinations(elemi_esemenyek, r):
                osszes_esemeny.append(set(combo))

        # Rejtett panel a listához, hogy ne legyen túl hosszú az oldal, ha n=6 (64 elem)
        with st.expander(f"👀 Kattints ide, hogy lásd mind a {2**n_elem} eseményt felépítve! (Az 5-ös tétel bizonyítása)"):
            for idx, esemeny in enumerate(osszes_esemeny):
                if len(esemeny) == 0:
                    st.write(f"**{idx+1}.** $\\emptyset$ *(Lehetetlen esemény)*")
                elif len(esemeny) == n_elem:
                    st.write(f"**{idx+1}.** `{esemeny}` *(Biztos esemény, $\\Omega$)*")
                elif len(esemeny) == 1:
                    st.write(f"**{idx+1}.** `{esemeny}` *(Elemi esemény)*")
                else:
                    # Ez vizuálisan demonstrálja a (4)-es és (5)-ös pontot
                    st.write(f"**{idx+1}.** `{esemeny}` *(Összetett esemény)*")

with tab2:
    st.header("🧠 Fogalmak definíciói")
    st.write("A valószínűségszámítás legfontosabb alapfogalmai a hivatalos definíciók alapján:")

    # ==========================================
    # DEFINÍCIÓK
    # ==========================================
    st.markdown("### 1. Kísérlet és Eseménytér")
    st.write(r"**Eseménytér (Sample Space - $\Omega$):** Egy adott kísérlethez tartozó halmaz, amelynek elemei a kísérlet kimenetelei (ez végtelen is lehet).")
    st.latex(r"\Omega := \{\omega_1, \omega_2, \dots, \omega_n\}")

    st.markdown("### 2. Események")
    st.write(r"**Esemény:** Az $\mathcal{F} \subseteq \wp(\Omega)$ (a teljes eseménytér hatványhalmaza) halmaz elemeit nevezzük eseménynek.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info(r"**Elemi események:**\n\nAz $\Omega$ egyelemű részhalmazai. (Olyan kimenetelek, amik tovább már nem bonthatók.)")
    with col2:
        st.warning(r"**Összetett események:**\n\nAz $\Omega$ többelemű részhalmazai. (Több elemi eseményből tevődnek össze.)")

    st.markdown("### 3. Bekövetkezés és Speciális események")
    st.write(r"**Bekövetkezés:** Ha egy $\Omega$ eseményterű kísérlet kimenetele $\omega \in \Omega$, $A \in \mathcal{F}$ és $\omega \in A$, akkor az $A$ esemény bekövetkezik.")
    
    col3, col4 = st.columns(2)
    with col3:
        st.success(r"**Biztos esemény ($\Omega$):**\n\nMaga a teljes eseménytér.")
    with col4:
        st.error(r"**Lehetetlen esemény ($\emptyset$):**\n\nAz üres halmaz.")
        
    st.markdown("---")
    
    # ==========================================
    # INTERAKTÍV TESZTELŐ
    # ==========================================
    st.markdown("### 🧩 Interaktív fogalom-tesztelő")
    st.write(r"Játsszunk egy dobókockával! Az eseménytér: $\Omega = \{1, 2, 3, 4, 5, 6\}$")
    
    kimenetel = st.slider(r"Állítsd be, mi lett a dobás eredménye ($\omega$)!)", 1, 6, 3)
    st.write(rf"A kísérlet konkrét kimenetele: **$\omega = {kimenetel}$**")
    
    st.markdown("#### 1. Elemi esemény vizsgálata")
    st.write(r"Nézzük meg az $E_1 = \{3\}$ elemi eseményt (azaz 'Hármast dobunk'). Bekövetkezett?")
    if kimenetel == 3:
        st.success(rf"**Igen!** Mivel az aktuális kimenetel ($\omega = {kimenetel}$) benne van az $E_1 = {{3}}$ halmazban, az elemi esemény bekövetkezett.")
    else:
        st.error(rf"**Nem!** Mivel az aktuális kimenetel ($\omega = {kimenetel}$) nincs benne az $E_1 = {{3}}$ halmazban, az elemi esemény nem következett be.")
        
    st.markdown("#### 2. Összetett esemény vizsgálata")
    st.write(r"Nézzük meg az $A = \{\text{Páros számot dobunk}\} = \{2, 4, 6\}$ összetett eseményt. Bekövetkezett?")
    if kimenetel in [2, 4, 6]:
        st.success(rf"**Igen!** Mivel az aktuális kimenetel ($\omega = {kimenetel}$) benne van az $A = {{2, 4, 6}}$ halmazban, az összetett esemény bekövetkezett.")
    else:
        st.error(rf"**Nem!** Mivel az aktuális kimenetel ($\omega = {kimenetel}$) nincs benne az $A = {{2, 4, 6}}$ halmazban, az összetett esemény nem következett be.")