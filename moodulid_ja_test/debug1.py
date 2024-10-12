def time_convert(date1):
    lista = []
    if "/" in date1:
        lista = date1.split("/")
        separator = "."
    elif ":" in date1:
        lista = date1.split(":")
        separator = ":"
        
    lias = []
    for pp in lista:
        date = pp.lstrip("0")
        lias.append(date)
    string = separator.join(lias)
    return(string)
    #print(string)

t = "Ters \n @Leivaviil 02/10/2024 01:01 \n"
print(t)
jada = t.split("\n")
sonum = jada[0]
manydates = (jada[1].strip(" ")).split(" ")
del manydates[0]
print(manydates)
uusjada = []
for liige in manydates:
    uusjada.append(time_convert(liige))
print(uusjada)