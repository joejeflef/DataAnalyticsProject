#This program was used to covert PDF data into workable .csv data
from tika import parser
import csv
import sys

washington_counties = [ 'ADAMS', 'ASOTIN', 'BENTON', 'CHELAN', 'CLALLAM', \
                        'CLARM', 'COLUMBIA', 'COWLITZ', 'DOUGLAS', 'FERRY', \
                        'FRANKLIN', 'GARFIELD', 'GRANT', 'GRAYS HARBOR', \
                        'ISLAND', 'JEFFERSON', 'KING', 'KITSAP', 'KITTITAS', \
                        'KLICKITAT', 'LEWIS', 'LINCOLN', 'MASON', 'OKANOGAN', \
                        'PACIFIC', 'PEND OREILLE', 'PIERCE', 'SAN JUAN', 'SKAGIT', \
                        'SKAMANIA', 'SNOHOMISH', 'SPOKANE', 'STEVENS', 'THURSTON', \
                        'WAHKIAKUM', 'WALLA WALLA', 'WHATCOM', 'WHITMAN', 'YAKIMA']

file_path_name = 'MedianHousePricesByCountyPDFs\\' + sys.argv[1]

parsed_pdf = parser.from_file(file_path_name)

data = parsed_pdf['content']

data = data.replace('$ ', '$')

county_information_dict = {}

for county in washington_counties:
    
    pos_start = data.find(county)
    
    if pos_start == -1:
        pos_start = data.find(county.title())
    
    pos_end = data[pos_start:].find('\n')
    
    county_information_str = data[pos_start : pos_start + pos_end]
    
    county_information_list = county_information_str.split(' ')
    
    #I am getting a blank line for some reason, don't really care to dig deeper
    if len(county_information_str) == 0:
        continue
    
    #Before splitting, you have to account for the fact that some counties have two words in their name
    if county_information_list[0][0].isalpha() and county_information_list[1][0].isalpha():
        #Adjust the county_information_list
        new_county_information_list = [county_information_list[0] + ' ' + county_information_list[1]]
        
        #print(new_county_information_list[0])
        
        for entry_i in range(len(county_information_list)):
            if entry_i != 0 and entry_i != 1:
                new_county_information_list.append(county_information_list[entry_i])
        
        county_information_list = new_county_information_list
    
    new_county_information_list = []
    for county_data_i in range(len(county_information_list)):
        if county_information_list[county_data_i] != '':
            new_county_information_list.append(county_information_list[county_data_i])
   
    county_information_list = new_county_information_list
    
    #Check if this pdf had blanks in the building permits position, instead of 0's or -'s
    if len(county_information_list) == 8:
        county_information_list.insert(4, '0')
        county_information_list.insert(5, '0')
    
    for county_data_i in range(len(county_information_list)):
        county_information_list[county_data_i] = county_information_list[county_data_i].replace('%', '')
        county_information_list[county_data_i] = county_information_list[county_data_i].replace('N/A', '0')
        county_information_list[county_data_i] = county_information_list[county_data_i].replace('NA', '0')
        county_information_list[county_data_i] = county_information_list[county_data_i].replace('$', '')
        county_information_list[county_data_i] = county_information_list[county_data_i].replace(',', '')
        county_information_list[county_data_i] = county_information_list[county_data_i].replace('*', '')
    
    #Convert everything except the name to an integer
    for entry_i in range(len(county_information_list)):
        #Skip converting the name
        if entry_i != 0:
            #Need to convert dashs to 0's
            if county_information_list[entry_i] == '-':
                county_information_list[entry_i] = '0'
                
            #Check if the number is a float
            if county_information_list[entry_i].find('.') == -1:
                county_information_list[entry_i] = int(county_information_list[entry_i])
            else:
                county_information_list[entry_i] = float(county_information_list[entry_i])
    
    county_information_dict[county] = county_information_list
    
#Export the data as a .csv
csv_name = 'MedianHousePricesByCountyCSVs\\' + sys.argv[1].replace('.pdf', '.csv')
with open(csv_name, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(['County', 'SAAR', '% Change by qtr', '% Change by year', \
                                'Building Permits', '% Change by year', 'Median Resale Price($)', \
                                '% Change by year', 'HAI', 'First-time HAI'])
    
    for county in county_information_dict:
        csv_writer.writerow(county_information_dict[county])
        
      