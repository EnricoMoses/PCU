import my_package.package1.my_math
print(my_package.package1.my_math.add(1,2))

from my_package import package1
print(package1.my_math.add(1, 2))

from my_package.package1.my_math import add
print(add(1, 2))

