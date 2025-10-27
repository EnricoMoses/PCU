k = 2
nums = [1,2,3,4,5]

net_k = k % len(nums)

for i in range(net_k):
    if k > 0:
        popped = nums.pop(len(nums)-1)
        nums.insert(0, popped)
    if k < 0:
        popped = nums.pop(0)
        nums.insert(popped)

print(nums)