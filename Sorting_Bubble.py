nums=list(map(int,input("Enter elements: ").split()))
print("Enter list is: ",nums)
for i in range(len(nums)):
    for j in range(i+1,len(nums)-1-i):
        if nums[j]>nums[j+1]:
           nums[j],nums[j + 1] =nums[j + 1],nums[j]
print("Sorted List is : ",nums)
