class student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def p(self):
        print('name: %s ; score: %d' % (self.name, self.score))

if __name__=='__main__':
    L = []
    pic = True
    # student = student()
    while pic:
    # student("jax", 99)
        print('name')
        name_input = input()
        print('score')
        score_input = input()
        L.append([name_input, score_input])
        print('go on?')
        i = input()
        i = int(i)
        if i == 0:
            break
    # student.p()
    for ii in range(len(L)):
        print(L[ii-1])
