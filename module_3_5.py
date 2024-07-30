def get_miltiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_miltiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_miltiplied_digits(40203)
print(result)
