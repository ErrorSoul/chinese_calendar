from datetime import datetime
from datetime import timedelta

a = "15:19 3/12/1918"
b = "23:11 2/12/1937"
c = "08:13 2/12/1956"
d = "00:50 3/12/1975"
e = "23:54 2/12/1994"
f = "00:23 3/12/2013"
g = "20:54 2/12/2032"
h = "09:38 3/12/2051"
i = "16:55 2/12/2070"
j = "03:14 2/12/2089"
k = "21:26 2/12/2108"
l = "21:05 3/12/2127"
m = "21:02 3/12/2146"
n = "16:02 3/12/2165"
o = "03:07 3/12/2184"
p = "10:16 4/12/2203"
r = "22:04 3/12/2222"
s = "17:47 3/12/2241"
t = "18:02 3/12/2260"
u = "17:29 4/12/2279"

lst = [a, b ,c, d, e, f, g, h,i,
       j, k,l, m, n, o, p, r, s, t,u ]



folder = map(lambda x:datetime.strptime(x, "%H:%M %d/%m/%Y"),lst)
print folder 

diff = [folder[num+1] - folder[num] for num in range(len(folder) - 1)]

foo = sum(map(timedelta.total_seconds, diff))

