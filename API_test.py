import requests
geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode=Москва, улица Красная площадь, дом 1&format=json"
response = None
try:
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        toponym_okrug = toponym["metaDataProperty"]["GeocoderMetaData"]["province"]
        toponym_coodrinates = toponym["Point"]["pos"]
        print(response.content)

        print(toponym_address, "имеет координаты:", toponym_okrug)
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
except:
    print("Запрос не удалось выполнить. Проверьте подключение к сети Интернет.")