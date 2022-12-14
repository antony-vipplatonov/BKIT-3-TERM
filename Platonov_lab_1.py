import sys
import math


# получение коэффициентов
def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        wrong = True
        while(wrong):
            try:
                coef_str = input(prompt)
                float(coef_str)
                wrong = False
            except ValueError:
                print("Введён неправильный коэффициент.")
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if (a != 0):
        if D == 0.0:
            root = -b / (2.0 * a)
            result.append(root)
        elif D > 0.0:
            sqD = math.sqrt(D)
            root1 = (-b + sqD) / (2.0 * a)
            root2 = (-b - sqD) / (2.0 * a)
            result.append(root1)
            result.append(root2)
    return result


def main():  # основная функция
    a = get_coef(1, 'Введите коэффициент А: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('У уравнения с коэффициентами {}, {}, {} нет корней'.format(a, b, c))
    elif len_roots == 1:
        print('У уравнения с коэффициентами {}, {}, {} \
один корень: {}'.format(a, b, c, roots[0]))
    elif len_roots == 2:
        print('У уравнения с коэффициентами {}, {}, {} \
два корня: {} и {}'.format(a, b, c, roots[0], roots[1]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
