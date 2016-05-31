# coding:utf8
class man(object):
    def color(self):
        print("不同人肤色不同")

    def height(self):
        print("different height")

    def language(self):
        print("a lot of kinds")

class usa(man):
    def color(self):
        print("白色，黑色")
    def language(self):
        print('english')

class china(man):
    def color(self):
        print('yellow')
    def language(self):
        print('chinese')

def tt(man):
    man.language()

if __name__ == '__main__':
    man = man()
    usa = usa()
    china = china()
    man.language()
    man.color()
    usa.language()
    usa.color()
    china.language()
    china.color()
    china.height()
    tt(china)
