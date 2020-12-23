"""
This file contains the functions that will call instances of the get_data classes
"""

from Modules.get_data import *
from Modules.wb_indicators import *
import datetime

"""
def set_args() -> tuple:
    the_date = datetime.datetime(2019, 1, 1), datetime.datetime(2018, 1, 1)
    the_indicator = Africa_development_indicators.gdp_per_capita_annual_growth
    the_country = Country.kenya
    
    return the_date, the_indicator, the_country
"""


indicators = datetime.datetime(2019, 1, 1), datetime.datetime(2018, 1, 1)
countries = Africa_development_indicators.gdp_per_capita_annual_growth
dates = Country.ghana


def get_data_list():
    country_result_list = Get_wb_data(indicators, countries, dates)     # create an instance of get Get_wb_data
    result_data = country_result_list.get_the_data()
    country_result_list.create_csv()


    return result_data
