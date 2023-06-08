# Необходимо написать алгоритм поиска всех доступных комбинаций
# (посчитать количество) для количества кубиков K с количеством граней N.
# 2. У вас есть 2 варианта на выбор – количество кубиков может быть строго
# ограничено (4 кубика, например), либо их количество будет
# динамическим. Выбор за вами.
# 3. Если вы реализуете простой вариант, обращает внимание, что данное
# решение имеет сложность O(n4
# ), но если количество кубиков сделать
# переменной, то она трансформируется в O(nk
# ), что будет представлять
# собой экспоненциальную сложность. Для второго решения очевидно, что
# его сложность O(nk
# ) с самого начала.
def allSelects(sides:int, qua=4):
    outcomes = []
    match qua:
        case 4:
            for i in range(sides):
                for j in range(sides):
                    for k in range(sides):
                        for l in range(sides):
                            outcomes.append((i,j,k,l))
        case 3:
            for i in range(sides):
                for j in range(sides):
                    for k in range(sides):
                            outcomes.append((i,j,k))
        case 2:
            for i in range(sides):
                for j in range(sides):
                            outcomes.append((i,j))
        case 1:
            for i in range(sides):
                outcomes.append((i,))
    return( len(outcomes))
if __name__ == "__main__":
    print(allSelects(6,1))
    print(allSelects(6,2))
    print(allSelects(6,3))
    print(allSelects(6,4))