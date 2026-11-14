#Hackerrank : Nested lists
#Difficulty : Medium

if __name__ == '__main__':
    students = []

    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grades = []

    for s in students:
        grades.append(s[1])

    grades = sorted(set(grades))
    names = []

    for s in students:
        if s[1] == grades[1]:
            names.append(s[0])

    names.sort()

    for name in names:
        print(name)
