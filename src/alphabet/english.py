class englishString:
    def small():
        return 'abcdefghijklmnopqrstuvwxyz'

    def smallAndBig():
        return englishString.small() + englishString.small().upper()

    def commonChars():
        return englishString.smallAndBig() + '!@#$%^&*()_+=-;.,:№"{}[]|\\?/<>~`±§¡™£¢∞¶•ªº≠œ∑´®†¥¨ˆøπ“‘åß∂ƒ©˙∆˚…æ«Ω≈ç√∫˜ \n' + "'"
