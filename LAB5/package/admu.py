if __package__:
    from .addition import add
    from .multi import multi
else:
    # Allows this file to be run directly from an editor as well.
    from addition import add
    from multi import multi

print("Addition =", add(10, 20))
print("Multiplication =", multi(5, 4))
