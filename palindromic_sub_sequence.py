def findLPS(s, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    if startIndex == endIndex:
        return 1
    if s[startIndex] == s[endIndex]:
        return 2 + findLPS(s, startIndex + 1, endIndex - 1)
    op1 = findLPS(s, startIndex + 1, endIndex)
    op2 = findLPS(s, startIndex, endIndex - 1)
    return max(op1, op2)


print(findLPS("ELRMENMET", 0, 8))