class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):return 0
        parent = {}
        found = set()
        for num in nums:
            if num in found:continue
            found.add(num)
            parent[num]=[num,num]
            if num-1 in found:
                prev = parent[num-1]
                # if prev[0]==-4:print("hello",prev)
                parent[prev[0]][1]=num
                # if prev[0]==-4:print("bye")
                parent[num][0]=prev[0]
                # parent[prev[0]][1]
                if num-1!=prev[0]:del parent[num-1]
            if num+1 in found:
                cur = parent[num]
                seq = parent[num + 1]
                parent[seq[1]][0]=cur[0]
                parent[cur[0]][1]=seq[1]
                parent[num][1]=seq[1]
                if num+1!=seq[1]:del parent[num+1]
                if cur[0]!=num:del parent[num]
            # print(parent,num)
        return max([i[1]-i[0]+1 for i in parent.values()])

        