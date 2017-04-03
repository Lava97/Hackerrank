from fractions import gcd
testcases = int(input())
for i in range(testcases):
    abc = input()
    a,b,c = [j for j in abc.strip().split()]
    if int(c)%gcd(int(a),int(b)) == 0 and (int(c)<=int(a) or int(c)<=int(b)):
        print("YES")
    else:
        print("NO")
