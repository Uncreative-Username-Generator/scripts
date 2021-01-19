"""
This script will print(std out) an array.
This array contains the original csv file and add a column at last.
Elements in the new last column is the product of the third row and the fourth row,
and it will ignore the first row(because it is normally titles for the rows)

Input:
""""""""
    * -i : CSV to combine

Output:
""""""""
    
    * Array containing original CSV file and additional column

Usage
"""""""

python parse-csv.py
"""
import csv
from argparse import ArgumentParser


__version__ = "1.0"
__status__ = "Dev"

def main():
    usage = "\n%prog  [options]"
    parser = ArgumentParser(description=usage)
    parser.add_argument("-i", "--infile", action="store", dest="infile", help="Input file")
    parser.add_argument('--version', '-V', action='version',
                        version="%(prog)s " + __version__)

    options = parser.parse_args()

    fr = open(options.infile, "r")
    data_frame = csv.reader(fr, delimiter=',', quotechar='"')
    ROW_COUNT = 0
    for row in data_frame:
        ROW_COUNT = ROW_COUNT + 1
        if ROW_COUNT == 1:
            continue
        new_row = row
        bmi = float(row[2]) * float(row[3])
        new_row.append(str(bmi))
        print(new_row)
    fr.close()


if __name__ == '__main__':
    main()
