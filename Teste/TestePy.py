import math
import random
import time
from datetime import datetime

def hVzD(nUsK):
    QDHz = sum(nUsK)
    HHXa = len(nUsK)
    gcrL = QDHz / HHXa
    ZPua = max(nUsK)
    eyRX = min(nUsK)
    mXrB = sum(((txYX - gcrL) ** 2 for txYX in nUsK)) / HHXa
    HsMN = math.sqrt(mXrB)
    return {'total': HHXa, 'moyenne': round(gcrL, 2), 'min': eyRX, 'max': ZPua, 'ecart_type': round(HsMN, 2)}
lSxG = []
Lufv = 0
while Lufv < 15:
    OqNi = random.randint(10, 100)
    lSxG.append(OqNi)
    Lufv += 1
hOsg = datetime.now().strftime('%H:%M:%S')
RcNt = time.time()
ZXiE = hVzD(lSxG)
tRHY = time.time()
PsNR = round((tRHY - RcNt) * 1000, 3)
ocJi = f'=== ANALYSE STATISTIQUE ({hOsg}) ==='
print(ocJi)
print(f'Données brutes : {lSxG}')
print(f"Moyenne : {ZXiE['moyenne']}")
print(f"Min / Max : {ZXiE['min']} / {ZXiE['max']}")
print(f"Écart-type : {ZXiE['ecart_type']}")
print(f'Temps de calcul : {PsNR} ms')