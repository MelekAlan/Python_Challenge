"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

nums = [i for i in range(1,21)]
nums_prime = []
for i in nums :
    prime = []
    for j in range(2,i) :
        prime.append(i % j != 0)
    if all(prime) and i != 1 :
        nums_prime += [i]
new_number = []
while True :
    for i in nums_prime :
        temp = []
        for j in range(len(nums)) :
            temp.append(nums[j] % i == 0)
            if nums[j] % i == 0 :
                nums[j] = nums[j] // i
        if any(temp) :
            new_number += [i]
    if sum(nums) == 20 :
        break
count = 1    
for i in new_number :
    count *= i
print(count)
