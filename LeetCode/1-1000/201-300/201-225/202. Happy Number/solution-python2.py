class Solution:
    # Pulling ideas from one of the supposed "fastest" solutions on LeetCode
    # copied verbatim below
    def isHappy(self, n: int) -> bool:
        values = set()
        while True:
            n = sum(map(lambda i: i * i, map(int, str(n))))
            if n == 1:
                return True
            if n not in values:
                values.add(n)
                continue
            return False

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         seen = set([n])
#         while True:
#             nn = sum(map(lambda i: i**2, map(int, str(n))))
#             if nn == 1:
#                 return True
#             if nn not in seen:
#                 seen.add(nn)
#                 n = nn
#                 continue
#             return False
