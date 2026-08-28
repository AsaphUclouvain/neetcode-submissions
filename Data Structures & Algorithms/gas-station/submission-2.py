"""
We do not need to restart the loop because having a positive
stream till the end ensure that we could have had a loop as we checked
whether the gaz sum is greater than the cost sum
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        tot = 0
        idx = -1
        for i in range(len(diff)):
            tot += diff[i]
            if tot < 0:
                tot = 0
                idx = -1
                continue
            if idx == -1:
                idx = i
        return idx

