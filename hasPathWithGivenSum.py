# Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s

# t = {
#     "value": 4,
#     "left": {
#         "value": 1,
#         "left": {
#             "value": -2,
#             "left": null,
#             "right": {
#                 "value": 3,
#                 "left": null,
#                 "right": null
#             }
#         },
#         "right": null
#     },
#     "right": {
#         "value": 3,
#         "left": {
#             "value": 1,
#             "left": null,
#             "right": null
#         },
#         "right": {
#             "value": 2,
#             "left": {
#                 "value": -2,
#                 "left": null,
#                 "right": null
#             },
#             "right": {
#                 "value": -3,
#                 "left": null,
#                 "right": null
#             }
#         }
#     }
# }

def hasPathWithGivenSum(t, s):
    if t is None:
        if s == 0:
            return 1
        else:
            return 0

    else:
        ans = 0
        subSum = s - t.value

        if subSum == 0 and t.left == None and t.right == None:
            return True

        if t.left is not None:
            ans = ans or hasPathWithGivenSum(t.left, subSum)

        if t.right is not None:
            ans = ans or hasPathWithGivenSum(t.right, subSum)

        return bool(ans)