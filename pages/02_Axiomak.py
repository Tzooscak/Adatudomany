import streamlit as st

st.title("📐 2. Kolmogorov valószínűségi axiómái")
st.markdown("---")

# Fülek létrehozása a letisztult dizájnért
tab1, tab2 = st.tabs(["📚 Tételek", "🧠 Fogalmak"])

with tab1:
    st.subheader("Tételek kidolgozása")
    # Ide jönnek majd a latex képletek a tételekhez
    with st.expander("2.1 A valószínűség tulajdonságai I."):
        st.write(r"Tetszőleges $(\Omega, \mathcal{F}, P)$ valószínűségi mezőben teljesülnek a következő állítások:")
        
        # ==========================================
        # 1. ÁLLÍTÁS: LEHETETLEN ESEMÉNY
        # ==========================================
        st.markdown("### (1) A lehetetlen esemény valószínűsége")
        st.latex(r"P(\emptyset) = 0")
        
        st.markdown("**Részletes magyarázat:**")
        st.write(r"Ez az állítás egyszerűen annyit mond, hogy egy olyan eseménynek, amely fizikailag vagy logikailag nem következhet be (lehetetlen esemény, jele: $\emptyset$), pontosan nulla a valószínűsége. Nincs esélye megtörténni.")
        
        if st.checkbox("💡 Részletes Bizonyítás (1)", key="biz1"):
            st.info("A bizonyítás logikája: Induljunk ki abból, amit már biztosan tudunk (axiómák), és trükkösen adjunk hozzá a semmit (üres halmazokat).")
            st.write("1. Tudjuk a (K2) axiómából, hogy a biztos esemény valószínűsége 1.")
            st.latex(r"1 = P(\Omega)")
            st.write("2. A biztos eseményhez hozzáadhatunk akárhány lehetetlen eseményt (üres halmazt), a halmaz nem változik. Mivel ezek egyszerre nem történhetnek meg, **egymást páronként kizáró események**.")
            st.latex(r"= P(\Omega \cup \emptyset \cup \emptyset \cup \dots)")
            st.write(r"3. A (K3) $\sigma$-additivitás axiómája kimondja, hogy ha események kizárják egymást, az uniójuk valószínűsége egyenlő a valószínűségük összegével.")
            st.latex(r"= P(\Omega) + P(\emptyset) + P(\emptyset) + \dots")
            st.write(r"4. Mivel végtelen sokszor adtuk hozzá a $P(\emptyset)$-t, ezt felírhatjuk egy határértékkel:")
            st.latex(r"= 1 + \lim_{i\to\infty} i \cdot P(\emptyset)")
            st.write(r"5. Mivel az egyenlet bal oldala 1, a jobb oldalán lévő határértéknek kötelezően 0-nak kell lennie. Ha $P(\emptyset)$ akármilyen pici, nullánál nagyobb szám lenne, akkor végtelenszer összeadva végtelent kapnánk. Így $P(\emptyset)$ csakis 0 lehet.")
            
        st.markdown("##### 🎲 Szimuláció 1: A lehetetlen kockadobás")
        st.write("Van egy szabályos, 6 oldalú dobókockánk. Mi az esélye annak az $A$ eseménynek, hogy **7-est** dobunk?")
        oldalak_szama = st.slider("Hány oldalú a kockád?", 4, 20, 6, key="kocka")
        lehetetlen_dobas = oldalak_szama + 1
        st.error(f"**Eredmény:** Mivel csak 1-től {oldalak_szama}-ig vannak számok, a {lehetetlen_dobas}-es dobás egy **lehetetlen esemény** ($\emptyset$).")
        st.latex(rf"P(\text{{Dobás}} = {lehetetlen_dobas}) = \frac{{0 \text{{ (kedvező eset)}}}}{{{oldalak_szama} \text{{ (összes eset)}}}} = \mathbf{{0}}")

        st.markdown("---")
        
        # ==========================================
        # 2. ÁLLÍTÁS: VÉGES ADDITIVITÁS
        # ==========================================
        st.markdown("### (2) Véges additivitás tulajdonság")
        st.write(r"Ha $A_1, A_2, \dots, A_n \in \mathcal{F}$ egymást páronként kizáró események, akkor:")
        st.latex(r"P\left(\sum_{i=1}^n A_i\right) = \sum_{i=1}^n P(A_i)")
        
        st.markdown("**Részletes magyarázat:**")
        st.write("A 3. axióma (K3) eredetileg *végtelen* sok eseményre mondja ki az összeadhatóságot. Ez az állítás azt garantálja, hogy ez az összeadás működik **véges** számú (pl. 2, 3 vagy 100) egymást kizáró esemény esetén is.")
        
        if st.checkbox("💡 Részletes Bizonyítás (2)", key="biz2"):
            st.info("A bizonyítás logikája: Használjuk a végtelen összeadást (K3 axióma), de a véges eseményeink után 'pótoljuk ki' a sort végtelen sok lehetetlen eseménnyel, amikről az előbb (1) bebizonyítottuk, hogy a valószínűségük nulla.")
            st.write("1. Felírjuk a véges uniót, és kipótoljuk üres halmazokkal a végtelenig:")
            st.latex(r"P\left(\bigcup_{i=1}^n A_i\right) = P\left(\bigcup_{i=1}^n A_i \cup \emptyset \cup \emptyset \cup \dots\right)")
            st.write(r"2. Alkalmazzuk a (K3) $\sigma$-additivitást a végtelen sok, egymást kizáró halmazra:")
            st.latex(r"= \sum_{i=1}^n P(A_i) + P(\emptyset) + P(\emptyset) + \dots")
            st.write(r"3. Az (1)-es tétel alapján tudjuk, hogy $P(\emptyset) = 0$, tehát csupa nullát adunk hozzá:")
            st.latex(r"= \sum_{i=1}^n P(A_i) + 0 + 0 + \dots = \sum_{i=1}^n P(A_i)")
            
        st.markdown("##### 🎱 Szimuláció 2: Golyók a zsákból")
        st.write("Van egy zsákod golyókkal. Kihúzol egyet. Mivel egy golyó nem lehet egyszerre piros és kék is, ezek **egymást kizáró események**. Add össze az esélyeiket!")
        col_r, col_b, col_g = st.columns(3)
        piros = col_r.number_input("Piros golyók száma:", 0, 10, 3)
        kek = col_b.number_input("Kék golyók száma:", 0, 10, 2)
        zold = col_g.number_input("Zöld golyók száma:", 0, 10, 5)
        
        osszes_golyo = piros + kek + zold
        if osszes_golyo > 0:
            p_piros = piros / osszes_golyo
            p_kek = kek / osszes_golyo
            st.success("**Véges additivitás a gyakorlatban:**\n\nKeresem annak az esélyét, hogy **Piros VAGY Kék** golyót húzok:")
            st.latex(f"P(\\text{{Piros}} \\cup \\text{{Kék}}) = P(\\text{{Piros}}) + P(\\text{{Kék}}) = {p_piros:.2f} + {p_kek:.2f} = \\mathbf{{{p_piros + p_kek:.2f}}}")
        else:
            st.error("Tegyél golyókat a zsákba!")

        st.markdown("---")
        
        # ==========================================
        # 3. ÁLLÍTÁS: KOMPLEMENTER ESEMÉNY
        # ==========================================
        st.markdown("### (3) A komplementer esemény valószínűsége")
        st.latex(r"A \in \mathcal{F} \implies P(A) = 1 - P(\overline{A})")
        
        st.markdown("**Részletes magyarázat:**")
        st.write(r"Egy esemény ($A$) és annak ellentettje, komplementere ($\overline{A}$) együtt lefedik a világ összes lehetséges forgatókönyvét. Ha holnap 30% az esélye az esőnek, akkor 70% az esélye annak, hogy nem esik.")
        
        if st.checkbox("💡 Részletes Bizonyítás (3)", key="biz3"):
            st.info("A bizonyítás logikája: Ha egy eseményt és az ellentettjét egyesítjük, megkapjuk a biztos eseményt (mindent). Utána csak átrendezzük a képletet.")
            st.write(r"1. Tekintsük az $A$ eseményt és komplementerét. Ezek uniója lefedi a teljes eseményteret ($\Omega$):")
            st.latex(r"A \cup \overline{A} = \Omega")
            st.write("2. Mivel egy esemény és az ellentettje sosem történhet meg egyszerre (kizárják egymást), használhatjuk az előbb bizonyított véges additivitást (2. állítás):")
            st.latex(r"P(\Omega) = P(A) + P(\overline{A})")
            st.write(r"3. Tudjuk, hogy a biztos esemény valószínűsége $P(\Omega) = 1$. Behelyettesítve:")
            st.latex(r"1 = P(A) + P(\overline{A})")
            st.write(r"4. Egyszerű algebrai átrendezéssel (kivonjuk mindkét oldalból a $P(\overline{A})$-t) megkapjuk a végeredményt:")
            st.latex(r"\implies P(A) = 1 - P(\overline{A})")

        st.markdown("##### 🥧 Szimuláció 3: Az eső és a komplementere")
        st.write(r"Állítsd be, mekkora eséllyel fog esni holnap az eső ($P(A)$)! Figyeld, hogyan számolja ki a gép a komplementer ($\overline{A}$, azaz nem esik) esélyét!")
        
        eso_esely = st.slider("Eső esélye P(A):", 0.0, 1.0, 0.3)
        nem_eso_esely = 1.0 - eso_esely
        
        st.latex(rf"P(\text{{Nem Esik}}) = 1 - P(\text{{Esik}}) = 1 - {eso_esely:.2f} = \mathbf{{{nem_eso_esely:.2f}}}")

        # Egy szép progress bar a vizualizációhoz
        st.write(f"**Eső esélye (A):** {eso_esely*100:.0f}%")
        st.progress(eso_esely)
        st.write(f"**Nem esik ($\\overline{{A}}$):** {nem_eso_esely*100:.0f}%")
        st.progress(nem_eso_esely)
    with st.expander("2.2 A valószínűség tulajdonságai II."):
        st.write("Tetszőleges $(\Omega, \mathcal{F}, P)$ valószínűségi mezőben teljesülnek a következő állítások :")
        
        # ==========================================
        # 4. ÁLLÍTÁS: ÖSSZEGZÉS (SZITA-FORMULA)
        # ==========================================
        st.markdown("### (4) Tetszőleges események összege")
        st.latex(r"A, B \in \mathcal{F} \implies P(A+B) = P(A) + P(B) - P(AB)")
        
        st.markdown("**Részletes magyarázat:**")
        st.write("Ha két esemény **nem zárja ki egymást** (azaz egyszerre is bekövetkezhetnek), akkor nem elég egyszerűen összeadni a valószínűségüket. Ha így tennénk, a közös részt (a metszetet, $AB$) kétszer is beleszámolnánk. Ezért a közös részt egyszer ki kell vonni. Ezt hívják szita-formulának.")
        
        if st.checkbox("💡 Részletes Bizonyítás (4)", key="biz4"):
            st.info("A bizonyítás logikája: Bontsuk fel a halmazokat egymást kizáró részekre, hogy használhassuk a véges additivitást .")
            st.write("1. A $B$ esemény felbontható két egymást kizáró részre: ami benne van $A$-ban is ($AB$), és ami nincs ($B \setminus A$). A véges additivitás miatt:")
            st.latex(r"P(B) = P(AB) + P(B \setminus A)")
            st.write("2. Az $A+B$ (unió) is felbontható: magára az $A$ eseményre, és arra a részre, ami csak $B$-ben van meg ($B \setminus A$).")
            st.latex(r"P(A+B) = P(A) + P(B \setminus A)")
            st.write("3. Rendezve: fejezzük ki az első egyenletből $P(B \setminus A)$-t, és helyettesítsük be a másodikba:")
            st.latex(r"P(B \setminus A) = P(B) - P(AB)")
            st.latex(r"\implies P(A+B) = P(A) + P(B) - P(AB)")
            
        st.markdown("##### 🎯 Szimuláció 4: Venn-diagram a gyakorlatban")
        st.write("Húzunk egy kártyát egy 52 lapos francia kártyapakliból. \n* $A$ esemény: A húzott lap **Pikk** (13 lap) \n* $B$ esemény: A húzott lap **Király** (4 lap)")
        
        p_pikk = 13/52
        p_kiraly = 4/52
        p_metszet = 1/52 # Pikk király
        p_unio = p_pikk + p_kiraly - p_metszet
        
        st.info("Mi az esélye, hogy **Pikk VAGY Király** lapot húzunk?")
        st.latex(rf"P(\text{{Pikk}} \cup \text{{Király}}) = \frac{{13}}{{52}} + \frac{{4}}{{52}} - \frac{{1}}{{52}} = \frac{{16}}{{52}} \approx \mathbf{{{p_unio*100:.1f}\%}}")
        st.write("Látod? Ha csak összeadnánk (13+4=17), a Pikk Királyt kétszer számoltuk volna!")

        st.markdown("---")
        
        # ==========================================
        # 5. ÁLLÍTÁS: MONOTONITÁS
        # ==========================================
        st.markdown("### (5) Monotonitás")
        st.latex(r"\text{Ha } A, B \in \mathcal{F} \text{ és } A \subseteq B, \text{ akkor } P(A) \le P(B)")
        
        st.markdown("**Részletes magyarázat:**")
        st.write("Ha az $A$ esemény maga után vonja a $B$ eseményt (azaz ha $A$ megtörténik, akkor $B$ is biztosan megtörténik, mert $A$ egy részhalmaza $B$-nek), akkor az $A$ esemény valószínűsége sosem lehet nagyobb, mint a $B$ valószínűsége.")
        
        if st.checkbox("💡 Részletes Bizonyítás (5)", key="biz5"):
            st.info("A bizonyítás logikája: Használjuk újra az előző (4-es) bizonyítás felbontását .")
            st.write("1. Ahogy az előbb láttuk a véges additivitásból:")
            st.latex(r"P(B) = P(AB) + P(B \setminus A)")
            st.write("2. Tegyük fel, hogy $A \subseteq B$. Ez azt jelenti, hogy az $A$ és $B$ közös része (metszete) maga az $A$ halmaz:")
            st.latex(r"A \subseteq B \implies A \cap B = A")
            st.write("3. Helyettesítsük be ezt az első egyenletbe:")
            st.latex(r"P(B) = P(A) + P(B \setminus A)")
            st.write("4. Rendezzük át:")
            st.latex(r"P(B \setminus A) = P(B) - P(A)")
            st.write("5. A (K1) axióma alapján minden valószínűség nemnegatív, tehát $0 \le P(B \setminus A)$. Ebből következik:")
            st.latex(r"0 \le P(B) - P(A) \implies P(A) \le P(B)")
            
        st.markdown("##### 🎲 Szimuláció 5: A részhalmaz esélye")
        st.write("Kockadobásnál állíts be egy szűkebb ($A$) és egy tágabb ($B$) eseményt!")
        
        col1, col2 = st.columns(2)
        with col1:
            a_halmaz = st.multiselect("A esemény (szűkebb):", [1, 2, 3, 4, 5, 6], default=[2])
        with col2:
            b_halmaz = st.multiselect("B esemény (tágabb):", [1, 2, 3, 4, 5, 6], default=[2, 4, 6])
            
        if set(a_halmaz).issubset(set(b_halmaz)):
            p_a_sim = len(a_halmaz) / 6
            p_b_sim = len(b_halmaz) / 6
            st.success(f"**Helyes!** Az $A$ részhalmaza a $B$-nek ($A \subseteq B$).\n\n$P(A) = {p_a_sim:.2f} \le P(B) = {p_b_sim:.2f}$")
        else:
            st.error("Jelenleg az $A$ nem részhalmaza a $B$-nek! Állítsd be úgy, hogy minden szám, ami az $A$-ban van, legyen benne a $B$-ben is!")

        st.markdown("---")
        
        # ==========================================
        # 6. ÁLLÍTÁS: FELSŐ KORLÁT
        # ==========================================
        st.markdown("### (6) A valószínűség felső korlátja")
        st.latex(r"A \in \mathcal{F} \implies P(A) \le 1")
        
        st.markdown("**Részletes magyarázat:**")
        st.write("A (K1) axiómából már tudjuk, hogy a valószínűség nem lehet negatív ($0 \le P$). Ez az állítás rögzíti a plafont: semminek sem lehet 100%-nál (1-nél) nagyobb az esélye.")
        
        if st.checkbox("💡 Részletes Bizonyítás (6)", key="biz6"):
            st.info("A bizonyítás logikája: Minden esemény a teljes eseménytér része, és az (5)-ös monotonitást alkalmazzuk a teljes eseménytérre .")
            st.write("1. A (K2) axióma kimondja, hogy a biztos esemény valószínűsége 1:")
            st.latex(r"P(\Omega) = 1")
            st.write("2. Bármely $A \in \mathcal{F}$ esemény definíció szerint a teljes eseménytér ($\Omega$) részhalmaza:")
            st.latex(r"A \subseteq \Omega")
            st.write("3. Az imént bizonyított monotonitás (5. állítás) miatt:")
            st.latex(r"P(A) \le P(\Omega)")
            st.write("4. Mivel $P(\Omega) = 1$, készen is vagyunk:")
            st.latex(r"\implies P(A) \le 1")

        st.markdown("##### 🚀 Szimuláció 6: A 100%-os plafon")
        st.write("Bármilyen hihetetlen is egy esemény bekövetkezése, a matematikai keretek nem engedik átlépni az 1-es korlátot.")
        
        esely = st.slider("Mennyire vagy biztos a dolgodban?", 0, 150, 80, format="%d%%")
        
        if esely <= 100:
            st.info(f"Matematikailag érvényes valószínűség: **$P(A) = {esely/100:.2f}$**")
            st.progress(esely / 100)
        else:
            st.error(f"Hiba! Hiába érzed {esely}%-nak az esélyt, a valószínűségszámításban $P(A) \le 1$. A plafon 100%!")
            st.progress(1.0) # Kimaxolva
        
    with st.expander("2.3 Klasszikus valószínűségi mező"):
        # ==========================================
        # 2.3 TÉTEL: KLASSZIKUS VALÓSZÍNŰSÉGI MEZŐ
        # ==========================================
        st.write("Legyen $\Omega$ véges nemüres halmaz, $\mathcal{F} = \wp(\Omega)$ és $P : \mathcal{F} \longrightarrow  \mathbb{R}$ valószínűség.")
        st.latex(r"\text{Ekkor minden } \omega_i, \omega_j \in \Omega \text{ esetén } P(\{\omega_i\}) = P(\{\omega_j\}) \iff (\Omega, \mathcal{F}, P) \text{ klasszikus valószínűségi mező.}")

        st.markdown("**Részletes magyarázat:**")
        st.write("Ez a tétel azt mondja ki, hogy egy véges valószínűségi mező pontosan akkor 'klasszikus', ha minden egyes elemi esemény (kimenetel) valószínűsége megegyezik. Ha ez teljesül, akkor bármely $A$ esemény valószínűsége egyszerűen a kedvező esetek száma osztva az összes eset számával:")
        st.latex(r"P(A) = \frac{|A|}{|\Omega|}")

        if st.checkbox("💡 Részletes Bizonyítás (2.3)", key="biz2_3"):
            st.info("A bizonyítás kétirányú ($\implies$ és $\impliedby$), mivel egyenértékűséget (Akkor és csak akkor) kell belátnunk.")

            st.markdown("**1. Irány ($\implies$): Tegyük fel, hogy klasszikus a valószínűségi mező.**")
            st.write("A definíció szerint ekkor bármely $A$ eseményre:")
            st.latex(r"P(A) = \frac{|A|}{|\Omega|}")
            st.write("Ha veszünk egy tetszőleges $\omega$ elemi eseményt, az egyetlen elemből áll, tehát $|\{\omega\}| = 1$. Ezt behelyettesítve a képletbe:")
            st.latex(r"P(\{\omega\}) = \frac{|\{\omega\}|}{|\Omega|} = \frac{1}{|\Omega|}")
            st.write("Mivel ez a számolás minden egyes $\omega$-ra pontosan ugyanezt az eredményt adja, az összes elemi esemény esélye egyenlő.")
            
            st.markdown("---")

            st.markdown("**2. Irány ($\impliedby$): Tegyük fel, hogy minden elemi esemény esélye egyenlő.**")
            st.write("Jelöljük ezt a közös valószínűséget $x$-szel:")
            st.latex(r"\forall \omega_i, \omega_j \in \Omega : P(\{\omega_i\}) = P(\{\omega_j\}) = x")
            st.write("Az 1.2 Tétel (5) alapján minden $A$ esemény egyértelműen felbontható az őt alkotó elemi események uniójára:")
            st.latex(r"A = \{\omega_{A_1}\} \cup \dots \cup \{\omega_{A_r}\}")
            st.write("Mivel az elemi események egymást páronként kizárják, használhatjuk a véges additivitást, azaz egyszerűen összeadhatjuk az esélyeiket:")
            st.latex(r"P(A) = P(\{\omega_{A_1}\}) + \dots + P(\{\omega_{A_r}\}) = |A| \cdot x")
            st.write("Tudjuk a (K2) axiómából, hogy a biztos esemény ($\Omega$) valószínűsége 1:")
            st.latex(r"P(\Omega) = |\Omega| \cdot x = 1 \implies x = \frac{1}{|\Omega|}")
            st.write("Végül helyettesítsük be az $x$-et a $P(A)$ képletébe, és meg is kapjuk a klasszikus valószínűségi mező definícióját:")
            st.latex(r"P(A) = |A| \cdot x = |A| \cdot \frac{1}{|\Omega|} = \frac{|A|}{|\Omega|}")

        st.markdown("##### 🎯 Szimuláció 2.3: A Klasszikus Rulettkerék")
        st.write("Egy klasszikus valószínűségi mezőben (mint egy fair rulett, dobókocka vagy lottósorsolás) minden kimenetel esélye hajszálpontosan egyenlő. Állítsd be az összes esetet és a kedvező eseteket!")
        
        col1, col2 = st.columns(2)
        with col1:
            omega_meret = st.number_input("Összes lehetséges kimenetel ($|\Omega|$):", min_value=2, max_value=100, value=37)
            st.caption("Pl. egy európai rulettkeréken 37 szám van (0-36).")
        with col2:
            a_meret = st.number_input("Kedvező kimenetelek száma ($|A|$):", min_value=1, max_value=omega_meret, value=18)
            st.caption("Pl. a Piros számok száma 18.")

        p_omega = 1 / omega_meret
        p_a = a_meret / omega_meret

        st.warning("**1. Lépés (Elemi események):**\nMivel ez egy klasszikus mező, minden EGYETLEN kimenetel (pl. kipörög a 7-es) esélye egyenlő:")
        st.latex(rf"P(\{{\omega\}}) = \frac{{1}}{{{omega_meret}}} \approx \mathbf{{{p_omega*100:.2f}}}\%")
        st.success("**2. Lépés (Összetett esemény):**\nAz $A$ esemény valószínűsége (kedvező esetek osztva az összes esettel):")
        st.latex(rf"P(A) = \frac{{|A|}}{{|\Omega|}} = \frac{{{a_meret}}}{{{omega_meret}}} \approx \mathbf{{{p_a*100:.2f}}}\%")
        
        # Vizualizáció egy egyszerű progress bar-ral
        st.write("**A kedvező esemény esélye vizuálisan:**")
        st.progress(p_a)

