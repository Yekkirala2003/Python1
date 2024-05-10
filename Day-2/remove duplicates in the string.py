#write a python program to remove duplicates in the string
s=input()
s1=""
for i in s:
    if i not in s1:
        s1+=i
print(s1)
