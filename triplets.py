import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    foo = bar = 0
    for i in range(3):
        if a[i] > b[i]:
            foo += 1
        elif a[i] < b[i]:
            bar += 1
    return foo, bar

    