class Personel:
    def __init__(self, adi, departmani, calismayili, maas):
        self.adi = adi
        self.departmani = departmani
        self.calismayili = calismayili
        self.maas = maas


class Firma:

    def __init__(self):
        self.personel_listesi: list[Personel] = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for i in self.personel_listesi:
            print(i.adi, i.departmani, i.calismayili, i.maas)

    def maas_zammi(self, personel, zam_orani):
        yeni_maas = personel.maas * (zam_orani / 100 + 1)
        print(yeni_maas)

    def personel_cikart(self, personel):
        self.personel_listesi.remove(personel)
