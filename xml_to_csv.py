import zipfile
import lxml.etree as ET
import os
import pandas as pd
import csv

path = '/Users/hayleeham/Documents/burning-glass-database/data/'
years = ['2018/', '2018_ongoing/', '2019/', '2020/']
fields = set(['CanonEmployer', 'JobURL', 'CanonYearsOfExperienceLevel', 'ConsolidatedONET', 
             'MaxDegreeLevel', 'IsDuplicate', 'CanonOtherDegrees', 'CanonRequiredDegrees', 
             'Telephone', 'JobText', 'MinDegreeLevel', 'CanonPostalCode', 'StandardMajor', 
             'Latitude', 'CanonCounty', 'BGTOcc', 'CanonCity', 'JobDomain', 'JobID', 'LMA', 
             'Email', 'CanonPreferredDegrees', 'Language', 'Source', 
             'InternshipFlag', 'PostingHTML', 'IsDuplicateOf', 'CanonState', 'ConsolidatedTitle', 
             'DivisionCode', 'Longitude', 'ConsolidatedInferredNAICS', 
             'JobDate', 'CanonJobTitle', 'MinAnnualSalary', 'CanonCountry',
             'CanonSkillClusters', 'MaxHourlySalary', 'YearsOfExperience', 'CanonJobHours', 
             'CanonMaximumDegree', 'MaxExperience', 'MSA', 'CanonYearsOfExperienceCanonLevel', 
             'ConsolidatedDegreeLevels', 'CanonIntermediary', 'BGTSubOcc', 'CIPCode', 
             'JobReferenceID', 'MinHourlySalary', 'CleanJobTitle', 'MaxAnnualSalary', 
             'CanonJobType', 'MinExperience', 'CanonMinimumDegree'])
fields_list = ["JobID", "CleanJobTitle", "JobDomain", "CanonCity", "CanonCountry", "CanonState", 
               "JobDate", "JobText", "JobURL", "PostingHTML", "Source", "JobReferenceID", 
               "Email", "CanonEmployer", "Latitude", "Longitude", "CanonIntermediary", 
               "Telephone", "CanonJobTitle", "CanonCounty", "DivisionCode", "MSA", "LMA", 
               "InternshipFlag", "ConsolidatedONET", "CanonSkillClusters", 
               "IsDuplicate", "IsDuplicateOf", "CanonMaximumDegree", "CanonMinimumDegree", 
               "CanonOtherDegrees", "CanonPreferredDegrees", "CanonRequiredDegrees", 
               "CIPCode", "StandardMajor", "MaxExperience", "MinExperience", 
               "ConsolidatedInferredNAICS", "BGTOcc", "MaxAnnualSalary", "MaxHourlySalary", 
               "MinAnnualSalary", "MinHourlySalary", "YearsOfExperience", "CanonJobHours", 
               "CanonJobType", "CanonPostalCode", "CanonYearsOfExperienceCanonLevel", 
               "CanonYearsOfExperienceLevel", "ConsolidatedTitle", "Language", "BGTSubOcc", 
               "ConsolidatedDegreeLevels", "MaxDegreeLevel", "MinDegreeLevel", "rr_company_1", 
               "rr_company_2", "rr_company_3", "rr_company_4", "rr_company_5"]

# read in all of the matches and group by
df1 = pd.read_csv("/Users/hayleeham/Documents/burning-glass-database/matches/matches_rr2_2007_present_MZ.csv")
df2 = pd.read_csv("/Users/hayleeham/Documents/burning-glass-database/matches/matches_rr1_2018_present_MZ.csv")
df3 = pd.read_csv("/Users/hayleeham/Documents/burning-glass-database/matches/matches_rr1_2007_2017.csv")
df_master = df1.append(df2)
df_master = df_master.append(df3)
dfg = df_master.groupby('company_2').agg(list)
companies_set = set(dfg.index.tolist())
print('All matches read in', flush=True)


def dict_to_csv_row(job_dict, csvwriter, csvfile):
    row = []
    if 'CanonEmployer' in job_dict and job_dict['CanonEmployer'] in companies_set:
        for field in fields_list:
            if field in job_dict:
                row.append(job_dict[field])
            else:
                row.append(None)
        
        for company in dfg.loc[job_dict['CanonEmployer']]['company_1']:
            row.append(company)
        
        csvwriter.writerow(row)
        csvfile.flush()
    
    else:
        pass



csvfilename = "rr_burning_glass.csv"
with open(csvfilename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(fields_list)
    csvfile.flush()
    print('Header written', flush=True)

    for year in years:
        print(year)
        for filename in os.listdir(path + year):
            print(filename)
            zf = zipfile.ZipFile(path + year + filename)
            xml_filename = filename[:-3] + 'xml'

            job_dict = {}
            job_count = 0
            for event, elem in ET.iterparse(zf.open(xml_filename), events=("end",)):
                if elem.tag == 'JobID':
                    if job_count == 0:
                        job_dict['JobID'] = elem.text
                        job_count += 1
                    else:
                        # write out dictionary to csv
                        dict_to_csv_row(job_dict, csvwriter, csvfile)
                        job_count += 1
                        job_dict = {}
                        job_dict['JobID'] = elem.text
                elif elem.tag in fields:
                    job_dict[elem.tag] = elem.text

                elem.clear()