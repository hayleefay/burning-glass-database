import csv

ids = set()
years = ['2007', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017',
         '2018', '2018_ongoing', '2019', '2020']

for year in years:
    csvfilename = '/export/projects2/rsadun_burning_glass_project/burning-glass-database/rr_burning_glass_' + year + '.csv'
    # stream in all job postings
    with open(csvfilename, 'r', newline='') as csvfile:
        print("opening")
        csvreader = csv.reader(csvfile)

        count = 0
        for row in csvreader:
            if count == 0:
                count += 1
                continue

            fprint = row[0] + row[1]
            if fprint in ids:
                print(year, row[0])
            else:
                ids.add(fprint)