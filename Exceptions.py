def printError(e):
    print("Error Code: {}".format(e))

n = int(input())
for _ in range(n):
    try:
        a, b = map(int,input().split())
        print (a//b)
    except ValueError as e:
        printError(e)
    except ZeroDivisionError as e:
        printError(e)
