from os import listdir
from os.path import isfile, join

projectDir = "D:/FER/Diplomski/Isem/Bioinformatika/Konačan projekt/Bioinformatics-LCSkpp-implementation/tests/tested"
onlyfiles = [f for f in listdir(projectDir) if isfile(join(projectDir, f))]

outFile = open("C:/Users/Toni/Desktop/data.txt", "w+")

exp2 = [];
exp3 = [];
exp4 = [];
exp5 = [];
exp6 = [];

for x in onlyfiles:
    lines = x.split("_")
    lang = lines[0];
    compl = lines[3][4:5];
    k = lines[3][0:2]
    num = lines[3][-5:-4];

    file = open(projectDir + "/" + x, "r");
    text = file.readlines()
    if (len(text) > 5):
        tl = text[4].split(":")
        time = tl[4].strip() + ":" + tl[5].strip()
        memory = text[9].split(":")[1].strip()
        if(compl == "2"):
            exp2.append(lang + ":" + k + "," + num + "," + time + "," + memory)
        elif(compl == "3"):
            exp3.append(lang + ":" + k + "," + num + "," + time + "," + memory)
        elif(compl == "4"):
            exp4.append(lang + ":" + k + "," + num + "," + time + "," + memory)
        elif(compl == "5"):
            exp5.append(lang + ":" + k + "," + num + "," + time + "," + memory)
        elif(compl == "6"):
            exp6.append(lang + ":" + k + "," + num + "," + time + "," + memory)

for entry in exp2:
    outFile.write(entry + "\n")

for entry in exp3:
    outFile.write(entry + "\n")

for entry in exp4:
    outFile.write(entry + "\n")

for entry in exp5:
    outFile.write(entry + "\n")

for entry in exp6:
    outFile.write(entry + "\n")

outFile.close()