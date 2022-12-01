import netCDF4


def myfun(x: str | float):
    """
    Args:
        x (int): blabla
    Returns:
        int: jotain

    Notes:
        jee, joo

    """
    y = netCDF4.Dataset
    if isinstance(x, float):
        return x * 2
    else:
        return 23


myfun(2)
