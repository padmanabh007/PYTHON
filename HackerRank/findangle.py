import math
degree_sign = u"\N{DEGREE SIGN}"
ab=int(input())
bc=int(input())
print(str(int(round(math.degrees(math.atan2(ab,bc)))))+degree_sign)