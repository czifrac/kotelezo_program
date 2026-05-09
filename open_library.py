import requests
import json
import csv


def konyv_kereso():
    print("--- Open Library Könyvkereső ---")
    isbn = input("Add meg a könyv ISBN számát (pl. 0451526538): ").strip()


    bibkey = f"ISBN:{isbn}"
    url = f"https://openlibrary.org/api/books?bibkeys={bibkey}&format=json&jscmd=data"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if not data:
            print("Sajnos nem található könyv ezzel az ISBN számmal.")
            return


        book_info = data[bibkey]
        cim = book_info.get("title", "Nincs cím")


        szerzok_listaja = book_info.get("authors", [])
        szerzo = ", ".join([s["name"] for s in szerzok_listaja]) if szerzok_listaja else "Ismeretlen szerző"

        kiadas_eve = book_info.get("publish_date", "Nincs adat")
        oldalszam = book_info.get("number_of_pages", "Nincs adat")

        print("\n--- Talált könyv adatai ---")
        print(f"Cím: {cim}")
        print(f"Szerző: {szerzo}")
        print(f"Kiadás éve: {kiadas_eve}")
        print(f"Oldalszám: {oldalszam}")


        mentesi_adatok = {
            "isbn": isbn,
            "cim": cim,
            "szerzo": szerzo,
            "kiadas_eve": kiadas_eve
        }

        valasztas = input("\nMilyen formátumban mentsük? (json/csv/nincs): ").lower()

        if valasztas == "json":
            fajlnev = f"konyv_{isbn}.json"
            with open(fajlnev, "w", encoding="utf-8") as f:
                json.dump(mentesi_adatok, f, ensure_ascii=False, indent=4)
            print(f"Sikeresen mentve: {fajlnev}")

        elif valasztas == "csv":
            fajlnev = f"konyv_{isbn}.csv"
            with open(fajlnev, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=mentesi_adatok.keys())
                writer.writeheader()
                writer.writerow(mentesi_adatok)
            print(f"Sikeresen mentve: {fajlnev}")
        else:
            print("A mentés elmaradt.")

    except requests.exceptions.RequestException as e:
        print(f"Hiba történt a lekérés során: {e}")


if __name__ == "__main__":
    konyv_kereso()