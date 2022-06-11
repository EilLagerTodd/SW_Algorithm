def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + ""
    return result.strip()


def solution(s):

    if s.isnumeric():
        return int(s)

    word = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    list = []
    number_str = []

    for i in s:
        if i.isnumeric():
            list.append(i)
        else:
            number_str.append(i)
            result = ''.join(s for s in number_str)
            value = word.get(result)
            if value == None:
                continue
            else:
                list.append(str(word[result]))
                number_str = []

    number = listToString(list)

    return int(number)


s = "one4seveneight"
print(solution(s))
