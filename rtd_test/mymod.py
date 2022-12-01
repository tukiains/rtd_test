import netCDF4


def myfun(x: str | float) -> int:
    """
    Args:
        x: blabla
    Returns:
        Something..

    Notes:
        jee, joo

    """
    y = netCDF4.Dataset
    if isinstance(x, float):
        return int(x * 2)
    else:
        return 23


myfun(2)
