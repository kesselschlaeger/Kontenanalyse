import tabula
import pandas as pd

# PDF-Datei einlesen und Tabellen extrahieren
pdf_file = "c:\\!\\privat\\Buchungen\\KontoauszugTradeRepublikAndre.pdf"
tables = tabula.read_pdf(pdf_file, pages="all", multiple_tables=True)

# Jede Tabelle in einer separaten Excel-Seite speichern
#excel_file = "ausgabe.xlsx"
#with pd.ExcelWriter(excel_file) as writer:
    #for i, table in enumerate(tables):
#        table.to_excel(writer, sheet_name=f"Tabelle_{i+1}", index=False)

#print(f"Tabellen erfolgreich in {excel_file} gespeichert.")
