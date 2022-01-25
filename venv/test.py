import math
import os
import random
import re
import sys


x = int(input())

if x%2==1:
    print("weird")
elif x%2==0 and 1<x<=5:
    print("not weird")
elif x%2==0 and 5<x<=20:
    print("weird")
elif x%2==0 and x<20:
    print("not weird")

