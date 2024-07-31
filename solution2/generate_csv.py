import csv
import re
import random
from faker import Faker

def generate_csv(file_name, num_rows):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file,  delimiter=',', lineterminator='\r\n', quotechar = "\"")
        writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
        
        for _ in range(num_rows):
            fake = Faker()
            data_row = [str(fake.first_name()),
                str(fake.last_name()),
                str(fake.address().replace("\n", " ")),
                str(fake.date_of_birth())]
            # print(data_row)
            writer.writerow(data_row)

# Generate a CSV with 100 rows for testing
generate_csv('test_data.csv', 100)