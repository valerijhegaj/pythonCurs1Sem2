class EnglishString:
    def small():
        return 'abcdefghijklmnopqrstuvwxyz'

    def small_and_big():
        return EnglishString.small() + EnglishString.small().upper()

    def common_chars():
        return EnglishString.small_and_big() + '!@#$%^&*()_+=-;.,:№"{}[]|\\?/<>~`±§¡™£¢∞¶•ªº≠œ∑´®†¥¨ˆøπ“‘åß∂ƒ©˙∆˚…æ«Ω≈ç√∫˜ \n' + "'"
