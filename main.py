class Ekspоnat:
    def __init__(self, nom, yil):
        self.nom = nom
        self.yil = yil

    def __repr__(self):
        return f"{self.nom} ({self.yil})"


class Muzey:
    def __init__(self):
        self.ekspоnatlar = []

    def ekspоnat_qosh(self, ekspоnat):
        self.ekspоnatlar.append(ekspоnat)

    def yil_ekspоnatlari(self, yil):
        return [e for e in self.ekspоnatlar if e.yil == yil]

e1 = Ekspоnat("Qadimiy sopol idish", 1850)
e2 = Ekspоnat("Oltin taqinchoq", 1920)
e3 = Ekspоnat("Qo‘lyozma kitob", 1850)

muzey = Muzey()
muzey.ekspоnat_qosh(e1)
muzey.ekspоnat_qosh(e2)
muzey.ekspоnat_qosh(e3)

print("Barcha ekspоnatlar:", muzey.ekspоnatlar)
print("1850-yildagi ekspоnatlar:", muzey.yil_ekspоnatlari(1850))
