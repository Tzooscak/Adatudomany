import streamlit as st

st.title("📊 5. Valószínűségi változó")
st.markdown("---")

tab1, tab2 = st.tabs(["📚 Tételek", "🧠 Fogalmak"])

with tab1:
    st.info("Ez a fejezet tartalmazza a legtöbb tételt. Oszd be jól az idődet a tanulásnál! (Az elrendezés most kényelmesen egymás alatti.)")
    
    with st.expander("5.1 Valószínűségi változók és események (TÉTEL)"):
        # ==========================================
        # 5.1 TÉTEL: VALÓSZÍNŰSÉGI VÁLTOZÓK ÉS ESEMÉNYEK
        # ==========================================
        st.write(r"Legyen $\xi$ egy $(\Omega, \mathcal{F}, P)$ valószínűségi mezőben értelmezett valószínűségi változó. Ekkor $\forall k, l \in \mathbb{R}$ esetén a")
        st.latex(r"\{\xi \le k\}, \quad \{\xi = k\}, \quad \{\xi > k\} \quad \text{és} \quad \{l < \xi < k\}")
        st.write(r"halmazok **események** (azaz garantáltan benne vannak az $\mathcal{F}$ $\sigma$-algebrában).")

        st.markdown(r"**Részletes magyarázat (Miért fontos ez a tétel?):**")
        st.write(r"Emlékezz vissza: a valószínűségi változó hivatalos definíciója *csak* azt kötötte ki, hogy a szigorúan kisebb ($\{\xi < k\}$) halmazok legyenek események. De a gyakorlatban ritkán kérdezzük csak ezt! Általában olyanokra vagyunk kíváncsiak, hogy 'Pistike pont 4-est dobott' ($=$), vagy 'Legalább 10 pontot ért el' ($\ge$).")
        st.write(r"Ez a tétel azt bizonyítja be, hogy a definícióból kiindulva, pusztán az alap halmazműveletek (metszet, komplementer) segítségével az összes többi matematikai egyenlőtlenséget fel tudjuk építeni. És mivel ezek események lesznek, **kiszámolhatjuk a valószínűségüket**!")

        if st.checkbox("💡 Részletes Bizonyítás (5.1)", key="biz5_1"):
            st.info(r"A bizonyítás során a $\sigma$-algebra tulajdonságait használjuk (komplementerképzés, végtelen metszet) úgy, mint a legókockákat.")
            
            st.markdown(r"**1. A kisebb-egyenlő $\{\xi \le k\}$ halmaz felépítése:**")
            st.write(r"A definícióból tudjuk, hogy minden pozitív $n$ egész számra a 'picit nagyobb' halmaz egy érvényes esemény:")
            st.latex(r"\{\xi < k + \frac{1}{n}\} \in \mathcal{F}")
            st.write(r"A $\sigma$-algebrában a megszámlálhatóan végtelen sok esemény metszete is esemény. Ha ezeket a halmazokat ($k+1$, $k+0.5$, $k+0.33$, stb.) mind elmetsszük egymással a végtelenig, a határértékük pontosan a 'kisebb vagy egyenlő' relációt adja ki:")
            st.latex(r"\bigcap_{n=1}^\infty \{\xi < k + \frac{1}{n}\} = \{\xi \le k\} \implies \{\xi \le k\} \in \mathcal{F}")
            
            st.markdown(r"**2. A többi reláció felépítése (Logikai legózás):**")
            
            st.write(r"**Nagyobb vagy egyenlő ($\ge$):** A $\sigma_2$ axióma alapján a komplementer (ellentett) is esemény:")
            st.latex(r"\{\xi < k\} \in \mathcal{F} \implies \overline{\{\xi < k\}} = \{\xi \ge k\} \in \mathcal{F}")
            
            st.write(r"**Pontosan egyenlő ($=$):** Ha valami kisebb-egyenlő $k$-nál, ÉS nagyobb-egyenlő $k$-nál, az csakis $k$ lehet. Ez két esemény metszete:")
            st.latex(r"\{\xi = k\} = \{\xi \le k\} \cap \{\xi \ge k\} \in \mathcal{F}")
            
            st.write(r"**Szigorúan nagyobb ($>$):** Egyszerűen a kisebb-egyenlő komplementere:")
            st.latex(r"\{\xi > k\} = \overline{\{\xi \le k\}} \in \mathcal{F}")
            
            st.write(r"**Két érték közé esik ($l < x < k$):** A szigorúan nagyobb és a szigorúan kisebb események metszete:")
            st.latex(r"\{l < \xi < k\} = \{\xi > l\} \cap \{\xi < k\} \in \mathcal{F}")

        st.markdown(r"##### 🧮 Szimuláció 5.1: A Reláció-építő")
        st.write(r"Legyen a kísérletünk egy D20-as (20 oldalú) kocka eldobása. A valószínűségi változónk a dobott érték: $\xi = x$. Játsszunk a relációkkal, és nézzük meg, hogyan adja ki a program az esemény halmazát!")
        
        col_k, col_rel = st.columns([1, 2])
        with col_k:
            k_ertek = st.number_input("Válassz egy 'k' értéket:", 1, 20, 10)
        with col_rel:
            relacio = st.selectbox("Melyik relációt (eseményt) vizsgáljuk?", 
                                  ["Szigorúan kisebb (Definíció): ξ < k", 
                                   "Kisebb vagy egyenlő: ξ ≤ k", 
                                   "Pontosan egyenlő: ξ = k", 
                                   "Szigorúan nagyobb: ξ > k",
                                   "Nagyobb vagy egyenlő: ξ ≥ k"])
        
        omega_d20 = set(range(1, 21))
        eredmeny_halmaz = []
        
        if "ξ < k" in relacio:
            eredmeny_halmaz = [x for x in omega_d20 if x < k_ertek]
            magyarazat = "Ezt kapjuk meg 'ingyen' a valószínűségi változó alap definíciójából."
        elif "ξ ≤ k" in relacio:
            eredmeny_halmaz = [x for x in omega_d20 if x <= k_ertek]
            magyarazat = "Ezt az egyre szűkülő halmazok végtelen metszetével építettük fel a bizonyításban."
        elif "ξ = k" in relacio:
            eredmeny_halmaz = [x for x in omega_d20 if x == k_ertek]
            magyarazat = "Ezt a (ξ ≤ k) és a (ξ ≥ k) halmazok metszeteként kaptuk meg."
        elif "ξ > k" in relacio:
            eredmeny_halmaz = [x for x in omega_d20 if x > k_ertek]
            magyarazat = "Ezt a (ξ ≤ k) halmaz komplementereként (ellentettjeként) számoltuk ki."
        elif "ξ ≥ k" in relacio:
            eredmeny_halmaz = [x for x in omega_d20 if x >= k_ertek]
            magyarazat = "Ezt a definíció szerinti (ξ < k) halmaz komplementereként kaptuk."
            
        st.success(f"**A kiválasztott esemény kimenetelei:** `{eredmeny_halmaz}`")
        st.caption(f"💡 *Hogyan jött ki matematikailag?* {magyarazat}")

    with st.expander(r"5.2 Tétel ({ξ < η} esemény)"):
        st.write(r"Legyenek $\xi$ és $\eta$ egy $(\Omega, \mathcal{F}, P)$ valószínűségi mezőben értelmezett valószínűségi változók. Ekkor a:")
        st.latex(r"\{\xi < \eta\} \text{ halmaz esemény.}")
        st.write(r"**Magyarázat:** Ez a tétel azt mondja ki, hogy nemcsak konstans számokkal (pl. $\xi < 5$) tudunk eseményeket létrehozni, hanem két valószínűségi változót is összehasonlíthatunk egymással (pl. 'Gabó dobása kisebb, mint Ricsi dobása', és ez is érvényes esemény lesz).")

    with st.expander(r"5.3 Diszkrét eloszlás összege (TÉTEL)"):
        # ==========================================
        # 5.3 TÉTEL: DISZKRÉT ELOSZLÁS ÖSSZEGE
        # ==========================================
        st.write(r"Ha $\xi$ egy $(\Omega, \mathcal{F}, P)$ valószínűségi mezőben értelmezett diszkrét valószínűségi változó $\langle p_x \rangle$ eloszlással, akkor:")
        st.latex(r"\sum_{x \in \text{rng}(\xi)} p_x = 1")
        
        st.markdown(r"**Részletes magyarázat:**")
        st.write(r"Ez a tétel azt mondja ki, hogy ha egy diszkrét valószínűségi változó (pl. egy dobókocka értéke) felvesz bizonyos értékeket (ez az értékkészlete, $\text{rng}(\xi)$), akkor ezekhez az értékekhez tartozó valószínűségek ($p_x$) összege mindig hajszálpontosan 1 (azaz 100%). Hiszen valaminek mindenképpen történnie kell a kísérlet során!")

        if st.checkbox(r"💡 Részletes Bizonyítás (5.3)", key="biz5_3"):
            st.info(r"A bizonyítás logikája: A lehetséges kimenetelek (értékek) egy teljes eseményrendszert alkotnak, aminek az összege a biztos esemény.")
            
            st.write(r"1. Jelölje $A_x$ azt az eseményt, hogy a változó éppen az $x$ értéket veszi fel:")
            st.latex(r"A_x := \{\xi = x\}, \quad x \in \text{rng}(\xi)")
            
            st.write(r"2. Mivel a $\xi$ függvény egy adott $\omega$ kimenetelhez csakis egyetlen számot rendelhet hozzá, ezek az $A_x$ halmazok páronként kizárják egymást. Valamelyik viszont biztosan bekövetkezik, tehát **teljes eseményrendszert alkotnak**!")
            
            st.write(r"3. Írjuk fel a valószínűségek összegét (a $\sigma$-additivitás és a teljes eseményrendszer miatt):")
            st.latex(r"\sum_{x \in \text{rng}(\xi)} p_x = \sum_{x \in \text{rng}(\xi)} P(A_x) = P\left( \sum_{x \in \text{rng}(\xi)} A_x \right) = P(\Omega) = 1")
            st.success(r"Mivel a biztos esemény ($P(\Omega)$) valószínűsége 1, a tétel bizonyítást nyert.")

        st.markdown(r"##### ⚖️ Szimuláció 5.3: A Cinkelt Kocka")
        st.write(r"Készítsünk egy cinkelt 3-oldalú dobókockát! Állítsd be az egyes oldalak esélyét ($p_1, p_2, p_3$). A matematika törvényei szerint az összegüknek szigorúan 1.0-nak kell lennie.")
        
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            p1 = st.number_input("P(ξ = 1)", min_value=0.0, max_value=1.0, value=0.3, step=0.1)
        with col_p2:
            p2 = st.number_input("P(ξ = 2)", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
        with col_p3:
            p3 = st.number_input("P(ξ = 3)", min_value=0.0, max_value=1.0, value=0.2, step=0.1)
            
        szumma_p = p1 + p2 + p3
        
        st.write(r"**Az eloszlás összege:**")
        st.latex(rf"\sum p_x = {p1:.2f} + {p2:.2f} + {p3:.2f} = \mathbf{{{szumma_p:.2f}}}")
        
        if abs(szumma_p - 1.0) < 0.001:
            st.success(r"✅ **Helyes eloszlás!** Az összeg pontosan 1, ez egy érvényes diszkrét valószínűségi változó.")
            st.progress(1.0)
        else:
            st.error(rf"❌ **Hibás eloszlás!** A valószínűségek összege {szumma_p*100:.0f}%, ami megsérti az 5.3-as tételt. Kérlek javítsd ki úgy, hogy pontosan 1.0 legyen!")
            st.progress(min(szumma_p, 1.0))
    with st.expander(r"5.4 $\xi$ egzisztenciája diszkrét eloszláshoz (TÉTEL)"):
        # ==========================================
        # 5.4 TÉTEL: EGZISZTENCIA
        # ==========================================
        st.write(r"Legyen $X \subset \mathbb{R}$ nemüres megszámlálható halmaz, $\langle p_x \rangle : X \rightarrow [0, 1]$ és:")
        st.latex(r"\sum_{x \in X} p_x = 1")
        st.write(r"Ekkor létezik olyan $(\Omega, \mathcal{F}, P)$ valószínűségi mező és azon értelmezett $\xi$ valószínűségi változó, amelyre $\text{rng}(\xi) = X$ és eloszlása $\langle p_x \rangle$.")

        st.markdown(r"**Részletes magyarázat (A 'Fordított Tervezés' tétele):**")
        st.write(r"Az 5.3-as tétel azt mondta, hogy ha van egy létező változónk, annak az eloszlása (a kimenetelek esélyei) kiadja az 1-et. Ez az 5.4-es tétel pontosan a fordítottja! Azt mondja ki, hogy ha valaki letesz az asztalra egy kupac számot és hozzájuk tartozó valószínűségeket úgy, hogy azok összege pontosan 1, akkor garantáltan fel tudunk építeni köré egy elméleti, de szabályos matematikai világot.")

        if st.checkbox(r"💡 Részletes Bizonyítás (5.4)", key="biz5_4"):
            st.info(r"A bizonyítás konstruktív jellegű: szó szerint legyártjuk a szükséges halmazokat és függvényeket a tétel állításához.")

            st.write(r"**1. A valószínűségi mező felépítése:** Legyen maga az $X$ halmaz a teljes eseményterünk, a $\sigma$-algebra pedig ennek minden lehetséges részhalmaza (hatványhalmaz):")
            st.latex(r"\Omega := X \quad \text{és} \quad \mathcal{F} = \wp(\Omega)")

            st.write(r"**2. A valószínűség ($P$) definiálása:** Bármely $A \in \mathcal{F}$ esemény valószínűsége legyen egyszerűen a benne lévő $x$ értékekhez tartozó $p_x$ valószínűségek összege:")
            st.latex(r"P : \mathcal{F} \rightarrow \mathbb{R}, \quad P(A) := \sum_{x \in A} p_x")

            st.write(r"**3. A valószínűségi változó ($\xi$) definiálása:** Végül ezen a kész mezőn értelmezzünk egy olyan $\xi : \Omega \rightarrow \mathbb{R}$ függvényt, ami minden elemet egyszerűen önmagába visz át (identitás):")
            st.latex(r"\xi_x = x")
            st.success(r"Ezzel készen is vagyunk! Sikerült egy olyan $(\Omega, \mathcal{F}, P)$ rendszert kreálnunk, ami pontosan a megadott $\langle p_x \rangle$ eloszlást követi.")

        st.markdown(r"##### 🏗️ Szimuláció 5.4: A Valószínűség-Építő")
        st.write(r"Kitalálsz egy saját számítógépes játékot, ahol a ládákból 10, 50, vagy 100 arany eshet. Ha a tervezett esélyek kiadják az 1-et (100%), a gép legenerálja neked a mögöttes valószínűségi mezőt!")

        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            p_10 = st.number_input("P(10 arany)", min_value=0.0, max_value=1.0, value=0.6, step=0.05)
        with col_p2:
            p_50 = st.number_input("P(50 arany)", min_value=0.0, max_value=1.0, value=0.3, step=0.05)
        with col_p3:
            p_100 = st.number_input("P(100 arany)", min_value=0.0, max_value=1.0, value=0.1, step=0.05)
            
        szumma = p_10 + p_50 + p_100
        
        if abs(szumma - 1.0) < 0.001:
            st.success(r"✅ **Sikeres építés!** A valószínűségek összege 1. A bizonyítás alapján a következő mezőt generáltuk le:")
            st.latex(r"\Omega = \{10, 50, 100\}")
            st.latex(r"\mathcal{F} = \{\emptyset, \{10\}, \{50\}, \{100\}, \{10, 50\}, \{10, 100\}, \{50, 100\}, \Omega\}")
            st.latex(rf"P(\{{10, 50\}}) = {p_10:.2f} + {p_50:.2f} = \mathbf{{{p_10 + p_50:.2f}}}")
        else:
            st.error(rf"❌ **Sikertelen építés!** A valószínűségek összege jelenleg {szumma*100:.0f}%. Az 5.4-es tétel csak akkor tudja felépíteni a mezőt, ha pontosan 100% az összeg!")
    with st.expander("5.5 Eloszlásfüggvény tulajdonságai *"):
        st.write("Kidolgozásra vár...")
    with st.expander("5.9 {a ≤ ξ < b} és a sűrűségfüggvény"):
        st.write("Kidolgozásra vár...")
    with st.expander("5.11 Sűrűségfüggvény integrálja"):
        st.write("Kidolgozásra vár...")
    with st.expander("5.16 A várható érték tulajdonságai"):
        st.write("Kidolgozásra vár...")
    with st.expander("5.18 A szórás tulajdonságai *"):
        st.write("Kidolgozásra vár...")
    with st.expander("5.19 A kovariancia kiszámolása"):
        st.write("Kidolgozásra vár...")
    with st.expander("5.20 Kovariancia és függetlenség"):
        st.write("Kidolgozásra vár...")
    with st.expander("5.25 Korreláció és függőség *"):
        st.write("Kidolgozásra vár...")

with tab2:
    st.header("🧠 Fogalmak definíciói")
    st.write("Az 5. fejezethez (Valószínűségi változó) tartozó hivatalos definíciók:")

    # ==========================================
    # 1. VALÓSZÍNŰSÉGI VÁLTOZÓ ÉS JELÖLÉSEK
    # ==========================================
    st.markdown("### 1. Valószínűségi változó és Jelölések")
    st.write(r"Legyen $\Omega$ egy eseménytér és $\xi : \Omega \rightarrow \mathbb{R}$ egy függvény.")
    st.write(r"Ekkor a $\{\xi = x\}$ jelölés azt az eseményt jelenti, amely tartalmazza az összes olyan kimenetelt, amelyre a függvény értéke $x$:")
    st.latex(r"\{\xi = x\} := \{\omega : \omega \in \Omega \land \xi(\omega) = x\}")
    st.write(r"Hasonlóan definiálhatjuk a $\{\xi < x\}$, $\{\xi > x\}$, $\{\xi = \eta\}$ stb. halmazokat is.")

    st.markdown("#### Definíció (Valószínűségi változó)")
    st.write(r"Legyen $(\Omega, \mathcal{F}, P)$ valószínűségi mező és $\xi : \Omega \rightarrow \mathbb{R}$.")
    st.write(r"A $\xi$-t **valószínűségi változónak** (Random Variable) nevezzük, ha minden valós számra a $\{\xi < k\}$ halmaz egy érvényes esemény (azaz benne van a $\sigma$-algebrában):")
    st.latex(r"\forall k \in \mathbb{R} : \{\xi < k\} \in \mathcal{F}")

    st.info(r"💡 **Józan paraszti ésszel:** A valószínűségi változó valójában nem is 'változó', hanem egy **függvény**! Fog egy szöveges/fizikai kimenetelt (pl. 'Fej', 'Kettes dobás'), és hozzárendel egy konkrét számot, hogy tudjunk vele számolni az egyenletekben.")

    # ==========================================
    # 2. DISZKRÉT VÁLTOZÓ ÉS ELOSZLÁS
    # ==========================================
    st.markdown("### 2. Diszkrét valószínűségi változó és Eloszlás")
    st.write(r"Egy valószínűségi változó **diszkrét valószínűségi változó**, ha értékkészlete megszámlálható számosságú. (Azaz fel tudjuk sorolni az értékeit, pl. dobókocka dobás, lottószámok, hibás termékek száma).")
    
    st.markdown("#### Eloszlás (Tömegfüggvény / PMF)")
    st.write(r"Legyen $\xi$ egy $(\Omega, \mathcal{F}, P)$ valószínűségi mezőben értelmezett diszkrét valószínűségi változó. Ekkor a:")
    st.latex(r"\langle p_x \rangle : \text{rng}(\xi) \rightarrow [0, 1], \quad p_x := P(\xi = x)")
    st.write(r"sorozat a $\xi$ **eloszlása** (angolul Probability Mass Function, PMF, magyarul gyakran Tömegfüggvény).")
    st.info(r"💡 **Gyakorlati jelentése:** Az eloszlás egyszerűen egy lista vagy táblázat, ami minden lehetséges kimenetelhez hozzárendeli, hogy pontosan mekkora eséllyel következik be. Például egy kockadobásnál: $p_1 = 1/6, p_2 = 1/6, \dots$")

    st.markdown("---")

    # ==========================================
    # INTERAKTÍV TESZTELŐ: VALÓSZÍNŰSÉGI VÁLTOZÓ
    # ==========================================
    st.markdown("### 🎲 Interaktív tesztelő: Készítsünk valószínűségi változót!")
    st.write("Dobjunk fel **két darab pénzérmét**. A lehetséges kimenetelek ( $\Omega$ ): `{FF, FÍ, ÍF, ÍÍ}`.")
    st.write(r"Definiáljuk a $\xi$ (kszí) valószínűségi változót így: **$\xi = \text{Fejek száma a dobásban}$**.")

    # A függvény leképezése
    st.write(r"Ez a $\xi$ függvény a következőképpen rendeli a számokat a kimenetelekhez:")
    st.latex(r"\xi(FF) = 2, \quad \xi(FÍ) = 1, \quad \xi(ÍF) = 1, \quad \xi(ÍÍ) = 0")

    st.write("Próbáljuk ki a jelöléseket a gyakorlatban! Állítsd be az $x$ értékét, és nézd meg, mely kimenetelek tartoznak az adott halmazba!")
    
    ertek = st.slider("Válaszd ki az 'x' értékét a vizsgálathoz:", -1, 3, 1)

    col1, col2 = st.columns(2)
    with col1:
        st.success(rf"**Esemény: $\\{{\xi = {ertek}\\}}$**")
        st.caption("Melyik dobásoknál lesz a fejek száma pontosan ennyi?")
        if ertek == 2:
            st.write("Kimenetelek: `{FF}`")
        elif ertek == 1:
            st.write("Kimenetelek: `{FÍ, ÍF}`")
        elif ertek == 0:
            st.write("Kimenetelek: `{ÍÍ}`")
        else:
            st.write("Kimenetelek: `∅` (Lehetetlen esemény)")
            
    with col2:
        st.warning(rf"**Esemény: $\\{{\xi < {ertek}\\}}$**")
        st.caption("Melyik dobásoknál lesz a fejek száma szigorúan kevesebb, mint ennyi?")
        halmaz = []
        if 0 < ertek: halmaz.append("ÍÍ")
        if 1 < ertek: 
            halmaz.append("FÍ")
            halmaz.append("ÍF")
        if 2 < ertek: halmaz.append("FF")
        
        if len(halmaz) > 0:
            st.write(f"Kimenetelek: `{{{', '.join(halmaz)}}}`")
        else:
            st.write("Kimenetelek: `∅` (Lehetetlen esemény)")

    # ==========================================
    # 3. ELOSZLÁSFÜGGVÉNY (CDF)
    # ==========================================
    st.markdown("### 3. Eloszlásfüggvény (CDF)")
    st.write(r"Legyen $\xi$ egy $(\Omega, \mathcal{F}, P)$ valószínűségi mezőben értelmezett valószínűségi változó. Ekkor az")
    st.latex(r"F_\xi : \mathbb{R} \rightarrow \mathbb{R}, \quad F_\xi(x) := P(\xi < x)")
    st.write(r"függvényt a $\xi$ **eloszlásfüggvényének** (Cumulative Distribution Function, CDF) nevezzük.")

    st.info(r"💡 **Fontos megjegyzések a diáról:**"
            "\n- A definíció miatt egy valószínűségi változónak **mindig** létezik eloszlásfüggvénye."
            "\n- Diszkrét valószínűségi változónak is van eloszlásfüggvénye (ez egy 'lépcsős' függvény), ekkor $F_\xi$ értékkészlete megszámlálható."
            "\n- ⚠️ **Beugratós kérdés:** A fordítottja nem igaz! Ha egy $F_\xi$ függvény értékkészlete megszámlálható, abból matematikai okok miatt még nem következik biztosan, hogy maga a $\xi$ változó diszkrét.")

    st.markdown("---")

    # ==========================================
    # INTERAKTÍV TESZTELŐ: ELOSZLÁSFÜGGVÉNY
    # ==========================================
    st.markdown("### 📈 Interaktív tesztelő: A dobókocka eloszlásfüggvénye")
    st.write(r"Az eloszlásfüggvény a **szigorúan kisebb** valószínűségeket 'gyűjti össze' (halmozza). Nézzük meg egy hagyományos 6-oldalú dobókocka eloszlásfüggvényét! A képlet: $F(x) = P(\xi < x)$.")

    x_val = st.slider("Vizsgált 'x' érték (lehet tizedestört is!):", 0.0, 7.0, 3.5, 0.5)

    import math
    
    # Kiszámoljuk a P(xi < x) értéket
    if x_val <= 1.0:
        cdf_val = 0.0
        magyarazat = "Mivel a kockával nem dobhatunk 1-nél kisebbet, a valószínűség garantáltan 0."
    elif x_val > 6.0:
        cdf_val = 1.0
        magyarazat = "A kockával biztosan 6-osat vagy annál kisebbet dobunk (ami szigorúan kisebb, mint a megadott érték). Ez a biztos esemény, valószínűsége 100%."
    else:
        # Kiszámoljuk, hány olyan egész szám (kockaoldal) van, ami szigorúan kisebb az x_val-nál
        kedvezo = math.ceil(x_val) - 1
        cdf_val = kedvezo / 6.0
        magyarazat = rf"Pontosan {kedvezo} db olyan szám van a kockán, ami szigorúan kisebb, mint {x_val:.1f} (a lehetséges 6-ból)."

    st.success(r"**Az eloszlásfüggvény értéke a megadott pontban:**")
    st.latex(rf"F_\xi({x_val:.1f}) = P(\xi < {x_val:.1f}) = \frac{{{int(cdf_val * 6)}}}{{6}} \approx \mathbf{{{cdf_val:.3f}}}")
    st.write(f"**Magyarázat:** {magyarazat}")
    
    st.write("**A 'halmozott' (kumulatív) valószínűség:**")
    st.progress(cdf_val)