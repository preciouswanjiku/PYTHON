try:
    number = 100
    answer = number / 0
    print(answer)
except Exception as e:
    print("There is an error: ", e)