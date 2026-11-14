# HackerRank: Find the Runner-Up Score!
# Difficulty: Easy

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maximum = max(arr)
    second = None
    for i in arr:
        if i<maximum:
            if second is None or i>second:
                second = i
    print(second)
