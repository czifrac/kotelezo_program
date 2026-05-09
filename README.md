# Open Library API

Ezzel a Python programmal ISBN szám alapján lehet könyvet keresni. Kulcs képességek: API használat, JSON, fájlba írás.

A megoldáshoz a requests modult kell telepíteni. (parancs: pip install requests)

# A program felépítése
1. Input: Bekérünk egy ISBN számot (pl. 0451526538), elválasztójelek nélkül.

2. Lekérés: Az Open Library API-t hívjuk meg. Az alkalmazás a jscmd=data paramétert használja, mert ez adja vissza az egyszerű adatokat (szerző, cím, évszám, oldalszám).

3. Feldolgozás: Lekérdezzük a szükséges adatokat a JSON válaszból. Siker esetén azonnal látható az eredmény. Ha nincs, a 4. lépés kimarad.

4. Mentés: A felhasználó választhat, hogy .json vagy .csv formátumban mentse el az eredményt, vagy nem kér mentést.

# Extra változat: mini katalógus

Hasonlít az előzőre, de most while ciklust is futtat. A program addig fut, amíg a felhasználó nem állítja le 'stop' vagy 'vege' paranccsal.
Itt lehetőség van több ISBN számmal keresni, összeállítva egy katalógust.
# Működés
1. Input: Bekérünk egy ISBN számot, viszont a számokat egyesével kell megadni! Minden szám után Enter gomb, különben a program hibás lesz. Hozzáadáskor visszajelző üzenet jön.

2. Lekérés: Az Open Library API-t hívjuk meg, miután kiválogattuk a szükséges könyveket.

3. Feldolgozás: Lekérdezzük a szükséges adatokat a JSON válaszból, mint az előzőben.

4. Mentés: A felhasználó most is választhat, hogy .json vagy .csv formátumban mentse el az eredményt, vagy nem tesz semmit.
