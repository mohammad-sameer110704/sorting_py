nums=list(map(int,input("Enter elements for sorting : ").split()))
n=len(nums)
for i in range(n):
    min=i
    for j in range(i+1,n):
        if nums[min] > nums[j]:
            min = j

    nums[i],nums[min] = nums[min],nums[i]

print(nums)

