# Complete the function below.


def  count(s):
    n = long(len(s))
    alist = []
    for i in range(1,n/2+1):
        str1 = "0"*i
        str2 = "1"*i
        str3= str1+str2
        str4 = str2 + str1
        alist.append(str3)
        alist.append(str4)
    length = len(alist)
    output=0
    count = 0
    for i in range(length):
        count = s.count(alist[i])
        output =  output + count
    return output