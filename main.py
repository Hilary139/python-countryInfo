from countryinfo import CountryInfo
name = input('Enter your country: ')
country = CountryInfo(name)
print('Capital is : ', country.capital())
print('Currencies is : ', country.currencies())
print('Languages is : ', country.languages())
print('Borders are : ', country.borders())
print('Other names is : ', country.alt_spellings())
print('Calling code is : ', country.calling_codes())
print('Population is : ', country.population())
print('Region is : ', country.region())
print('Time zone is : ', country.timezones())
print('Wikipedia link is : ', country.wiki())

print('Code by Hilary!!')
