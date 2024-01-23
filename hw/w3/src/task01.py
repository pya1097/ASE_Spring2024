from data import DATA 
from helper import *
from config import *
import csv
from tests import Tests

if __name__ == "__main__":
    
    files = ["data/weather.csv","data/diabetes.csv","data/soybean.csv"]
    for file in files:
        data = DATA(file)
        cls_data = data.classes_data()

        print('-----------------Output-----------------')
        print(cls_data)

    # Save results to a file
    # with open('w3_task1.out', 'w', newline='') as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     csv_writer.writerow([str(cls_data)])

       





    