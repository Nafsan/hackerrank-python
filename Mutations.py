string = input()
n, k = map(str, input().split())
n = int(n)
string = string[:n]+k+string[n:]
print(string)
