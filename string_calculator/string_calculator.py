import re


class StringCalculator:

    def __init__(self, ):
        pass

    def add(self, nums_str: str):
        if not nums_str:
            return 0
        # todo can you pass to split method ... two separators
        nums = re.split(r"[,\n]", nums_str)
        nums = list(map(int, nums))
        return sum(nums)
