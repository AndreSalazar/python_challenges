
if __name__ == '__main__':
    average = 0
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks:
        for items in student_marks.get(query_name):
            average += items

    print("{:.2f}".format(average/3))