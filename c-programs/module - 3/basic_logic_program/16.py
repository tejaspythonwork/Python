# Convert Country Name Into abbreviated form

def abbr_country(full_country_name):
    country = full_country_name.replace('Of','').replace('of','')
    splited_name = country.split()

    abbr = ''.join(w[0].upper() for w in splited_name)
    abbr_with_dots = '.'.join(abbr) + '.'
    return abbr_with_dots



country_name = input('Please Enter Country Name')
country_abbr_name = abbr_country(country_name)
print(country_abbr_name)    