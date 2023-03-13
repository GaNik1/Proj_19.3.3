import requests
import json
import pytest

def test_add_pet(): # добавляем информацию об питомце
    pet_id = 2442
    input_pet = {
        "id": 2442,
        "category": {
            "id": 22,
            "name": "Strelka"
        },
        "name": "doggie",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 12,
                "name": "Dog"
            }
        ],
        "status": "available"
    }

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    # делаем POST запрос на создание животного
    res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)

    assert res_post.status_code == 200
    # убеждаемся в том что мы передали равно тому что получилось
    print(res_post.json())
    assert res_post.json() == input_pet


    # делаем GET запрос на проверку изменения животного
    res_get = requests.get(url='https://petstore.swagger.io/v2/pet/2442', headers={'accept': 'application/json'})
    assert res_get.status_code == 200
    assert res_get.json() == res_post.json() == input_pet


    # делаем PUT запрос на изменение нового животного
    requests.put(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)

    # делаем GET запрос на проверку изменения животного
    res_get = requests.get(url='https://petstore.swagger.io/v2/pet/2442')

    assert res_get.status_code == 200
    # проверили по id что "name": "Strelka" поменялось на  "name": "Bobik"

    # # делаем запрос на изменение животного
    # res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    #
    # # преобразуем текст в формат json, затем в дикт
    # res_json = json.loads(res_post.text)
    # assert input_pet == res_json
    # делаем DELETE запрос на удаление животного
    res_delete = requests.delete(url=f'https://petstore.swagger.io/v2/pet/2442')

    assert res_delete.status_code == 200

    assert res_delete.json()["message"] == str(pet_id)

    # убеждаемся что питомец удалился
    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/2442')

    assert res_get.status_code == 404 # 404 тест не пройден так как этого животного pet/2442 уже нет

    # делаем GET запрос и убеждаемся что питомец удалился
    assert res_get.json()["message"] == "Pet not found"