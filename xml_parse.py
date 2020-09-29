import zipfile
import lxml.etree as ET
import os

path = '/Users/hayleeham/Documents/burning-glass-database/data/'
years = ['2018/', '2018_ongoing/', '2019/', '2020/']

with open('outfile', 'wt') as out:
    for year in years:
        print(year)
        for filename in os.listdir(path + year):
            print(filename)
            zf = zipfile.ZipFile(path + year + filename)
            xml_filename = filename[:-3] + 'xml'
            for event, elem in ET.iterparse(zf.open(xml_filename), events=("end",)):
                if elem.tag == 'CanonEmployer' and elem.text:
                    out.write(f'{elem.text}\n')
                    elem.clear()