"""This module has one class i.e., EntryClass."""


from branch.justanotherclass import JustAnotherClass


class EntryClass:
    """Class EntryClass."""

    def __init__(self, id_number: int):
        """EntryClass constructor."""
        self.id = id_number

    def first_method(self):
        """
        This method is our very first method of the mysphinx project.

        This method calls :meth:`branch.justanotherclass.second_method`
        :return:
        """

        JustAnotherClass().second_method(self.id, 'ops')


if __name__ == '__main__':
    EntryClass(9).first_method()
