import streamlit as st

st.title("🔗 3. Feltételes valószínűség")
st.markdown("---")

tab1, tab2 = st.tabs(["📚 Tételek", "🧠 Fogalmak"])

with tab1:
    with st.expander("3.1 Szorzás tétel *"):
        # ==========================================
        # 3.1 TÉTEL: SZORZÁSTÉTEL
        # ==========================================
        st.write(r"Ha $(\Omega, \mathcal{F}, P)$ valószínűségi mező, $A, B \in \mathcal{F}$ és $P(B) \neq 0$, akkor:")
        st.latex(r"P(AB) = P(A|B) \cdot P(B)")
        
        st.markdown("**Részletes magyarázat:**")
        st.write("Ez a tétel a feltételes valószínűség definíciójának egyszerű átrendezése. Azt mondja meg, hogy mennyi az esélye annak, hogy két esemény (A és B) **egyszerre** bekövetkezik (ezt jelöli a $P(AB)$ metszet). Ezt úgy kapjuk meg, hogy az egyik esemény valószínűségét megszorozzuk a másik esemény feltételes valószínűségével (vagyis azzal az eséllyel, hogy a második bekövetkezik, *feltéve*, hogy az első már megtörtént).")
        
        if st.checkbox("💡 Logikai indoklás (3.1)", key="biz3_1"):
            st.info("Mivel a tétel csillagos (*), a vizsgán nem kell elvont levezetés, elég az alap definícióból kiindulni:")
            st.write("1. Induljunk ki a feltételes valószínűség alapdefiníciójából ($P(B) \neq 0$):")
            st.latex(r"P(A|B) = \frac{P(AB)}{P(B)}")
            st.write("2. Mivel feltettük, hogy $P(B) \neq 0$, nyugodtan szorozhatjuk az egyenlet mindkét oldalát $P(B)$-vel:")
            st.latex(r"P(A|B) \cdot P(B) = P(AB)")
            st.write("3. Az egyenlet két oldalát felcserélve meg is kaptuk a tételt.")
            
        st.markdown("##### 🃏 Szimuláció 3.1: Kártyahúzás visszatevés nélkül")
        st.write("Húzzunk két lapot egy 52 lapos francia kártyapakliból **visszatevés nélkül**. Mi az esélye, hogy **mindkét lap Ász** lesz ($P(AB)$)?")
        
        col1, col2 = st.columns(2)
        with col1:
            osszes_lap = st.number_input("Lapok száma a pakliban:", min_value=10, max_value=100, value=52)
        with col2:
            keresett_lap = st.number_input("Keresett lapok (pl. Ászok) száma:", min_value=1, max_value=20, value=4)
        
        if keresett_lap >= 2:
            # Számolás
            p_b = keresett_lap / osszes_lap
            p_a_felteteve_b = (keresett_lap - 1) / (osszes_lap - 1)
            p_ab = p_b * p_a_felteteve_b
            
            st.warning("**1. Lépés (B esemény):** Az első lap Ász.")
            st.latex(rf"P(B) = \frac{{{keresett_lap}}}{{{osszes_lap}}} \approx \mathbf{{{p_b*100:.1f}\%}}")
            
            st.warning("**2. Lépés (A|B feltételes esemény):** A második lap is Ász, *feltéve*, hogy az első is az volt. (Figyeld meg, hogy egy Ász és egy lap már hiányzik a pakliból!)")
            st.latex(rf"P(A|B) = \frac{{{keresett_lap - 1}}}{{{osszes_lap - 1}}} \approx \mathbf{{{p_a_felteteve_b*100:.1f}\%}}")
            
            st.success("**Eredmény (Szorzástétel):** A két esemény együttes bekövetkezése (Ász ÉS Ász):")
            st.latex(rf"P(AB) = P(A|B) \cdot P(B) = \frac{{{keresett_lap - 1}}}{{{osszes_lap - 1}}} \cdot \frac{{{keresett_lap}}}{{{osszes_lap}}} \approx \mathbf{{{p_ab*100:.2f}\%}}")
        else:
            st.error("Ahhoz, hogy két Ászt húzzunk, legalább 2 Ásznak kell lennie a pakliban!")
    with st.expander("3.2 A feltételes valószínűség valószínűség"):
        #
        st.write(r"Ha $(\Omega, \mathcal{F}, P)$ valószínűségi mező, $A, B \in \mathcal{F}$ és $P(B) \neq 0$, akkor teljesülnek a Kolmogorov-axiómák a feltételes valószínűségre is:")
        
        st.markdown("#### (1) Nemnegativitás")
        st.latex(r"A \in \mathcal{F} \implies P(A|B) \ge 0")
        
        st.markdown("#### (2) A biztos esemény feltételes valószínűsége")
        st.latex(r"P(\Omega|B) = 1")
        
        st.markdown("#### (3) Végtelen additivitás (σ-additivitás)")
        st.write(r"Ha $A_1, A_2, \dots \in \mathcal{F}$ egymást páronként kizáró események, akkor:")
        st.latex(r"P\left(\sum_{i=1}^\infty A_i \middle| B\right) = \sum_{i=1}^\infty P(A_i|B)")

        st.markdown("**Részletes magyarázat:**")
        st.write("Ez a tétel azt mondja ki, hogy ha feltételként szabunk egy eseményt ($B$), azzal lényegében egy **új, szűkebb valószínűségi mezőt (univerzumot)** hozunk létre, ahol a $B$ lesz az új biztos esemény ($100\%$). Ebben az új 'világban' pontosan ugyanúgy érvényesek a valószínűség alapszabályai, mint az eredetiben.")

        if st.checkbox("💡 Részletes Bizonyítás (3.2)", key="biz3_2"):
            st.info("A bizonyítás lépésről lépésre visszavezeti az állításokat az eredeti Kolmogorov-axiómákra és a feltételes valószínűség definíciójára.")
            
            st.write("**Bizonyítás (1):** Mivel a valószínűség (K1 axióma) eleve nem lehet negatív, egy nemnegatív számot (metszet) osztunk egy pozitív számmal ($P(B)$), ami szintén nemnegatív marad.")
            
            st.write("**Bizonyítás (2):** A biztos eseménnyel ($\Omega$) vett metszet önmaga a halmaz.")
            #
            st.latex(r"P(\Omega|B) = \frac{P(\Omega B)}{P(B)} = \frac{P(B)}{P(B)} = 1")
            
            st.write("**Bizonyítás (3):** Írjuk fel az unió feltételes valószínűségét a definíció alapján!")
            #
            st.latex(r"P\left(\sum_{i=1}^\infty A_i \middle| B\right) = \frac{P\left((A_1 + A_2 + \dots) \cdot B\right)}{P(B)} = \frac{P(A_1B + A_2B + \dots)}{P(B)}")
            st.write("Mivel az $A_i$ események páronként kizárják egymást (metszetük üres), a $B$-vel vett metszeteik is ki fogják zárni egymást:")
            #
            st.latex(r"A_iB \cdot A_jB = A_iA_jBB = A_iA_jB = \emptyset B = \emptyset")
            st.write("Mivel kizárják egymást, a számlálóra alkalmazhatjuk az eredeti (K3) σ-additivitást:")
            #
            st.latex(r"= \frac{\sum_{i=1}^\infty P(A_iB)}{P(B)} = \sum_{i=1}^\infty \frac{P(A_iB)}{P(B)} = \sum_{i=1}^\infty P(A_i|B)")

        st.markdown("##### 🎲 Szimuláció 3.2: Az új univerzum")
        st.write("Dobjunk egy kockával. Legyen a feltételünk ($B$ esemény), hogy **párosat dobtunk** ($B = \{2, 4, 6\}$). Ezzel a $B$ esemény lett az 'új' biztos eseményünk (új $\Omega$, ahol a kimenetelek száma már csak 3)!")
        
        st.info("Próbáljuk ki a (3)-as állítást (additivitás) ebben az új világban! Válassz két egymást kizáró eseményt!")
        
        col1, col2 = st.columns(2)
        with col1:
            a1_esemeny = st.multiselect("A1 esemény (pl. Kettes):", [1, 2, 3, 4, 5, 6], default=[2])
        with col2:
            a2_esemeny = st.multiselect("A2 esemény (pl. Hatos):", [1, 2, 3, 4, 5, 6], default=[6])
            
        b_halmaz = {2, 4, 6}
        a1_halmaz = set(a1_esemeny)
        a2_halmaz = set(a2_esemeny)
        
        if len(a1_halmaz.intersection(a2_halmaz)) == 0:
            # Számolások: A feltételes térben (B) az összes eset száma 3
            kedvezo_a1_b_ben = len(a1_halmaz.intersection(b_halmaz))
            kedvezo_a2_b_ben = len(a2_halmaz.intersection(b_halmaz))
            p_a1_b = kedvezo_a1_b_ben / 3
            p_a2_b = kedvezo_a2_b_ben / 3
            
            unio_halmaz = a1_halmaz.union(a2_halmaz)
            kedvezo_unio_b_ben = len(unio_halmaz.intersection(b_halmaz))
            p_unio_b = kedvezo_unio_b_ben / 3
            
            st.success("**Additivitás a feltételes térben:**")
            st.latex(rf"P(A_1|B) + P(A_2|B) = \frac{{{kedvezo_a1_b_ben}}}{{3}} + \frac{{{kedvezo_a2_b_ben}}}{{3}} = \mathbf{{{p_a1_b + p_a2_b:.2f}}}")
            st.latex(rf"P(A_1 \cup A_2 | B) = \frac{{{kedvezo_unio_b_ben}}}{{3}} = \mathbf{{{p_unio_b:.2f}}}")
            st.write("Látod? A két érték tökéletesen megegyezik! A Kolmogorov-axiómák a szűkített, 'feltételes' halmazban is hibátlanul működnek.")
        else:
            st.error("Az A1 és A2 eseményeknek egymást kizárónak (metszet nélkülinek) kell lenniük az axióma teszteléséhez! Kérlek, válassz különböző számokat.")
    with st.expander("3.3 A feltételes valószínűség tulajdonságai *"):
        # ==========================================
        # 3.3 TÉTEL: FELTÉTELES VALÓSZÍNŰSÉG TULAJDONSÁGAI
        # ==========================================
        st.write(r"Ha $(\Omega, \mathcal{F}, P)$ valószínűségi mező és $A, B, C \in \mathcal{F}$, akkor:")
        
        st.markdown("#### (1) Felső korlát")
        st.latex(r"P(A|B) \le 1, \text{ ha } P(B) \neq 0")
        
        st.markdown("#### (2) Részhalmaz (Biztos esemény lesz)")
        st.latex(r"P(A|B) = 1, \text{ ha } B \subseteq A \text{ és } P(B) \neq 0")
        
        st.markdown("#### (3) Komplementer szabály")
        st.latex(r"P(\overline{A}|B) = 1 - P(A|B), \text{ ha } P(B) \neq 0")
        
        st.markdown("#### (4) Szita-formula feltétellel")
        st.latex(r"P(A+B|C) = P(A|C) + P(B|C) - P(AB|C), \text{ ha } P(C) \neq 0")
        
        st.markdown("#### (5) Események különbsége")
        st.latex(r"P(A-B|C) = P(A|C) - P(AB|C), \text{ ha } P(C) \neq 0")
        
        st.markdown("#### (6) Alsó és felső becslés (Korlátok)")
        st.latex(r"\frac{P(A) + P(B) - 1}{P(B)} \le P(A|B) \le \frac{P(A)}{P(B)}, \text{ ha } P(B) \neq 0")

        st.markdown("**Részletes magyarázat:**")
        st.write("Ahogy az előző tételnél is láttuk, a feltételes valószínűség egy 'új univerzumot' hoz létre. Ez a 6 pont csak megerősíti, hogy a normál valószínűségszámítás szabályai (pl. a komplementer vagy a szita-formula) ebben az új, szűkített univerzumban is pontosan ugyanúgy működnek. A 6. pont egy hasznos becslést ad arra az esetre, ha a feltételes valószínűséget nem tudjuk pontosan kiszámolni, de $P(A)$ és $P(B)$ ismert.")

        if st.checkbox("💡 Logikai indoklás (3.3)", key="biz3_3"):
            st.info("Mivel a tétel csillagos (*), elég szavakkal megindokolni a logikát.")
            st.write("**Ad (1):** Mivel a feltételes valószínűség is egy valószínűség, nem lehet 1-nél nagyobb.")
            st.write("**Ad (2):** Ha $B$ bekövetkezése automatikusan maga után vonja $A$ bekövetkezését (mert $B \subseteq A$), akkor ha tudjuk, hogy $B$ megtörtént, 100% (azaz 1), hogy $A$ is megtörtént.")
            st.write("**Ad (3)-(5):** Ezek az eredeti 2.2-es tételek megfelelői, csak mindent elosztottunk (feltételként betettük) a megadott eseménnyel.")
            st.write("**Ad (6):** Ez a $P(AB) = P(A|B)P(B)$ szorzástétel és a $P(A \cup B) \le 1$ összefüggés kombinációjából adódik, ami megadja a minimum és maximum lehetséges értékét a metszetnek.")

        st.markdown("##### 🎚️ Szimuláció 3.3: A rejtélyes (6)-os korlát tesztelése")
        st.write("Játsszunk a (6)-os állítással! Csak a két alapesemény esélyét tudjuk: $P(A)$ és $P(B)$. A program kiszámolja, hogy milyen minimum és maximum értékek közé kell esnie a $P(A|B)$ feltételes valószínűségnek!")
        
        col1, col2 = st.columns(2)
        with col1:
            p_a_sim = st.slider("P(A) értéke:", 0.0, 1.0, 0.7, 0.05)
        with col2:
            p_b_sim = st.slider("P(B) értéke:", 0.1, 1.0, 0.8, 0.05)
            
        # A becslés kiszámítása
        also_korlat = max(0.0, (p_a_sim + p_b_sim - 1) / p_b_sim)
        felso_korlat = min(1.0, p_a_sim / p_b_sim)
        
        st.info("A (6)-os képlet alapján a feltételes valószínűség határai:")
        st.latex(rf"\frac{{{p_a_sim:.2f} + {p_b_sim:.2f} - 1}}{{{p_b_sim:.2f}}} \le P(A|B) \le \frac{{{p_a_sim:.2f}}}{{{p_b_sim:.2f}}}")
        
        st.success(f"**Eredmény:** Még ha nem is tudjuk a pontos $P(AB)$ metszetet, azt biztosra állíthatjuk, hogy:\n\n**$P(A|B)$ értéke valahol $\mathbf{{{also_korlat*100:.1f}\%}}$ és $\mathbf{{{felso_korlat*100:.1f}\%}}$ között lesz!**")
    with st.expander("3.4 A teljes valószínűség tétele"):
        # ==========================================
        # 3.4 TÉTEL: A TELJES VALÓSZÍNŰSÉG TÉTELE
        # ==========================================
        st.write(r"Legyen $(\Omega, \mathcal{F}, P)$ valószínűségi mező, $B_1, B_2, \dots \in \mathcal{F}$ teljes eseményrendszer és $P(B_i) \neq 0$ minden $i \in \mathbb{N}^+$-ra.")
        st.write("Ekkor tetszőleges $A \in \mathcal{F}$-re teljesül, hogy:")
        st.latex(r"P(A) = \sum_{i=1}^\infty P(A|B_i) \cdot P(B_i)")

        st.markdown("**Részletes magyarázat:**")
        st.write("Gyakorlatban ez a tétel a 'Bontsd részekre és uralkodj' elve. Ha egy $A$ esemény valószínűségét közvetlenül nehéz kiszámolni, de a világot fel tudjuk osztani egymást kizáró és mindent lefedő esetekre ($B_i$ teljes eseményrendszer), akkor elég megnézni, hogy az egyes esetekben mennyi az esélye $A$-nak ($P(A|B_i)$), és ezt beszorozni az adott eset esélyével ($P(B_i)$). Ezeket összeadva megkapjuk a teljes valószínűséget.")

        if st.checkbox("💡 Részletes Bizonyítás (3.4)", key="biz3_4"):
            st.info("A bizonyítás logikája: Az A eseményt felszeleteljük a B eseményrendszer darabjaival, majd a szorzástételt és az additivitást használjuk.")
            
            st.write("**1. Lépés:** A $B_i$-k teljes eseményrendszert alkotnak (lefedik $\Omega$-t) és egymást páronként kizárják (e.p.k.e). Ezért az $A$ esemény felírható a $B_i$-kkel vett metszetek uniójaként:")
            st.latex(r"A = \sum_{i=1}^\infty AB_i")
            
            st.write("**2. Lépés:** Írjuk fel a tétel jobb oldalán lévő szummát, és alkalmazzuk rá a már bizonyított Szorzástételt ($P(A|B_i)P(B_i) = P(AB_i)$):")
            st.latex(r"\sum_{i=1}^\infty P(A|B_i)P(B_i) = \sum_{i=1}^\infty P(AB_i)")
            
            st.write("**3. Lépés:** Mivel a $B_i$-k kizárják egymást, az $AB_i$ metszetek is egymást páronként kizáró események (e.p.k.e). Így használhatjuk rájuk a $\sigma$-additivitást (az összegek valószínűsége = valószínűségek összege):")
            st.latex(r"= P\left(\sum_{i=1}^\infty AB_i\right) = P(A)")
            st.write("Ezzel a láncolattal el is jutottunk a jobb oldaltól a bal oldalig, a tétel bizonyítást nyert.")

        st.markdown("##### 🏭 Szimuláció 3.4: A Hegesztő Üzem (Vizsgapélda!)")
        st.write("Egy üzemben 3 ember dolgozik. Állítsd be, hogy a dolgozók a termelés hány százalékát adják (ez a $B_i$ teljes eseményrendszer, összegüknek 100%-nak kell lennie!), és mennyi a saját selejtaranyuk ($P(A|B_i)$).")
        
        st.write("**A termelés megoszlása $P(B_i)$:**")
        col1, col2, col3 = st.columns(3)
        with col1:
            p_b1 = st.number_input("Gabó termelése (%):", 0, 100, 40) / 100
            p_a_b1 = st.number_input("Gabó selejtaranya (%):", 0, 100, 5) / 100
        with col2:
            p_b2 = st.number_input("Taki Szaki termelése (%):", 0, 100, 25) / 100
            p_a_b2 = st.number_input("Taki selejtaranya (%):", 0, 100, 2) / 100
        with col3:
            p_b3 = st.number_input("Ricsi termelése (%):", 0, 100, 35) / 100
            p_a_b3 = st.number_input("Ricsi selejtaranya (%):", 0, 100, 3) / 100
            
        if abs((p_b1 + p_b2 + p_b3) - 1.0) < 0.001:
            # Teljes valószínűség kiszámítása
            p_a_total = (p_b1 * p_a_b1) + (p_b2 * p_a_b2) + (p_b3 * p_a_b3)
            
            st.success("**Számítás a Teljes Valószínűség Tételével:**\n\nMennyi az esélye, hogy a nap végén egy véletlenszerűen kiválasztott termék **selejt** lesz ($P(A)$)?")
            st.latex(rf"P(A) = P(A|Gabo)P(Gabo) + P(A|Taki)P(Taki) + P(A|Ricsi)P(Ricsi)")
            st.latex(rf"P(A) = ({p_a_b1:.2f} \cdot {p_b1:.2f}) + ({p_a_b2:.2f} \cdot {p_b2:.2f}) + ({p_a_b3:.2f} \cdot {p_b3:.2f}) = \mathbf{{{p_a_total*100:.2f}\%}}")
        else:
            st.error(f"Hiba! A dolgozók termelésének összege pontosan 100% kell legyen (Most: {(p_b1 + p_b2 + p_b3)*100:.0f}%). Kérlek javítsd a számokat!")
    with st.expander("3.5 Bayes-tétel"):
        # ==========================================
        # 3.5 TÉTEL: BAYES-TÉTEL
        # ==========================================
        st.write(r"Legyen $(\Omega, \mathcal{F}, P)$ valószínűségi mező, $B_1, B_2, \dots \in \mathcal{F}$ teljes eseményrendszer, $P(B_i) \neq 0$ minden $i \in \mathbb{N}^+$-ra, továbbá $A \in \mathcal{F}$ és $P(A) \neq 0$.")
        st.write("Ekkor tetszőleges $i \in \mathbb{N}^+$-ra teljesül, hogy:")
        st.latex(r"P(B_i | A) = \frac{P(A | B_i)P(B_i)}{\sum_{k=1}^\infty P(A | B_k)P(B_k)}")

        st.markdown("**Részletes magyarázat:**")
        st.write("Míg a teljes valószínűség tétele az *okozat* (A) bekövetkezésének esélyét számolja ki, a Bayes-tétel pontosan fordítva gondolkodik: az **okok valószínűségét** adja meg. Azt kérdezi: *Ha tudom, hogy az okozat (A) már biztosan bekövetkezett, mekkora eséllyel okozta azt a $B_i$ esemény?* Ezt a hétköznapokban 'visszafelé következtetésnek' is hívják.")

        if st.checkbox("💡 Részletes Bizonyítás (3.5)", key="biz3_5"):
            st.info("A bizonyítás eleganciája abban rejlik, hogy mindössze a feltételes valószínűség definícióját és az előző tételt (Teljes valószínűség) kell behelyettesíteni.")
            
            st.write("**1. Lépés:** Induljunk ki a feltételes valószínűség alapdefiníciójából:")
            st.latex(r"P(B_i|A) = \frac{P(AB_i)}{P(A)}")
            
            st.write("**2. Lépés:** A számlálóban lévő metszetet a definíció (vagy a szorzástétel) alapján írjuk át úgy, hogy a feltételt megfordítjuk:")
            st.latex(r"P(AB_i) = P(A|B_i)P(B_i) \implies \frac{P(A|B_i)P(B_i)}{P(A)}")
            
            st.write("**3. Lépés:** A nevezőben lévő $P(A)$ valószínűségre egyszerűen alkalmazzuk a 3.4-es Teljes valószínűség tételét:")
            st.latex(r"= \frac{P(A|B_i)P(B_i)}{\sum_{k=1}^\infty P(A|B_k)P(B_k)}")
            st.write("És ezzel a tétel bizonyítást is nyert!")

        st.markdown("##### 🕵️ Szimuláció 3.5: Nyomozás a Hegesztő Üzemben (2. Kérdés)")
        st.write("Folytassuk a 3.4-es példát! Művezető József talál egy **selejtet** (A esemény biztosan bekövetkezett). Kinek keverjen le egy pofont? Melyik dolgozó volt a legvalószínűbb elkövető?")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            p_b1 = st.number_input("Gabó termelése (P(B1)):", 0.0, 1.0, 0.40, 0.01)
            p_a_b1 = st.number_input("Gabó selejtaranya (P(A|B1)):", 0.0, 1.0, 0.05, 0.01)
        with col2:
            p_b2 = st.number_input("Taki termelése (P(B2)):", 0.0, 1.0, 0.25, 0.01)
            p_a_b2 = st.number_input("Taki selejtaranya (P(A|B2)):", 0.0, 1.0, 0.02, 0.01)
        with col3:
            p_b3 = st.number_input("Ricsi termelése (P(B3)):", 0.0, 1.0, 0.35, 0.01)
            p_a_b3 = st.number_input("Ricsi selejtaranya (P(A|B3)):", 0.0, 1.0, 0.03, 0.01)
            
        if abs((p_b1 + p_b2 + p_b3) - 1.0) < 0.001:
            # 1. Teljes valószínűség kiszámítása (Nevező)
            p_a_total = (p_b1 * p_a_b1) + (p_b2 * p_a_b2) + (p_b3 * p_a_b3)
            
            # 2. Bayes-tétel alkalmazása (Okok valószínűsége)
            bayes_gabo = (p_a_b1 * p_b1) / p_a_total
            bayes_taki = (p_a_b2 * p_b2) / p_a_total
            bayes_ricsi = (p_a_b3 * p_b3) / p_a_total
            
            st.warning("**A Bayes-tétel kiszámolja, mekkora eséllyel készült a selejt az egyes dolgozóknál:**")
            
            st.latex(rf"P(\text{{Gabó}} | \text{{Selejt}}) = \frac{{{p_a_b1:.2f} \cdot {p_b1:.2f}}}{{{p_a_total:.4f}}} = \mathbf{{{bayes_gabo*100:.1f}\%}}")
            st.latex(rf"P(\text{{Taki}} | \text{{Selejt}}) = \frac{{{p_a_b2:.2f} \cdot {p_b2:.2f}}}{{{p_a_total:.4f}}} = \mathbf{{{bayes_taki*100:.1f}\%}}")
            st.latex(rf"P(\text{{Ricsi}} | \text{{Selejt}}) = \frac{{{p_a_b3:.2f} \cdot {p_b3:.2f}}}{{{p_a_total:.4f}}} = \mathbf{{{bayes_ricsi*100:.1f}\%}}")
            
            import pandas as pd
            df = pd.DataFrame({
                "Dolgozók": ["Gabó", "Taki Szaki", "Prof Ricsi"],
                "Bűnösség esélye": [bayes_gabo, bayes_taki, bayes_ricsi]
            })
            st.write("**Vizuális eredmény (ki kapja a pofont?):**")
            st.bar_chart(df.set_index("Dolgozók"))
            
        else:
            st.error("Hiba! A dolgozók termelésének összege (P(B1)+P(B2)+P(B3)) pontosan 1.0 kell legyen!")

