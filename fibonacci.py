# Using a for loop.

print("Loop Method")
print("-----------")   
prev1 = 0
prev2 = 1

print(prev1)
print(prev2)

for fibo in range(18):
    newFibo = prev1 + prev2
    print(newFibo)
    prev1 = prev2
    prev2 = newFibo


# Recursive Method

print("Recursive Method")
print("----------------")    
print(0)
print(1)
count = 2

def fibonacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev1 = prev2
        prev2 = newFibo
        count += 1
        fibonacci(prev1, prev2)
    else:
        return

fibonacci(0, 1)

# Finding the n-th Fibonacci number

print("Finding the n-th Fibonacci number.")
print("----------------------------------")
def nthfibo(n):
    if n<=1:
        return n
    else:
        return nthfibo(n - 1) + nthfibo(n - 2)
    
print(nthfibo(19))