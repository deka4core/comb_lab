def inverse(permutation):
    """
    Вычисляет вектор инверсии по заданной перестановке
    :param permutation: изначальная перестановка
    :return: вектор инверсий перестановки
    """
    vector_len = len(permutation)
    inversion_vector = [0] * vector_len
    bit_tree = [0] * (vector_len + 1)  # Инициализация бинарного дерева нулями. Представление в виде списка

    def update(index, val):
        """
        Обновляет значение в бинарном дереве отрезков
        :param index: индекс элемента
        :param val: добавочное значение
        :return:
        """
        while index <= vector_len:
            bit_tree[index] += val
            index += index & -index  # Добавляем к индексу младший бит

    def query(index):
        """
        Возвращает сумму элементов в бинарном дереве от 1 до index (Кумулятивная сумма)
        :param index: индекс элемента
        :return: кумулятивная сумма
        """
        try:
            res = 0
            while index > 0:
                res += bit_tree[index]
                index -= index & -index
            return res
        except IndexError:
            print("Ошибка входных данных.")

    for i, num in enumerate(permutation):
        inversion_vector[i] = query(vector_len) - query(num + 1)  # Записывает кол-во чисел больших num справа
        update(num + 1, 1)  # Добавляем 1 в бинарное дерево отрезков для элемента num

    return inversion_vector


def recover(inversion_vector):
    """
    Восстановление перестановки по вектору инверсий
    :param inversion_vector: Вектор инверсий
    :return: Восстановленная перестановка из вектора инверсий
    """
    vector_len = len(inversion_vector)
    permutation = [0] * vector_len
    items = [x for x in range(vector_len)]  # Множество чисел от 0 до max числа в перестановке

    """
        Sn - множество перестановок
        Dn - множество инверсий  
        Теорема: Отображение Vn: Sn -> Dn является биекцией, причем любая перестановка a, принадлежащая Sn,
            однозначно восстанавливается по её вектору инверсий Vn(a) 
    """
    for i in range(vector_len - 1, -1, -1):  # Перебор вектора инверсий с конца
        index = inversion_vector[i] + 1
        permutation[i] = items.pop(-index)

    return permutation


try:
    """
        Ввод данных
    """
    p = list(map(int, input().split()))
    if len(set(p)) != len(p):
        raise ValueError
    print(f"Перестановка: {p}")
    print(f"Инверсия: {inverse(p)}")
    print(f"Восстановленная перестановка: {recover(inverse(p))}")
except ValueError:
    print("Некорректный ввод.")
