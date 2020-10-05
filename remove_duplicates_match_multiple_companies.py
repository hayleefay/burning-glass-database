import csv
import math

ids = set()
years = ['2007', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017',
         '2018', '2019', '2020']

multiple_df = pd.read_csv("/export/projects2/rsadun_burning_glass_project/burning-glass-database/multiple_matches.csv")
multiples_set = set(multiple_df['clean1'].tolist() + multiple_df['clean2'].tolist() + multiple_df['clean3'].tolist() + multiple_df['clean4'].tolist())


for year in years:
    csvfilename = '/export/projects2/rsadun_burning_glass_project/burning-glass-database/rr_data/rr_burning_glass_' + year + '.csv'
    csvfilename_out = '/export/projects2/rsadun_burning_glass_project/burning-glass-database/rr_burning_glass_' + year + '.csv'
    # stream in all job postings
    with open(csvfilename, 'r', newline='') as csvfile:
        print("opening")
        csvreader = csv.reader(csvfile)
        with open(csvfilename_out, 'w', quoting=csv.QUOTE_MINIMAL) as csvfile_out:
            csvwriter = csv.writer(csvfile_out)

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

                    rr1 = row[-5] == None
                    rr2 = row[-4] == None
                    rr3 = row[-3] == None
                    rr4 = row[-2] == None
                    rr5 = row[-1] == None

                    print("-------------------------------")

                    multiple_company_name = None

                    # check if the company is a multiple
                    if rr1:
                        if row[-5] in multiples_set:
                            multiple_company_name = rr[-5]
                            if isinstance(multiple_company_name, str):
                                print("-5")
                    if rr2:
                        if row[-4] in multiples_set: 
                            multiple_company_name = rr[-4]
                            if isinstance(multiple_company_name, str):
                                print("-4")
                    if rr3:
                        if row[-3] in multiples_set:
                            multiple_company_name = rr[-3]
                            if isinstance(multiple_company_name, str):
                                print("-3")
                    if rr4:
                        if row[-2] in multiples_set:
                            multiple_company_name = rr[-2]
                            if isinstance(multiple_company_name, str):
                                print("-2")
                    if r5:
                        if row[-1] in multiples_set:
                            multiple_company_name = rr[-2]
                            if isinstance(multiple_company_name, str):
                                print("-1")
                    
                    print(multiple_company_name)
                    
                    if isinstance(multiple_company_name, str):
                        df_match = multiple_df[multiple_df.isin([multiple_company_name]).any(axis=1)]
                        if df_match.shape[1] > 1:
                            print("Shape larger than 1!")
                            import pdb; pdb.set_trace()
                        else:
                            insert_companies = [df_match['clean1'].iloc[0], df_match['clean2'].iloc[0], df_match['clean3'].iloc[0], df_match['clean4'].iloc[0]]
                            insert_companies = [x if not math.isnan(x) for x in insert_companies]
                            insert_companies = [x if x!=multiple_company_name for x in insert_companies]
                            print(len(insert_companies))

                            for company in insert_companies:
                                if rr1 is False:
                                    row[-5] = company
                                    rr1 = True
                                elif rr2 is False
                                    row[-4] = company
                                    rr2 = True
                                elif rr3 is False
                                    row[-3] = company
                                    rr3 = True
                                elif rr4 is False
                                    row[-2] = company
                                    rr4 = True
                                elif rr5 is False
                                    row[-1] = company
                                    rr5 = True
                                else:
                                    print("All True!")
                                    import pdb; pdb.set_trace()


                    csvwriter.writerow(row)
            