import csv

#kolommen is een tuple
def writeTupleToFile(file, kolommen):
    f = open(file,'a', encoding='UTF8', newline="")
    writer = csv.writer(f)
    data = ""
    for kolom in kolommen:
        data = data + "{0};".format(kolom)
    writer.writerow([data])
    f.close()
    
writeTupleToFile("test.csv", (2,3,4,"rev", "21-08-2022") )