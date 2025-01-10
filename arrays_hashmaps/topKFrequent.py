import heapq
def topKFrequent(nums, k):
    # Bucket Sort method , result is not sorted
    # freq = {}
    # for num in nums:
    #     freq[num] = freq.get(num, 0) + 1

    # buckets = [[] for _ in range(len(nums) + 1)]
    # for key, val in freq.items():
    #     buckets[val].append(key)

    # res = []
    # for i in range(1, len(buckets)):
    #     for num in buckets[i]:
    #         res.append(num)
    #         if len(res) == k:
    #             return res

    # Bucket sort with heap to maintain it being sorted with the runtime being O(N)
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        heapq.heappush(buckets[count], num)

    res = []
    for i in range(len(buckets) - 1, 0, -1):
        while buckets[i]:
            res.append(heapq.heappop(buckets[i]))
            if len(res) == k:
                return res



nums = [1,2,2,2,3,3,3]
k = 2
print(topKFrequent(nums, k))