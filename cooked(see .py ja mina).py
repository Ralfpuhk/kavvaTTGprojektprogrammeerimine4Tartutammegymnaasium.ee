from spire.xls import *
from spire.xls.common import *

def lisa_kuupaev(x):
    a = 1
    cell_kuupaev = str("A" + str(a)) # see ei toota!!
    a =+ 1 #(see tuleb siis kui keegi lisab midagi tabelisse ja funktsioon aktiveerub)
    sheet.Range[cell_kuupaev].Text = x
    
# Create a Workbook object
wb = Workbook()

# Remove default worksheets
wb.Worksheets.Clear()

# Add a worksheet and name it "Employee"
sheet = wb.Worksheets.Add("kalender")

kuupaev = "1.10.2024" #Rando motleb valja kuida kasutajaliidesest siia saada
sonum = "noor piff, kooli!" #Rando motleb valja kuida kasutajaliidesest siia saada
kell = "12.55" #Rando motleb valja kuida kasutajaliidesest siia saada

lisa_kuupaev(kuupaev)




sheet.Rows[0].RowHeight = 30


# Save to a .xlsx file
wb.SaveToFile("info/tabel.xlsx", FileFormat.Version2016)