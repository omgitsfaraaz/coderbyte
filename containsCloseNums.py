nums = [0, 1, 2, 3, 5, 2]
k = 3

def containsCloseNums(nums, k):

    last_seen = dict()

    for pos, num in enumerate(nums):
        try:
            if pos - last_seen[num] <= k: return True
        except:
            pass
        last_seen[num] = pos

    return False

containsCloseNums(nums, k)