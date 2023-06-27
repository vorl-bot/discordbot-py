import fishing
text1 =''
text2 =''


def fisht1():
    fish_result = fishing.getFish()
    
    if fish_result == '실패':
        text1 = '이런!'

    elif fish_result == '직박구리 씨':
        text1 = '바닷속을 점검하던 직박구리 씨?!'

    elif fish_result == '쓰레기' or fish_result =='돌멩이' or fish_result =='1아티' or fish_result =='유리병':
        text1 = fish_result+'을(를) 낚았다!'
        
    elif fish_result == '고래상어' or fish_result =='철갑상어' or fish_result =='실러캔스' or fish_result =='피라루쿠' or fish_result =='청상아리' or fish_result =='청새치' or fish_result =='킹크랩' or fish_result =='거대오징어' or fish_result =='크라켄'or fish_result == '대왕참치':
        fsize = fsize + 100

        text1 = fish_result+'을(를) 낚았다!'
    
    else:
        text1 = fish_result+'을(를) 낚았다!'

    return text1
        

def fisht2():
    fsize = fishing.sizing()
    
    if fish_result == '실패':
        text2 = '물고기가 도망갔다. 아무것도 낚지 못했다...'

    elif fish_result == '직박구리 씨':
        text2 = '\"삐이이익!!!! 파티서펀트!!!!! 이것은 공무집행방해입니다!!!!\" 직박구리 씨는 호통을 치고 날아갔다...'

    elif fish_result == '쓰레기' or fish_result =='돌멩이' or fish_result =='1아티' or fish_result =='유리병':
        text2 = '물고기가 아니잖아!'
        
    elif fish_result == '고래상어' or fish_result =='철갑상어' or fish_result =='실러캔스' or fish_result =='피라루쿠' or fish_result =='청상아리' or fish_result =='청새치' or fish_result =='킹크랩' or fish_result =='거대오징어' or fish_result =='크라켄'or fish_result == '대왕참치':
        fsize = fsize + 100

        text2 = '성과 기록: 무려 '+str(fsize)+'cm?!'
    
    else:
        text2 = '성과 기록: '+str(fsize)+'cm'

    return text2
