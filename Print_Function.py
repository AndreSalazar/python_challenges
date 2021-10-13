if __name__ == '__main__':
    n = int(input())

    result_string = ""

    for counter in range(1, n + 1):
        result_string += str(counter)
        counter += 1

    print(result_string)