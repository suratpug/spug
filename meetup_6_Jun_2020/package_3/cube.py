# relative imports are somewhat tricky
# always run it as python module when running at the terminal
# current package
from . import area # noqa

""" 
NOTE: runing this as a script will give you following error: 

ImportError: attempted relative import with no known parent package

run as python -m <parent_package>.<sub_package>.<module_name>

directory structure - 
parent_package
    sub_package_1
        module_1
    sub_package_2
        module_2

"""

print("area of circle is:", round(area.area_circle(5), 2))

def vol_cyl(height, radius):
    return height * area.area_circle(radius)

print("volume of cylinder is:", round(vol_cyl(1, 5), 2))
