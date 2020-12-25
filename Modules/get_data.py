"""
This file contains the main classes for accessing data from the various API's and modules
"""
from Modules.fields import *
import wbdata as wb
import csv


class Get_wb_data:
    def __init__(self, dates, indicators, countries):
        self.the_date = dates
        self.the_indicator = indicators
        self.the_countries = countries

    # generated fields for the csv file
    global fieldnames
    fieldnames = list(create_fields())

    def get_the_data(self) -> dict:
        # using the wbdata api to access the data
        the_data = wb.get_data(self.the_indicator, self.the_countries, self.the_date)
        data_dict = {}
        list_of_field_names = list(fieldnames)

        i = 0
        while i < len(the_data):                                    # len(the_data) counts the number of years in the data
            for field in list_of_field_names:
                data_dict.setdefault(field, the_data[i][field])     # = year_data[field]

            for year_data in the_data:                              # year_data is a dictionary for year's data, the_data is a list of dicts
                for key in year_data:
                    if key in fieldnames:                           # if the field exists in the list of desired fields
                        index_value = year_data[key]                # returns a values for the year's data
                        if index_value['value']:
                            print(key, '->', index_value['value'])
                        else:
                            print(key, '->', year_data[key])
            i += 1
            print('------------------')
        return data_dict

    def create_csv(self):
        with open('bccm_file.csv', 'w', newline='') as csvfile:
            bccmwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

            bccmwriter.writeheader()
            data_row = self.get_the_data()  # data row is a dict with two field names and their corresponding values
            print(data_row)
            bccmwriter.writerow(data_row)

            """
            # bccm writer works with dictionaries
            bccmwriter.writerow({fieldnames[0]: 'Value', fieldnames[1]: 'Chain'})
            """

