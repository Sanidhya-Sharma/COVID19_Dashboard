from flask import Flask, render_template
import pandas as pd
from flask import request
from covid import Covid

app = Flask(__name__)

@app.route('/')

@app.route('/home', methods=['GET', 'POST'])
def homepage():

    #information Source
    covid_1 = Covid(source="worldometers")

    # TOTAL ACTIVE CASES
    active_cases = covid_1.get_total_active_cases()

    # TOTAL CONFIRMED CASES
    confirmed_cases = covid_1.get_total_confirmed_cases()

    # TOTAL DEATHS
    deaths_cases = covid_1.get_total_deaths()

    # TOTAL RECOVERED
    recovered_cases = covid_1.get_total_recovered()

    #source_2
    covid = Covid(source="worldometers")

    #total data

    covid_data = covid.get_data()


    #Creating datframe
    dfObj_wld = pd.DataFrame.from_dict(covid_data).sort_values('confirmed', ascending=False)

    wld_table_list_data = dfObj_wld[['country', 'confirmed', 'deaths', 'recovered']]


    wld_table_covid_fact = []

    for rows in wld_table_list_data.to_numpy():
        wld_table_covid_fact.append(rows)


    dropdown_data_list = []

    dropdown_data = dfObj_wld['country']

    for rows in dropdown_data.to_numpy():
        dropdown_data_list.append(rows)


    #GETTING VALUES FROM THE DROP DOWN USING REQUEST
    select = request.form.get('comp_select')

    print(select)

    if select == None:
        select = 'India'
        print(select)

    # GET COVID CASES BY COUNTRY NAME
    select_country = covid.get_status_by_country_name(select)

    dfObj = pd.DataFrame.from_dict(select_country , orient='index')

    # Transpose dataframe object
    dfObj = dfObj.transpose()
    pd.set_option('display.expand_frame_repr', False)
    print(dfObj)

    ind_table_list = dfObj[['confirmed','deaths','recovered','active']]


    #Bar Chart for selected data
    ind_table_data = []

    for rows in ind_table_list.to_numpy():
        ind_table_data.append(rows)

    ind_table_covid_fact = ind_table_data

    #Chart Data
    row_val = ind_table_data[0]
    col_val = ['Confirmed','Deaths','Recovered','Active']
    legend = "COVID-19 Cases"


    #for doughnut chart
    doughnut_data_values = dfObj[['confirmed','deaths', 'recovered']]

    doughnut_data = []

    for rows in doughnut_data_values.to_numpy():
        doughnut_data.append(rows)

    doughnut_data_names = ['Confirmed','Deaths','Recovered']

    doughnut_data_value = doughnut_data[0]


    #Top Confirmed COVID-19 Countries

    Conf_table = dfObj_wld[['country','confirmed']]
    Death_table = dfObj_wld[['country','deaths']]
    Recovered_table = dfObj_wld[['country','recovered']]

    # extracting Top 25
    top20_confirmed = Conf_table.nlargest(25, "confirmed")
    top20_deaths = Death_table.nlargest(25, "deaths")
    top20_recovered = Recovered_table.nlargest(25, "recovered")

    top_conf_data_name = []
    top_conf_data_values = []

    top_death_data_name = []
    top_death_data_values = []

    top_recovered_data_name = []
    top_recovered_data_values = []

    for rows in top20_confirmed.to_numpy():
        top_conf_data_name.append(rows[0])
        top_conf_data_values.append(rows[1])

    for rows in top20_deaths.to_numpy():
        top_death_data_name.append(rows[0])
        top_death_data_values.append(rows[1])

    for rows in top20_recovered.to_numpy():
        top_recovered_data_name.append(rows[0])
        top_recovered_data_values.append(rows[1])

    countries_confirmed_name = top_conf_data_name
    countries_confirmed_count = top_conf_data_values

    countries_death_name = top_death_data_name
    countries_death_count = top_death_data_values

    countries_recovered_name = top_recovered_data_name
    countries_recovered_count = top_recovered_data_values

    return render_template("home.html",values=row_val, labels=col_val, legend=legend,select=select,
                           active_cases=active_cases,confirmed_cases=confirmed_cases,deaths_cases=deaths_cases,
                           recovered_cases=recovered_cases,ind_table_covid_fact=ind_table_covid_fact,wld_table_covid_fact=wld_table_covid_fact,
                           dropdown_data_list=dropdown_data_list,doughnut_data_names=doughnut_data_names,doughnut_data_value=doughnut_data_value,
                           countries_confirmed_name=countries_confirmed_name,countries_confirmed_count=countries_confirmed_count,countries_death_name=countries_death_name,
                           countries_death_count=countries_death_count,countries_recovered_name=countries_recovered_name,countries_recovered_count=countries_recovered_count)


@app.route('/Who_am_i', methods=['GET', 'POST'])
def whoami():

    name = 'Sanidhya Sharma'

    img = '/static/images/me.png'

    return render_template("whoami.html", name=name, img=img)

if __name__ == "__main__":
    app.run(debug=True)


