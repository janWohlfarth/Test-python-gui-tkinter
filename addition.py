import tkinter as tk
from tkinter import messagebox
import csv
import os

# Funktion zum Berechnen der Summe und Speichern in CSV
def berechne_und_speichere():
    try:
        zahl1 = float(entry1.get())
        zahl2 = float(entry2.get())
        summe = zahl1 + zahl2

        # Datei erstellen, falls sie nicht existiert, und Kopfzeile hinzufügen
        dateiname = "ergebnisse.csv"
        datei_existiert = os.path.exists(dateiname)

        with open(dateiname, mode="a", newline="") as file:
            writer = csv.writer(file)
            if not datei_existiert:  # Kopfzeile hinzufügen
                writer.writerow(["Zahl 1", "Zahl 2", "Summe"])
            writer.writerow([zahl1, zahl2, summe])

        # Ergebnis anzeigen
        messagebox.showinfo("Ergebnis", f"Die Summe ist: {summe}")
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Fehler", "Bitte geben Sie gültige Zahlen ein.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Addition mit Tkinter")

# Fenstergröße festlegen
root.geometry("400x150")  # Breite x Höhe

# Grid-Spalten ausdehnen, um Inhalte zu zentrieren
root.grid_columnconfigure(0, weight=1)  # Linke Spalte
root.grid_columnconfigure(1, weight=1)  # Rechte Spalte
root.grid_columnconfigure(2, weight=1)  # Zusätzlicher Platz

# Labels und Eingabefelder
label1 = tk.Label(root, text="Zahl 1:", font=("Arial", 10))
label1.grid(row=0, column=0, padx=5, pady=1, sticky="e")

entry1 = tk.Entry(root, font=("Arial", 10), width=10)
entry1.grid(row=0, column=1, padx=5, pady=1)

label2 = tk.Label(root, text="Zahl 2:", font=("Arial", 10))
label2.grid(row=1, column=0, padx=5, pady=1, sticky="e")

entry2 = tk.Entry(root, font=("Arial", 10), width=10)
entry2.grid(row=1, column=1, padx=5, pady=1)

# Frame für den Button
button_frame = tk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=3, pady=20)

# Button mittig platzieren
button = tk.Button(button_frame, text="Berechnen & Speichern", font=("Arial", 10), command=berechne_und_speichere)
button.pack()  # Pack für Zentrierung verwenden

# Hauptschleife starten
root.mainloop()
