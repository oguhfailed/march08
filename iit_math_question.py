"""
IIT JEE Math Question — Classic Problem

Question (IIT JEE 2010, Paper 2):
-----------------------------------
Let f be a real-valued differentiable function defined on R (the set of all real
numbers) such that f(1) = 1. If the y-intercept of the tangent drawn to the curve
y = f(x) at any point (x, f(x)) is equal to the cube of the abscissa of that point,
then the value of f(-3) is equal to _____.

That is, the tangent at (x, f(x)) has y-intercept = x^3.

Solution:
---------
The equation of the tangent at point (x, f(x)) is:
    Y - f(x) = f'(x) * (X - x)

Setting X = 0 to find the y-intercept:
    Y = f(x) - x * f'(x)

Given that this y-intercept equals x^3:
    f(x) - x * f'(x) = x^3

Rearranging:
    x * f'(x) - f(x) = -x^3

Dividing both sides by x^2:
    [x * f'(x) - f(x)] / x^2 = -x

This is equivalent to:
    d/dx [f(x) / x] = -x

Integrating both sides:
    f(x) / x = -x^2 / 2 + C

So:
    f(x) = -x^3 / 2 + Cx

Applying the initial condition f(1) = 1:
    1 = -1/2 + C
    C = 3/2

Therefore:
    f(x) = -x^3/2 + (3/2)x

Finding f(-3):
    f(-3) = -(-3)^3 / 2 + (3/2)(-3)
           = -(-27) / 2 + (-9/2)
           = 27/2 - 9/2
           = 18/2
           = 9
"""

def f(x):
    """
    The function satisfying the IIT JEE condition.
    f(x) = -x^3/2 + (3/2)x
    """
    return -x**3 / 2 + (3 / 2) * x


def tangent_y_intercept(x):
    """
    Returns the y-intercept of the tangent to f at point x.
    Should equal x^3 by the problem's condition.
    """
    # f'(x) = -3x^2/2 + 3/2
    f_prime = -3 * x**2 / 2 + 3 / 2
    return f(x) - x * f_prime


# Verification
if __name__ == "__main__":
    print("IIT JEE 2010 — Classic Tangent Problem")
    print("=" * 45)
    print(f"f(x) = -x³/2 + (3/2)x")
    print()

    print("Verify initial condition f(1) = 1:")
    print(f"  f(1) = {f(1)}")
    print()

    print("Verify y-intercept condition (should equal x³ at each x):")
    for x in [1, 2, -1, -2, 3]:
        yi = tangent_y_intercept(x)
        print(f"  x = {x:2d} | y-intercept = {yi:7.2f} | x³ = {x**3:7.2f} | Match: {abs(yi - x**3) < 1e-9}")
    print()

    print("Answer:")
    print(f"  f(-3) = {f(-3)}")
