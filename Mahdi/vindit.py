'''Applicatie voor het beheren van verkopen bij Vind it!'''
import sqlite3

'''Verbind met lokale SQLite-database'''
verbinding = sqlite3.connect("db/vindit.db")
verbinding.row_factory = sqlite3.Row # om kolomnamen te kunnen gebruiken bij het tonen van data
verbinding.autocommit = True
cursor = verbinding.cursor()

menu_opties = (
    "1.  Toon alle verkopen",
    "2.  Toon alle kleding-verkopen",
    "3.  Toon alle boek-verkopen",
    "4.  Toon alle overige verkopen",
    "5.  Nieuwe verkoop toevoegen",
    "6.  Totale opbrengst tonen",
    "7.  Toon alle gebruikte categorieen",
    "8.  Maak de tabel leeg",
    "9.  Maak een nieuwe tabel aan",
    "10. Sorteer de verkopen van hoog naar laag",
    "11. Sorteer de verkopen van laag naar hoog",
    "12. Toon de totale opbrengst per maand",
    "13. Verwijder een verkoop",
    "x.  Afsluiten",
)

while True:
    print("+--------------------------------------------+")
    print("Vindit")
    print()
    print("Maak je keuze:")

    # for-lus = herhaal de print voor iedere optie in de tuple
    for optie in menu_opties:
        print(optie)

    print("+--------------------------------------------+")
    print()

    keuze = input("Wat is je keuze: ")

    if keuze == "1":
        cursor.execute("SELECT * FROM Verkoop")
        resultaat = cursor.fetchall()
        for rij in resultaat:
            print(rij[0], ' - ', rij[1], ' - ', rij[2], 'euro')

    elif keuze == "2":
        cursor.execute("SELECT * FROM Verkoop WHERE categorie = 'kleding'") 
        resultaat = cursor.fetchall()
        for rij in resultaat:
            print(rij[0], " - ", rij[1], " - ", rij[2], "euro")
    
    elif keuze == "3": 
        cursor.execute("SELECT * FROM Verkoop WHERE categorie = 'boeken'") 
        resultaat = cursor.fetchall() 
        for rij in resultaat: 
            print(rij[0], " - ", rij[1], " - ", rij[2], "euro")
    
    elif keuze == "4": 
        cursor.execute(""" SELECT * FROM Verkoop WHERE categorie != 'kleding' AND categorie != 'boeken' """) 
        resultaat = cursor.fetchall()
        for rij in resultaat: 
            print(rij[0], " - ", rij[1], " - ", rij[2], "euro")
    
    elif keuze == "5": 
        verkoopmoment = input("Datum en tijd: ") 
        categorie = input("Categorie: ") 
        opbrengst = input("Opbrengst: ") 
        cursor.execute("INSERT INTO Verkoop (verkoopmoment, categorie, opbrengst) VALUES (?, ?, ?)", (verkoopmoment, categorie, opbrengst)) 
        print("Verkoop toegevoegd!")

    elif keuze == "6":
        cursor.execute("SELECT SUM(opbrengst) AS totale_opbrengst FROM Verkoop")
        resultaat = cursor.fetchone()  
        print("Totale opbrengst:", resultaat["totale_opbrengst"], "euro")
    
    elif keuze == "7":
        cursor.execute("SELECT DISTINCT categorie FROM Verkoop")
        resultaat = cursor.fetchall()
        print("Alle gebruikte categorien: ")
        for rij in resultaat:
            print(rij[0])

    elif keuze == "8":
        cursor.execute("DELETE FROM Verkoop")
        print("Tabel is leeg gemaakt.")

    elif keuze == "9":
        tabelnaam = input("Geef een naam voor de nieuwe tabel: ")
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tabelnaam}(
            verkoopmoment DATETIME PRIMARY KEY,
            categorie TEXT NOT NULL,
            opbrengst FLOAT NOT NULL)""")
        print("Nieuwe tabel toegevoegd: ", tabelnaam)

    elif keuze == "10":
        cursor.execute("SELECT * FROM Verkoop ORDER BY opbrengst DESC")
        resultaat = cursor.fetchall()
        for rij in resultaat:
            print(rij[0], " - ", rij[1], " - ", rij[2], "euro")

    elif keuze == "11":
        cursor.execute("SELECT * FROM Verkoop ORDER BY opbrengst ASC")
        resultaat = cursor.fetchall()
        for rij in resultaat:
            print(rij[0], " - ", rij[1], " - ", rij[2], "euro")

    elif keuze == "12":
        cursor.execute("""
        SELECT strftime('%Y-%m', verkoopmoment) AS maand, 
        SUM(opbrengst) AS totale_opbrengst FROM Verkoop
        GROUP BY strftime('%Y-%m', verkoopmoment) ORDER BY maand ASC """)
        resultaat = cursor.fetchall()
        for rij in resultaat:
            print(rij["maand"], " - €", rij["totale_opbrengst"])

    elif keuze == "13":
        while True:
            verkoopmoment = input("Wat is de datum en de tijd van de verkoop die u wilt verwijderen: ")
            if verkoopmoment.lower() == "x":
                break

            cursor.execute("DELETE FROM Verkoop WHERE verkoopmoment = ?", (verkoopmoment,)) # (verkoopmoment,) = geef verkoopmoment als één waarde mee
            if cursor.rowcount > 0:
                print("Verkoop verwijderd!")
                break
            else:
                print("Geen verkoop gevonden met deze datum en tijd. Probeer het op nieuw.")
                print("Vul x in om terug te gaan naar het menu.")
                print()

    elif keuze.lower() == "x":
        print("Tot ziens!")
        quit()

    else: 
        print("Verkeerde input.")

