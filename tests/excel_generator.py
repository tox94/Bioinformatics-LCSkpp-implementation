from xlrd import open_workbook
from xlutils.copy import copy

projectDir = "C:/Users/Toni/Desktop"
inputFile = "data.txt"
inputWB = "C:/Users/Toni/Desktop/rezultati.xls"
outputWB = "C:/Users/Toni/Desktop/rezultati2.xls"

file = open(projectDir + "/" + inputFile, "r");
book = open_workbook(inputWB)

wb = copy(book)
sheet = wb.get_sheet(0)

list = file.readlines()
cnt = 0;
for x in list:
    pod = x.split(",");
    time = pod[2]
    mem = pod[3]
	
    eksp = cnt//60;
    extra = 2 + eksp*15;
    base = cnt%60;

    row = base%15 + extra;
	
    if(base<15):
        colM = 5;
        colT = 6;
    elif(base<30):
        colM = 3;
        colT = 4;
    elif(base<45):
        colM = 7;
        colT = 8;
    else:
        colM = 9;
        colT = 10;
		
    cnt += 1;
	
    sheet.write(row, colM, mem)
    sheet.write(row, colT, time)
	
wb.save(outputWB);