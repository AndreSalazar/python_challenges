# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N = int(input())
    items = 1
    phone_book = {}

    for items in range(N):
        entries = input().split()
        phone_book[entries[0]] = entries[1]
        items += 1

    while True:
        try:
            input_keys = input()
            if input_keys in phone_book:
                output = input_keys + "=" + phone_book[input_keys]
            else:
                output = "Not found"
            print(output)
        except:
            break