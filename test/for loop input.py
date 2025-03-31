start = int(input("Start num"))
stop = int(input("stop num"))
if start > stop:
    for i in range(start, stop-1, -1):
        print(i)
elif start <stop:
    for i in range(start, stop+1):
        print(i)

