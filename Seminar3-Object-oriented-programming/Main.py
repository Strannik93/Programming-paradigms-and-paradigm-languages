from Tic_tac_toe import Tic_tac_toe
from random import randint as RI

# Определяем класс с меню для настроек игры
class Menu:
    def __init__(self):
        self.tic_tac_toe = Tic_tac_toe()
        self.mode = False
    
    # Главное меню
    def main_menu(self):
        while True:
            print('введите: start - начать игру, mode - режим игры, exit - выход')
            if self.mode == False: print('Текущий режим - 2 игрока.')
            else: print('Текущий режим - против бота.')
            command = input('Введите команду: ')
            if command == 'start': self.new_game()
            elif command == 'mode': 
                if self.mode == False: self.mode = True
                else: self.mode = False
            elif command == 'exit': exit()

    # Метод вывода завершения программы
    def exit(self):
        print('завершение программы')

    # Метод с жеребьевкой перед началом игры и циклом, в котором проходит сама игра
    def new_game(self):
        self.tic_tac_toe.print_matrix()
        toss = RI(False, True) # жеребьевка
        if toss == True:
            first = 'X'
            second = 'O'
        else:
            first = 'O'
            second = 'X'
        if self.mode == False: 
            first_player = '1 игрок'
            second_player = '2 игрок'
        else:
            first_player = '1 игрок'
            second_player = 'Бот'
        print(f'{first_player} ставит {first}, {second_player} ставит {second}')
        steps = True
        # цикл, в котором проходит игра
        while steps == True:
            if toss == True:
                print(f'Ходит {first_player}({first}):')
                line, row = self.tic_tac_toe.step()
                self.tic_tac_toe.matrix[line][row] = first
                self.tic_tac_toe.print_matrix()
                toss = False
                steps = self.tic_tac_toe.check_steps(first,first_player)
            else:
                if self.mode == False:
                    print(f'Ходит {second_player}({second}):')
                    line, row = self.tic_tac_toe.step()
                    self.tic_tac_toe.matrix[line][row] = second
                    self.tic_tac_toe.print_matrix()
                    toss = True
                    steps = self.tic_tac_toe.check_steps(second,second_player)
                else:
                    print(f'Ходит {second_player}({second}):')
                    line, row = self.tic_tac_toe.bot_step(second)
                    self.tic_tac_toe.matrix[line][row] = second
                    self.tic_tac_toe.print_matrix()
                    toss = True
                    steps = self.tic_tac_toe.check_steps(second,second_player)
        exit()

# Инициализация меню и вызов начальноо метода
menu = Menu()
menu.main_menu()