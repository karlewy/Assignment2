n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    cmd = input().split()
    operation = cmd[0]

    if operation == "pop":
        
        s.remove(min(s))
    elif operation == "remove":
        try:
            s.remove(int(cmd[1]))
        except KeyError:
            pass
    elif operation == "discard":
        s.discard(int(cmd[1]))

print(sum(s))
