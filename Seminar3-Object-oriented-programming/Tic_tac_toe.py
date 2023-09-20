# Определяем класс для игры в крестики нолики
class Tic_tac_toe:
    def __init__(self):
        self.matrix = [['*' for _ in range(3)], ['*' for _ in range(3)], ['*' for _ in range(3)]]

    # Метод для вывода матрицы на экран
    def print_matrix(self):
        for i in range(len(self.matrix)):
            print(*self.matrix[i], sep=' ')
    
    # Метод для получения координаты от пользователя
    # Повторяет запрос, пока не будет выбрана свободная для заполнения координата
    def step(self):
        while True:
            try:
                line = int(input('Введите номер строки(сверху вниз от 1 до 3): '))
                row = int(input('Введите номер столбца(слева направо от 1 до 3): '))
                if 0 < line < 4 and 0 < row < 4 and self.matrix[line-1][row-1] == '*':
                    return line-1, row-1
                elif 0 < line < 4 and 0 < row < 4: print('Место уже занято!')
                else: print('Такая позиция не существует!')
            except:
                print('Номер строки и столбца должны быть целыми!')
    
    # Метод для проверки всех победных кобминации
    # Принимает символ проверяемого игрока
    # Возвращает истину, если игра продолжается
    def control(self, player):
        count = 0
        for i in range(len(self.matrix)):
            if self.matrix[i][i] == player: count += 1
        if count == 3:
            return False
        count = 0
        for i in range(len(self.matrix)):
            if self.matrix[i][len(self.matrix)-i-1] == player: count += 1
        if count == 3:
            return False
        for i in range(len(self.matrix)):
            count = 0
            for k in range(len(self.matrix[i])):
                if self.matrix[i][k] == player: count += 1
            if count == 3:
                return False
        for k in range(len(self.matrix[0])):
            count = 0
            for i in range(len(self.matrix)):
                if self.matrix[i][k] == player: count += 1
            if count == 3: 
                return False
        return True
    
    # Метод для проверки, что игра окончена
    def check_steps(self,player,name_player):
        steps = self.control(player)
        if steps == False: 
            print(f'{name_player} победил')
            return steps
        else:
            steps = self.control_free_steps()
            if steps == False: print('Ничья')
            return steps
        
    # Метод для поиска хотя бы одной свободной координаты
    def control_free_steps(self):
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                if self.matrix[i][k] == '*':
                    return True
        return False
    
    # Метод, проверяющий можно ли закрыть последнюю координату из победной комбинации
    # На вход принимает символ игрока, у которого проверяет победные комбинации
    def check_free_slot(self,coord,player):
        count = 0
        for i in range(len(coord)):
            line, row = coord[i]
            if self.matrix[line][row] == player: count += 1
        if count == 2:
            for i in range(len(coord)):
                line, row = coord[i]
                if self.matrix[line][row] == '*': return line, row
        return False
    
    # Метод для перебора ботом всех победных комбинации
    def check_player(self, player):
        coord = ['' for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            coord[i] = (i,i)
        check = self.check_free_slot(coord,player)
        if type(check) == tuple: return check
        for i in range(len(self.matrix)):
            coord[i] = (i,len(self.matrix)-i-1)
        check = self.check_free_slot(coord,player)
        if type(check) == tuple: return check
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                coord[k] = (i,k)
            check = self.check_free_slot(coord,player)
            if type(check) == tuple: return check
        for k in range(len(self.matrix[0])):
            for i in range(len(self.matrix)):
                coord[i] = (i,k)
            check = self.check_free_slot(coord,player)
            if type(check) == tuple: return check
        return False
    
    # Метод для хода бота, где он перебирает возможные ходы до первого подходящего
    def bot_step(self,player):
        if player == 'X': opponent = 'O'
        else: opponent = 'X'
        if self.matrix[1][1] == '*': return 1, 1
        check = self.check_player(player)
        if type(check) == tuple: return check
        check = self.check_player(opponent)
        if type(check) == tuple: return check
        if self.matrix[1][1] == self.matrix[0][0] == player:
            if self.matrix[0][1] == self.matrix[0][len(self.matrix)-1] == self.matrix[len(self.matrix)-1][1] == '*': return 0, 1
            elif self.matrix[1][0] == self.matrix[len(self.matrix)-1][0] == self.matrix[1][len(self.matrix)-1] == '*': return 1, 0
        elif self.matrix[1][1] == self.matrix[0][len(self.matrix)-1] == player:
            if self.matrix[1][len(self.matrix)-1] == self.matrix[len(self.matrix)-1][len(self.matrix)-1] == self.matrix[1][0] == '*':
                return 1, len(self.matrix)-1
            elif self.matrix[0][1] == self.matrix[0][0] == self.matrix[len(self.matrix)-1][1] == '*': return 0, 1
        elif self.matrix[1][1] == self.matrix[len(self.matrix)-1][len(self.matrix)-1] == player:
            if self.matrix[1][len(self.matrix)-1] == self.matrix[0][len(self.matrix)-1] == self.matrix[1][0] == '*':
                return 1, len(self.matrix)-1
            elif self.matrix[len(self.matrix)-1][1] == self.matrix[len(self.matrix)-1][0] == self.matrix[0][1] == '*':
                return len(self.matrix)-1, 1
        elif self.matrix[1][1] == self.matrix[len(self.matrix)-1][0] == player:
            if self.matrix[1][0] == self.matrix[0][0] == self.matrix[1][len(self.matrix)-1] == '*':
                return 1, 0
            elif self.matrix[len(self.matrix)-1][1] == self.matrix[len(self.matrix)-1][len(self.matrix)-1] == self.matrix[0][1] == '*':
                return len(self.matrix)-1, 1
        if player == 'X':
            for i in range(len(self.matrix)):
                for k in range(len(self.matrix[i])):
                    if self.matrix[i][k] == opponent:
                        if i > 0 and k > 0 and self.matrix[0][0] == '*': return 0, 0
                        elif i > 0 and k < len(self.matrix[i])-1 and self.matrix[0][len(self.matrix[i])-1] == '*':
                            return 0, len(self.matrix[i])-1
                        elif i < len(self.matrix)-1 and k < len(self.matrix[i])-1 and self.matrix[len(self.matrix)-1][len(self.matrix[i])-1] == '*':
                            return len(self.matrix)-1, len(self.matrix[i])-1
                        elif i < len(self.matrix)-1 and k > 0 and self.matrix[len(self.matrix)-1][0] == '*':
                            return len(self.matrix)-1, 0
            for i in range(len(self.matrix)):
                for k in range(len(self.matrix[i])):
                    if self.matrix[i][k] == '*': return i, k
        else:
            if self.matrix[1][1] == opponent:
                if self.matrix[0][0] == '*': return 0, 0
                elif self.matrix[0][len(self.matrix)-1] == '*': return 0, len(self.matrix)-1
                elif self.matrix[len(self.matrix)-1][len(self.matrix)-1] == '*':
                    return len(self.matrix)-1, len(self.matrix)-1
                elif self.matrix[len(self.matrix)-1][0] == '*': return len(self.matrix)-1, 0
                for i in range(len(self.matrix)):
                    for k in range(len(self.matrix[i])):
                        if self.matrix[i][k] == '*': return i, k
            else:
                if self.matrix[len(self.matrix)-1][len(self.matrix)-1] == opponent: 
                    if self.matrix[0][0] == '*': return 0, 0
                    elif self.matrix[len(self.matrix)-2][len(self.matrix)-1] == '*':
                        return len(self.matrix)-2, len(self.matrix)-1
                    elif self.matrix[len(self.matrix)-1][len(self.matrix)-2] == '*':
                        return len(self.matrix)-1, len(self.matrix)-2
                elif self.matrix[len(self.matrix)-1][0] == opponent:
                    if self.matrix[0][len(self.matrix)-1] == '*': return 0, len(self.matrix)-1
                    elif [len(self.matrix)-2][0] == '*': return len(self.matrix)-2, 0
                    elif self.matrix[len(self.matrix)-1][1] == '*': return len(self.matrix)-1, 1
                elif self.matrix[0][0] == opponent:
                    if self.matrix[len(self.matrix)-1][len(self.matrix)-1] == '*': return len(self.matrix)-1, len(self.matrix)-1
                    elif self.matrix[1][0] == '*': return 1, 0
                    elif self.matrix[0][1] == '*': return 0, 1
                elif self.matrix[0][len(self.matrix)-1] == opponent: 
                    if self.matrix[len(self.matrix)-1][0] == '*': return len(self.matrix)-1, 0
                    elif self.matrix[1][len(self.matrix)-1] == '*': return 1, len(self.matrix)-1
                    elif self.matrix[0][len(self.matrix)-2] == '*': return 0, len(self.matrix)-2