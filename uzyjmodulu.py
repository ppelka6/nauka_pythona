# importujemy moduł i nadajemy mu alias

from mytoolkit import matematyczny as mat
from mytoolkit import pomocniczy as pom
#wywołanie funcji/metodyn z mytoolkit/matematyczny (alias: 'mat')

print(mat.dodaj(4, 14))
print(mat.odejmij(10, 5))
#wywołanie funcji/metody z mytoolkit/pomocniczy (alias: 'pom')
pom.czesc()
