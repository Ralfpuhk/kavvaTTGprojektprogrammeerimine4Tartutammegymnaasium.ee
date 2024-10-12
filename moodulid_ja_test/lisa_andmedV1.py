from spire.xls import *
from spire.xls.common import *


def lisa(row, input_kuupaev, input_kell, input_sonum, user):
    
    assignment = [input_kuupaev, input_kell, input_sonum]
    column = ["A", "B", "C"]
    for num in column:
        cell = ("%s%s" % (num, row))
        sheet.Range[cell].Text = assignment[column.index(num)]
        
    i = row + 1
    path = ("info/"+ user_ID +".xlsx")
    # Save to a .xlsx file
    wb.SaveToFile(path, FileFormat.Version2016)
    
    return i

i=1
# Create a Workbook object
wb = Workbook()
# Remove default worksheets
wb.Worksheets.Clear()
# Add a worksheet and name it "Employee"
sheet = wb.Worksheets.Add("kalender")
user_ID = input("Input your custom ID: ")

while True:
    sonum = input("Input message: ")
    kuupaev = input("Input date (d/dd.m/mm.yyyy): ")#kontrolli hiljem kuida need vormistatud
    kell = input("Input time(x/xx:y/yy): ")
    i = lisa(i, kuupaev, kell, sonum, user_ID)



#i = lisa(i, kuupaev2, kell2, sonum2, user_ID)





