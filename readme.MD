# Global Country Information and Currency Explorer

## Overview

The **Global Country Information and Currency Explorer** is a web-based application that provides detailed information about countries and their currencies using SOAP web services. Users can input a country name to retrieve full country details or find out which countries use a specific currency. The application uses a publicly available WSDL service http://www.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL= for gathering country and currency information.

## Features

- **Full Country Info**: Retrieve comprehensive details (e.g., name, capital, currency, language) about any country.
- **Countries by Currency**: List all countries that use a specific currency.
- **Currency by a Country**: Give currency and currency code for a specific country.
- **Get Flag and Phone Code by Country**: Retrieve flag and phone code by country name.
- **SOAP-Based Integration**: Utilizes SOAP and WSDL-based web services to fetch data from the server.
- **User-Friendly Interface**: Simple and intuitive interface with tables and structured data presentation.

## Available Operations

The application is built on top of SOAP web services that provide the following functionalities:

- `ListOfCurrenciesByName`: Get a list of currencies and iso code.
- `CountriesUsingCurrency`: List all countries that use a specified currency.
- `CountryCurrency`: Get the currency of a country.
- `CountryFlag`: Get the URL of the flag of a country.
- `CountryISOCode`: Get the ISO code of a country.
- `CountryIntPhoneCode`: Get the international phone code of a country.
- `FullCountryInfo`: Retrieve comprehensive information about a country.
- `ListOfCountryNamesByCode`: Get a list of countries by their ISO code.

## Technologies Used

- **Backend**:
  - **Python**
  - **Flask** (for handling web requests)
  - **Zeep** (for handling SOAP requests)
  
- **Frontend**:
  - **HTML**
  - **CSS**
  
## Project Structure

```
global_country_info
│
├── static/
│   └── styles.css           # Custom CSS styles for the application
│
├── templates/
│   ├── index.html                   # Main page for fetching country information
│   ├── countries_by_currency.html   # Displays countries using a specified currency
│   ├── flag_phone_code.html         # Displays the flag and phone code of a country
│   ├── country_info.html            # Displays full information of  a country
│   ├── currency_by_country.html     # Displays the currency used by a country
│
├── app.py                   # Main Flask application file
├── available_operations.py  # Give all the operations of this WSDL service
│
├── requirements.txt         # Project dependencies
└── README.md                # Project overview and details

```

## Setup Instructions

1. **Clone the repository**:

   ```bash
   git@github.com:raufur-simanto/Global-Country-Info.git
   cd Global-Country-Info
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   flask run or
   python app.py
   ```

5. **Access the application**:

   Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

### Full Country Info
1. Enter the name of a country on the home page to get detailed information such as:
   - ISO code
   - Capital city
   - Currency ISO code
   - Continent code
   - Language(s)
   - Country flag (as an image)
   
2. This information will be displayed in a structured table format.

### Countries Using a Specific Currency
1. Enter the ISO code of a currency (e.g., `USD`, `EUR`, `BDT`) to retrieve a list of countries that use that currency.
2. The countries will be displayed in a tabular format with their corresponding ISO codes.

## Examples

- **Full Country Info for Bangladesh**: Provides details like ISO code `BD`, capital city `Dhaka`, currency `BDT`, etc.
- **Countries using USD**: Lists countries such as the United States, Ecuador, and others that use the US Dollar.
