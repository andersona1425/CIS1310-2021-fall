def mysum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(mysum(10, 20, 30))