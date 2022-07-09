n = int(input())

a = []
for i in range(n) :
    a.append(int(input()))
    if a[-1] == 0 :
        a.remove[-1]
        a.remove[-2]
    
print(sum(a))