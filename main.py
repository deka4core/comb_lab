import itertools

alphabet = [i for i in range(1, 9)]


def task_1():
    with open("task_1_output.txt", "w+", encoding='utf-8') as fout:
        perm = list(itertools.permutations(alphabet, r=5))
        for item in perm:
            fout.write("".join(list(map(str, item))) + '\n')
        fout.write("Кол-во размещений: " + str(len(perm)))


def task_2():
    with open("task_2_output.txt", "w+", encoding='utf-8') as fout:
        perm = list(itertools.product(alphabet, repeat=7))
        count = 0
        for item in perm:
            c_perm = [item.count(x) for x in item]
            if (c_perm.count(3) == 3) and (c_perm.count(2) == 2):
                fout.write("".join(list(map(str, item))) + '\n')
                count += 1
        fout.write(f"Кол-во возможных слов длины 7: {count}")


def task_3():
    with open("task_3_output.txt", "w+", encoding='utf-8') as fout:
        perm = list(itertools.product(alphabet, repeat=6))
        count = 0
        for item in perm:
            if item.count(2) == 3:
                fout.write("".join(list(map(str, item))) + '\n')
                count += 1
        fout.write(f"Кол-во возможных слов длины 6, \nв которых 2 повторяется три раза: {count}")


task_3()
