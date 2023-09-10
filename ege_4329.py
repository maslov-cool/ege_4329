def divs(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst


def common_divs(lst1, lst2):
    cnt = 0
    for i in lst1:
        if i in lst2:
            cnt += 1
    return cnt


with open('17_4329.txt') as f:
    A = [int(i) for i in f]
lst_max_del = max([divs(i) for i in A], key=len)

B = [common_divs(divs(A[i]), divs(A[i + 1])) for i in range(len(A) - 1) if common_divs(divs(A[i]), lst_max_del) >= 3 and
     common_divs(divs(A[i + 1]), lst_max_del) >= 3]

print(len(B), max(B))
