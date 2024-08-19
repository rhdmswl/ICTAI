from googletrans import Translator

def translate_text(text, target_lang='ko'):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text

def select_translation_option():
    print("번역할 옵션을 선택하세요:")
    print("1: 한국어 -> 영어")
    print("2: 영어 -> 한국어")
    print("3: 한국어 -> 일본어")
    option = input("옵션 번호를 입력하세요 (1 또는 2 또는 3): ")
    return option


def perform_translation_5():
    korean_text = input("번역할 한국어 문장을 입력하세요: ")
    english_translation = translate_text(korean_text, target_lang='en')
    japanese_translation = translate_text(korean_text, target_lang='ja')
    french_translation = translate_text(korean_text, target_lang='fr')
    chinese_translation = translate_text(korean_text, target_lang='zh-cn')
    spanish_translation = translate_text(korean_text, target_lang='es')
    dutch_translation = translate_text(korean_text, target_lang='nl')
    print(f"\n한국어: {korean_text}")
    print(f"영어 번역: {english_translation}")
    print(f"일본어 번역: {japanese_translation}")
    print(f"프랑스어 번역: {french_translation}")
    print(f"중국어 번역: {chinese_translation}")
    print(f"스페인어 번역: {spanish_translation}")
    print(f"네덜란드어 번역: {dutch_translation}")


def translation():
    print("번역할 언어 번호를 선택하세요: ")
    print("1 : 영어")
    print("2 : 일본어")
    print("3 : 프랑스어")
    print("4 : 중국어")
    print("5 : 스페인어")
    print("6 : 네덜란드어")
    print("7 : 이탈리아어")
    print('8 : 독일어')
    print('9 : 러시아어')
    langages = {
        '1' : ('en', '영어'),
        '2' : ('ja', '일본어'),
        '3' : ('fr', '프랑스어'),
        '4' : ('zh-ch', '중국어'),
        '5' : ('es', '스페인어'),
        '6' : ('nl', '네덜란드어'),
        '7' : ('it', '이탈리어아어'),
        '8' : ('de', '독일어'),
        '9' : ('ru', '러시아어')
    }

    option = input("번역할 언어 번호를 입력하세요")
    korean_text = input("번역할 한국어 문장을 입력하세요: ")
    
