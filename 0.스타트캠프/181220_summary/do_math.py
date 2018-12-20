print(__name__)

# import math_functions

# math_functions.cube(5)
# math_functions.average([10,20,30])

from math_functions import cube,average
#여기서 import한 파일에서 print(__name__)하면 __main__이 아닌 해당 파일이름이 나온다.



print(average([10,20,30]))
print(cube(5))