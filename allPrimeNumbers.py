#Question is find all prime numbers from 0 to n
#brute force method is to take each value from 2 to n and check if it is a prime number or not
#optimised way is to remove all the multiples of found prime numbers from the candidacy list and keep on repeating this process.


def prime_numbers(n):
    if n<2:
        return []
    l = [False,False]+[True]*(n-1)
    result = []

    for i in range(2,n+1):
        if l[i]:
            result.append(i)
            j=2
            k=1
            while True:

                k = i*j
                if k>n:
                    break
                l[k]=False
                j+=1
    return result

n = int(input('Enter the value upto which prime numbers are to be found: '))
print("List of Prime numbers are: ",prime_numbers(n))

