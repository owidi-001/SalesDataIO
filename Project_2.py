import csv

#Problem 1
with open('POS.csv', newline='') as csvPOS:
    my_reader = csv.reader(csvPOS, delimiter=',')

    quaters = []
    northAmericanHoliday=[]
    months=[]
    flag = 0 

    for row in my_reader:
        if flag == 0:     
            flag = 1
        else:             
            if row[16] not in quaters:
                quaters.append(row[16])
            if row[18] not in months:
                months.append(row[18])
            if row[24] not in northAmericanHoliday:
                northAmericanHoliday.append(row[24])

    print(quaters)
    print(northAmericanHoliday)
    print(months)
    

with open('AverageSales.csv', 'w', newline='') as csvWrite:
    writer=csv.writer(csvWrite)

    header1=['Quater','Average sales']
    header2=['Holiday','Average sales']
    header3=['Month','Average sales']

    writer.writerow(header1)
    for quater in quaters[1:]:
        flag = 0
        cnt = 0
        total_sum=0
        with open('POS.csv', newline='') as csvPOS:
            my_reader = csv.reader(csvPOS, delimiter=',')

            for row in my_reader:
                if flag == 0:
                    flag = 1
                else:
                    if row[16] == quater:
                        cnt+=1
                        total_sum += float(row[11])

            avg_sales=total_sum/cnt

        row1=[quater,avg_sales]
        writer.writerow(row1)
    writer.writerow([])
    
    writer.writerow(header2)
    for holiday in northAmericanHoliday[1:]:
        flag = 0
        cnt = 0
        total_sum=0
        with open('POS.csv', newline='') as csvPOS:
            my_reader = csv.reader(csvPOS, delimiter=',')

            for row in my_reader:
                if flag == 0:
                    flag = 1
                else:
                    if row[24] == holiday:
                        cnt+=1
                        total_sum += float(row[11])

            avg_sales=total_sum/cnt

        row1=[holiday,avg_sales]
        writer.writerow(row1)
    writer.writerow([])
    
    writer.writerow(header3)
    for month in months[1:]:
        flag = 0
        cnt = 0
        total_sum=0
        with open('POS.csv', newline='') as csvPOS:
            my_reader = csv.reader(csvPOS, delimiter=',')

            for row in my_reader:
                if flag == 0:
                    flag = 1
                else:
                    if row[18] == month:
                        cnt+=1
                        total_sum += float(row[11])

            avg_sales=total_sum/cnt

        row1=[month,avg_sales]
        writer.writerow(row1)
        