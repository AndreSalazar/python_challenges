if __name__ == '__main__':
    N = int(input())
    result = list()
    i = 1
    items = ""

    for i in range(N):
        command = input()

        value = command.split(" ")

        if value[0] == "insert":
            result.insert(int(value[1]), int(value[2]))
        if value[0] == "print":
            print(result)
        if value[0] == "remove":
            result.remove(int(value[1]))
        if value[0] == "append":
            result.append(int(value[1]))
        if value[0] == "sort":
            result.sort()
        if value[0] == "pop":
            result.pop()
        if value[0] == "reverse":
            result.reverse()

        i += 1


