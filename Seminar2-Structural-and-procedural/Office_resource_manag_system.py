# Мы разрабатываем систему управления ресурсами в офисе.
# У нас есть несколько комнат, в каждой из которых размещены разные устройства
# (компьютеры, принтеры, лампы и т. д.).
# Каждое устройство имеет следующие характеристики:
# тип (компьютер, принтер, лампа и т. д.), статус (включено или выключено), идентификатор.

# Мы хотим выполнить следующие операции:
# Добавить новое устройство в комнату.
# Включить или выключить устройство в комнате.
# Поиск устройства по типу и статусу.
# Получить список всех устройств в конкретной комнате.
# Подсчитать общее количество устройств каждого типа в офисе.

# функция добавления устройства в комнату
def add_device(device, room: list):
    flag = True
    for current in room:
        if current['id'] == device['id']:
            flag = False
            break
    if flag:
        room.append(device)

# функция для переключения статуса
def switching_status(status: bool):
    if status:
        return False
    else:
        return True

# функция включения/выключения устройства в комнате
def device_switch(device_id, room: list):
    for current in room:
        if current['id'] == device_id:
            current['status'] = switching_status(current['status'])

# Поиск устройства по типу и статусу
def find_device(type: str, status: bool, room: list):
    list_devices = []
    for device in room:
        if device['type'] == type and device['status'] == status:
            list_devices.append(device)
    return list_devices

# Получить список всех устройств в конкретной комнате
def list_all_devices(room_id: int, office: list):
    for room in office:
        if room['id'] == room_id:
            return room['devices']
    return None

# Подсчитать общее количество устройств каждого типа в офисе
def count_devices(office: list):
    counts_devices = {'computer': 0, 'lamp': 0, 'printer': 0}
    for room in office:
        for device in room['devices']:
            counts_devices[device['type']] = counts_devices.get(device['type']) + 1
    return counts_devices

# office, состоящий из комнат
office = [
{'id': 0, 'devices':
[
{'type': 'computer', 'status': False, 'id': 0},
{'type': 'lamp', 'status': True, 'id': 1},
{'type': 'printer', 'status': True, 'id': 2},
{'type': 'computer', 'status': False, 'id': 3},
{'type': 'lamp', 'status': False, 'id': 4},
] },
{'id': 1, 'devices':
[
{'type': 'computer', 'status': False, 'id': 5},
{'type': 'lamp', 'status': True, 'id': 6},
{'type': 'computer', 'status': False, 'id': 7},
] },
{'id': 2, 'devices':
[
{'type': 'computer', 'status': False, 'id': 8},
{'type': 'lamp', 'status': True, 'id': 9},
{'type': 'computer', 'status': False, 'id': 10},
{'type': 'printer', 'status': True, 'id': 11},
] },
]

# Проверка поиска по типу и статусу, добавления нового устройства
# и подсчета общего количества устройств каждого типа в офисе
device = {'type': 'printer', 'status': False, 'id': 12}
print(f"Поиск отключенного принтера в 1 комнате: {find_device('printer',False,office[1]['devices'])}")
print(f"Подсчет всех устройств в офисе: {count_devices(office)}")
add_device(device, office[1]['devices'])
print("После добавления устройства")
print(f"Поиск отключенного принтера в 1 комнате: {find_device('printer',False,office[1]['devices'])}")
print(f"Подсчет всех устройств в офисе: {count_devices(office)}")

# Проверка получиения списка всех устройств в конкретной комнате и включения/выключения устройства в комнате
print(f"Получение списка устройств в комнате 2: {list_all_devices(2,office)}")
device_switch(8,office[2]['devices'])
print("После включения компьютера с id 8")
print(f"Получение списка устройств в комнате 2: {list_all_devices(2,office)}")