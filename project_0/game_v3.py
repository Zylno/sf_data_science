import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min = 1
    max = 101
    predict_number = np.random.randint(min, max) # предполагаемое число

    while True:
        count += 1
        mid = round((min+max)/2) 
        if number > predict_number:
            max = mid
        elif number < predict_number:
            min = mid 
        else:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict(15)}')

