if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    result = []
    array_list = list(arr)
    max_value = max(array_list)

    for value in array_list:
        if value != max_value:
            result.append(value)
    final_result = max(result)

    print(final_result)


