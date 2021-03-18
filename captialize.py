def solve(s):
    cap=s.split(" ")
    listy=[]
    for i in cap:
        a=i.capitalize()
        listy.append(a)
    a=(" ".join(listy))
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
