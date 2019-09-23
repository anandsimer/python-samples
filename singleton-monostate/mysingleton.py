"""
In this module we are going to see how the state of the
singleton class behaves when dealing with mutliple
objects creation of the singleton class.
"""


from singleton_decorator import singleton


@singleton
class MySingleton:
    """Singleton class"""

    def __init__(self, ids: str = None):
        """Constructor, while instantiating this MySingleton class object
        we will be passing different strings to the ids and two or more
        reference objects state will be compared based on instance variable
        'ids' below.
        """

        self.ids = ids


class MySecondClass:

    @staticmethod
    def make_object_reference():
        """In this method we are making reference variables to the singleton
        class object and using the print statements to describe the state of
        the singleton class object by printing its instance variable 'ids'.
        """

        a = MySingleton('simer')
        print(f'ids in a reference variable a.ids: {a.ids}')
        # print -> ids in a reference variable a.ids: simer

        b = MySingleton('anand')
        print(f'ids in a reference variable b.ids: {b.ids}')
        # print -> ids in a reference variable b.ids: simer

        print(f'Is "a" and "b" reference same?.. {a == b}')
        # print -> Is "a" and "b" reference same?.. True

        print(f'ids in a reference variable a.ids: {a.ids}')
        # print -> ids in a reference variable a.ids: simer


if __name__ == '__main__':
    MySecondClass.make_object_reference()
