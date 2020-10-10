def get_value_from_list(object_list, separator, key):
    """Функция находит значение ключа key из списка object_list
    по разделителю separator
    :param object_list: список строк
    :param separator: разделитель
    :param key: искомый ключ"""
    value = None
    for element in object_list:
        words = element.split(separator)
        if words[0] == key:
            value = words[1]
    return value

log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""

log_list = []
records = log.split('\n')

for log_record in records:
    record_dict = {
        'name': '',
        'gender': '',
        'item': '',
        'item_cost': 0,
    }

    elements = log_record.split(';')

    user_name = get_value_from_list(elements, ':', 'name')
    user_gender = get_value_from_list(elements, ':', 'gender')
    item_title = get_value_from_list(elements, ':', 'item')
    item_cost = get_value_from_list(elements, ':', 'item_cost')

    record_dict['name'] = user_name
    record_dict['gender'] = user_gender
    record_dict['item'] = item_title
    record_dict['item_cost'] = item_cost

    log_list.append(record_dict)
    
    low_cost_items = []
    max_cost = 13000

    for record in log_list:
        if int(record['item_cost']) < max_cost and record['item'] not in low_cost_items:
            low_cost_items.append(record['item'])

print(low_cost_items)