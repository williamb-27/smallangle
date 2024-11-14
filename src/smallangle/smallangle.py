import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    """ The smallangle command and the subcommand sin and tan generate lists of values between 0 and 2pi
        and their corresponding sine and tangent values.
        Using the option -n you can set the amount of steps between 0 and 2pi.
        Without the option -n the programme uses the default value of 10 steps
    """
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 10,
    help = "choose the number of steps between 0 and 2pi",
    show_default=True
)
def sin(number):
    """returns a list of sine values between 0 and 2pi

    Args:
        number (int): the list contains this amount of calculations between 0 and 2pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default = 10,
    help = "choose the number of steps between 0 and 2pi",
    show_default=True
)
def tan(number):
    """returns a list of tangent values between 0 and 2pi

    Args:
        number (int): the list contains this amount of calculations between 0 and 2pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    sin(10)