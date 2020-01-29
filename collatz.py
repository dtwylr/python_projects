#! usr/local/bin/python3

def isEven(num):
    if num%2 == 0:
        return True
    else:
        return False

def collatz(num):
    sum = 0
    while num != 1:
        if isEven(num):
            num = num/2
            sum += 1
        else:
            num == (3*num+1) / 2
            sum += 2
    return sum

    # sum = 0;
    # if num == 1:
    #     #sum += 1
    #     return sum
    # elif isEven(num):
    #     num = num/2
    #     sum += 1
    # else:
    #     num == (3*num+1) / 2
    #     sum += 2
    # return collatz(num)

def main():
    longest = 0
    for i in range(1,1000000):
        print(i)
        it = collatz(i)
        if it > longest:
            longest = it
    print(longest)

main()
