from abc import ABC, abstractmethod

# Интерфейс, определяющий метод execute
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Метод, реализующий интерфейс команды (включение света)
class LightOnCommand(Command):
    def __init__(self, light) :
        self.light = light
    
    def execute(self):
        self.light.turn_on()

# Метод, реализующий интерфейс команды (выключение света)
class LightOffCommand(Command):
    def __init__(self, light) :
        self.light = light
    
    def execute(self):
        self.light.turn_off()

# Определяем класс для света с командами вывода текущего состояния
class Light:
    def turn_on(self):
        print("Свет включен")

    def turn_off(self):
        print("Свет выключен")

# Класс для пульта управления, вызывающего команду, когда пользователь нажимает кнопку
class RemoteControl:
    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

light = Light() # Создание света
light_on = LightOnCommand(light) # Включение света
light_off = LightOffCommand(light) # Выключение света

remote = RemoteControl() # Создание пульта

remote.set_command(light_on) # Включаем свет
remote.press_button() # Вывод: Свет включен

remote.set_command(light_off) # Выключаем свет
remote.press_button() # Вывод: Свет выключен