from data import DATA 
from helper import *
import csv


if __name__ == "__main__":
    file_path = 'w2/data/auto93.csv'
    data = DATA(file_path)
    stats = stats(data)

    with open('/w2/w2.out', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([str(stats)])