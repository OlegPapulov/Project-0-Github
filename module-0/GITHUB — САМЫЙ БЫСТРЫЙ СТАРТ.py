import numpy as np

count = 0                           # счетчик попыток
number = np.random.randint(1,101)      # загадали число
print ("Загадано число от 1 до 100")
for count in range(1,101):         # более компактный вариант счетчика
    if number == count: break      # выход из цикла, если угадали      
#print (f"Вы угадали число {number} за {count} попыток.")

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return count # выход из цикла, если угадали
      
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного.
    Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадал

def game_core_v3(number):
    '''Сначала определяем, где находится целевое число относительно медианы диапазона.
    В нашем случае это 50.
    Затем определяем медиану уменьшенного диапазона.
    в зависимости от результата первой проверки это будет 25 или 75.
    И так далее, до определения целевого числа.'''
    count = 1
    min_threshold = 0
    max_threshold = 100
    guess = int((min_threshold + max_threshold) / 2)
    while number != guess:
        count += 1
        if number > guess:
            min_threshold = int((min_threshold + max_threshold) / 2)
            guess = int((min_threshold + max_threshold) / 2)
        elif number < guess:
            max_threshold = int((min_threshold + max_threshold) / 2)
            guess = int((min_threshold + max_threshold) / 2)
    return count

score_game(game_core_v3)
