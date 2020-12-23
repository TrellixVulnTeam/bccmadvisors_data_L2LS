import os
import wbdata as wb
import datetime
import pandas as pd
import csv
import json
from wb_indicators import Source, world_development_indicators, africa_development_indicators, country


def main():
    the_indicator = africa_development_indicators.gdp_per_capita_annual_growth
    the_country = country.kenya
    the_data = wb.get_data(the_indicator, the_country)
    print(the_data)
    # print(wb.get_data(africa_development_indicators.gdp_per_capita_current, country=country.kenya))


if __name__ == '__main__':
    main()