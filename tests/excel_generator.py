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
    extra = 2 + eksp*18;
    base = cnt%60;

    extra += base % 15 // 5;
    row = base%15 + extra;
    if(base<15):
        colM = 7;
        colT = 8;
    elif(base<30):
        colM = 4;
        colT = 5;
    elif(base<45):
        colM = 10;
        colT = 11;
    else:
        colM = 13;
        colT = 14;
    cnt += 1;
    sheet.write(row, colM, mem)
    sheet.write(row, colT, time)
wb.save(outputWB);