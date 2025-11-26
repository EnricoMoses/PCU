def analisa(d):
    number = []
    longest_string = ""
    values_type = {
    }
    for i in list(d.values()):
        if i == "True":
            i = True

        elif i == "False":
            i = False
        else:
            try:
                i = int(i)
                number.append(i)
            except:
                try:
                    i = float(i)
                    number.append(i)
                except:
                    try:
                        if len(i) > len(longest_string):
                            longest_string = i
                    except:
                        pass

        if type(i).__name__ not in values_type:
            values_type[type(i).__name__] = 1
        else:
            values_type[type(i).__name__] += 1

    print(number)

    return {
        'numeric_sum': sum(number),
        'numeric_avg': sum(number) / len(number),
        'longest_string': longest_string,
        'values_type': values_type
    }


dictionary = {"a": "5", "b": "2.5", "c": "python", "d": "ai", "e": "True"}

print(analisa(dictionary))
