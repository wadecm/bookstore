from django.test import TestCase

# Create your tests here.
def deco(func):
     def inner():
         print('running inner()')
     return inner
@deco
def target():
    print('running target()')
print(target)

# <function deco.<locals>.inner at 0x10063b598>