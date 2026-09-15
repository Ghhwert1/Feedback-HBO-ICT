'''Applicatie voor het beheren van verkopen bij Vind it!'''
import sqlite3

data = []
'''Verbind met lokale SQLite-database'''
verbinding = sqlite3.connect("/home/student/ictjou/2026P1-ICTJOU-2183836/niveau1/oefen-vindit/db/vindit.db")
verbinding.row_factory = sqlite3.Row # om kolomnamen te kunnen gebruiken bij het tonen van data
verbinding.autocommit = True
cursor = verbinding.cursor()


while True:
    print("""+----------------------------------------------+
| VIND IT! VERKOOPMANAGER                      |
|                                              |
| Maak je keuze:                               |
| 1. Toon alle verkopen                        |
| 2. Toon alle kleding-verkopen                |
| 3. Toon alle boeken-verkopen                 |
| 4. Toon alle overige verkopen                |
| 5. Nieuwe verkoop toevoegen                  |
| 6. Totale opbrengst tonen                    |
| 7. Toon alle gebruikte categorieën           |
| X. Afsluiten                                 |
+----------------------------------------------+
""")
    gebr_input = input("Kies wat je wilt doen: ")
    if gebr_input == "1":
        cursor.execute("SELECT * FROM Verkoop")
        data = cursor.fetchall()
        print("+------------------------------------------+")
        for rows in data:
            print(' - '.join(str(item) for item in rows))
        input("Enter om verder te gaan... ")
    elif gebr_input == "7":
        cursor.execute("SELECT DISTINCT categorie FROM Verkoop")
        data = cursor.fetchall()
        print("+------------+")
        for rows in data:
            print(rows[0])
        input("Enter om verder te gaan... ")
    else: gebr_input == "x" or "X":
        print("Verkeerde input.")
