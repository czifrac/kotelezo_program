import requests
import json
import csv


def adat_lekeres(isbn):
    """Lekéri egyetlen könyv adatait az Open Library API-ból."""
    bibkey = f"ISBN:{isbn}"
    url = f"https://openlibrary.org/api/books?bibkeys={bibkey}&format=json&jscmd=data"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not data:
            return None

        book_info = data[bibkey]
        szerzok_listaja = book_info.get("authors", [])
        szerzo = ", ".join([s["name"] for s in szerzok_listaja]) if szerzok_listaja else "Ismeretlen szerző"

        return {
            "isbn": isbn,
            "cim": book_info.get("title", "Nincs cím"),
            "szerzo": szerzo,
            "kiadas_eve": book_info.get("publish_date", "Nincs adat")
        }
    except requests.exceptions.RequestException as e:
        print(f"Hálózati hiba az ISBN({isbn}) lekérésekor: {e}")
        return None


def katalogus_keszito():
    print("--- 📚 Saját Mini Könyvkatalógus Készítő ---")
    print("Írd be a könyvek ISBN számát egyenként.")
    print("Ha befejezted a listázást, írd be, hogy 'stop' vagy 'vege'.\n")

    katalogus = []

    while True:
        felhasznaloi_bemenet = input("ISBN szám (vagy 'stop'): ").strip().lower()

        if felhasznaloi_bemenet in ['stop', 'vege']:
            break

        if not felhasznaloi_bemenet:
            continue

        print("Adatok lekérése...")
        konyv_adat = adat_lekeres(felhasznaloi_bemenet)

        if konyv_adat:
            katalogus.append(konyv_adat)
            print(f"✅ Hozzáadva a katalógushoz: {konyv_adat['cim']} ({konyv_adat['szerzo']})\n")
        else:
            print("❌ Sajnos nem található adat, vagy hibás az ISBN.\n")


    if katalogus:
        print(f"\n--- Összegzés ---")
        print(f"Összesen {len(katalogus)} könyv került a katalógusba.")
        valasztas = input("Milyen formátumban mentsük a teljes katalógust? (json/csv/nincs): ").lower()

        if valasztas == "json":
            with open("sajat_katalogus.json", "w", encoding="utf-8") as f:

                json.dump(katalogus, f, ensure_ascii=False, indent=4)
            print("Sikeresen mentve a 'sajat_katalogus.json' fájlba.")

        elif valasztas == "csv":
            with open("sajat_katalogus.csv", "w", newline="", encoding="utf-8") as f:

                mezo_nevek = katalogus[0].keys()
                writer = csv.DictWriter(f, fieldnames=mezo_nevek)
                writer.writeheader()
                writer.writerows(katalogus)
            print("Sikeresen mentve a 'sajat_katalogus.csv' fájlba.")
        else:
            print("A mentés elmaradt. A katalógus tartalma elveszett.")
    else:
        print("\nA katalógus üres maradt, nincs mit menteni.")


if __name__ == "__main__":
    katalogus_keszito()