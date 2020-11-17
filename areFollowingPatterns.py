strings = ["cat", "dog", "dog"]
patterns = ["a", "b", "b"]

def areFollowingPatterns(strings, patterns):
    if len(strings) != len(patterns):
        return False
    d = {}
    for i in range(len(strings)):
        if patterns[i] not in d:
            if strings[i] not in d.values():
                d[patterns[i]] = strings[i]
            else:
                return False
        else:
            if d[patterns[i]] != strings[i]:
                return False
    return True

areFollowingPatterns(strings, patterns)