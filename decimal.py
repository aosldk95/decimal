# 소수를 순서대로 열거하면,2, 3, 5, 7, 11, 13 ... 이고 6번째 소수는 13입니다.
# 10001번째 소수는 무엇인가요?
goal = 10001
numberlist = []
number = 1
while len(numberlist) < goal :
    number += 1
    numberlist.append(number)
    for i in range (2, number) :
        if (number % i) == 0:
            numberlist.remove(number)
            break
print(max(numberlist))
    
    
    
