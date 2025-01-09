import heapq

def k_closest(nums, target, k):
    nums.sort()
    l,r = 0, len(nums) - 1
    min_heap = []

    while l < r:
        cur_sum = nums[l] + nums[r]
        diff = abs(target - cur_sum)

        heapq.heappush(min_heap, (diff, [nums[l], nums[r]]))

        if cur_sum < target:
            l += 1

        else:
            r -= 1

        
    return [pair for _,pair in heapq.nsmallest(k, min_heap)]


    

nums = [10, 22, 28, 29, 30, 40]
target = 54
K = 3  
print(k_closest(nums, target, K)) 