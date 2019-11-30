import requests
print('request')
type_of_place='cafe'
longitude=30.272765
latitude = 59.937059
request = "https://search-maps.yandex.ru/v1/?text="+ type_of_place+"&ll="+str(longitude)+"," + str(latitude) + "&spn=3.552069,2.400552&lang=ru_RU&apikey=8bdea3a2-ac05-4026-9666-a66104c79cca"
print(request)
data = requests.get(request)
response = data.json()
i :int
i = 0
result ={}
print(response)
while i<2:
    print('kak')
    answer = type_of_place +": " + response['features'][i]['properties']['name'] + "\n"\
    + "at the address:" + response['features'][i]['properties']['description'] +"\n"\
    + "With number: " + response['features'][i]['properties']['CompanyMetaData']['Phones'][0]['formatted'] + "\n" \
    + "Time the work " + response['features'][i]['properties']['CompanyMetaData']['Hours']['text']
    result[str(i)+'longitude'] = response['features'][i]['geometry']['coordinates'][0]
    result[str(i)+'latitude'] = response['features'][i]['geometry']['coordinates'][1]
    print('kak')
    result[str(i)+'answer'] = answer
    i += 1
    print(i)
print(result)