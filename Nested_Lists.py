if __name__ == '__main__':
    name_list = []
    score_list = []
    minimun_score = 0
    count = 0
    result_name = ""
    result_score = 0

    for _ in range(int(input())):
        name = input()
        score = float(input())

        name_list.append([score, name])

    name_list.sort()
    minimun_score = min(name_list)

    for items in name_list:
        if count == 1 and items[0] != minimun_score[0]:
            result_name += items[1] + "\n"
            result_score = items[0]
        elif items[0] == result_score:
            result_name += items[1] + "\n"
            result_score = items[0]
        elif result_score == 0 and items[0] != minimun_score[0] and count >= 2:
            result_name += items[1] + "\n"
            result_score = items[0]

        count += 1

    print(result_name)