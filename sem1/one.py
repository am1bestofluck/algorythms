def sum_list(inc:list) -> int:
    sum = 0
    for i in inc:
        try:
            sum += i
        except TypeError:
            continue
    return sum

if __name__ =="__main__":
    print(sum_list([1,2,3,4,"в сумме дадут десять"]))