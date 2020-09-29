import zipfile
import lxml.etree as ET
import os
import pandas as pd

path = '/Users/hayleeham/Documents/burning-glass-database/data/'
years = ['2018/', '2018_ongoing/', '2019/', '2020/']
fields = set('CanonEmployer', 'JobURL', 'CanonYearsOfExperienceLevel', 'ConsolidatedONET', 
             'MaxDegreeLevel', 'IsDuplicate', 'CanonOtherDegrees', 'CanonRequiredDegrees', 
             'Telephone', 'JobText', 'MinDegreeLevel', 'CanonPostalCode', 'StandardMajor', 
             'Latitude', 'CanonCounty', 'BGTOcc', 'CanonCity', 'JobDomain', 'JobID', 'LMA', 
             'Email', 'CanonPreferredDegrees', 'CanonSkills', 'Language', 'Source', 
             'InternshipFlag', 'PostingHTML', 'IsDuplicateOf', 'CanonState', 'ConsolidatedTitle', 
             'DivisionCode', 'Longitude', 'ConsolidatedInferredNAICS', 
             'JobDate', 'CanonJobTitle', 'MinAnnualSalary', 'CanonCountry',
             'CanonSkillClusters', 'MaxHourlySalary', 'YearsOfExperience', 'CanonJobHours', 
             'CanonMaximumDegree', 'MaxExperience', 'MSA', 'CanonYearsOfExperienceCanonLevel', 
             'ConsolidatedDegreeLevels', 'CanonIntermediary', 'BGTSubOcc', 'CIPCode', 
             'JobReferenceID', 'MinHourlySalary', 'CleanJobTitle', 'MaxAnnualSalary', 
             'CanonJobType', 'MinExperience', 'CanonMinimumDegree')

# read in all of the matches and group by
df1 = pd.read_csv("/Users/hayleeham/Documents/burning-glass-database/matches/matches_rr2_2007_present_MZ.csv")
df2 = pd.read_csv("/Users/hayleeham/Documents/burning-glass-database/matches/matches_rr1_2018_present_MZ.csv")
df3 = pd.read_csv("/Users/hayleeham/Documents/burning-glass-database/matches/matches_rr1_2007_2017.csv")
df_master = df1.append(df2)
df_master = df_master.append(df3)
dfg = df_master.groupby('company_2').agg(list)
companies_set = set(dfg.index.tolist())

# if elem in dfg.index:
#     for company in dfg.loc[elem]['company_1']:
#         # add the company(s) to the record before writing out

with open('rr1_2018_present_records.csv', 'wt') as out:
    for year in years:
        print(year)
        for filename in os.listdir(path + year):
            print(filename)
            zf = zipfile.ZipFile(path + year + filename)
            xml_filename = filename[:-3] + 'xml'

            job_count = 0
            for event, elem in ET.iterparse(zf.open(xml_filename), events=("end",)):
                if elem.tag == 'JobID':
                    job_count += 1

                if job_count == 100:

                elem.clear()


# JobID
# CleanJobTitle
# JobDomain
# CanonCity
# CanonCountry
# CanonState
# JobDate
# JobText
# JobURL
# PostingHTML
# Source
# JobReferenceID
# Email
# CanonEmployer
# Latitude
# Longitude
# CanonIntermediary
# Telephone
# CanonJobTitle
# CanonCounty
# DivisionCode
# MSA
# LMA
# InternshipFlag
# ConsolidatedONET
# CanonSkillClusters
# CanonSkills
# IsDuplicate
# IsDuplicateOf
# CanonMaximumDegree
# CanonMinimumDegree
# CanonOtherDegrees
# CanonPreferredDegrees
# CanonRequiredDegrees
# CIPCode
# StandardMajor
# MaxExperience
# MinExperience
# ConsolidatedInferredNAICS
# BGTOcc
# MaxAnnualSalary
# MaxHourlySalary
# MinAnnualSalary
# MinHourlySalary
# YearsOfExperience
# CanonJobHours
# CanonJobType
# CanonPostalCode
# CanonYearsOfExperienceCanonLevel
# CanonYearsOfExperienceLevel
# ConsolidatedTitle
# Language
# BGTSubOcc
# ConsolidatedDegreeLevels
# MaxDegreeLevel
# MinDegreeLevel