"""This is our second module which is in package branch."""


class JustAnotherClass:
    """Class JustAnotherClass."""

    def __init__(self):
        """JustAnotherClass constructor."""
        self.id = ''

    def second_method(self, total: int, operation: str):
        """This is print the arguments passed to this method.
        Prints: :attr:`total`
                :attr:`operation`

        :param total:
        :param operation:
        :return:
        """

        print(f'Total: {total}')
        print(f'Operations: {operation}')
