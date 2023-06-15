""" Дано целое число N из отрезка [1; 1000]. 
Также даны N целых чисел Ai из отрезка [1; 1000000]. 
Требуется для каждого числа Ai вывести количество различных делителей этого числа. 
В этой задаче несколько верных решений, попробуйте найти наиболее оптимальное. 
Для полученного решения укажите сложность в О-нотации. """
from datetime import datetime
import random
class Randomizer():
    """собираем массив чисел для выборки"""
    def __init__(self,quantity_i:int):
        self.__quantity = quantity_i
    def randomize(self) -> list[int]:
        return random.sample(range(1000001),k=self.__quantity)


class DevisorsFinder():
    """тут находим делители чисел"""
    def __init__(self, body_i:list[int]):
        self.__keys = body_i
        self.__out = dict()
        self.globalOps = 0
        self.__startTime = datetime.now()
    
    def Complexity(self):
        print(f"""количество значений: {len(self.__keys)}\n"""\
            + f"количество операций в цикле: {self.globalOps}\n"\
            + f"затраченное время: {(datetime.now() - self.__startTime).seconds}")

    def __calculateOutput(self) -> None:
        for i in self.__keys:
            self.__out[i]= self.__FindDevisors(i)
        
    def __shapeOutput(self) -> str:
        tmp = ""
        for keyvalue in self.__out:
            tmp += f"{keyvalue}: {self.__out[keyvalue]}\n"
        return tmp

    def __FindDevisors(self,num:int) -> list[int]:
        out = set()
        for i in range(2,num):
            if not num%i:
                out.add(i)
                self.globalOps +=1
        return len(out)

    def printOutput(self) -> str:
        self.__calculateOutput()
        out_strfied = self.__shapeOutput()

        print( out_strfied)



def main():
    sup_val = Randomizer(random.choice(range(1,1001)))
    fun = DevisorsFinder(sup_val.randomize())
    fun.printOutput()
    fun.Complexity()
    print("""По сложности .... каждая N даёт ещё одну проходку по A[i]"""\
          + "Предпложу что это O(n) потому что хоть циклов и 2, но O(n**2) алгоритм не тянет."
          )


if __name__ == "__main__":
    main()