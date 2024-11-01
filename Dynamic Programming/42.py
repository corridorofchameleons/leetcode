import math


def define_nth_bit_1(n: int, k: int):
    '''Способ через список'''

    #  проверка валидности
    if n < 0 or (k + 1 > 3 ** (n - 1)):
        return None

    if n in (0, 1):
        return 0

    #  создание начальной последовательности с n = 1
    sequence = [False]

    for _ in range(n - 1):
        #  создание негативного списка и его присоединение
        new_list = [not el for el in sequence]
        sequence.extend(new_list * 2)

    return int(sequence[k])


def define_nth_bit_2(k: int):
    '''Способ через прокси элементов'''
    #  нужен индекс от 1
    ind = k + 1

    #  конечная последовательность
    initial = {
        1: False,
        2: True,
        3: True
    }

    counter = 0

    #  сжимаем фрактал до состояния initial
    while ind > 3:
        #  определяем размер сегмента
        n = math.ceil(math.log(ind, 3))
        prev_seq = 3 ** (n - 1)

        #  ищем прокси элемента в уменьшенной последовательности
        q = ind // prev_seq
        #  если элемент последний в последовательности
        if ind % prev_seq == 0:
            q -= 1
        ind -= q * prev_seq
        
        counter += 1

    val = initial.get(ind)
    for _ in range(counter):
        val = not val

    return int(val)


assert define_nth_bit_1(3, 8) == define_nth_bit_2(8)
assert define_nth_bit_1(5, 70) == define_nth_bit_2(70)
assert define_nth_bit_1(5, 39) == define_nth_bit_2(39)
assert define_nth_bit_1(5, 55) == define_nth_bit_2(55)
assert define_nth_bit_1(4, 26) == define_nth_bit_2(26)
assert define_nth_bit_1(6, 200) == define_nth_bit_2(200)
