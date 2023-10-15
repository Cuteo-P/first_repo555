import tabula
file = "police.pdf"
fileRead = tabula.read_pdf(file)
print(fileRead)
tabula.convert_into(file, "police.csv")
print("Successful")