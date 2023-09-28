import csv

def writeToFile(file, kolom1, kolom2, kolom3):
    f = open(file,'a', encoding='UTF8', newline="")
    writer = csv.writer(f)
    data = "{0};{1};{2}".format(kolom1, kolom2, kolom3)
    writer.writerow([data])
    f.close()
    
writeToFile("test.csv", 2,3,4)