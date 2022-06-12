def solution(periods, payments, estimates):
    cntO, cntX = 0, 0
    for i in range(len(periods)):
        if periods[i] == 23:
            if sum(payments[i][1:]) + estimates[i] >= 900000:
                cntO += 1
                continue
        if periods[i] == 59:
            if 600000 <= sum(payments[i][1:]) + estimates[i] < 900000:
                cntO += 1
                continue
        if 60 > periods[i] >= 24:
            if sum(payments[i][1:]) + estimates[i] >= 900000 and sum(payments[i]) < 900000:
                cntO += 1
                continue
        if periods[i] >= 60:
            if sum(payments[i][1:]) + estimates[i] >= 600000 and sum(payments[i]) < 600000:
                cntO += 1
                continue
        if periods[i] == 23:
            if sum(payments[i]) >= 900000 and sum(payments[i][1:]) + estimates[i] < 900000:
                cntX += 1
                continue
        if periods[i] == 59:
            if sum(payments[i]) >= 600000 and sum(payments[i][1:]) + estimates[i] < 600000:
                cntX += 1
                continue
        if 60 > periods[i] >= 24:
            if sum(payments[i][1:]) + estimates[i] < 900000 and sum(payments[i]) >= 900000:
                cntX += 1
                continue
        if periods[i] >= 60:
            if sum(payments[i][1:]) + estimates[i] < 600000:
                if sum(payments[i]) >= 600000:
                    cntX += 1
                    continue

    return [cntO, cntX]
