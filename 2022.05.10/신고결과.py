def solution(id_list, report, k):
    answer = [] * len(id_list)
    lst = {}
    check = {}
    user = id_list

    report_set = list(set(report))

    for i in report_set:
        x, y = i.split()

        if x not in check:
            check[x] = 1
        else:
            check[x] += 1

        if x not in lst:
            lst[x] = [y]
        else:
            if x not in lst[y]:
                lst[x] += y

    for id_, n in check.items():
        if n >= k:
            for user, user2 in lst.items():
                if id_ in user2:
                    answer[id_list.index(user)] += 1

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo",
                                                    "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
