from types import MethodType

def run(self, speed = 1):
    f_speed = speed*3
    print('your speed is', f_speed)

class man(object):
    pass
man.speed = run
jax = man()
jax.speed = MethodType(run, jax)
jax.speed(6)
jack = man()
jack.speed()