with tab2:
    st.header("🧠 Fogalmak definíciói")
    st.write("A 2. tételhez (Kolmogorov axiómái) tartozó legfontosabb alapfogalmak:")

    # ==========================================
    # 1. VALÓSZÍNŰSÉGI MEZŐ ÉS AXIÓMÁK
    # ==========================================
    st.markdown("### 1. Kolmogorov valószínűségi axiómái és a valószínűségi mező")
    st.write(r"Tekintsünk egy $\Omega$ nemüres halmazt és $\mathcal{F} \subseteq \wp(\Omega)$ $\sigma$-algebrát. Ekkor **valószínűségnek** nevezzük azt a $P : \mathcal{F} \rightarrow \mathbb{R}$ függvényt, amelyre fennállnak a következő állítások:")
    
    st.latex(r"(K1) \quad A \in \mathcal{F} \implies P(A) \ge 0")
    st.latex(r"(K2) \quad P(\Omega) = 1")
    st.write(r"(K3) Ha $A_1, A_2, \dots \in \mathcal{F}$ egymást páronként kizáró események, akkor:")
    st.latex(r"P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)")
    
    st.info(r"💡 **Megjegyzés:** A nagy unió ($\bigcup$) jel helyett a szumma ($\Sigma$) is használható! $P\left(\sum_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$")
    
    st.write(r"Továbbá az $(\Omega, \mathcal{F}, P)$ hármast **valószínűségi mezőnek**, míg a (K3) tulajdonságot **$\sigma$-additivitásnak** hívjuk.")

    # ==========================================
    # INTERAKTÍV TESZTELŐ: AXIÓMÁK
    # ==========================================
    st.markdown("#### ⚖️ Interaktív tesztelő: Érvényes valószínűségi mező-e?")
    st.write("Egy kísérletnek pontosan 3 lehetséges kimenetele van (A, B, C események, melyek teljes eseményrendszert alkotnak). Állítsd be a valószínűségüket, és nézzük meg, teljesítik-e a Kolmogorov-axiómákat!")
    
    colA, colB, colC = st.columns(3)
    with colA:
        p_a = st.number_input("P(A) esélye:", -0.5, 1.5, 0.3, 0.1)
    with colB:
        p_b = st.number_input("P(B) esélye:", -0.5, 1.5, 0.4, 0.1)
    with colC:
        p_c = st.number_input("P(C) esélye:", -0.5, 1.5, 0.3, 0.1)
        
    k1_pass = p_a >= 0 and p_b >= 0 and p_c >= 0
    osszeg = p_a + p_b + p_c
    k2_pass = abs(osszeg - 1.0) < 0.0001
    
    if not k1_pass:
        st.error("❌ **(K1) Axióma megsértve:** A valószínűség nem lehet negatív! (Legalább egy esemény esélye < 0)")
    elif not k2_pass:
        st.error(f"❌ **(K2) Axióma megsértve:** A biztos esemény (A, B, C együtt) valószínűsége pontosan 1 kell hogy legyen! (A te összeged: {osszeg:.2f})")
    else:
        st.success("✅ **Sikeres axióma-teszt!** Nincs negatív érték (K1 pipa), és az összeg pontosan 1 (K2 pipa). Ez egy érvényes valószínűségi mező!")
        st.write("A **(K3) $\sigma$-additivitás** alapján kiszámolható tetszőleges unió:")
        st.latex(rf"P(A \cup B) = P(A) + P(B) = {p_a:.2f} + {p_b:.2f} = \mathbf{{{p_a+p_b:.2f}}}")

    st.markdown("---")

    # ==========================================
    # 2. KLASSZIKUS VALÓSZÍNŰSÉGI MEZŐ
    # ==========================================
    st.markdown("### 2. Klasszikus valószínűségi mező")
    st.write(r"Legyen $\Omega$ véges nemüres halmaz, $\mathcal{F} = \wp(\Omega)$ és $P : \mathcal{F} \rightarrow \mathbb{R}$, ahol minden $A \in \mathcal{F}$-re:")
    st.latex(r"P(A) = \frac{|A|}{|\Omega|}")
    st.write(r"Ekkor $(\Omega, \mathcal{F}, P)$ **klasszikus valószínűségi mező**.")

    # ==========================================
    # 3. GEOMETRIAI VALÓSZÍNŰSÉGI MEZŐ
    # ==========================================
    st.markdown("### 3. Geometriai valószínűségi mező")
    st.write(r"Tekintsünk egy $(\Omega, \mathcal{F}, P)$ valószínűségi mezőt, ahol $\Omega$ azonosítható egy véges mértékű geometriai alakzattal (pl. egy vonalszakasz, egy síkidom, vagy egy térbeli test).")
    st.write("Tetszőleges $A \subseteq \Omega$ esemény valószínűségét így számoljuk:")
    st.latex(r"P(A) = \frac{\lambda(A)}{\lambda(\Omega)}")
    st.write(r"Ahol $\lambda$ a megfelelő geometriai mérték (hosszúság, terület vagy térfogat), és $0 < \lambda(\Omega) < \infty$.")

    st.markdown("---")

    # ==========================================
    # INTERAKTÍV TESZTELŐ: GEOMETRIA
    # ==========================================
    st.markdown("### 🎯 Interaktív tesztelő: Geometriai valószínűség")
    st.write("Képzeljük el, hogy Gabó dartsot játszik. A céltábla egy $20 \times 20$ cm-es négyzet. Gabó mindig eltalálja a négyzetet, méghozzá teljesen véletlenszerűen, minden pontot egyenlő eséllyel.")
    st.write("A négyzet közepén van egy kör alakú célpont. Állítsd be a kör sugarát, és nézd meg, mennyi az esélye a találatnak!")

    r = st.slider("Célpont sugara (r cm-ben):", 1.0, 10.0, 5.0, 0.5)

    # Számolások
    t_negyzet = 20 * 20
    t_kor = (r ** 2) * 3.14159265

    p_talalat = t_kor / t_negyzet

    col1, col2 = st.columns(2)
    with col1:
        st.warning(f"**Teljes terület $\lambda(\Omega)$:**\nA $20 \\times 20$ négyzet területe:\n\n$\lambda(\Omega) = 400 \\text{{ cm}}^2$")
    with col2:
        st.success(f"**Kedvező terület $\lambda(A)$:**\nAz $r={r}$ sugarú kör területe:\n\n$\lambda(A) = {r}^2 \cdot \pi \approx {t_kor:.1f} \\text{{ cm}}^2$")

    st.info("**Geometriai valószínűség kiszámítása:**")
    st.latex(rf"P(\text{{Találat}}) = \frac{{\lambda(A)}}{{\lambda(\Omega)}} = \frac{{{t_kor:.1f}}}{{400}} \approx \mathbf{{{p_talalat*100:.1f}\%}}")

    st.write("**Találat esélye vizuálisan:**")
    st.progress(min(p_talalat, 1.0))