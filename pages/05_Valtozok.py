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

