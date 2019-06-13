import csv
import re
from imports.misc import category, acccode, strp, day_to_net
from imports.iban import bank_details
from imports.country import country_details
from tqdm import tqdm

inputcsv = open('input.csv')
totalrows = sum(1 for line in open('input.csv'))
rows = tqdm(csv.reader(open('input.csv')), total=totalrows)

def main():
    ## Loop through each row in the CSV file
    for row in rows:
        ## Query IBAN API and return results
        bankinfo = bank_details('GB', '000000', '00000000')
        ## Write to Sage formatted CSV
        data = [
                ['B', strp(category(row[0])), '', strp(row[5]), row[0], 'AD1', 'GBP', '', '', '', 'DMG', strp(day_to_net(row[15])), acccode(row[0]), 2, 999999],
                ['A', 'AD1', '', row[60], row[61], row[62], row[67], row[65], 'country_code_here', row[118], row[119], row[115]],
                ['R', 'GB', bankinfo['iban'], bankinfo['bic']],
            ]
        ## Open writer for output
        csv.writer(open('output.csv', 'a', newline='')).writerows(data)

# Run above
main()
