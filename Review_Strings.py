# Enter your code here. Read input from STDIN. Print output to STDOUT
def indexes(string):
    counter = 0
    even_list = list()
    odd_list = list()

    for character in string:
        if counter == 0 or (counter % 2) == 0:
            even_list.append(character)
        else:
            odd_list.append(character)
        counter += 1

    even_string = ''.join(map(str, even_list))
    odd_string = ''.join(map(str, odd_list))
    print(even_string, odd_string)

amount_string = int(input())
for i in range(amount_string):
    string = str(input())
    indexes(string)