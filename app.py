from flask import Flask, render_template, request
from zeep import Client

app = Flask(__name__)

# WSDL URL
wsdl = 'http://www.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
client = Client(wsdl)

def get_currency_code_by_currency(curr_name):
    data = client.service.ListOfCurrenciesByName()
    for currency in data:
        if currency["sName"] == curr_name:
            return currency["sISOCode"]
    return None


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/country-info', methods=['POST'])
def country_info():
    country_name = request.form.get('country_name')
    iso_code = client.service.CountryISOCode(sCountryName=country_name)
    country_info = client.service.FullCountryInfo(sCountryISOCode=iso_code)
    return render_template('country_info.html', country_info=country_info)

@app.route('/countries-by-currency', methods=['POST'])
def countries_by_currency():
    currency = request.form.get('currency')
    print(currency)
    currency_code = get_currency_code_by_currency(currency)
    print(currency_code)
    if currency_code:
        countries = client.service.CountriesUsingCurrency(sISOCurrencyCode=currency_code)
        return render_template('countries_by_currency.html', countries=countries, enumerate=enumerate)
    

@app.route('/currency-by-country', methods=['POST'])
def currency_by_country():
    country_name = request.form.get('country_name')
    iso_code = client.service.CountryISOCode(sCountryName=country_name)
    currency = client.service.CountryCurrency(sCountryISOCode=iso_code)
    return render_template('currency_by_country.html', currency=currency)


@app.route('/flag-phone-code', methods=['POST'])
def flag_phone_code():
    country_name = request.form.get('country_name')
    iso_code = client.service.CountryISOCode(sCountryName=country_name)
    flag_url = client.service.CountryFlag(sCountryISOCode=iso_code)
    phone_code = client.service.CountryIntPhoneCode(sCountryISOCode=iso_code)
    return render_template('flag_phone_code.html', flag_url=flag_url, phone_code=phone_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
