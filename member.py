import random

members = ['구구','눈누난나','닝닝','레테','루치','버섯P','베베','블랑','사샤','사수','아라매','오베론','위니','윈터','중복닉','총상백','칸타렐라','클로티드','킹마드','팅커벨']

getarti = []

def LucheiSkill():
    while len(getarti) < 4:
        getarti = getarti + random.choice(members)

    return getarti