from zeep import Client


wsdl = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
client = Client(wsdl)

# Print out available operations
for service in client.wsdl.services.values():
    for port in service.ports.values():
        operations = sorted(port.binding._operations.keys())
        for op in operations:
            print("Available operations:", op)
print("----------------------------------------")


iso_code = client.service.CountryISOCode(sCountryName='Bangladesh')
response = client.service.FullCountryInfo(sCountryISOCode=iso_code)
print(response)