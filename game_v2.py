import numpy as np

def binary_search_predict(number: int = 1) -> int:
    """Угадываем число бинарным поиском.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток.
    """
    count = 1
    left = 1
    right = 100

    while left <= right:
        predict = (left + right) // 2
        if predict == number:
            break
        elif predict < number:
            left = predict + 1
        else:
            right = predict - 1
        count += 1

    return count

def score_game(predict_function) -> int:
    """Оцениваем среднее количество попыток угадывания.

    Args:
        predict_function (function): Функция угадывания числа.

    Returns:
        int: Среднее количество попыток угадывания.
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)

    for number in random_array:
        count_ls.append(predict_function(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score

if __name__ == "__main__":
    score_game(binary_search_predict)
