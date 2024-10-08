from spire.xls import *
from spire.xls.common import *


def lisa(input_kuupaev, input_kell, input_sonum, user):
    
    assignment = [row, input_kuupaev, input_kell, input_sonum]
    column = ["A", "B", "C"]
    for num in column:
        cell = ("%s%s" % (num, row))
        sheet.Range[cell].Text = assignment[column.index(num)]
        
    path = ("info/"+ user_ID +".xlsx")
    # Save to a .xlsx file
    wb.SaveToFile(path, FileFormat.Version2016)
    i =+ 1
    return i


file_list = []

for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
            
        file_amount += 1
        file_list.append(os.path.basename(path).split('/')[-1])

# Create a Workbook object
wb = Workbook()
# Remove default worksheets
wb.Workaheets.Clear()
# Add a worksheet and name it "Employee"
sheet = wb.Worksheets.Add("kalender")

user_ID = input("Input your custom ID: ")
if (user_ID) + ".xlsx" not in file_list:
    i=1
    lisa(".",".",".")
else:
    df = pd.read_excel(os.path.join(dir_path, (user_ID) + ".xlsx"), header=None)  # Read without headers to get raw data
        
        values = df.values.flatten()
        num_cols = 3
        matrix = values.reshape(-1, num_cols).tolist()
        #print(matrix)
        for info in matrix:
            
            #lll = 1
        
            if info[1] == (".",".","."):
                i = matrix.index(info)
print(i)

    
    

while True:
    sonum = input("Input message: ")
    kuupaev = input("Input date (d/dd.m/mm.yyyy): ")#kontrolli hiljem kuida need vormistatud
    kell = input("Input time(x/xx:y/yy): ")
    i = lisa(i, kuupaev, kell, sonum, user_ID)



#i = lisa(i, kuupaev2, kell2, sonum2, user_ID)




