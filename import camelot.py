import camelot
import pandas as pd
import PyPDF2

# PDF-Datei einlesen und Tabellen extrahieren
tables = camelot.read_pdf("c:\\!\\privat\\Buchungen\\KontoauszugTradeRepublikAndre.pdf", pages="all")

# Erste Tabelle als Beispiel
df = tables[0].df

# Optional: Tabelle in eine Excel-Datei speichern
df.to_excel("extrahierte_tabelle.xlsx", index=False)

# Einlesen der gespeicherten Excel-Datei mit pandas
df_excel = pd.read_excel("extrahierte_tabelle.xlsx")

print(df_excel)
