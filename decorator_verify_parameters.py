def verify_args_not_none(func):
    """Decorator wrapper method."""

    def inner(*args):
        """Method which verifies argument not none.
        If all of the args is None then call does not
        return to the caller.
        If all of the args are not None then call returns
        to the caller."""
        for arg in args:
            print("Argument: ", arg)
            if not arg:
                return None
        return func(*args)

    return inner


@verify_args_not_none
def verify_deco(var1, var2):

    print('Inside verify_deco method')


verify_deco(None, 'var2')
# prints -> Argument:  None


verify_deco('None', 'var2')
# prints ->
# Argument:  None
# Argument:  var2
# Inside verify deco method

verify_deco('var1', None)
# prints ->
# Argument:  var1
# Argument:  None
