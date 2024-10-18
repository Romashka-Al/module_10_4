import sys


sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


mas = [-1] + [int(x) for x in input().split()] + [-1]
n = len(mas)
mnl, mnr = [0] * n, [n - 1] * n
st = [n - 1]
for i in range(n - 2, 0, -1):
    while st and mas[st[-1]] > mas[i]:
        mnl[st.pop()] = i
    st.append(i)
st = [0]
for i in range(1, n - 1):
    while st and mas[st[-1]] > mas[i]:
        mnr[st.pop()] = i
    st.append(i)
ans = []
for i in range(1, n - 1):
    ans.append(mas[i] * (mnr[i] - mnl[i] - 1))
print(max(ans))

sys.stdin.close()
sys.stdout.close()
