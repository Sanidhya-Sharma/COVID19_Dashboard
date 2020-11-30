from flask import Flask, render_template
import pandas as pd
from flask import request
from covid import Covid


covid = Covid()

# covid = Covid(source="worldometers")

# ALL COVID DATA
covid_data = covid.get_data()

# ALL countries
# countries = covid.list_countries()

# ITALY COVID CASES
# italy_cases = covid.get_status_by_country_id(88)

# GET LIST OF COUNTRIES
# countries = covid.list_countries()

# TOTAL ACTIVE CASES
# active = covid.get_total_active_cases()

#TOTAL CONFIRMED CASES
# confirmed = covid.get_total_confirmed_cases()

#TOTAL DEATHS
# deaths = covid.get_total_deaths()

#TOTAL RECOVERED
# recovered = covid.get_total_recovered()

# GET COVID CASES BY COUNTRY NAME
# select_country = covid.get_status_by_country_name("india")



# dfObj = pd.DataFrame.from_dict(covid_data)
#
# wld_table_list = dfObj[['country','confirmed','new_cases','deaths','recovered','active','new_deaths', 'total_tests']]
#
# print(wld_table_list)

print(covid_data)

