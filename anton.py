x=int(input())
y=input()
cnt_A=y.count('A')
cnt_D=y.count('D')
if cnt_A>cnt_D:
    print("Anton")
elif cnt_A<cnt_D:
    print("Danik")
else:
    print("Friendship")