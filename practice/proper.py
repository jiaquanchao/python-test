# coding:utf8

class Screen(object):

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, wnum):
        self._width = wnum

    @height.setter
    def height(self, hnum):
        self._height = hnum

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
