from typing import List


def intToRoman(num:int) -> str:
    """
    :type num: int
    :rtype: str
    """
    ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    hrns = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    ths =["","M","MM","MMM"]
    result = ths[int(num/1000)] + hrns[int((num%1000)/100)] + tens[int((num%100)/10)] + ones[int(num%10)]
    return result.strip()


# print(intToRoman(3))
# print(intToRoman(10))
# print(intToRoman(200))

print(intToRoman(4))