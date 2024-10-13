import geo

ip = geo.getIP()
print(ip)

country_plain = geo.getCountry(ip, 'plain')
print(country_plain)

country_json = geo.getCountry(ip, 'json')
print(country_json)

geoData = geo.getGeoData(ip)
print(geoData)

ptrData = geo.getPTR(ip)
print(ptrData)

geo.showIpDetails('216.239.32.0')

geo.showCountryDetails('216.239.32.0')
