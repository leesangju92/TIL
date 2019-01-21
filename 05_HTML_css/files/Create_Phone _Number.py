def create_phone_number(n):
    n_string = ""
    for number in n:
        n_string += str(number)
        
    return "({}) {}-{}".format( n_string[0:3], n_string[3:6], n_string[6:])