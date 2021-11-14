import csv

#Problem 1
with open('POS.csv', newline='') as csvPOS:
    my_reader = csv.reader(csvPOS, delimiter=',')

    col1 = []
    class_name=[]
    flag = 0    
    for row in my_reader:
        if flag == 0:     
            flag = 1
        else:             
            if row[3] not in col1:
                col1.append(row[3])
            if row[4] not in class_name:
                class_name.append(row[4])
    
with open('BrandAnalysis.csv', 'w', newline='') as csvWrite:
    writer = csv.DictWriter(csvWrite, fieldnames = ["BrandName", "ClassName", "Aggregate Sales Amount"])
    writer.writeheader()
    writer=csv.writer(csvWrite)

    for brand in col1[1:]:
        flag = 0
        cnt = 0
        sum_regular=0
        sum_economy=0
        with open('POS.csv', newline='') as csvPOS:
            my_reader = csv.reader(csvPOS, delimiter=',')

            for row in my_reader:
                if flag == 0:
                    flag = 1
                else:
                    if row[3] == brand and row[4]==class_name[1]:
                        sum_regular += float(row[11])
                    elif row[3]==brand and row[4]==class_name[2]:
                        sum_economy += float(row[11])

        row1=[brand,class_name[1],sum_regular]
        row2=[' ',class_name[2],sum_economy]
        writer.writerow(row1)
        writer.writerow(row2)