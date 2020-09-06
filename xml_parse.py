import zipfile
import lxml.etree as ET
import os

path = '/export/projects2/rsadun_burning_glass_project/Burning Glass Data/Text Data/'
years = ['2007/', '2010/', '2011/', '2012/', '2013/', '2014/', '2015/', '2016/', '2017/', 
         '2018/', '2018_ongoing/', '2019/', '2020/']

with open(path + 'outfile', 'wt') as out:
    for year in years:
        print(year)
        for filename in os.listdir(path + year):
            print(filename)
            zf = zipfile.ZipFile(path + year + filename)
            xml_filename = filename[:-3] + 'xml'
            for event, elem in ET.iterparse(zf.open(xml_filename), events=("end",)):
                if elem.tag == 'CanonEmployer':
                    out.write(f'{elem.text}\n')
                    elem.clear()