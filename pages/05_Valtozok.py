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

    with st.expander("5.3 Diszkrét eloszlás összege"):
        st.write("Kidolgozásra vár...")
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