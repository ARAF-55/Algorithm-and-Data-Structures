def LCSS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + LCSS(s1, s2, index1 + 1, index2 + 1)
    else:
        op1 = LCSS(s1, s2, index1 + 1, index2)
        op2 = LCSS(s1, s2, index1, index2 + 1)
        return max(op1, op2)


print(LCSS("elephant", "eretpat", 0, 0))
