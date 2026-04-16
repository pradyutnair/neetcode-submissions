class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bs(num_list: List[int], val:int) -> bool:
            if not num_list:
                return None
            i, j = 0, len(num_list) - 1
            while i<=j:
                mid = (i + j) // 2
                if num_list[mid] == val:
                    return mid
                elif num_list[mid] < val:
                    i = mid+1
                else:
                    j = mid - 1
            return None

        
        for index, num in enumerate(numbers):
            diff = target - num
            second_idx = bs(numbers[index+1:], diff)
            if second_idx is not None:
                return [index + 1, index + 1 + second_idx + 1]