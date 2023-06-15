from math import floor,sqrt
def isPrimeNumber(candidate:int) -> bool:
    for j in range(candidate-1,2,-1):
        if not candidate%j:
            return False
    return True
    
if __name__ == "__main__":
    print(isPrimeNumber(10))
    print(isPrimeNumber(7))