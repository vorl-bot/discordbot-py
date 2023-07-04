import random
reward1 = ['코니콘 홀로그램 키링','고양이 열쇠고리','5cm 인형 옷','5cm 코니콘 인형','강아지 열쇠고리','병따개','5cm 곰인형','토끼 열쇠고리','목캔디 한 봉지']
reward2 = ['10cm 코니콘 인형','코니콘 머리띠','쿠키 한 통','10cm 인형 옷','탁상용 알람시계','주사위 세트','코니랜드 디퓨저','인어의 섬 후링']
reward3 = ['코니랜드 우드 퍼즐','코니베이 레고 세트','코니콘 1000pc 퍼즐','20cm 코니콘 인형','20cm 인형 옷','나비 넥타이','인어의 섬 워터볼','고래 인형']
reward4 = ['커다란 펭귄 인형','실물 사이즈 코니콘 인형','1/8 사이즈 한정판 황금색 코니콘 피규어','코니콘 다키마쿠라','힙스터 선글라스','황금색 머니건']

def shootingresult():
    score = random.randrange(0,101)
    
    if score >= 0 and score <= 10:
        st1 = '당신의 점수는... '+str(score)+'점!?'
        st2 = '형편없는 사격이었다... 아무것도 따내지 못했다.'

    if score > 10 and score <= 40:
        reward = random.choice(reward1)
        st1 = '당신의 점수는... '+str(score)+'점!'
        st2 = '그냥저냥 쏜 것 같다. 장려상으로 '+reward+'을(를) 획득했다.'    

    if score > 40 and score <= 70:
        reward = random.choice(reward2)
        st1 = '당신의 점수는... '+str(score)+'점!'
        st2 = '무난하게 잘 쏜 것 같다. 3등상으로 '+reward+'을(를) 획득했다.'   

    if score > 70 and score <= 90:
        reward = random.choice(reward3)
        st1 = '당신의 점수는... '+str(score)+'점!'
        st2 = '이 정도면 제법 잘 쏜 것 같다. 2등상으로 '+reward+'을(를) 획득했다.'   
    
    if score > 90 and score <= 100:
        reward = random.choice(reward4)
        st1 = '당신의 점수는... '+str(score)+'점!?'
        st2 = '굉장해! 무척 깔끔하게 잘 쏜 것 같다. 1등상으로 '+reward+'을(를) 획득했다.'

    return st1, st2