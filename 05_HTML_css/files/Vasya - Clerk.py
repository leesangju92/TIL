def tickets(people):
    count_25 = count_50 = 0
    for dollars in people:
        if dollars == 25:
            count_25 += 1
            continue
        elif dollars == 50:
            if count_25 >= 1:
                count_25 -= 1
                count_50 += 1
                continue
            else:
                return "NO"
        else:
            if count_25 >=1 and count_50 >= 1:
                count_25 -= 1
                count_50 -= 1
                continue
            elif count_25 >= 3:
                 count_25 -= 3
                 continue
            else:
                return "NO"
    return "YES"