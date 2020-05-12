from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # 使用字典（哈希表）来存储索引位置
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i  # 记录索引位置
            else:
                # 如果i和j的差的绝对值最多为k，那么就找到了i和j
                if abs(i-d[nums[i]]) <= k:
                    return True
                else:
                    # 否则，更新索引位置为j的位置，继续查找
                    d[nums[i]] = i
        # 找完数组都没有发现，则返回false
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsNearbyDuplicate([1, 0, 1, 1], 1) == True
    assert s.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
    assert s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
