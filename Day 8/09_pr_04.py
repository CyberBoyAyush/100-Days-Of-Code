# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

d = recur_sum(5)
print(d)    