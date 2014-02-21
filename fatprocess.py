__author__ = 'Graham Voysey'
import argparse
import csv
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("-infile", help="a CSV containing fatness data")
parser.add_argument("-outfile", help="where the corrected fat data goes")
args = parser.parse_args()

weights = [datetime, str]
with open(args.infile, 'r') as f:
    reader = csv.DictReader(f, delimiter=',', quotechar='\"')
    for row in reader:
        if row["Type"] == "Weight":
            dt = datetime.strptime(' '.join([row["Date"], row["Time"]]), '%m/%d/%y %H:%M')
            weights.append((dt, row["Value"]))
weights.sort()

with open(args.outfile, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Weight"])
    for weight in weights:
        writer.writerow(weight)
print "success."