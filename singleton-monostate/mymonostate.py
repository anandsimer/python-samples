"""
In this module we will see the how the state of an Monostate class
is shared among its all reference objects.
"""


class Borg:
    """simplistic borg example from python cookbook.
    Borg is solution to the singleton design pattern
    in which all the instances of the subclass of this
    Borg class share state and behaviour."""

    _shared_state = {}
    """Also, if you want instances of your class to share state
    among themselves but not with instances of other subclasses
    of Borg, make sure that your class has the statement:
    
    _shared_state = {}
    
    in class scope so that it doesnt inherit the_shared_state
    attribute fromBorg but rather overrides it.
    It’s to enable this usage that Borg’s __init__ method refers
    to self._shared_state instead of Borg._shared_state.
    
    credit: Alex Martelli
    """

    def __init__(self):
        self.__dict__ = self._shared_state


class MyBorg(Borg):
    """Monostate class with inheriting Borg class.
    """

    def __init__(self, ids: str = None):
        """Constructor, while instantiating this MyBorg class object
        we will be passing different strings to the ids and two or more
        reference objects state will be compared based on instance variable
        'ids' below.
        """

        Borg.__init__(self)  # call to super class
        self.ids = ids


class MyBoringClass:

    @staticmethod
    def make_object_references():
        """In this method we are making reference variables to the Monostate
        class object and using the print statements to describe the state of
        the Monostate class object by printing its instance variable 'ids'.
        """

        a = MyBorg('simer')
        print(f'ids in a reference variable a.ids: {a.ids}')
        # print -> ids in a reference variable a.ids: simer

        b = MyBorg('anand')
        print(f'ids in a reference variable b.ids: {b.ids}')
        # print -> ids in a reference variable b.ids: anand

        print(f'Is "a" and "b" reference same?.. {a == b}')
        # print -> Is "a" and "b" reference same?.. False

        print(f'ids in a reference variable a.ids: {a.ids}')
        # print -> ids in a reference variable a.ids: anand


if __name__ == '__main__':
    MyBoringClass.make_object_references()
