# @author: Pedro Campos Miranda
# @version: 1.0

def centuryFromYear(year):
    if year<100:
        return 1
    elif year%100!=0:
        return (year//100) + 1
    else:
        return year//100