with tab2:
    st.header("🧠 Fogalmak definíciói")
    st.write("A 3. tételhez (Feltételes valószínűség) tartozó hivatalos definíciók:")

    # ==========================================
    # 1. FELTÉTELES VALÓSZÍNŰSÉG
    # ==========================================
    st.markdown("### 1. Feltételes valószínűség")
    st.write(r"Legyen $(\Omega, \mathcal{F}, P)$ valószínűségi mező, $A, B \in \mathcal{F}$ és $P(B) \neq 0$. Ekkor a következő hányadost az $A$ esemény $B$-re vonatkozó **feltételes valószínűségének** nevezzük:")
    st.latex(r"P(A|B) := \frac{P(AB)}{P(B)}")
    
    st.info("💡 **Intuitív jelentés:** Azt mutatja meg, hogy mekkora eséllyel következik be az $A$ esemény, ha azt az extra információt kapjuk, hogy a $B$ esemény már biztosan bekövetkezett. Ilyenkor a $B$ esemény lesz az 'új' univerzumunk (a nevező).")

    # ==========================================
    # 2. TÁGABB ÉRTELEMBEN VETT TELJES ESEMÉNYRENDSZER
    # ==========================================
    st.markdown("### 2. Tágabb értelemben vett teljes eseményrendszer")
    st.write(r"A $\mathcal{B} := B_1, B_2, \dots$ eseményrendszert, amelynek elemei egymást páronként kizáróak és:")
    st.latex(r"P\left(\sum_{i=1}^{\infty} B_i\right) = 1")
    st.write(r"**tágabb értelemben vett teljes eseményrendszernek** nevezzük.")
    
    st.warning("⚠️ **Mi a különbség a sima teljes eseményrendszertől?** A 'sima' definíciónál a halmazok uniójának hajszálpontosan ki kell adnia a teljes $\Omega$ teret. A 'tágabb' értelemnél elég, ha a valószínűségük összege 1 (tehát kimaradhatnak olyan 0 valószínűségű, lehetetlen események, amik fizikailag léteznek ugyan, de matematikai esélyük nulla).")

    st.markdown("---")

    # ==========================================
    # INTERAKTÍV TESZTELŐ: FELTÉTELES VALÓSZÍNŰSÉG
    # ==========================================
    st.markdown("### 🎲 Interaktív tesztelő: Az 'Új Univerzum'")
    st.write("Dobjunk egy szabályos 6-oldalú kockával. Számoljuk ki a feltételes valószínűséget a definíció alapján!")
    
    col1, col2 = st.columns(2)
    with col1:
        a_lista = st.multiselect("A esemény (Amit keresünk):", [1, 2, 3, 4, 5, 6], default=[6])
    with col2:
        b_lista = st.multiselect("B esemény (A feltétel, ami TUDJUK, hogy bekövetkezett):", [1, 2, 3, 4, 5, 6], default=[2, 4, 6])
        
    A = set(a_lista)
    B = set(b_lista)
    metszet = A.intersection(B)
    
    p_a = len(A) / 6
    p_b = len(B) / 6
    p_metszet = len(metszet) / 6
    
    if p_b > 0:
        p_a_feltetel_b = p_metszet / p_b
        
        st.write(f"**Alap valószínűségek:** $P(A) = {len(A)}/6$, $P(B) = {len(B)}/6$, $P(AB) = {len(metszet)}/6$")
        
        st.success(f"**Feltételes valószínűség $P(A|B)$:**")
        st.latex(rf"P(A|B) = \frac{{P(AB)}}{{P(B)}} = \frac{{{len(metszet)}/6}}{{{len(B)}/6}} = \frac{{{len(metszet)}}}{{{len(B)}}} = \mathbf{{{p_a_feltetel_b*100:.1f}\%}}")
        
        st.write("Vedd észre: Amint megtudtuk, hogy B bekövetkezett, az összes lehetséges eset (a képlet legvégi nevezője) 6-ról lecsökkent B elemeinek számára!")
    else:
        st.error("A feltétel (B) valószínűsége nem lehet 0! Válassz legalább egy elemet a B eseményhez.")