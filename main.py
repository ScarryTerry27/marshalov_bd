import random
import numpy
import pandas as pd


class TABLE1:
    columns = [
        "Пол", "Возраст", "Рост",  "Вес, кг", "Образование", 'Соц.статус', "ASA", "АГ", 'СН', 'Курение', 'ААНК',
        'Варикоз', "СД", "GLU", "ХБП", 'Г-з травмы', 'Тип травмы', "ЦВЗ", "Аритмии", 'АСТМА', 'ХОБЛ', "c",
        "2лод", "3лод", "Над суставной", "Межсуставной", "Вывих", "HGB", "WBC", "FBG", "CRT", 'NEUT', 'ALB', "N_PAR",
        "t до опер.", "t опер", "Поверх.осложнения", "Глубокие осложнения", "Инф.осложнения", "Отек", "t активизации",
        "ПТА"]

    def __init__(self, count):
        self.df = pd.DataFrame(columns=self.columns)
        self.count = count
        self.hgb = iter(numpy.random.normal(118, 9, size=(1, count))[0])
        self.wbc = iter(numpy.random.normal(11.2, 2.2, size=(1, count))[0])
        self.fib = iter(numpy.random.normal(5.29, 0.52, size=(1, count))[0])
        self.crt = iter(numpy.random.normal(90, 10, size=(1, count))[0])
        self.neut = iter(numpy.random.normal(75, 2.1, size=(1, count))[0])
        self.alb = iter(numpy.random.normal(35, 2.5, size=(1, count))[0])
        self._3lod = iter(numpy.random.normal(73, 5.5, size=(1, count))[0])
        self.t_act_normal = iter(numpy.random.normal(16, 1.8, size=(1, count*3))[0])
        self.np = []
        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        self.count4 = 0
        self.count5 = 0
        self.count6 = 0

    def create_table(self):
        c1 = self.c1()
        c = self.s_v(c1)
        lod = self._lod(c1)

        table = [[pol := self.pol_zav(), old := self.old_zav(pol), self.rost_zav(pol), ves := self.ves_zav(),
                  self.edu(), self.pr_t(old), self.asa_zav(old), self.ag(old, ves), self.sn(old),
                  self.smoke_zav(pol), self.ank(old), self.v_z(), *self.sd(), self.hbp(old), self.char(),
                  self.tip(), 0, 0, 0, 0, c1 := self.c1(), *(self._lod(c1)), *(c := self.s_v(c1)), *(self.lab()),
                  self.data_op(), self.t_op(c[1]), z1 := self.pov_inf(), z2 := self.gl_inf(z1), z := int(bool(z1 + z2)),
                  self.otek(z), t:= self.t_active(z), self.pta(t)]
                 for _ in range(self.count)]
        new_data = pd.DataFrame(table, columns=self.columns)
        return pd.concat([self.df, new_data], ignore_index=True)

    @staticmethod
    def stat(lst, sm, avg):
        print(f"MAX: {max(lst)}")
        print(f"MIN: {min(lst)}")
        print(f"SIGMA: {sm}")
        print(f"AVG: {avg}")

    @staticmethod
    def edu():
        x = random.randint(1, 100)
        if x > 21.4:
            return 0
        return 1

    @staticmethod
    def pr_t(old):
        if 25 > old:
            x = random.randint(1, 100)
            if x > 40:
                return 0
        if old > 60:
            x = random.randint(1, 100)
            if x > 60:
                return 0
        return 1

    @staticmethod
    def old_zav(pol):
        x = random.randint(1, 100)
        if pol == 'М':
            if x < 51:
                return random.randint(18, 30)
            elif x < 86:
                return random.randint(31, 45)
            else:
                return random.randint(46, 65)
        else:
            if x < 25:
                return random.randint(18, 47)
            elif x < 70:
                return random.randint(44, 58)
            else:
                return random.randint(59, 65)

    @staticmethod
    def pol_zav():
        return ["Ж", "М"][random.randint(1, 100) > 57.1]

    @staticmethod
    def rost_zav(pol):
        x = random.randint(1, 100)
        if pol == 'М':
            if x < 40:
                return random.randint(162, 166)
            elif x < 80:
                return random.randint(167, 179)
            return random.randint(180, 187)
        else:
            if x < 40:
                return random.randint(162, 166)
            elif x < 80:
                return random.randint(167, 177)
            return random.randint(178, 187)

    @staticmethod
    def ves_zav():
        x = random.randint(1, 100)
        if x < 86:
            return random.randint(56, 100)
        elif x < 93:
            return random.randint(100, 132)
        return random.randint(49, 55)

    @staticmethod
    def asa_zav(old):
        x = random.randint(1, 100)
        if old < 25:
            return 1
        if x < 80:
            return 2
        return 3

    @staticmethod
    def ag(old, pg):
        x = random.randint(1, 100)
        if x > 35:
            y = random.randint(1, 100)
            if old > 45 or pg > 95:
                if y > 15:
                    return 1
            else:
                if y <= 15:
                    return 1
        return 0

    @staticmethod
    def sn(old):
        y = random.randint(1, 100)
        if old > 60 and y > 55:
            return 1
        return 0

    @staticmethod
    def char():
        x = random.randint(1, 100)
        if x < 4:
            return "Спортивная"
        elif x < 22:
            return "Дорожная"
        return 'Падение'

    @staticmethod
    def smoke_zav(pol):
        x = random.randint(1, 100)
        if pol == 'М':
            if x <= 40:
                return 1
        else:
            if x <= 20:
                return 1
        return 0

    @staticmethod
    def ank(old):
        y = random.randint(1, 100)
        if old > 60 and y > 70:
            return 1
        return 0

    @staticmethod
    def v_z():
        y = random.randint(1, 100)
        if y < 22:
            return 1
        return 0

    @staticmethod
    def sd():
        y = random.randint(1, 100)
        if y < 5:
            return 1, random.randint(7, 14) + random.randint(1, 10)/10
        return 0, random.randint(3, 5) + random.randint(1, 10)/10

    @staticmethod
    def hbp(old):
        y = random.randint(1, 100)
        if old > 45 and y > 65:
            return 1
        return 0

    @staticmethod
    def tip():
        x = random.randint(1, 100)
        if x < 56:
            return "Ч-з_д"
        elif x < 89:
            return "Над_синтез"
        return 'Задний вывих'

    @staticmethod
    def c1():
        x = random.randint(1, 100)
        if x < 41:
            return 1
        elif x < 91:
            return 2
        return 3

    @staticmethod
    def _lod(c1):
        x = random.randint(1, 100)
        if c1 == 1:
            return 0, 1
        elif c1 == 2:
            return [(1, 0), (0, 1)][x < 91]
        elif c1 == 3:
            return 1, 0

    @staticmethod
    def s_v(c1):
        x = random.randint(1, 100)
        if c1 == 3:
            return [(1, 0, 0), (1, 0, 1)][x <= 10]
        else:
            return [(0, 1, 0), (0, 1, 1)][x <= 10]

    @staticmethod
    def kt_0():
        pass

    @staticmethod
    def kt_1():
        pass

    @staticmethod
    def kt_2():
        pass

    @staticmethod
    def kt_3():
        pass

    @staticmethod
    def kt_4():
        pass

    @staticmethod
    def active(otek, hgb, wbc, fib, crt, net, alb):
        pass

    def lab(self):
        hgb = round(next(self.hgb))
        wbc = round(next(self.wbc), 2)
        fib = round(next(self.fib), 2)
        crt = round(next(self.crt))
        neut = round(next(self.neut), 1)
        alb = round(next(self.alb), 1)
        self.np.append(round(neut / alb, 2))
        pcz = [hgb, wbc, fib, crt, neut, alb, round(neut / alb, 2)]
        return pcz

    @staticmethod
    def data_op():
        x = random.randint(1, 100)
        if x < 87:
            return 2
        elif x < 97:
            return 1
        else:
            return 3

    def t_op(self, char):
        if char == 1:
            return round(next(self._3lod))
        else:
            return 0

    def t_active(self, z):
        if z:
            return random.randint(36, 48)
        return round(next(self.t_act_normal))

    def pov_inf(self):
        np = self.np[-1]
        x = random.randint(1, 100)
        if np > 2.3:
            if x < 67:
                self.count1 += 1
                if self.count1 <= 69:
                    return 1
        elif np > 1.8:
            if 10 >= x:
                self.count2 += 1
                if self.count2 <= 13:
                    return 1
        elif x >= 94:
            self.count2 += 1
            if self.count2 <= 13:
                return 1
        return 0

    def gl_inf(self, z1):
        if z1:
            return 0
        np = self.np[-1]
        x = random.randint(1, 100)
        if np > 2.3:
            if x < 80:
                self.count3 += 1
                if self.count3 <= 26:
                    return 1
        elif np > 1.8:
            if 20 >= x:
                self.count4 += 1
                if self.count4 <= 6:
                    return 1
        elif x >= 90:
            self.count4 += 1
            if self.count4 <= 6:
                return 1
        return 0

    def otek(self, z):
        if not z:
            return round(random.uniform(1.8, 4.2), 2)
        return round(random.uniform(4.2, 4.9), 2)

    def pta(self, t):
        x = random.randint(1, 100)
        if t > 35:
            if self.count5 <= 26:
                self.count5 += 1
                return 1
        elif self.count6 <= 6:
            self.count6 += 1
            return 1
        return 0


df = TABLE1(654)
df = df.create_table()
df.to_excel("output.xlsx", index=False)
print(df)
