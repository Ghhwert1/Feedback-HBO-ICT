'''Applicatie voor het beheren van verkopen bij Vind it!'''
import sqlite3

'''Verbind met lokale SQLite-database'''
verbinding = sqlite3.connect("/home/student/ictjou/2026P1-ICTJOU-2189442/niveau1/oefen-vindit/db/vindit.db")
verbinding.row_factory = sqlite3.Row
verbinding.autocommit = True
cursor = verbinding.cursor()

x_naar_een: dict = {
    "x": 8
    , "X": 8
}

def print_table(resultaten):
    if not resultaten:
        print("Geen resultaten.")
        return
    
    kolom_namen = resultaten[0].keys()
    print(" - ".join(kolom_namen))
    print("-" * 40)

    for rij in resultaten:
        print(" - ".join(str(rij[kolom]) for kolom in kolom_namen))

def keuze_verwerker(keuze: int) -> bool:
    match keuze:
        case 1:
            cursor.execute("SELECT verkoopmoment, categorie, PRINTF('%.2f euro', opbrengst / 100.0) AS 'opbrengst' FROM Verkoop")
            resultaten = cursor.fetchall()
            print_table(resultaten)
            return True
        case 2:
            cursor.execute("SELECT verkoopmoment, categorie, PRINTF('%.2f euro', opbrengst / 100.0) AS 'opbrengst' FROM Verkoop WHERE categorie LIKE 'kleding'")
            resultaten = cursor.fetchall()
            print_table(resultaten)
            return True
        case 3:
            cursor.execute("SELECT verkoopmoment, categorie, PRINTF('%.2f euro', opbrengst / 100.0) AS 'opbrengst' FROM Verkoop WHERE categorie LIKE 'boeken'")
            resultaten = cursor.fetchall()
            print_table(resultaten)
            return True
        case 4:
            cursor.execute("SELECT verkoopmoment, categorie, PRINTF('%.2f euro', opbrengst / 100.0) AS 'opbrengst' FROM Verkoop WHERE categorie LIKE 'overige'")
            resultaten = cursor.fetchall()
            print_table(resultaten)
            return True
        case 5:
            verkoopmoment: str = input("Verkoopmoment: ")
            categorie: str = input("Categorie: ")
            opbrengst: str = input("Opbrengst: ")
            cursor.execute("INSERT INTO Verkoop (verkoopmoment, categorie, opbrengst) VALUES (?, ?, ?)",(verkoopmoment, categorie, opbrengst))
            cursor.execute("SELECT verkoopmoment, categorie, PRINTF('%.2f euro', opbrengst / 100.0) AS 'opbrengst' FROM Verkoop ORDER BY verkoopmoment LIMIT 5")
            resultaten = cursor.fetchall()
            print_table(resultaten)
            return True
        case 6:
            cursor.execute("SELECT SUM(opbrengst) AS totale_opbrengst FROM Verkoop")
            resultaten = cursor.fetchall()
            print_table(resultaten)
            return True
        case 7:
            cursor.execute("SELECT verkoopmoment, categorie, PRINTF('%.2f euro', opbrengst / 100.0) AS 'opbrengst' FROM Verkoop GROUP BY categorie")
            resultaten = cursor.fetchall()
            print_table(resultaten)
            return True
        case 8:
            return False
        case _:
            return True


print("+-------------------------------------+")
print("| VIND IT! VERKOOPMANAGER             |")
print("|                                     |")
print("| Maak je keuze:                      |")
print("| 1. Toon alle verkopen               |")
print("| 2. Toon alle kleding-verkopen       |")
print("| 3. Toon alle boeken-verkopen        |")
print("| 4. Toon alle overige-verkopen       |")
print("| 5. Nieuwe verkoop toevoegen         |")
print("| 6. Totale opbrengst tonen           |")
print("| 7. Toon alle gebruikte categorieen  |")
print("| X. Afsluiten                        |")
print("+-------------------------------------+")

running: bool = True
while running:
    user_input_before: str = input("> ")

    if user_input_before in x_naar_een:
        user_input_after: int = x_naar_een[user_input_before]
        running = keuze_verwerker(user_input_after)

    elif user_input_before.isdigit():
        user_input_after = int(user_input_before)
        if 1 <= user_input_after <= 7:
            running = keuze_verwerker(user_input_after)
        else:
            print("Dit is geen optie, probeer opnieuw.")
    else:
        print("Dit is geen optie, probeer opnieuw.")
    print("+-------------------------------------+")
