# DEPRECATED - non-performant
# def _max_sat(self, satisfaction: List[int]) -> int:
#     if len(satisfaction) == 0:
#         return 0
#     elif len(satisfaction) == 1:
#         return max(satisfaction[0], 0)
#
#     sub_sat = self.maxSatisfaction(satisfaction[1:])
#     subtotal = sum(satisfaction)
#
#     if subtotal + sub_sat > sub_sat:
#         return subtotal + sub_sat
#     else:
#         return sub_sat
#
# def maxSatisfaction(self, satisfaction: List[int]) -> int:
#     satisfaction.sort()
#     return self._max_sat(satisfaction)


def maxSatisfaction(self, satisfaction: List[int]) -> int:
    satisfaction.sort(reverse=True)
    last = current = su= 0

    for dish in satisfaction:
        current = last + dish
        if current < 0:
            break
        su += current
        last += dish

    return su
