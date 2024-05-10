#write a python program to print count of vowels in both even and odd positions
s=input()
ec,oc=0,0
for i in range(len(s)):
    if i%2==0:
        if s[i] in "aeiouAEIOU":
           ec+=i
        else:
            if s[i] in "aeiouAEIOU":
                oc+=i
print(ec,oc)
