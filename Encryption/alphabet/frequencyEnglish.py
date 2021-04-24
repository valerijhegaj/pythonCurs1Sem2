class frequencyEnglish:
    def getFrequency():
        frequency = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094]
        frequency+= [6.966, 0.153, 0.772, 4.025,  2.406, 6.749, 7.507, 1.929]
        frequency+= [0.095, 5.987, 6.327, 9.056,  2.758, 0.978, 2.360, 0.150]
        frequency+= [1.974, 0.074]
        for i in range(len(frequency)):
            frequency[i] /= 100
        return frequency
