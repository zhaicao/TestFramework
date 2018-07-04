# 送礼物接口
class GiveGift(object):
    # 送洋娃娃
    def GiveDolls(self):
        pass
     # 送花
    def GiveFlowers(self):
         pass

    # 送巧克力
    def GiveChocolate(self):
         pass


# 被追求者类
class SchoolGirl(object):
     def __init__(self, name):
         self.name = name


# 追求者类
class Pursuit(GiveGift):
    def __init__(self, Girl):
        self.Girl = Girl

    def GiveDolls(self):
         print(self.Girl.name, '送你洋娃娃')

    def GiveFlowers(self):
        print(self.Girl.name, '送你花')

    def GiveChocolate(self):
        print(self.Girl.name, '送你巧克力')


# 代理类
class Proxy(GiveGift):
    def __init__(self, Girl):
        self.proxy = Pursuit(Girl)

    # 送洋娃娃
    def GiveDolls(self):
        self.proxy.GiveDolls()

    # 送花
    def GiveFlowers(self):
        self.proxy.GiveFlowers()

    # 送巧克力
    def GiveChocolate(self):
        self.proxy.GiveChocolate()


if __name__ == '__main__':
    jiaojiao = SchoolGirl('jiaojiao')
    daili = Proxy(jiaojiao)
    daili.GiveDolls()
    daili.GiveFlowers()
    daili.GiveChocolate()