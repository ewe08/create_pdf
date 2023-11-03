import json

def get_data(json_name: str):
    f = open(json_name)
    input_data = json.load(f)

    data = {
        'Автор(ы) научной статьи': input_data['name'],
        'Научное издание': input_data['magazine'],
        'Выпуск издания': f"{input_data['number']} выпуск {input_data['year']} года",
        'Направление': input_data['chapter'],
        'Секция': '-',
        'Название научной статьи': input_data['topic'],
        'Научный руководитель': input_data['assistant'],
        'Ориентировочная дата опубликования': input_data['date_publication'],
    }

    return data.items()