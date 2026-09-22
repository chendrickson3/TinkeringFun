import math


def cylider_calcs(height, radius):
    """Calculate the surface area and volume of a cylinder."""

    surface_area = 2 * math.pi * radius**2 + 2 * math.pi * radius * height
    volume = math.pi * radius**2 * height

    return surface_area, volume

surface_area, volume = cylider_calcs(1,3)
print(f"surface_area = {surface_area} and volume ={volume}")
