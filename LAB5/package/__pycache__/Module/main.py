if __package__:
    from . import calculator
else:
    # Allows this file to be run directly from an editor as well.
    import calculator

print("Addition =", calculator.add(10, 20))
print("Multiplication =", calculator.multiply(5, 4))
