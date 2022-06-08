from filmData import film
import openpyxl
workbook = openpyxl.load_workbook("FilmExel/247PhimLe.xlsx")
sheet1 = workbook.active
index = 1

for name in film :
    sheet1.cell(1,index,name)
    index=index+1
workbook.save("FilmExel/247PhimLe.xlsx")



