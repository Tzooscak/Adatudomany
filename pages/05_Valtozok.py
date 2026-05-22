import streamlit as st

st.title("📊 5. Valószínűségi változó")
st.markdown("---")

tab1, tab2 = st.tabs(["📚 Tételek", "🧠 Fogalmak"])

with tab1:
    st.info("Ez a fejezet tartalmazza a legtöbb tételt. Oszd be jól az idődet a tanulásnál!")
    
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

    with st.expander(r"5.5 Eloszlásfüggvény tulajdonságai (TÉTEL)"):
        # ==========================================
        # 5.5 TÉTEL: ELOSZLÁSFÜGGVÉNY TULAJDONSÁGAI
        # ==========================================
        st.write(r"Legyen $\xi$ egy $(\Omega, \mathcal{F}, P)$ valószínűségi mezőben értelmezett valószínűségi változó. Ekkor az $F_\xi$ eloszlásfüggvényre igazak a következők:")
        
        st.latex(r"(F1) \quad F_\xi \text{ monoton növő}")
        st.latex(r"(F2) \quad \lim_{x \to +\infty} F_\xi(x) = 1")
        st.latex(r"(F3) \quad \lim_{x \to -\infty} F_\xi(x) = 0")
        st.latex(r"(F4) \quad F_\xi \text{ minden pontban balról folytonos}")

        st.markdown(r"**Magyarázat az 5.5-höz:**")
        st.write(r"Ezek a tulajdonságok logikusak, ha belegondolunk, hogy az eloszlásfüggvény a 'felhalmozott' valószínűséget mutatja. Nem csökkenhet (hiszen a valószínűség sosem negatív, így mindig csak adunk hozzá). A mínusz végtelenben még semmi sem történt (0%), a plusz végtelenben pedig már minden lehetséges eset megtörtént, így kimaxoljuk a 100%-ot (1). A balról folytonosság pedig egyszerűen a szigorúan kisebb ($<$) reláció matematikai következménye a definícióból.")

        st.markdown(r"##### 📈 Szimuláció 5.5: CDF Tulajdonságok Vizsgálata")
        st.write(r"Nézzük meg ezeket a tulajdonságokat egy valós, folytonos függvényen (például a híres Haranggörbe, azaz a normális eloszlás eloszlásfüggvényén)! Mozgasd az $x$ értékét a végtelenek felé!")

        x_val_cdf = st.slider("Vizsgált x érték (a végtelenek szimulálásához):", -4.0, 4.0, 0.0, 0.2)

        import math
        # Standard normális eloszlás CDF közelítése (math.erf használatával)
        cdf_ertek = 0.5 * (1 + math.erf(x_val_cdf / math.sqrt(2)))

        st.latex(rf"F_\xi({x_val_cdf:.1f}) = \mathbf{{{cdf_ertek:.4f}}}")
        st.progress(cdf_ertek)

        if x_val_cdf >= 3.8:
            st.success(r"Látod? Ahogy megyünk a $+\infty$ felé, a függvény értéke majdnem eléri a maximumot, az 1-et! Ez az **(F2)** tulajdonság.")
        elif x_val_cdf <= -3.8:
            st.info(r"Ahogy megyünk a $-\infty$ felé, a függvény értéke szinte teljesen 0! Ez az **(F3)** tulajdonság.")
        else:
            st.write(r"Ahogy tolod jobbra a csúszkát, az érték és a kék sáv is csak nőni tud, sosem csökken. Ez az **(F1)** monoton növő tulajdonság!")

    with st.expander(r"5.6 $\xi$ létezése eloszlásfüggvényhez (TÉTEL)"):
        # ==========================================
        # 5.6 TÉTEL: LÉTEZÉS
        # ==========================================
        st.write(r"Az $F : \mathbb{R} \rightarrow \mathbb{R}$ függvényre teljesüljenek az (F1) - (F4) tulajdonságok. Ekkor létezik olyan $(\Omega, \mathcal{F}, P)$ valószínűségi mező és azon értelmezett $\xi$ valószínűségi változó, amelynek eloszlásfüggvénye $F$.")

        st.markdown(r"**Magyarázat az 5.6-hoz:**")
        st.write(r"Ez pontosan olyan 'Fordított Tervezés', mint az 5.4-es tétel volt a diszkrét eloszlásoknál! Ha te a semmiből felrajzolsz egy függvényt, ami monoton nő 0-tól 1-ig és balról folytonos, a matematika garantálja, hogy létezik hozzá egy valószínűségi változó a háttérben.")
    with st.expander(r"5.7 Tétel ({a ≤ ξ < b} valószínűsége)"):
        # ==========================================
        # 5.7 TÉTEL: INTERVALLUM VALÓSZÍNŰSÉGE
        # ==========================================
        st.write(r"Legyen $\xi$ egy $(\Omega, \mathcal{F}, P)$ valószínűségi mezőben értelmezett valószínűségi változó és $a < b$ valós számok. Ekkor:")
        st.latex(r"P(a \le \xi < b) = F_\xi(b) - F_\xi(a)")

        st.markdown(r"**Magyarázat:**")
        st.write(r"Ez a tétel rendkívül praktikus! Azt mondja meg, hogy ha egy valószínűségi változó egy adott $[a, b)$ intervallumba esésének esélyét akarjuk kiszámolni, akkor elegendő a felső határ eloszlásfüggvény-értékéből kivonni az alsó határét. Gondolj rá úgy, mint egy 'távolságra' a valószínűségek között a halmozott görbén.")

        if st.checkbox(r"💡 Részletes Bizonyítás (5.7)", key="biz5_7"):
            st.info(r"A bizonyítás azon alapul, hogy a kisebb halmaz része a nagyobbnak, így használhatjuk az események különbségére vonatkozó szabályt.")
            
            st.write(r"1. Mivel $a < b$, ezért minden olyan kimenetel, amire $\xi < a$, automatikusan teljesíti azt is, hogy $\xi < b$. Vagyis a kisebb halmaz részhalmaza a nagyobbnak:")
            st.latex(r"\{\xi < a\} \subseteq \{\xi < b\}")
            
            st.write(r"2. Az $\{a \le \xi < b\}$ esemény pontosan az a halmaz, amit úgy kapunk, hogy a 'mindent b-ig' halmazból *kivonjuk* a 'mindent a-ig' halmazt:")
            st.latex(r"\{a \le \xi < b\} = \{\xi < b\} \setminus \{\xi < a\}")
            
            st.write(r"3. Mivel részhalmazról van szó, a halmazok különbségének valószínűsége megegyezik a valószínűségek különbségével:")
            st.latex(r"P(\{a \le \xi < b\}) = P(\{\xi < b\}) - P(\{\xi < a\})")
            
            st.write(r"4. Az eloszlásfüggvény definíciója szerint $P(\{\xi < x\}) = F_\xi(x)$, így ezt egyszerűen behelyettesítjük a képletbe:")
            st.latex(r"= F_\xi(b) - F_\xi(a)")
            
            st.success(r"A tétel bizonyítást nyert.")
            
        st.markdown(r"##### 🎯 Szimuláció 5.7: Esély az intervallumban")
        st.write(r"Tegyük fel, hogy a lottón egy gép sorsol egy számot 0 és 100 között (egyenletes eloszlással, $F(x) = x/100$). Számoljuk ki a képlettel, mennyi az esélye, hogy a szám $a$ és $b$ közé esik!")
        
        col_a, col_b = st.columns(2)
        with col_a:
            a_val = st.slider("Alsó határ (a):", 0.0, 100.0, 20.0, 5.0)
        with col_b:
            b_val = st.slider("Felső határ (b):", 0.0, 100.0, 80.0, 5.0)
            
        if a_val < b_val:
            f_a = a_val / 100.0
            f_b = b_val / 100.0
            p_intervallum = f_b - f_a
            
            st.write(r"**Az eloszlásfüggvény értékei:**")
            st.latex(rf"F_\xi({a_val:.0f}) = {f_a:.2f}, \quad F_\xi({b_val:.0f}) = {f_b:.2f}")
            st.success(r"**Az intervallumba esés valószínűsége a tétel alapján:**")
            st.latex(rf"P({a_val:.0f} \le \xi < {b_val:.0f}) = {f_b:.2f} - {f_a:.2f} = \mathbf{{{p_intervallum:.2f}}} \text{{ (azaz {p_intervallum*100:.0f}\%)}}")
        else:
            st.error(r"Hiba: Az alsó határnak (a) szigorúan kisebbnek kell lennie a felső határnál (b)!")
    with st.expander(r"5.8 Tétel és Következményei (Pontbeli valószínűség)"):
        # ==========================================
        # 5.8 TÉTEL ÉS KÖVETKEZMÉNYEI
        # ==========================================
        st.write(r"**5.8 Tétel ($\xi$ valószínűsége pontban és eloszlásfüggvény)**")
        st.write(r"Legyen $\xi$ egy $(\Omega, \mathcal{F}, P)$ valószínűségi mezőben értelmezett valószínűségi változó és $a \in \mathbb{R}$. Ekkor létezik $F_\xi$-nek jobboldali határértéke $a$-ban és:")
        st.latex(r"P(\xi = a) = F_\xi(a+0) - F_\xi(a)")
        
        st.markdown(r"---")
        st.write(r"**Következmény I**")
        st.write(r"Legyen $\xi$ valószínűségi változó és $a \in \mathbb{R}$ tetszőleges. $F_\xi$ akkor és csak akkor folytonos $a$-ban, ha:")
        st.latex(r"P(\xi = a) = 0")
        
        st.markdown(r"---")
        st.write(r"**Következmény II**")
        st.write(r"Legyen $\xi$ valószínűségi változó, $a < b$ valós számok és $F_\xi$ **mindenütt folytonos**. Ekkor:")
        st.latex(r"F_\xi(b) - F_\xi(a) = P(a \le \xi < b) = P(a < \xi < b) = P(a < \xi \le b) = P(a \le \xi \le b)")

        st.markdown(r"**Magyarázat (Az 'Ugrás' és a Folytonosság):**")
        st.write(r"Ez a három állítás egyetlen gyönyörű logikai ívet alkot. Az 5.8-as tétel megmutatja, hogy egy pontos érték (pl. pontosan 3-ast dobunk) valószínűsége megegyezik az eloszlásfüggvény grafikonján lévő 'ugrás' méretével ($F(a+0)$ a jobboldali limesz, ahova ugrik, $F(a)$ pedig ahonnan indul).")
        st.write(r"A Következmény I. kimondja a nyilvánvalót: ha a függvény folytonos (nincs lépcsőfok, nem ugrik egyet sem), akkor az ugrás mérete nulla, tehát egyetlen, hajszálpontos érték valószínűsége kereken 0.")
        st.write(r"A Következmény II. pedig learatja a babérokat: mivel a folytonos (pl. normális) eloszlásoknál egy pont valószínűsége nulla, teljesen mindegy, hogy az intervallum határainál megengedjük-e az egyenlőséget ($\le$) vagy sem ($<$). A valószínűség (a görbe alatti terület) nem változik, mert a hajszálvékony 'határvonal' önmagában 0 esélyű!")

        st.markdown(r"##### 📏 Szimuláció 5.8: A 'Szigorú' és a 'Megengedő' intervallum")
        st.write(r"Válassz, hogy Diszkrét (lépcsős, pl. kockadobás) vagy Folytonos (pl. testmagasság) változót vizsgálsz. Nézd meg, számítanak-e a relációs jelek!")
        
        valtozo_tipus = st.radio("Milyen változót vizsgálunk?", ["Diszkrét (Van 'ugrás')", "Folytonos (Nincs 'ugrás')"])
        
        if "Diszkrét" in valtozo_tipus:
            st.warning(r"**Diszkrét esetben az egyenlőségjel (≤) ÉLETBEVÁGÓ!**")
            st.write(r"Példa: Dobókockával dobunk. $a=2$, $b=4$.")
            st.latex(r"P(2 \le \xi < 4) \implies \text{Kimenetelek: } \{2, 3\} \implies P = \frac{2}{6}")
            st.latex(r"P(2 < \xi < 4) \implies \text{Kimenetelek: } \{3\} \implies P = \frac{1}{6}")
            st.write(r"Látod? Mivel $P(\xi=2) \neq 0$ (ugrás van a kettesnél), nagyon is számít, hogy a 2-est belefoglaljuk-e az intervallumba!")
        else:
            st.success(r"**Folytonos esetben az egyenlőségjel (≤) LÉNYEGTELEN (Következmény II)!**")
            st.write(r"Példa: Egy ember magassága. $a=170$ cm, $b=180$ cm.")
            st.latex(r"P(170 \le \xi < 180) = P(170 < \xi < 180)")
            st.write(r"Mivel annak az esélye, hogy valaki hajszálpontosan, atomi szinten $170.00000...$ cm magas, matematikai értelemben $0$, az egyenlőségjel elhagyása egyáltalán nem változtatja meg a valószínűséget. $P(\xi = 170) = 0$.")
    with st.expander(r"5.9 Tétel ({a ≤ ξ < b} és a sűrűségfüggvény)"):
        # ==========================================
        # 5.9 TÉTEL: INTEGRÁLÁS ÉS SŰRŰSÉGFÜGGVÉNY
        # ==========================================
        st.write(r"**5.9 Tétel ($\{a \le \xi < b\}$ valószínűsége és a sűrűségfüggvény)**")
        st.write(r"Legyen $\xi$ az $(\Omega, \mathcal{F}, P)$ valószínűségi mezőn értelmezett **abszolút folytonos** eloszlású valószínűségi változó. Ekkor minden $a < b$ valós szám esetén:")
        st.latex(r"P(a \le \xi < b) = \int_{a}^{b} f_\xi(x) dx")

        st.markdown(r"**Fontos észrevételek a diáról:**")
        st.write(r"- Mivel a változó abszolút folytonos, egyetlen pont valószínűsége mindig nulla: $\forall x \in \mathbb{R} : P(\xi = x) = 0$.")
        st.write(r"- Ebből következik, hogy a képlet akkor is tökéletesen működik, ha az intervallum szigorú ($<$), azaz $P(a < \xi < b)$ esetén is pontosan ugyanez az integrál a megoldás!")

        if st.checkbox(r"💡 Részletes Bizonyítás (5.9)", key="biz5_9"):
            st.info(r"A bizonyítás pofonegyszerű: csak összekapcsoljuk a korábbi 5.7-es tételt a sűrűségfüggvény definíciójával.")
            
            st.write(r"1. Az 5.7-es tétel alapján tudjuk az intervallum valószínűségét az eloszlásfüggvénnyel felírni:")
            st.latex(r"P(a \le \xi < b) = F_\xi(b) - F_\xi(a)")
            
            st.write(r"2. A sűrűségfüggvény definíciója szerint $F_\xi(x) = \int_{-\infty}^{x} f_\xi(t) dt$. Helyettesítsük be ezt a $b$-re és az $a$-ra is:")
            st.latex(r"= \int_{-\infty}^{b} f_\xi(x) dx - \int_{-\infty}^{a} f_\xi(x) dx")
            
            st.write(r"3. Az integrálszámítás szabályai szerint, ha a mínusz végtelentől $b$-ig tartó területből kivonjuk a mínusz végtelentől $a$-ig tartó területet, pont az $a$ és $b$ közötti terület marad meg:")
            st.latex(r"= \int_{a}^{b} f_\xi(x) dx")
            st.success(r"A tétel bizonyítást nyert.")

        st.markdown(r"##### 📐 Szimuláció 5.9: A Görbe Alatti Terület")
        st.write(r"A folytonos változóknál a valószínűség nem más, mint az integrál (terület)! Nézzük ezt meg egy egyszerű Egyenletes eloszláson a $[0, 10]$ intervallumon, ahol a 'görbe' magassága állandó: $f(x) = 0.1$.")
        
        col_int_a, col_int_b = st.columns(2)
        with col_int_a:
            int_a = st.slider("Alsó határ (a):", 0.0, 10.0, 2.0, 1.0, key="int_a")
        with col_int_b:
            int_b = st.slider("Felső határ (b):", 0.0, 10.0, 7.0, 1.0, key="int_b")
            
        if int_a < int_b:
            terulet = (int_b - int_a) * 0.1
            st.success(r"**Az integrál kiszámítása egyszerű téglalapként (Szélesség $\times$ Magasság):**")
            st.latex(rf"\int_{{{int_a:.0f}}}^{{{int_b:.0f}}} 0.1 \, dx = ({int_b:.0f} - {int_a:.0f}) \cdot 0.1 = \mathbf{{{terulet:.2f}}}")
            st.write(r"Esély vizuálisan:")
            st.progress(terulet)
        else:
            st.error(r"Az alsó határ (a) legyen szigorúan kisebb, mint a felső (b)!")
    with st.expander(r"5.10 Tétel (Abszolút folytonos ξ eloszlásfüggvénye)"):
        # ==========================================
        # 5.10 TÉTEL: CDF ÉS PDF KAPCSOLATA (DERIVÁLÁS)
        # ==========================================
        st.write(r"**5.10 Tétel (Abszolút folytonos $\xi$ eloszlásfüggvénye)**")
        st.write(r"Ha az $(\Omega, \mathcal{F}, P)$ valószínűségi mezőn értelmezett $\xi$ valószínűségi változó **abszolút folytonos**, akkor az eloszlásfüggvénye folytonos és majdnem mindenütt differenciálható (pontosan ott, ahol a sűrűségfüggvény folytonos).")
        st.write(r"Továbbá a differenciálható pontokban az eloszlásfüggvény deriváltja maga a sűrűségfüggvény:")
        st.latex(r"F'_\xi(x) = f_\xi(x)")

        st.markdown(r"---")
        
        st.write(r"**Következmények (A diszkrét és folytonos világ elválása):**")
        st.write(r"1. Ha $\xi$ diszkrét valószínűségi változó $\implies F_\xi$ nem folytonos (ugrásai vannak) $\implies \xi$ nem abszolút folytonos, azaz **nem létezik sűrűségfüggvénye**.")
        st.write(r"2. Ha $\xi$ abszolút folytonos eloszlású $\implies F_\xi$ folytonos $\implies \text{rng}(F_\xi)$ nem megszámlálható $\implies \xi$ **nem diszkrét**.")

        st.markdown(r"**Magyarázat:**")
        st.write(r"Ez a tétel a valószínűségszámítás 'Newton-Leibniz' formulája! Ha van egy halmozott valószínűséget mutató görbéd (eloszlásfüggvény), és megnézed a meredekségét (deriválod), akkor megkapod a sűrűségfüggvényt. A következmény pedig egyszerű logikai lánc: a diszkrét változóknál a grafikon lépcsős. A lépcsőket (ugrásokat) nem lehet deriválni, ezért a diszkrét változóknak soha nem lehet sűrűségfüggvényük!")

        st.markdown(r"##### 📈 Szimuláció 5.10: Deriváljunk valószínűséget!")
        st.write(r"Tegyük fel, hogy egy $\xi$ változó eloszlásfüggvénye a $[0, 10]$ intervallumon egy parabola: $F(x) = \frac{x^2}{100}$. Ellenőrizzük a tételt! A tétel szerint a sűrűségfüggvény a derivált: $f(x) = (\frac{x^2}{100})' = \frac{2x}{100} = \frac{x}{50}$.")
        
        x_deriv = st.slider("Válassz egy x pontot az intervallumból:", 0.0, 10.0, 5.0, 0.5)
        
        # Matematikai számolás
        F_x = (x_deriv ** 2) / 100.0
        f_x = x_deriv / 50.0
        
        col_F, col_f = st.columns(2)
        with col_F:
            st.info(r"**Eloszlásfüggvény (CDF)**")
            st.latex(rf"F({x_deriv:.1f}) = \frac{{{x_deriv:.1f}^2}}{{100}} = \mathbf{{{F_x:.3f}}}")
            st.write(r"*(Eddig felhalmozott valószínűség)*")
        with col_f:
            st.success(r"**Sűrűségfüggvény (PDF)**")
            st.latex(rf"f({x_deriv:.1f}) = F'({x_deriv:.1f}) = \frac{{{x_deriv:.1f}}}{{50}} = \mathbf{{{f_x:.3f}}}")
            st.write(r"*(A görbe meredeksége ebben a pontban)*")
            
        st.progress(F_x)
    with st.expander(r"5.11 Tétel (Sűrűségfüggvény integrálja)"):
        # ==========================================
        # 5.11 TÉTEL: SŰRŰSÉGFÜGGVÉNY INTEGRÁLJA = 1
        # ==========================================
        st.write(r"**5.11 Tétel (Sűrűségfüggvény integrálja $(-\infty, \infty)$-n)**")
        st.write(r"Legyen $\xi$ az $(\Omega, \mathcal{F}, P)$ valószínűségi mezőn értelmezett **abszolút folytonos** eloszlású valószínűségi változó. Ekkor a sűrűségfüggvény teljes görbéje alatti terület pontosan 1:")
        st.latex(r"\int_{-\infty}^{\infty} f_\xi(x) dx = 1")

        st.markdown(r"**Magyarázat:**")
        st.write(r"Ez pontosan az 5.3-as tétel (Diszkrét eloszlás összege) folytonos 'testvére'. Ahogy a diszkrét esélyek összege 100% kell hogy legyen, úgy a folytonos sűrűségfüggvény alatti teljes terület is szigorúan 1-et kell, hogy kiadjon. Hiszen a változó valamilyen értéket mindenképpen fel fog venni a mínusz végtelen és plusz végtelen között!")

        if st.checkbox(r"💡 Részletes Bizonyítás (5.11)", key="biz5_11"):
            st.info(r"A bizonyítás az improprius (végtelenig tartó) integrál és az eloszlásfüggvény tulajdonságainak elegáns kombinációja.")
            
            st.write(r"1. Írjuk fel a végtelenig tartó integrált egy határérték (limesz) segítségével:")
            st.latex(r"\int_{-\infty}^{\infty} f_\xi(x) dx = \lim_{t \to \infty} \int_{-\infty}^{t} f_\xi(x) dx")
            
            st.write(r"2. A sűrűségfüggvény definíciója szerint az integrál a mínusz végtelentől $t$-ig nem más, mint az eloszlásfüggvény értéke $t$-ben ($F_\xi(t)$):")
            st.latex(r"= \lim_{t \to \infty} F_\xi(t)")
            
            st.write(r"3. Az 5.5-ös tétel (F2) tulajdonsága alapján tudjuk, hogy az eloszlásfüggvény a plusz végtelenben mindig 1-hez tart:")
            st.latex(r"= 1")
            st.success(r"A tétel bizonyítást nyert.")

        st.markdown(r"##### 🍕 Szimuláció 5.11: A 'Valószínűség-tészta'")
        st.write(r"Képzeld el a valószínűséget úgy, mint 1 kg tésztát. Ha egy széles intervallumon kenjük szét (nagy szórás), akkor a tészta nagyon vékony lesz (kis $f(x)$ magasság). Ha egy szűk intervallumra gyúrjuk össze, akkor nagyon vastag lesz. De a tészta mennyisége (a terület) mindig pontosan 1 marad!")
        
        szelesseg = st.slider("Mennyire nyújtsuk szét a tésztát? (Egyenletes eloszlás szélessége):", 1.0, 20.0, 10.0, 1.0)
        magassag = 1.0 / szelesseg
        
        st.info(r"**A sűrűségfüggvény magassága:**")
        st.latex(rf"f(x) = \frac{{1}}{{{szelesseg:.0f}}} = \mathbf{{{magassag:.3f}}}")
        
        st.success(r"**Teljes terület (Integrál):** Szélesség $\times$ Magasság")
        st.latex(rf"\int f(x) dx = {szelesseg:.0f} \cdot {magassag:.3f} = \mathbf{{1.000}}")
    with st.expander(r"5.12 Valószínűségi változó sűrűségfüggvényhez (TÉTEL)"):
        # ==========================================
        # 5.12 TÉTEL: SŰRŰSÉGFÜGGVÉNY EGZISZTENCIA
        # ==========================================
        st.write(r"**5.12 Tétel (Valószínűségi változó sűrűségfüggvényhez)**")
        st.write(r"Legyen $f : \mathbb{R} \rightarrow \mathbb{R}$ nemnegatív függvény, amelyre:")
        st.latex(r"\int_{-\infty}^{\infty} f(x) dx = 1")
        st.write(r"Ekkor létezik olyan $(\Omega, \mathcal{F}, P)$ valószínűségi mező és rajta értelmezett $\xi$ abszolút folytonos eloszlású valószínűségi változó, amelynek sűrűségfüggvénye $f$.")

        st.markdown(r"**Magyarázat (A folytonos 'Fordított Tervezés'):**")
        st.write(r"Ez teszi lehetővé a statisztikusok számára, hogy mindenféle 'őrült' alakú eloszlásokat (sűrűségfüggvényeket) találjanak ki a való élet modellezésére! Ha garantálod, hogy a függvényed értéke sosem negatív, és kiszámolod, hogy az integrálja (a teljes terület) hajszálpontosan 1, akkor a tétel kimondja: jogod van ezt valószínűségként használni, a háttérben a matematika felépíti a megfelelő univerzumot ($\Omega$).")

        st.markdown(r"##### 📐 Szimuláció 5.12: Építsünk érvényes Sűrűségfüggvényt!")
        st.write(r"Hozzunk létre egy egyszerű 'háromszög' alakú sűrűségfüggvényt a $[0, b]$ intervallumon! A háromszög magassága legyen $h$. Állítsd be az alapot és a magasságot úgy, hogy a tétel értelmében érvényes sűrűségfüggvényt kapjunk!")

        col_alap, col_mag = st.columns(2)
        with col_alap:
            b_alap = st.slider("Háromszög alapja (b, azaz a szélesség):", 1.0, 10.0, 4.0, 0.5)
        with col_mag:
            h_mag = st.slider("Háromszög magassága (h):", 0.1, 2.0, 0.5, 0.1)

        terulet = (b_alap * h_mag) / 2.0

        st.write(r"**A háromszög alatti terület (integrál):**")
        st.latex(rf"\text{{Terület}} = \frac{{\text{{alap}} \cdot \text{{magasság}}}}{{2}} = \frac{{{b_alap:.1f} \cdot {h_mag:.1f}}}{{2}} = \mathbf{{{terulet:.2f}}}")

        if abs(terulet - 1.0) < 0.001:
            st.success(r"✅ **Sikeres építés!** A terület pontosan 1. Az 5.12-es tétel garantálja, hogy létezik ilyen valószínűségi változó!")
        else:
            st.error(rf"❌ **Sikertelen építés!** A terület jelenleg {terulet:.2f}. Próbáld úgy beállítani az alapot és a magasságot, hogy a szorzatuk pontosan 2 legyen (így osztva kettővel 1-et ad)!")
    with st.expander(r"5.13 Tétel (Az együttes sűrűségfüggvény integrálja)"):
        # ==========================================
        # 5.13 TÉTEL: EGYÜTTES SŰRŰSÉGFÜGGVÉNY INTEGRÁLJA
        # ==========================================
        st.write(r"**5.13 Tétel (Az együttes sűrűségfüggvény integrálja $(-\infty, \infty)$-n)**")
        st.write(r"Minden $f_{\xi,\eta} : \mathbb{R}^2 \rightarrow \mathbb{R}$ együttes sűrűségfüggvényre igaz, hogy a teljes kétdimenziós téren vett integrálja 1:")
        st.latex(r"\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{\xi,\eta}(x, y) dx dy = 1")
        
        st.markdown(r"**Magyarázat:**")
        st.write(r"Ez az 5.11-es tétel ('A valószínűség-tészta' szabály) 2D-s kiterjesztése. Képzeld el a valószínűséget most ne egyetlen vonalon elkenve, hanem egy asztalon eloszló domborműként (például egy hegyként). A tétel azt mondja ki, hogy a hegy teljes térfogata (a 2D-s görbe alatti térrész) pontosan 1 (azaz 100%) kell, hogy legyen. Bárhogyan is oszlik el az esély a $\xi$ és $\eta$ tengelyek mentén, a biztos esemény valószínűsége marad 1.")
    with st.expander(r"5.14 Tétel (Sűrűségfüggvény és függetlenség)"):
        # ==========================================
        # 5.14 TÉTEL: FÜGGETLENSÉG PDF-FEL
        # ==========================================
        st.write(r"**5.14 Tétel (Sűrűségfüggvény és függetlenség)**")
        st.write(r"Legyen az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ és $\eta$ valószínűségi változók együttes eloszlása abszolút folytonos.")
        st.write(r"Ekkor $\xi$ és $\eta$ pontosan akkor **függetlenek**, ha a közös együttes sűrűségfüggvényük megegyezik a perem-sűrűségfüggvényeik szorzatával (egy nullmértékű halmaz kivételével $\forall x, y \in \mathbb{R}$-ra):")
        
        st.latex(r"f_{\xi,\eta}(x, y) = f_\xi(x) \cdot f_\eta(y)")

        st.markdown(r"**Magyarázat:**")
        st.write(r"Ez a klasszikus 'szorzásszabály' kiterjesztése folytonos függvényekre. Ha két mérés (pl. egy ember magassága és az IQ-szintje) teljesen független egymástól, akkor a 2D-s 'hegy' (az együttes sűrűség) bármelyik pontjának magasságát megkapod, ha egyszerűen összeszorzod a két 1D-s görbe magasságát az adott koordinátákon. A 'nullmértékű halmaz kivételével' pedig csak matematikai óvatoskodás: egy-két végtelenül vékony pontban lehet hiba, az nem rontja el az integrált.")

        st.markdown(r"##### ✖️ Szimuláció 5.14: A Szorzásszabály")
        st.write(r"Vizsgáljunk két független eseményt! $\xi$ legyen a hőmérséklet, $\eta$ pedig egy dobókocka eredménye. Állítsd be a perem-sűrűségeket egy adott pontban, és a rendszer kiszámolja a 2D-s együttes sűrűséget a tétel alapján!")
        
        col_fx, col_fy = st.columns(2)
        with col_fx:
            f_x_val = st.slider("Hőmérséklet sűrűsége adott pontban, f(x):", 0.0, 1.0, 0.4, 0.1)
        with col_fy:
            f_y_val = st.slider("Kockadobás sűrűsége adott pontban, f(y):", 0.0, 1.0, 0.5, 0.1)
            
        st.success(r"**Az együttes sűrűségfüggvény magassága az adott (x,y) koordinátán:**")
        st.latex(rf"f_{{\xi,\eta}}(x, y) = {f_x_val:.1f} \cdot {f_y_val:.1f} = \mathbf{{{f_x_val * f_y_val:.2f}}}")
    with st.expander(r"5.15 Tétel (aξ + bη + c várható értéke)"):
        # ==========================================
        # 5.15 TÉTEL: A VÁRHATÓ ÉRTÉK LINEARITÁSA
        # ==========================================
        st.write(r"**5.15 Tétel ($a\xi + b\eta + c$ várható értéke)**")
        st.write(r"Legyen $\xi$ és $\eta$ valószínűségi változó és $a, b, c \in \mathbb{R}$. Ekkor:")
        st.latex(r"E(a\xi + b\eta + c) = aE(\xi) + bE(\eta) + c")

        st.markdown(r"**Magyarázat:**")
        st.write(r"Ezt hívják a **várható érték linearitásának**. Nagyon hasznos tulajdonság! Azt jelenti, hogy ha egy játékban megduplázzák a tétet ($2\xi$), akkor a várható nyereményed is a duplája lesz ($2E(\xi)$). Ha pedig mindenki kap fix 1000 Ft belépési bónuszt ($+ c$), akkor a várható érték is pontosan ennyivel nő. Még akkor is igaz, ha $\xi$ és $\eta$ nem függetlenek egymástól!")

        st.markdown(r"##### 🧮 Szimuláció 5.15: Fizetésemelés!")
        st.write(r"Képzeld el, hogy a programozói alapfizetésed egy cégben változó (függ a projektektől), várható értéke $E(\xi) = 600$ ezer Ft. Év végén a főnököd bejelenti: mindenki fizetését megemeli $10\%$-kal (azaz $1.1$-szeresére), és ad egy fix $50$ ezer Ft-os bónuszt. Mennyi lesz az új várható fizetésed?")
        
        col_a, col_c = st.columns(2)
        with col_a:
            szorzo = st.slider("Szorzó (a):", 1.0, 2.0, 1.1, 0.1)
        with col_c:
            bonusz = st.slider("Fix bónusz (c) ezer Ft-ban:", 0, 200, 50, 10)
            
        e_xi = 600
        uj_fizetes = (szorzo * e_xi) + bonusz
        
        st.success(r"**A tétel alapján az új várható érték:**")
        st.latex(rf"E({szorzo:.1f} \cdot \xi + {bonusz}) = {szorzo:.1f} \cdot E(\xi) + {bonusz} = {szorzo:.1f} \cdot {e_xi} + {bonusz} = \mathbf{{{uj_fizetes:.0f}}}")
    with st.expander(r"5.16 Tétel (A várható érték tulajdonságai)"):
        # ==========================================
        # 5.16 TÉTEL: A VÁRHATÓ ÉRTÉK TULAJDONSÁGAI
        # ==========================================
        st.write(r"**5.16 Tétel (A várható érték tulajdonságai)**")
        st.write(r"Tegyük fel, hogy az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ és $\eta$ valószínűségi változóknak létezik várható értéke.")
        
        st.markdown(r"**(1) Nemnegativitás megőrzése:**")
        st.latex(r"\text{Ha } \xi \ge 0, \text{ akkor } E(\xi) \ge 0.")
        st.caption(r"Magyarázat: Ha egy változó (pl. valakinek a magassága) sosem lehet negatív, akkor az átlaga (várható értéke) sem lehet az.")

        st.markdown(r"**(2) A biztos nulla:**")
        st.latex(r"\text{Ha minden } \omega \in \Omega \text{ esetén } \xi(\omega) \ge 0 \text{ és } E(\xi) = 0, \text{ akkor } P(\xi = 0) = 1.")
        st.caption(r"Magyarázat: Ha egy kísérlet eredménye sosem negatív, de az átlaga mégis kereken 0, az csak úgy lehetséges, ha 100% eséllyel mindig pontosan 0-t 'dobunk'.")

        st.markdown(r"**(3) Konstans várható értéke:**")
        st.latex(r"\text{Ha valamely } c \in \mathbb{R} \text{ esetén } P(\xi = c) = 1, \text{ akkor } E(\xi) = c.")
        st.caption(r"Magyarázat: Ha egy 'változó' valójában nem is változik (mindig c-t vesz fel), akkor az átlaga is c marad.")

        st.markdown(r"**(4) Monotonitás:**")
        st.latex(r"\text{Ha } \xi \ge \eta, \text{ akkor } E(\xi) \ge E(\eta).")
        st.caption(r"Magyarázat: Ha András ($\xi$) minden lehetséges helyzetben több pontot szerez, mint Béla ($\eta$), akkor András pontjainak átlaga is nagyobb lesz.")

        st.markdown(r"**(5) Függetlenek szorzata:**")
        st.write(r"Ha $\xi$ és $\eta$ egyaránt diszkrétek vagy abszolút folytonosak, és **függetlenek** egymástól, akkor $\xi\eta$-nak is létezik várható értéke, és:")
        st.latex(r"E(\xi\eta) = E(\xi) \cdot E(\eta)")
        st.caption(r"Magyarázat: A független változók szorzatának várható értéke megegyezik a várható értékeik szorzatával.")

        st.markdown(r"---")
        st.markdown(r"##### 🎲 Szimuláció 5.16: Független változók szorzata")
        st.write(r"Vizsgáljuk meg az **(5)-ös tulajdonságot** két független dobókockával! Legyen $\xi$ az egyik, $\eta$ a másik kocka dobásának eredménye. Mindkét kocka várható értéke külön-külön tudjuk, hogy $3.5$.")
        st.write(r"Mivel a két dobás teljesen független egymástól, a tétel szerint a szorzatuk elméleti várható értéke:")
        st.latex(r"E(\xi \cdot \eta) = E(\xi) \cdot E(\eta) = 3.5 \cdot 3.5 = \mathbf{12.25}")
        
        st.write(r"Végezzünk el sok ezer szimulált dupla kockadobást a háttérben, és nézzük meg, tényleg ehhez az elméleti számhoz közelít-e a szorzatok tapasztalati átlaga!")
        
        dobasok_szama = st.slider("Szimulált dobások (szorzatok) száma:", 100, 10000, 1000, 100)
        
        import random
        osszeg = 0
        for _ in range(dobasok_szama):
            # Első kocka * Második kocka
            osszeg += random.randint(1, 6) * random.randint(1, 6)
            
        tapasztalati_atlag = osszeg / dobasok_szama
        
        st.info(rf"**Tapasztalati átlag {dobasok_szama} dobás alapján:** **{tapasztalati_atlag:.3f}**")
        
        if abs(tapasztalati_atlag - 12.25) < 0.5:
            st.success(r"Látod? A tapasztalati átlag nagyon közel van a tétel által jósolt $12.25$-ös elméleti várható értékhez!")
    with st.expander(r"5.17 Tétel (A szórásnégyzet kiszámolása)"):
        # ==========================================
        # 5.17 TÉTEL: A SZÓRÁSNÉGYZET KISZÁMOLÁSA
        # ==========================================
        st.write(r"**5.17 Tétel (A szórásnégyzet kiszámolása)**")
        st.write(r"Tegyük fel, hogy az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ valószínűségi változónak létezik várható értéke.")
        st.write(r"$\xi$-nek pontosan akkor létezik szórása, ha $\xi^2$-nek létezik várható értéke, és ekkor:")
        st.latex(r"D^2(\xi) = E(\xi^2) - E^2(\xi)")

        st.markdown(r"**Megjegyzés (Hogyan számoljuk az $E(\xi^2)$-et?):**")
        st.write(r"A várható érték definíciójában szereplő esetekben rendre a következő értékek jelentik $\xi^2$ várható értékét (amennyiben ezek az értékek végesek):")
        
        st.latex(r"(0) \text{ Véges diszkrét:} \quad E(\xi^2) = \sum_{k=1}^{n} x_k^2 \cdot P(\xi = x_k)")
        st.latex(r"(1) \text{ Végtelen diszkrét:} \quad E(\xi^2) = \sum_{i} p_i x_i^2")
        st.latex(r"(2) \text{ Folytonos:} \quad E(\xi^2) = \int_{-\infty}^{\infty} x^2 f_\xi(x) dx")

        st.info(r"💡 **Konyhanyelven (Vizsgatipp!):** Ezt hívják a szórásnégyzet 'számolási képletének'. A definíció szerinti számolás nagyon lassú lenne. Ehelyett ezzel a tétellel sokkal gyorsabb a dolgunk: csak kiszámolod a sima várható értéket (majd négyzetre emeled), meg kiszámolod a négyzetek várható értékét, és a végén kivonod a kettőt egymásból!")

        st.markdown(r"##### 🎲 Szimuláció 5.17: Kockadobás Szórásnégyzete")
        st.write(r"Számoljuk ki egy szabályos $N$-oldalú dobókocka szórásnégyzetét a fenti gyors számolási képlettel!")
        
        n_oldal = st.slider("Kocka oldalainak száma (N):", 4, 20, 6, 1)
        
        # Matematikai számolás
        e_xi = (n_oldal + 1) / 2.0
        e_xi_negyzet = e_xi ** 2
        
        # E(ξ^2) = (1^2 + 2^2 + ... + N^2) / N
        # A négyzetösszeg képlete: N(N+1)(2N+1)/6. Ezt osztva N-nel: (N+1)(2N+1)/6
        e_xi2 = ((n_oldal + 1) * (2 * n_oldal + 1)) / 6.0
        
        var_xi = e_xi2 - e_xi_negyzet
        
        col_e1, col_e2 = st.columns(2)
        with col_e1:
            st.write(r"**1. Lépés:** $\xi$ várható értékének négyzete:")
            st.latex(rf"E(\xi) = {e_xi:.2f} \implies E^2(\xi) = \mathbf{{{e_xi_negyzet:.2f}}}")
        with col_e2:
            st.write(r"**2. Lépés:** $\xi^2$ várható értéke:")
            st.latex(rf"E(\xi^2) = \frac{{1^2 + 2^2 + \dots + {n_oldal}^2}}{{{n_oldal}}} = \mathbf{{{e_xi2:.2f}}}")
            
        st.success(r"**3. Lépés: A szórásnégyzet a Tétel alapján (Különbség):**")
        st.latex(rf"D^2(\xi) = E(\xi^2) - E^2(\xi) = {e_xi2:.2f} - {e_xi_negyzet:.2f} = \mathbf{{{var_xi:.2f}}}")
    with st.expander(r"5.18 Tétel (A szórás tulajdonságai)"):
        # ==========================================
        # 5.18 TÉTEL: A SZÓRÁS TULAJDONSÁGAI
        # ==========================================
        st.write(r"**5.18 Tétel (A szórás tulajdonságai)**")
        st.write(r"Tegyük fel, hogy az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ valószínűségi változónak létezik szórása. Ekkor minden $a, b, c \in \mathbb{R}$ konstansra:")

        st.markdown(r"**(1) Minimális négyzetes eltérés:**")
        st.latex(r"D^2(\xi) \le E\left((\xi - c)^2\right), \quad \text{egyenlő } \Longleftrightarrow \text{ ha } c = E(\xi).")
        st.caption(r"Magyarázat: Bármilyen 'c' számot is vonunk le a változóból, az eltérések négyzetének átlaga akkor lesz a legkisebb, ha a várható értéket (az igazi átlagot) vonjuk le. A szórásnégyzet tehát a lehető legkisebb átlagos négyzetes hiba.")

        st.markdown(r"**(2) Nemnegativitás és a biztos konstans:**")
        st.latex(r"D(\xi) \ge 0, \quad \text{egyenlő } \Longleftrightarrow \text{ ha } P(\xi = E(\xi)) = 1.")
        st.caption(r"Magyarázat: A szórás sosem negatív. Pontosan akkor nulla, ha a változó egyáltalán nem 'szóródik', vagyis 100% eséllyel fixen mindig ugyanazt az egyetlen értéket veszi fel.")

        st.markdown(r"**(3) Lineáris transzformáció szórása:**")
        st.write(r"$a\xi + b$ és $c$ valószínűségi változóknak is létezik szórása, és:")
        st.latex(r"D^2(a\xi + b) = a^2 D^2(\xi), \quad \text{vagyis} \quad D(a\xi + b) = |a| D(\xi)")
        st.latex(r"D^2(c) = 0, \quad \text{vagyis} \quad D(c) = 0")
        st.caption(r"Magyarázat (Vizsgaszabály!): Ha egy eloszlás minden eleméhez hozzáadunk 'b'-t, a szórás NEM változik (a grafikon csak eltolódik). Ha viszont megszorozzuk 'a'-val, a szórás is |a|-szorosára nő. Egy fix 'c' szám szórása pedig nulla.")

        st.markdown(r"---")
        st.markdown(r"##### 📏 Szimuláció 5.18: Fizetésemelés és Szórás")
        st.write(r"Nézzük meg a (3)-as szabályt a gyakorlatban! Adott egy cég, ahol a fizetések szórása (a bérszakadék mértéke) $D(\xi) = 150$ ezer Ft. Emeljük meg a fizetéseket szorzóval és egy fix bónusszal!")

        col_a, col_b = st.columns(2)
        with col_a:
            szorzo_a = st.slider("Fizetés-szorzó (a):", -2.0, 3.0, 2.0, 0.5)
        with col_b:
            bonusz_b = st.slider("Fix bónusz (b):", 0, 500, 100, 50)

        eredeti_d = 150
        uj_d = abs(szorzo_a) * eredeti_d

        st.success(r"**Az új szórás a Tétel alapján:**")
        st.latex(rf"D({szorzo_a:.1f}\xi + {bonusz_b}) = |{szorzo_a:.1f}| \cdot D(\xi) = {abs(szorzo_a):.1f} \cdot {eredeti_d} = \mathbf{{{uj_d:.0f}}}")
        
        if bonusz_b > 0:
            st.info(r"Vedd észre: a fix bónusz (b) egyáltalán nem jelenik meg a szórás végeredményében! Mindenki ugyanannyival kapott többet, így az egymáshoz viszonyított távolságuk nem nőtt.")
        if szorzo_a < 0:
            st.warning(r"Mínuszos szorzó esetén is a szórás (a távolság) pozitív marad a képletben lévő abszolútérték miatt!")
    with st.expander(r"5.19 Tétel (A kovariancia kiszámolása)"):
        # ==========================================
        # 5.19 TÉTEL: A KOVARIANCIA KISZÁMOLÁSA
        # ==========================================
        st.write(r"**5.19 Tétel (A kovariancia kiszámolása)**")
        st.write(r"Ha az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ és $\eta$ valószínűségi változók egyszerre diszkrétek vagy abszolút folytonosak, továbbá $\xi$-nek, $\eta$-nak és $\xi\eta$-nak létezik várható értéke, akkor létezik $\xi$ és $\eta$ kovarianciája, és:")
        
        st.latex(r"\text{cov}(\xi, \eta) = E(\xi\eta) - E(\xi)E(\eta)")
        
        st.info(r"💡 **Piros dobozos észrevétel a diáról:** A kovariancia tulajdonképpen a **függetlenség 'mérőszáma'**. Emlékszel az 5.16-os tételre? Ha két változó független, akkor $E(\xi\eta) = E(\xi)E(\eta)$. Ha ezt behelyettesítjük ide, akkor $E(\xi\eta) - E(\xi\eta) = 0$. Tehát **független változók kovarianciája MINDIG 0**!")
        
        if st.checkbox(r"💡 Részletes Bizonyítás (5.19)", key="biz5_19"):
            st.write(r"A bizonyítás egyszerű algebrai bontás a várható érték linearitása (5.15 Tétel) alapján:")
            st.latex(r"\text{cov}(\xi, \eta) = E\left((\xi - E(\xi))(\eta - E(\eta))\right)")
            st.write("Beszorozva a zárójeleket:")
            st.latex(r"= E\left(\xi\eta - \eta E(\xi) - \xi E(\eta) + E(\xi)E(\eta)\right)")
            st.write("A várható érték linearitását alkalmazva (a konstans várható értékeket kiemelve):")
            st.latex(r"= E(\xi\eta) - E(\eta)E(\xi) - E(\xi)E(\eta) + E(\xi)E(\eta)")
            st.write("Összevonás után megkapjuk a tételt:")
            st.latex(r"= E(\xi\eta) - E(\xi)E(\eta)")
            st.success(r"A tétel bizonyítást nyert.")

        st.markdown(r"---")
        st.markdown(r"##### 🧮 Szimuláció 5.19: A számolási kiskapu")
        st.write(r"Pont úgy, ahogy a szórásnégyzetnél, a kovarianciát is sokkal könnyebb ezzel a tétellel (várható értékekkel) számolni, mint az eredeti definícióval. Próbáld ki!")
        
        col_ex, col_ey, col_exy = st.columns(3)
        with col_ex:
            ex = st.number_input(r"$E(\xi)$ értéke:", value=3.5, step=0.5)
        with col_ey:
            ey = st.number_input(r"$E(\eta)$ értéke:", value=2.0, step=0.5)
        with col_exy:
            exy = st.number_input(r"$E(\xi\eta)$ szorzat várható értéke:", value=7.0, step=0.5)
            
        cov_calc = exy - (ex * ey)
        
        st.success(r"**A kovariancia a tétel alapján:**")
        st.latex(rf"\text{{cov}}(\xi, \eta) = {exy} - ({ex} \cdot {ey}) = \mathbf{{{cov_calc:.2f}}}")
        
        if cov_calc == 0:
            st.warning(r"Mivel a kovariancia $0$, $\xi$ és $\eta$ nagy eséllyel **függetlenek egymástól**.")
        elif cov_calc > 0:
            st.info(r"Pozitív kovariancia: a két változó **együtt mozog**.")
        else:
            st.error(r"Negatív kovariancia: a két változó **ellentétesen mozog**.")
    with st.expander(r"5.20 Tétel (Kovariancia és függetlenség)"):
        # ==========================================
        # 5.20 TÉTEL: KOVARIANCIA ÉS FÜGGETLENSÉG
        # ==========================================
        st.write(r"**5.20 Tétel (Kovariancia és függetlenség)**")
        st.write(r"Ha az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ és $\eta$ valószínűségi változók egyszerre diszkrétek vagy abszolút folytonosak, továbbá létezik várható értékük és **FÜGGETLENEK**, akkor létezik $\xi$ és $\eta$ kovarianciája, és:")
        
        st.latex(r"\text{cov}(\xi, \eta) = 0")
        
        st.error(r"⚠️ **A VIZSGÁK LEGNAGYOBB CSAPDÁJA (A piros megjegyzés):**")
        st.write(r"Visszafelé ez **NEM IGAZ**! Attól, hogy a kovariancia nulla, a két változó még nagyon is függhet egymástól. A nulla kovariancia csupán annyit jelent, hogy nincs köztük *lineáris* (egyenes arányosságú) kapcsolat, de valamilyen bonyolultabb (pl. parabolikus) kapcsolat még simán lehet!")
        st.latex(r"\text{cov}(\xi, \eta) = 0 \quad \not\Rightarrow \quad \xi \text{ és } \eta \text{ független.}")

        st.markdown(r"---")
        st.markdown(r"##### 🤯 Szimuláció 5.20: A Nulla Kovariancia Csapdája")
        st.write(r"Lássunk egy példát, amikor a kovariancia $0$, a két változó mégis 100%-osan függ egymástól! Legyen $\xi$ egy véletlen egész szám $-2$ és $2$ között. Legyen $\eta$ egyszerűen a $\xi$ négyzete ($\eta = \xi^2$). Ezek egyértelműen függnek egymástól: ha $\xi = 2$, akkor $\eta$ garantáltan $4$!")
        
        import pandas as pd
        
        # Adatok generálása
        xi_ertekek = [-2, -1, 0, 1, 2]
        eta_ertekek = [x**2 for x in xi_ertekek]
        
        df_csapda = pd.DataFrame({
            "ξ (Eredeti szám)": xi_ertekek,
            "η (A szám négyzete)": eta_ertekek
        })
        
        col_t, col_c = st.columns([1, 2])
        with col_t:
            st.write("**A kimenetelek táblázata:**")
            st.dataframe(df_csapda, hide_index=True)
            
        with col_c:
            # Várható értékek számolása
            e_xi = sum(xi_ertekek) / len(xi_ertekek) # -2 -1 + 0 + 1 + 2 = 0
            e_eta = sum(eta_ertekek) / len(eta_ertekek) # 4 + 1 + 0 + 1 + 4 = 10 / 5 = 2
            
            # E(ξ*η) számolása (ami ξ^3)
            szorzat_atlag = sum([x * (x**2) for x in xi_ertekek]) / len(xi_ertekek) # -8 -1 + 0 + 1 + 8 = 0
            
            # Kovariancia képlet: E(XY) - E(X)E(Y)
            cov_csapda = szorzat_atlag - (e_xi * e_eta)
            
            st.write(r"**Számoljuk ki a kovarianciát (5.19 tétel alapján):**")
            st.latex(rf"E(\xi) = {e_xi}, \quad E(\eta) = {e_eta}")
            st.latex(rf"E(\xi \cdot \eta) = {szorzat_atlag}")
            st.success(rf"\text{{cov}}(\xi, \eta) = {szorzat_atlag} - ({e_xi} \cdot {e_eta}) = \mathbf{{{cov_csapda}}}")
            
        st.warning(r"Látod? A kovariancia pontosan $0$, mert a grafikon egy U-alakot (parabolát) ír le, nem pedig egy egyenest. A matematika lineárisan nem talál összefüggést, pedig $\eta$ teljesen ki van szolgáltatva $\xi$-nek!")
    with st.expander(r"5.21 Tétel (A standardizált várható értéke és szórásnégyzete)"):
        # ==========================================
        # 5.21 TÉTEL: STANDARDIZÁLT VÁLTOZÓ
        # ==========================================
        st.write(r"**5.21 Tétel (A standardizált várható értéke és szórásnégyzete)**")
        st.write(r"Tegyük fel, hogy az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ valószínűségi változónak létezik standardizáltja ($\tilde{\xi}$). Ekkor:")
        
        st.latex(r"E(\tilde{\xi}) = 0 \quad \text{és} \quad D^2(\tilde{\xi}) = 1")

        st.markdown(r"**Magyarázat (Miért logikus ez?):**")
        st.write(r"Ez a korábbi 5.15-ös és 5.18-as tételek közvetlen következménye!")
        st.write(r"1. Amikor a változóból kivonjuk a saját várható értékét ($\xi - E(\xi)$), akkor a 'középpont' pontosan a $0$-ra tolódik el.")
        st.write(r"2. Amikor ezt az egészet elosztjuk a szórással ($D(\xi)$), akkor a 'szélességet' (az adat szóródását) pontosan $1$-re préseljük össze vagy nyújtjuk ki.")
        st.write(r"Bármilyen eloszlásból is indulunk ki, a standardizálás után mindig egy $0$ közepű, $1$ szórású egységes eloszlást kapunk!")

        st.markdown(r"---")
        st.markdown(r"##### 📏 Szimuláció 5.21: A Matematikai Bizonyítás Gépezete")
        st.write(r"Állíts be egy tetszőleges induló várható értéket és szórást, és nézd meg lépésről lépésre, hogyan 'darálja le' a matematika $0$-ra és $1$-re!")
        
        col_ex, col_dx = st.columns(2)
        with col_ex:
            eredeti_e = st.number_input(r"Eredeti $E(\xi)$ (Átlag):", value=50.0, step=5.0)
        with col_dx:
            eredeti_d = st.number_input(r"Eredeti $D(\xi)$ (Szórás):", min_value=0.1, value=10.0, step=1.0)
            
        st.write(r"**1. Lépés: A standardizált várható értékének levezetése (5.15-ös tétel alapján):**")
        st.latex(rf"E(\tilde{{\xi}}) = E\left(\frac{{\xi - {eredeti_e}}}{{{eredeti_d}}}\right) = \frac{{1}}{{{eredeti_d}}} \cdot (E(\xi) - {eredeti_e}) = \frac{{1}}{{{eredeti_d}}} \cdot ({eredeti_e} - {eredeti_e}) = \mathbf{{0}}")
        
        st.write(r"**2. Lépés: A standardizált szórásának levezetése (5.18-as tétel alapján):**")
        st.latex(rf"D(\tilde{{\xi}}) = D\left(\frac{{\xi - {eredeti_e}}}{{{eredeti_d}}}\right) = \left|\frac{{1}}{{{eredeti_d}}}\right| \cdot D(\xi) = \frac{{1}}{{{eredeti_d}}} \cdot {eredeti_d} = \mathbf{{1}}")
        
        st.success(r"✅ Látod? Teljesen mindegy, milyen számokat írtál be, a végeredmény matematikailag **mindig 0 és 1** lesz!")
    with st.expander(r"5.22 Tétel (Várható érték, kovariancia, korreláció)"):
        # ==========================================
        # 5.22 TÉTEL: KORRELÁCIÓ = STANDARDIZÁLT KOVARIANCIA
        # ==========================================
        st.write(r"**5.22 Tétel (Várható érték, kovariancia, korreláció)**")
        st.write(r"Tegyük fel, hogy az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ és $\eta$ valószínűségi változóknak létezik standardizáltja ($\tilde{\xi}$ és $\tilde{\eta}$).")
        st.write(r"Ha $E(\tilde{\xi}\tilde{\eta})$, $\text{corr}(\xi, \eta)$, és $\text{cov}(\tilde{\xi}, \tilde{\eta})$ közül egy létezik, akkor a másik kettő is, és ekkor:")
        
        st.latex(r"E(\tilde{\xi}\tilde{\eta}) = \text{corr}(\xi, \eta) = \text{cov}(\tilde{\xi}, \tilde{\eta})")

        st.info(r"💡 **Konyhanyelven:** Ez a tétel nagyon elegáns! Azt mondja ki, hogy a **korreláció nem más, mint a standardizált változók kovarianciája**. Mivel a standardizálással 'letöröltük' az eredeti mértékegységeket és léptékeket (pl. millió forintok vs. centiméterek), a korreláció egy tiszta, 'skálázatlan' viszonyszám lesz, ami pusztán csak az együttmozgás erejét méri!")

    with st.expander(r"5.23 Tétel (A korreláció korlátja)"):
        # ==========================================
        # 5.23 TÉTEL: A KORRELÁCIÓ KORLÁTJA
        # ==========================================
        st.write(r"**5.23 Tétel (A korreláció korlátja)**")
        st.write(r"Ha az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ és $\eta$ valószínűségi változók egyszerre diszkrétek vagy abszolút folytonosak, továbbá létezik korrelációs együtthatójuk, akkor:")
        
        st.latex(r"|\text{corr}(\xi, \eta)| \le 1")
        
        st.write(r"**Következmény (A piros dobozból):**")
        st.latex(r"|\text{cov}(\xi, \eta)| \le D(\xi)D(\eta)")

        st.markdown(r"**Magyarázat:**")
        st.write(r"Ez a statisztika alaptörvénye. A korreláció sosem lépheti túl az $1$-et (vagy a $-1$-et). Az $1$ jelentése: a két változó tökéletes pozitív egyenes vonalú (lineáris) kapcsolatban van (pl. ha X nő eggyel, Y mindig nő kettővel). A $-1$ a tökéletes ellentétes kapcsolat. A következmény pedig megadja a kovariancia 'plafonját': sosem lehet nagyobb, mint a két szórás szorzata.")

        st.markdown(r"---")
        st.markdown(r"##### 📏 Szimuláció 5.23: A Kovariancia Plafonja")
        st.write(r"A tétel következménye (ami a híres Cauchy–Schwarz-egyenlőtlenségből jön) szerint a kovariancia nem vehet fel akármilyen hatalmas értéket. A maximális értékét a két változó szórása korlátozza. Állítsd be a szórásokat, és nézzük meg a határokat!")
        
        col_dx, col_dy = st.columns(2)
        with col_dx:
            dx_val = st.number_input(r"$D(\xi)$ (Első változó szórása):", min_value=0.1, value=5.0, step=1.0)
        with col_dy:
            dy_val = st.number_input(r"$D(\eta)$ (Második változó szórása):", min_value=0.1, value=8.0, step=1.0)
            
        max_cov = dx_val * dy_val
        
        st.info(rf"**A Tétel következménye alapján a kovariancia elméleti határai:**")
        st.latex(rf"-{max_cov:.2f} \le \text{{cov}}(\xi, \eta) \le {max_cov:.2f}")
        
        st.write(r"Most állítsd be a köztük lévő tényleges korrelációt ($-1$ és $1$ között), és nézzük meg a valós kovarianciát!")
        corr_val = st.slider("Aktuális korreláció (corr):", -1.0, 1.0, 0.5, 0.1)
        aktualis_cov = corr_val * dx_val * dy_val
        
        st.success(rf"**Számított aktuális kovariancia:** $\text{{cov}} = {aktualis_cov:.2f}$")
        
        if abs(corr_val) == 1.0:
            st.warning(r"⚠️ Elértük a korlátot! A két változó szigorú, tökéletes determinisztikus (lineáris) kapcsolatban van.")
    with st.expander(r"5.24 Tétel (Függőség és korreláció)"):
        # ==========================================
        # 5.24 TÉTEL: FÜGGŐSÉG -> KORRELÁCIÓ
        # ==========================================
        st.write(r"**5.24 Tétel (Függőség $\implies$ korreláció)**")
        st.write(r"Tegyük fel, hogy az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ valószínűségi változónak létezik szórása és $D(\xi) \neq 0$, továbbá bevezetünk egy új változót, ami $\xi$ lineáris függvénye: $\eta := a\xi + b$ (valamely $0 \neq a$ és $b$ valós számokra).")
        st.write(r"Ekkor létezik $\xi$ és $\eta$ korrelációs együtthatója, és:")
        st.latex(r"\text{corr}(\xi, \eta) = \begin{cases} 1, & \text{ha } a > 0, \\ -1, & \text{ha } a < 0. \end{cases}")

        st.markdown(r"---")
        st.markdown(r"##### 📈 Szimuláció 5.24: A determinisztikus egyenes")
        st.write(r"Lássuk, mi történik, ha egy változót egy matematikai szabállyal ($\eta = a\xi + b$) egy másikhoz láncolunk! Próbáld meg változtatni az $a$ (meredekség) és $b$ (eltolás) paramétereket!")

        col_a, col_b = st.columns(2)
        with col_a:
            a_val = st.slider("Meredekség (a):", -5.0, 5.0, 2.0, 0.5)
        with col_b:
            b_val = st.slider("Eltolás (b):", -10.0, 10.0, 0.0, 1.0)

        import numpy as np
        import pandas as pd

        if a_val == 0:
            st.warning(r"⚠️ Ha az $a = 0$, akkor $\eta$ egy fix konstans lesz. Konstansnak a szórása 0, így a korreláció képletében 0-val osztanánk, vagyis a korreláció nem értelmezett! (Ezért köti ki a tétel, hogy $a \neq 0$).")
        else:
            # Generálunk 50 pontot
            x_pontok = np.linspace(-10, 10, 50)
            y_pontok = a_val * x_pontok + b_val

            df_lin = pd.DataFrame({
                "ξ (X tengely)": x_pontok,
                "η (Y tengely)": y_pontok
            })

            st.scatter_chart(df_lin, x="ξ (X tengely)", y="η (Y tengely)")

            if a_val > 0:
                st.success(rf"**Eredmény (5.24 tétel alapján):** Mivel az $a = {a_val} > 0$, a grafikon szigorúan emelkedik. Bármit is írsz a 'b' helyére, a pontok egy egyenesre esnek, így a korreláció elméletileg pontosan $\mathbf{{\text{{corr}} = 1}}$.")
            elif a_val < 0:
                st.error(rf"**Eredmény (5.24 tétel alapján):** Mivel az $a = {a_val} < 0$, a grafikon szigorúan süllyed. Bármit is írsz a 'b' helyére, a pontok egy egyenesre esnek, így a korreláció elméletileg pontosan $\mathbf{{\text{{corr}} = -1}}$.")

    with st.expander(r"5.25 Tétel (Korreláció és függőség)"):
        # ==========================================
        # 5.25 TÉTEL: KORRELÁCIÓ -> FÜGGŐSÉG
        # ==========================================
        st.write(r"**5.25 Tétel (Korreláció $\implies$ függőség)**")
        st.write(r"Tegyük fel, hogy az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ és $\eta$ valószínűségi változóknak létezik korrelációs együtthatója, és $|\text{corr}(\xi, \eta)| = 1$.")
        st.write(r"Ekkor léteznek olyan $0 \neq a$ és $b$ valós számok, amelyekre:")
        st.latex(r"P(\eta = a\xi + b) = 1")

        st.error(r"💡 **Következmény (A Piros doboz):** $\xi$ és $\eta$ pontosan akkor alkotnak $1$ valószínűséggel (biztosan) egy lineáris függvényt egymással, ha $|\text{corr}(\xi, \eta)| = 1$. Ezért a korrelációs együttható a **lineáris FÜGGŐSÉG 'mérőszáma'**.")

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
            r"<br>- A definíció miatt egy valószínűségi változónak **mindig** létezik eloszlásfüggvénye."
            r"<br>- Diszkrét valószínűségi változónak is van eloszlásfüggvénye (ez egy 'lépcsős' függvény), ekkor $F_\xi$ értékkészlete megszámlálható."
            r"<br>- ⚠️ **Beugratós kérdés:** A fordítottja nem igaz! Ha egy $F_\xi$ függvény értékkészlete megszámlálható, abból matematikai okok miatt még nem következik biztosan, hogy maga a $\xi$ változó diszkrét.")

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

    # ==========================================
    # 4. ABSZOLÚT FOLYTONOS VÁLTOZÓ ÉS PDF
    # ==========================================
    st.markdown(r"### 4. Abszolút folytonos valószínűségi változó és Sűrűségfüggvény")
    st.write(r"A $\xi$ **abszolút folytonos valószínűségi változó**, ha létezik olyan $f_\xi : \mathbb{R} \rightarrow \mathbb{R}$ nemnegatív függvény, amelyre az eloszlásfüggvény előállítható integrálként:")
    st.latex(r"F_\xi(x) = \int_{-\infty}^{x} f_\xi(t) dt \quad \text{teljesül } \forall x \in \mathbb{R} \text{ esetén.}")
    st.write(r"Ekkor ezt az $f_\xi$ függvényt a $\xi$ **sűrűségfüggvényének** (Probability Density Function, PDF) nevezzük.")

    st.info(r"💡 **Trükkös észrevétel a vizsgára:** Egy $\xi$ abszolút folytonos valószínűségi változónak *végtelen sok* sűrűségfüggvénye van! Miért? Mert ha egy függvény értékét egyetlen pontban megváltoztatjuk, a görbe alatti terület (az integrál) nem változik meg. Ezt úgy mondják a matematikusok, hogy ezek a függvények 'majdnem mindenütt megegyeznek'.")

    st.markdown(r"---")

    # ==========================================
    # 5. EGYENLETES ELOSZLÁS
    # ==========================================
    st.markdown(r"### 5. Egyenletes eloszlás az $[a, b]$ intervallumon")
    st.write(r"A $\xi$ valószínűségi változót az $[a, b]$ intervallumon **egyenletes eloszlásúnak** (Uniform Distribution) nevezzük, ha minden érték 'ugyanakkora eséllyel' fordul elő a határokon belül. Ennek matematikai definíciói:")

    col_cdf, col_pdf = st.columns(2)
    with col_cdf:
        st.markdown(r"**Eloszlásfüggvénye (CDF - Halmozott esély):**")
        st.latex(r"F(x) = \begin{cases} 0, & \text{ha } x \le a \\ \frac{x-a}{b-a}, & \text{ha } a < x \le b \\ 1, & \text{ha } b < x \end{cases}")
    with col_pdf:
        st.markdown(r"**Sűrűségfüggvénye (PDF - Görbe magassága):**")
        st.latex(r"f(x) = \begin{cases} \frac{1}{b-a}, & \text{ha } a \le x \le b \\ 0, & \text{egyébként} \end{cases}")

    # ==========================================
    # INTERAKTÍV TESZTELŐ: EGYENLETES ELOSZLÁS
    # ==========================================
    st.markdown(r"#### 📏 Interaktív tesztelő: Az Egyenletes Eloszlás")
    st.write(r"Állíts be egy intervallumot (a és b), majd vizsgálj meg egy x pontot! Nézd meg, hogyan működik a sűrűségfüggvény és az eloszlásfüggvény a gyakorlatban!")

    col_a, col_b = st.columns(2)
    with col_a:
        unif_a = st.number_input("Alsó határ (a):", value=10.0, step=1.0)
    with col_b:
        unif_b = st.number_input("Felső határ (b):", value=20.0, step=1.0)

    if unif_a < unif_b:
        unif_x = st.slider("Vizsgált pont (x):", unif_a - 5.0, unif_b + 5.0, (unif_a + unif_b) / 2, 0.5)
        
        # PDF számítás
        if unif_a <= unif_x <= unif_b:
            pdf_val = 1.0 / (unif_b - unif_a)
        else:
            pdf_val = 0.0
            
        # CDF számítás
        if unif_x <= unif_a:
            cdf_val = 0.0
        elif unif_x > unif_b:
            cdf_val = 1.0
        else:
            cdf_val = (unif_x - unif_a) / (unif_b - unif_a)
            
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.warning(r"**Sűrűségfüggvény $f(x)$:**")
            st.latex(rf"f({unif_x}) = \mathbf{{{pdf_val:.4f}}}")
            if pdf_val > 0:
                st.caption(r"A pont az intervallumon belül van, így a sűrűség konstans: $\frac{1}{b-a}$")
            else:
                st.caption(r"A pont az intervallumon kívül van, így a sűrűség 0.")
                
        with col_res2:
            st.success(r"**Eloszlásfüggvény $F(x)$:**")
            st.latex(rf"F({unif_x}) = P(\xi < {unif_x}) = \mathbf{{{cdf_val:.4f}}}")
            st.progress(float(cdf_val))
            
    else:
        st.error(r"Az alsó határnak szigorúan kisebbnek kell lennie, mint a felső határnak!")


    # ==========================================
    # 6. KEVERT VALÓSZÍNŰSÉGI VÁLTOZÓ
    # ==========================================
    st.markdown(r"### 6. Kevert valószínűségi változó")
    st.write(r"A $\xi$ valószínűségi változó **kevert valószínűségi változó** (Mixed Random Variable), ha nem abszolút folytonos eloszlású és nem is diszkrét.")

    st.info(r"💡 **Mit jelent ez a gyakorlatban?** Egy kevert változó eloszlásfüggvénye 'hibrid': vannak benne folytonosan növekvő (ferde) szakaszok, mint a folytonos változóknál, de vannak benne hirtelen ugrások (lépcsők) is, mint a diszkrét változóknál.")

    st.markdown(r"#### Példa egy kevert eloszlásfüggvényre:")
    st.latex(r"F(x) := \begin{cases} 0, & \text{ha } x \le 0 \\ x, & \text{ha } 0 < x \le 1/2 \\ 1, & \text{ha } x > 1/2 \end{cases}")

    st.write(r"**Miért kevert ez az eloszlás?**")
    st.write(r"1. Az (F1)-(F4) szabályok (5.5-ös tétel) teljesülnek rá, így az 5.6-os Tétel alapján biztosan létezik ilyen valószínűségi változó.")
    st.write(r"2. Mivel az $F$ értékkészlete nem megszámlálható (tartalmazza az egész $[0, 0.5]$ intervallumot), a változó **nem diszkrét**.")
    st.write(r"3. Mivel az $F$ az $x = 1/2$ pontban nem folytonos (hiszen balról az érték $0.5$, de jobbról hirtelen $1$-re ugrik), a változó **nem abszolút folytonos**.")

    # ==========================================
    # INTERAKTÍV TESZTELŐ: KEVERT ELOSZLÁS
    # ==========================================
    st.markdown(r"##### 🧪 Interaktív tesztelő: A Kevert Eloszlás")
    st.write(r"Mozgasd a csúszkát, és figyeld meg az ugrást az $x = 0.5$ pontnál!")
    
    x_kevert = st.slider("Vizsgált x érték a kevert függvénynél:", -0.2, 1.0, 0.25, 0.05)
    
    if x_kevert <= 0:
        f_val = 0.0
        st.write(r"**Szabály:** $x \le 0 \implies F(x) = 0$")
    elif x_kevert <= 0.5:
        f_val = x_kevert
        st.write(r"**Szabály:** $0 < x \le 1/2 \implies F(x) = x$ (Folytonos növekedés)")
    else:
        f_val = 1.0
        st.warning(r"⚠️ **UGRÁS TÖRTÉNT!** A függvény hirtelen $0.5$-ről $1$-re ugrott!")
        st.write(r"**Szabály:** $x > 1/2 \implies F(x) = 1$ (Konstans maximum)")
        
    st.success(r"**Eloszlásfüggvény értéke:**")
    st.latex(rf"F({x_kevert:.2f}) = \mathbf{{{f_val:.2f}}}")
    st.progress(float(f_val))

    # ==========================================
    # 7. VALÓSZÍNŰSÉGI VEKTORVÁLTOZÓ ÉS EGYÜTTES ELOSZLÁS
    # ==========================================
    st.markdown(r"### 7. Valószínűségi vektorváltozó és Együttes eloszlás")
    
    st.markdown(r"#### Valószínűségi vektorváltozó")
    st.write(r"Legyen $\xi$ és $\eta$ valószínűségi változó ugyanazon az $(\Omega, \mathcal{F}, P)$ valószínűségi mezőn. Ekkor a $(\xi, \eta)$ párt **valószínűségi vektorváltozónak** (Random Vector Variable) nevezzük.")
    st.info(r"💡 **Gyakorlati jelentés:** Sokszor egy kísérlet során nem csak egy, hanem egyszerre több dolgot is megfigyelünk. Például egy embernél mérjük a testmagasságát ($\xi$) ÉS a testtömegét ($\eta$). Ezeket együtt egy $(\xi, \eta)$ vektorként kezeljük, mert összefügghetnek!")

    st.markdown(r"#### Együttes eloszlás (Diszkrét esetben)")
    st.write(r"Ha $\xi$ és $\eta$ **diszkrét** valószínűségi változók, akkor az **együttes eloszlásukon** (Joint Distribution) a következő sorozatot értjük:")
    st.latex(r"\langle p_{k,l} \rangle : \mathbb{R}_\xi \times \mathbb{R}_\eta \rightarrow [0, 1]")
    st.latex(r"p_{k,l} := P(\xi = k, \eta = l)")
    st.write(r"Ahol a vessző az 'ÉS' kapcsolatot (metszetet) jelenti: $\{\xi = k, \eta = l\} := \{\xi = k\} \cap \{\eta = l\}$.")
    
    # ==========================================
    # INTERAKTÍV TESZTELŐ: EGYÜTTES ELOSZLÁS
    # ==========================================
    st.markdown(r"##### 📊 Interaktív tesztelő: Együttes eloszlás (Két érme)")
    st.write(r"Dobjunk fel két érmét! Legyen $\xi$ az első érme eredménye (0=Írás, 1=Fej), $\eta$ pedig a második érme eredménye (0=Írás, 1=Fej). Nézzük meg az együttes eloszlásukat!")
    
    st.write(r"Válaszd ki, melyik $p_{k,l}$ együttes valószínűségre vagy kíváncsi:")
    col_k, col_l = st.columns(2)
    with col_k:
        k_val = st.selectbox("Első érme (ξ = k):", [0, 1], format_func=lambda x: "1 (Fej)" if x==1 else "0 (Írás)")
    with col_l:
        l_val = st.selectbox("Második érme (η = l):", [0, 1], format_func=lambda x: "1 (Fej)" if x==1 else "0 (Írás)")
        
    st.success(rf"**A kiválasztott együttes valószínűség:**")
    st.latex(rf"p_{{{k_val},{l_val}}} = P(\xi = {k_val}, \eta = {l_val}) = \frac{{1}}{{2}} \cdot \frac{{1}}{{2}} = \mathbf{{0.25}} \text{{ (25%)}}")
    st.write(r"Mivel a két érme független, mind a 4 lehetséges kombináció (0-0, 0-1, 1-0, 1-1) esélye pontosan $0.25$. Az összes $p_{k,l}$ összege természetesen kiadja az $1$-et (100%-ot)!")

    # ==========================================
    # 8. PEREMELOSZLÁSOK ÉS EGYÜTTES ELOSZLÁSFÜGGVÉNY
    # ==========================================
    st.markdown(r"### 8. Peremeloszlás és Együttes eloszlásfüggvény")
    
    st.markdown(r"#### Peremeloszlások (Marginal Distributions)")
    st.write(r"Legyen $\xi$ és $\eta$ valószínűségi változó $(\Omega, \mathcal{F}, P)$-n. Ekkor $\xi$ és $\eta$ (önálló) eloszlásai a $(\xi, \eta)$ valószínűségi vektorváltozó **peremeloszlásai**.")
    
    st.info(r"💡 **Konyhanyelven:** Képzelj el egy 2D-s táblázatot, ahol a sorok egy dobókocka, az oszlopok egy érme eredményeit mutatják. Az *együttes eloszlás* a táblázat belseje. A *peremeloszlás* pedig az, amikor az egyik változót letakarod a kezeddel, mintha ott sem lenne, és csak a maradék egyetlen változó eloszlását vizsgálod. A nevét onnan kapta, hogy régen a statisztikusok a táblázatok 'peremére' (szélére) összegezték a sorokat és az oszlopokat.")

    st.markdown(r"#### Együttes eloszlásfüggvény (Joint CDF)")
    st.write(r"Az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ és $\eta$ valószínűségi változók **együttes eloszlásfüggvénye** a 2D-s térben ($x, y$ koordinátákon) értelmezett függvény:")
    st.latex(r"F_{\xi,\eta} : \mathbb{R}^2 \rightarrow [0, 1], \quad F_{\xi,\eta}(x,y) := P(\xi < x, \eta < y)")
    st.write(r"ahol a vessző 'ÉS' kapcsolatot (metszetet) jelent: $\{\xi < x, \eta < y\} := \{\xi < x\} \cap \{\eta < y\}$.")
    
    st.write(r"Ekkor a különálló $F_\xi$ és $F_\eta$ függvényeket a $(\xi, \eta)$ valószínűségi vektorváltozó **perem-eloszlásfüggvényeinek** nevezzük.")

    # ==========================================
    # 9. EGYÜTTES SŰRŰSÉGFÜGGVÉNY (2D PDF) ÉS PEREM-SŰRŰSÉG
    # ==========================================
    st.markdown(r"### 9. Együttes sűrűségfüggvény és Perem-sűrűségfüggvény")
    
    st.write(r"$\xi$ és $\eta$ együttes eloszlása **abszolút folytonos**, ha minden $x, y \in \mathbb{R}$-ra létezik $f_{\xi,\eta} : \mathbb{R}^2 \rightarrow \mathbb{R}$ nemnegatív függvény, amelyre a halmozott eloszlásfüggvény felírható kettős integrálként:")
    st.latex(r"F_{\xi,\eta}(x, y) = \int_{-\infty}^{x} \int_{-\infty}^{y} f_{\xi,\eta}(u, v) dv du")
    
    st.write(r"Ekkor ezt az $f_{\xi,\eta}$ függvényt a $\xi$ és $\eta$ **együttes sűrűségfüggvényének** (Joint PDF) nevezzük.")
    
    st.write(r"Továbbá a különálló $f_\xi$ és $f_\eta$ függvényeket a $(\xi, \eta)$ valószínűségi vektorváltozó **perem-sűrűségfüggvényeinek** (Marginal PDFs) nevezzük.")
    
    st.info(r"💡 **Konyhanyelven:** Ez a 2D-s megfelelője a sima sűrűségfüggvénynek. Míg a sima $f(x)$ egy vonal (görbe) feletti magasságot mutatott, az együttes sűrűségfüggvény egy 2D-s sík (mint egy térkép) feletti domborzatot, egy 'hegyet' ír le. A perem-sűrűségfüggvény pedig az, amikor ezt a hegyet pontosan oldalról nézed, és csak az egyik dimenzió mentén vizsgálod a sziluettjét.")

    # ==========================================
    # 10. FÜGGETLEN VALÓSZÍNŰSÉGI VÁLTOZÓK
    # ==========================================
    st.markdown(r"### 10. Független valószínűségi változók")
    
    st.write(r"Az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ és $\eta$ valószínűségi változók **függetlenek** (Independent Random Variables), ha minden valós $x$ és $y$ értékre a közös eloszlásfüggvényük megegyezik a perem-eloszlásfüggvények szorzatával:")
    
    st.latex(r"F_{\xi,\eta}(x, y) = F_\xi(x) \cdot F_\eta(y)")
    
    st.info(r"💡 **Konyhanyelven:** Két dolog akkor független, ha az egyik esélye egyáltalán nem befolyásolja a másikat. A matematikában ezt úgy ellenőrizzük, hogy megnézzük: a 'kettő együtt teljesül' valószínűsége megegyezik-e a külön-külön vett valószínűségek szorzatával. Ugyanez igaz volt a 3. fejezetben az elemi eseményekre is ($P(A \cap B) = P(A) \cdot P(B)$), most pedig a halmozott valószínűségekre (CDF) is érvényes kiterjesztettük.")

    # ==========================================
    # 11. VÁRHATÓ ÉRTÉK (EXPECTED VALUE)
    # ==========================================
    st.markdown(r"### 11. Várható érték, $E(\xi)$")
    
    st.write(r"Legyen $\xi$ az $(\Omega, \mathcal{F}, P)$-n értelmezett valószínűségi változó. Az $E(\xi)$ számot a $\xi$ **várható értékének** (Expected Value) nevezzük, és a következőképpen definiáljuk:")

    st.markdown(r"**(0) Véges diszkrét eset:**")
    st.write(r"Ha $\xi$ diszkrét és az értékkészlete véges, azaz $\text{rng}(\xi) = \{x_1, x_2, \dots, x_n\}$, akkor:")
    st.latex(r"E(\xi) := \sum_{k=1}^{n} x_k \cdot P(\xi = x_k)")
    
    st.markdown(r"**(1) Végtelen diszkrét eset:**")
    st.write(r"Ha $\xi$ diszkrét, de az értékkészlete megszámlálhatóan végtelen, $\text{rng}(\xi) = \{x_1, x_2, \dots\}$, és teljesül az abszolút konvergencia feltétele:")
    st.latex(r"\sum_{i} p_i |x_i| < \infty \quad \text{(ahol } p_i := P(\xi = x_i)\text{)}")
    st.write(r"akkor legyen:")
    st.latex(r"E(\xi) := \sum_{i} p_i x_i")

    st.markdown(r"**(2) Abszolút folytonos eset:**")
    st.write(r"Ha $\xi$ abszolút folytonos és teljesül az alábbi (abszolút integrálhatósági) feltétel:")
    st.latex(r"\int_{-\infty}^{\infty} |x| f_\xi(x) dx < \infty")
    st.write(r"akkor a várható érték:")
    st.latex(r"E(\xi) := \int_{-\infty}^{\infty} x \cdot f_\xi(x) dx")

    st.error(r"⚠️ **Fontos szabály az (1) és (2) esetekhez:** Ha a fenti konvergencia-feltételek *nem* teljesülnek (azaz a szumma vagy az integrál végtelenbe tart), akkor azt mondjuk, hogy **$E(\xi)$ nem létezik**!")

    st.info(r"💡 **Konyhanyelven:** A várható érték egyszerűen egy súlyozott átlag. Minden lehetséges értéket ($x$) megszorzunk azzal, hogy mekkora eséllyel következik be ($P$ vagy $f(x)$), majd ezeket összeadjuk. Hosszú távon egy kaszinójátékban vagy egy tőzsdei befektetésnél a várható érték mutatja meg, hogy nyereséges leszel-e.")

    # ==========================================
    # INTERAKTÍV TESZTELŐ: VÁRHATÓ ÉRTÉK
    # ==========================================
    st.markdown(r"##### ⚖️ Szimuláció 11: Érdemes-e játszani?")
    st.write(r"Képzeld el, hogy játszunk egy játékot: befizetsz 1,000 Ft-ot. Ha nyersz, kapsz 10,000 Ft-ot (azaz 9,000 Ft a tiszta haszon). Ha vesztesz, elbukod az ezrest ($-1000$ Ft). Állítsd be a nyerési esélyt, és nézzük meg a játék várható értékét ($E(\xi)$)!")
    
    nyeresi_esely = st.slider("Nyerés valószínűsége (p):", 0.0, 1.0, 0.05, 0.01)
    vesztesi_esely = 1.0 - nyeresi_esely
    
    x_nyeres = 9000  # Tisztán nyert összeg
    x_vesztes = -1000 # Elbukott összeg
    
    varhato_ertek = (x_nyeres * nyeresi_esely) + (x_vesztes * vesztesi_esely)
    
    st.latex(rf"E(\xi) = (9000 \cdot {nyeresi_esely:.2f}) + (-1000 \cdot {vesztesi_esely:.2f}) = \mathbf{{{varhato_ertek:.0f} \text{{ Ft}}}}")
    
    if varhato_ertek > 0:
        st.success(r"✅ **Pozitív várható érték!** Bár néha veszíteni fogsz, ha ezt a játékot nagyon sokszor lejátszod, körönként átlagosan ennyi forintot fogsz nyerni. Ez egy jó üzlet!")
    elif varhato_ertek == 0:
        st.warning(r"⚖️ **Nulla várható érték (Igazságos játék).** Hosszú távon pont nullára jössz ki. Se nem nyersz, se nem vesztesz.")
    else:
        st.error(r"❌ **Negatív várható érték!** A kaszinók erre épülnek. Rövid távon lehet szerencséd, de ha sokszor játszol, körönként átlagosan biztosan veszíteni fogsz. Ne játssz!")

    # ==========================================
    # 12. MOMENTUM ÉS CENTRÁLIS MOMENTUM
    # ==========================================
    st.markdown(r"### 12. Momentum és Centrális momentum")
    
    st.write(r"Tegyük fel, hogy valamely $k \ge 0$ egészre és $\xi$ valószínűségi változóra léteznek a következő értékek:")
    st.latex(r"E(\xi^k) \quad \text{és} \quad E\left((\xi - E(\xi))^k\right)")
    
    st.write(r"Ekkor ezeket rendre a $\xi$ valószínűségi változó:")
    st.markdown(r"- **$k$-adik momentumának**, illetve")
    st.markdown(r"- **$k$-adik centrális momentumának** nevezzük.")
    
    st.info(r"💡 **Kritikus észrevétel (Piros doboz a dián):** A várható érték ($E(\xi)$) nem más, mint a $\xi$ **első momentuma** (hiszen $k=1$ esetén $E(\xi^1) = E(\xi)$).")
    
    st.write(r"**További fontos észrevétel:**")
    st.write(r"Magasabb rendű momentum létezése $\implies$ alacsonyabb rendű momentum létezése. (Tehát ha létezik a 4. momentum, akkor garantáltan létezik a 3., a 2., és az 1. is).")

    st.markdown(r"##### 🔍 Miért jók nekünk a momentumok?")
    st.write(r"A fizikához hasonlóan, ahol a momentumok egy test tömegeloszlását írják le, a statisztikában ezek az értékek egy eloszlás alakját határozzák meg:")
    st.markdown(r"- **1. momentum ($k=1$):** Várható érték (Hol van az eloszlás közepe?)")
    st.markdown(r"- **2. centrális momentum ($k=2$):** Szórásnégyzet/Variancia (Milyen széles az eloszlás?)")
    st.markdown(r"- **3. centrális momentum ($k=3$):** Ferdeség (Jobbra vagy balra dől-e a haranggörbe?)")
    st.markdown(r"- **4. centrális momentum ($k=4$):** Csúcsosság (Milyen hegyes a görbe teteje?)")

    # ==========================================
    # 13. SZÓRÁS ÉS SZÓRÁSNÉGYZET
    # ==========================================
    st.markdown(r"### 13. Szórás és Szórásnégyzet (Variancia)")
    
    st.write(r"Tegyük fel, hogy az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ valószínűségi változónak és a $(\xi - E(\xi))^2$ kifejezésnek létezik várható értéke. Ekkor:")
    
    st.markdown(r"**1. Szórásnégyzet / Variancia (Variance):**")
    st.latex(r"D^2(\xi) := E\left((\xi - E(\xi))^2\right)")
    st.info(r"💡 **Észrevétel a piros dobozból:** Ez pontosan a $\xi$ **második centrális momentuma**! Azt méri, hogy az értékek átlagosan mennyire 'térnek el a négyzetesen' a várható értéktől.")
    
    st.markdown(r"**2. Szórás (Standard Deviation):**")
    st.latex(r"D(\xi) := \sqrt{E\left((\xi - E(\xi))^2\right)}")
    st.write(r"*(A szórás egyszerűen a szórásnégyzet négyzetgyöke.)*")
    
    st.warning(r"⚠️ **Fontos matematikai finomság (a dia aljáról):** Abból, hogy az $E(\xi)$ (várható érték) létezik, **NEM következik** automatikusan, hogy a $D(\xi)$ (szórás) is létezik! ($E(\xi) \text{ létezik } \not\Rightarrow D(\xi) \text{ létezik}$). Ennek az az oka, hogy a négyzetre emelés miatt az integrál/szumma a szórásnál már 'felrobbanhat' (végtelenbe tarthat), hiába volt a sima átlag véges.")

    st.markdown(r"---")
    st.markdown(r"##### 🎯 Szimuláció 13: Két mesterlövész esete")
    st.write(r"A várható érték csak a 'közepet' mutatja meg. A szórás mondja meg, hogy mennyire 'szétzórtak' az adatok! Képzelj el két mesterlövészt. Mindkettő átlagosan pontosan a céltábla közepét (0 pont) találja el, de a szórásuk eltérő. Generáljunk 50-50 lövést mindkettőnek!")
    
    szoras_lovesz = st.slider("A Kezdő mesterlövész szórása (D):", 0.5, 5.0, 2.5, 0.5)
    
    import numpy as np
    import pandas as pd
    
    # 1. mesterlövész: profi, fixen kicsi szórás (D=0.5)
    lovesek_profi = np.random.normal(0, 0.5, 50)
    # 2. mesterlövész: kezdő, változtatható szórás
    lovesek_kezdo = np.random.normal(0, szoras_lovesz, 50)
    
    df_lovesek = pd.DataFrame({
        "Profi lövész (D = 0.5)": lovesek_profi,
        f"Kezdő lövész (D = {szoras_lovesz:.1f})": lovesek_kezdo
    })
    
    st.scatter_chart(df_lovesek)
    st.caption(r"A grafikonon (y tengely a találat helye) jól láthatod: a Profi lövész találatai sűrűn a 0 vonal körül csoportosulnak. A Kezdő lövész is átlagosan a 0 köré lő, de a találatai sokkal jobban 'szóródnak' a nagyobb $D$ miatt!")

    # ==========================================
    # 14. KOVARIANCIA
    # ==========================================
    st.markdown(r"### 14. Kovariancia (Covariance)")
    
    st.write(r"Az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ és $\eta$ valószínűségi változók **kovarianciája** a következőképpen definiálható (feltéve, hogy a képletben szereplő várható értékek léteznek):")
    
    st.latex(r"\text{cov}(\xi, \eta) := E\left( (\xi - E(\xi))(\eta - E(\eta)) \right)")
    
    st.error(r"💡 **Kritikus észrevétel (Piros doboz):** Egy változó önmagával vett kovarianciája pontosan megegyezik a saját szórásnégyzetével! Vagyis: $\text{cov}(\xi, \xi) = D^2(\xi)$.")
    
    st.info(r"💡 **Konyhanyelven:** A kovariancia azt méri, hogyan mozog együtt két dolog. Például $\xi$ legyen a 'Tanulással töltött órák száma', $\eta$ pedig a 'Vizsgán elért pontszám'. Ha a diákok többsége mindkettőben az átlag felett teljesít (sokat tanul = sok pont), akkor a két zárójel szorzata pozitív lesz, így a kovariancia **pozitív**. Ha ellentétesen mozognak (pl. 'Bulizással töltött órák' és 'Vizsgapontszám'), akkor a kovariancia **negatív**. Ha nincs közük egymáshoz, a kovariancia $0$ körül lesz.")

    st.markdown(r"---")
    st.markdown(r"##### 📈 Szimuláció 14: Együttmozgás a gyakorlatban")
    st.write(r"Állítsd be, hogy milyen kapcsolat legyen két változó között (pl. Magasság és Súly), és nézzük meg, hogyan változik a kovariancia és a pontfelhő alakja!")
    
    kapcsolat = st.slider("Változók közötti kapcsolat iránya és ereje:", -1.0, 1.0, 0.8, 0.1)
    
    import numpy as np
    import pandas as pd
    
    # 100 darab véletlenszerű adatpont generálása a megadott kapcsolat (korreláció) alapján
    np.random.seed(42) # Hogy mindig ugyanúgy nézzen ki betöltéskor
    x_val = np.random.normal(170, 10, 100) # Pl. Magasság (Átlag 170, Szórás 10)
    noise = np.random.normal(0, 10, 100)
    y_val = (kapcsolat * x_val) + (np.sqrt(1 - kapcsolat**2) * noise) + (70 - kapcsolat*170) # Pl. Súly trükkös generálása
    
    df_cov = pd.DataFrame({
        "Magasság (ξ)": x_val,
        "Súly (η)": y_val
    })
    
    # Kovariancia kiszámítása numpy-val (a mátrix [0,1] eleme a két változó kovarianciája)
    szamitott_cov = np.cov(x_val, y_val)[0, 1]
    
    col_c1, col_c2 = st.columns([1, 2])
    with col_c1:
        st.write("**Számított Kovariancia:**")
        if szamitott_cov > 5:
            st.success(rf"$\text{{cov}} = \mathbf{{{szamitott_cov:.1f}}}$ (Pozitív, együtt mozognak!)")
        elif szamitott_cov < -5:
            st.error(rf"$\text{{cov}} = \mathbf{{{szamitott_cov:.1f}}}$ (Negatív, ellentétesen mozognak!)")
        else:
            st.warning(rf"$\text{{cov}} = \mathbf{{{szamitott_cov:.1f}}}$ (Nulla közeli, függetlennek tűnnek.)")
            
    with col_c2:
        st.scatter_chart(df_cov, x="Magasság (ξ)", y="Súly (η)")

    # ==========================================
    # 15. STANDARDIZÁLT VALÓSZÍNŰSÉGI VÁLTOZÓ
    # ==========================================
    st.markdown(r"### 15. Standardizált valószínűségi változó")
    
    st.write(r"Tegyük fel, hogy az $(\Omega, \mathcal{F}, P)$-n értelmezett $\xi$ valószínűségi változónak létezik szórása és az nem nulla ($D(\xi) \neq 0$).")
    st.write(r"Ekkor $\xi$ **standardizáltja** (Standardized Random Variable) a következő valószínűségi változó:")
    
    st.latex(r"\tilde{\xi} = \frac{\xi - E(\xi)}{D(\xi)}")
    
    st.info(r"💡 **Konyhanyelven:** Ezt az eljárást arra használjuk, hogy különböző 'skálájú' dolgokat össze tudjunk hasonlítani. Ha egy diák 80 pontot kapott a matek ZH-n (ahol az átlag 60, a szórás 10), akkor a standardizált értéke: $\frac{80 - 60}{10} = +2$. Ez azt jelenti, hogy ő **2 szórással az átlag felett** teljesített. Ha történelemből 60 pontot kapott, de ott az átlag 40 volt, a szórás pedig 10, akkor a standardizált értéke ott is $\frac{60 - 40}{10} = +2$. Vagyis a látszólag különböző pontszámok ellenére a két tárgyból pontosan ugyanolyan jól (a csoportjához képest egyaránt 2 szórással jobban) teljesített!")