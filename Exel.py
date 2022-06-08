import openpyxl
import pprint
workbook = openpyxl.load_workbook("censuspopdata.xlsx")
sheet1 = workbook.active

countryData = {}
for row in range(2,sheet1.max_row+1) : 
    
    tracts = sheet1['A'+str(row)].value
    state = sheet1['B'+str(row)].value
    country = sheet1['C'+str(row)].value
    pop = sheet1['D'+str(row)].value
    countryData.setdefault(state,{})
    countryData[state].setdefault(country,{"tracts" : '0', 'pop' : '0'})
    (countryData[state])[country]['pop'] = pop
    (countryData[state])[country]['tracts'] = tracts


with open("temp/country.py","w") as f :
    f.write(pprint.pformat(countryData))
