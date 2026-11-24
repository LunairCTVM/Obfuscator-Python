import math as m
import random
import time
import numpy as np
qXkV = 8
MnPj = 30
zGLb = 2
XIlf = 1.4
QcTA = 30
akga = 13.0
pVqB = 0.9
njIx = 2.4
VJWJ = 4.0
SkoB = 5.4
eXHj = 28.0
mmqE = 14.0
BHXs = SkoB + eXHj
TIiq = SkoB + 3.5
gLCF = 26.0
PHPS = 0.78
uyvx, WDcV = (0.3, 0.2)
YNCj = 0.27
Vjlg = 0.098
yGSo = 0.085
nbjH = 1.5
YRBb = ' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
DWSw = len(YRBb) - 1
hnxe = {Ogvl: Fynp for Fynp, Ogvl in enumerate(YRBb)}
vNdd = 24
hMYz = np.random.RandomState(5)
FKhC = random.Random(9)

def sJiA(TpFB, jJzp, RXcw):
    YlSF = np.clip((RXcw - TpFB) / (jJzp - TpFB), 0.0, 1.0)
    return YlSF * YlSF * (3 - 2 * YlSF)

def IwWo(YlSF):
    YlSF = min(max(YlSF, 0.0), 1.0)
    return YlSF * YlSF * (3 - 2 * YlSF)

def gQyV(YlSF):
    return IwWo((YlSF - SkoB) / eXHj)

def MkuP(TpFB, jJzp, APkY):
    return TpFB + (jJzp - TpFB) * APkY

def Brix(jJzp, iulD):
    zNOb = jJzp.shape[0]
    Bcrd = np.arange(iulD) * zNOb / iulD
    MmEL = Bcrd.astype(np.int64) % zNOb
    WdhR = (MmEL + 1) % zNOb
    irnb = Bcrd - np.floor(Bcrd)
    irnb = (irnb * irnb * (3 - 2 * irnb)).astype(np.float32)
    YlSF = jJzp[:, MmEL] * (1 - irnb) + jJzp[:, WdhR] * irnb
    return YlSF[MmEL, :] * (1 - irnb)[:, None] + YlSF[WdhR, :] * irnb[:, None]

def GWRv(iulD, APkY=4.0):
    return np.clip(0.5 + (iulD - iulD.mean()) / (iulD.std() * APkY + 1e-09), 0, 1).astype(np.float32)

def qXZO(iulD, IKkD):
    MxLx = np.zeros((iulD, iulD), np.float32)
    GKIi = 1.0
    for zNOb in IKkD:
        MxLx += GKIi * Brix(hMYz.rand(zNOb, zNOb).astype(np.float32), iulD)
        GKIi *= 0.55
    return GWRv(MxLx)

def cbJS(iulD, zNOb):
    WaAQ = hMYz.rand(zNOb)
    Bcrd = np.arange(iulD) * zNOb / iulD
    MmEL = Bcrd.astype(np.int64) % zNOb
    WdhR = (MmEL + 1) % zNOb
    irnb = Bcrd - np.floor(Bcrd)
    irnb = irnb * irnb * (3 - 2 * irnb)
    return (WaAQ[MmEL] * (1 - irnb) + WaAQ[WdhR] * irnb).astype(np.float32)

def RnEl(fogL, QkYw, AKKs):
    iulD = fogL.shape[0]
    kcjw = np.floor(QkYw)
    YlKA = np.floor(AKKs)
    JaaK = QkYw - kcjw
    stUb = AKKs - YlKA
    MmEL = kcjw.astype(np.int32) % iulD
    TcDp = YlKA.astype(np.int32) % iulD
    WdhR = (MmEL + 1) % iulD
    lnZV = (TcDp + 1) % iulD
    return (fogL[TcDp, MmEL] * (1 - JaaK) + fogL[TcDp, WdhR] * JaaK) * (1 - stUb) + (fogL[lnZV, MmEL] * (1 - JaaK) + fogL[lnZV, WdhR] * JaaK) * stUb
print('Preparing textures...')
wkiD = qXZO(1024, (6, 20, 64, 200))
mYep = qXZO(1024, (8, 24, 64, 160))
LKPK = hMYz.rand(512, 512).astype(np.float32)
Zvps = qXZO(512, (5, 12, 30))
bjkj = 1 - np.abs(2 * Zvps - 1)
lwVY = qXZO(512, (3, 7, 16))
FFHF = 1 - np.abs(2 * lwVY - 1)
MOLv = 4096
Bfgh = GWRv(0.5 * cbJS(MOLv, 900) + 0.3 * cbJS(MOLv, 300) + 0.2 * cbJS(MOLv, 120), 3.0)
VWZC = GWRv(0.5 * cbJS(MOLv, 700) + 0.3 * cbJS(MOLv, 200) + 0.2 * cbJS(MOLv, 80), 3.0)
tuLQ = GWRv(cbJS(MOLv, 13), 3.0)
nGDT = GWRv(cbJS(MOLv, 48), 3.0)
MqHW = 3200
eZks = hMYz.uniform(-1, 1, MqHW).astype(np.float32)
gwlf = hMYz.uniform(-1, 1, MqHW).astype(np.float32)
FJva = hMYz.uniform(0.06, 1.0, MqHW).astype(np.float32)
YmtX = (0.1 + 0.9 * hMYz.rand(MqHW) ** 3.5).astype(np.float32)
BvsD = hMYz.rand(MqHW, 1).astype(np.float32)
oVqb = MkuP(np.array([0.7, 0.82, 1.0], np.float32), np.array([1.0, 0.8, 0.55], np.float32), BvsD ** 1.5)
HUGm = hMYz.uniform(0, 6.28, MqHW).astype(np.float32)
ZpYX = hMYz.uniform(1.0, 3.5, MqHW).astype(np.float32)
bPvc = [(0.0, 0.0, 0.0)]
DCQp = 1.7
oBPj = random.Random(4)
while DCQp < 40:
    bPvc.append((DCQp, oBPj.uniform(-0.045, 0.045), oBPj.uniform(-0.022, 0.02)))
    DCQp += oBPj.uniform(0.9, 2.4)
eqkI = random.Random(21)
KTvu = []
YIjm = 44
for Fynp in range(YIjm):
    KTvu.append((-0.92 + 1.84 * Fynp / (YIjm - 1), eqkI.uniform(0.92, 1.08), 0.0, 1.0))
Mdfo = []
jffJ = 20
for Fynp in range(jffJ):
    Mdfo.append((-0.7 + 1.4 * Fynp / (jffJ - 1), eqkI.uniform(0.9, 1.1), 0.0, 1.0))
YEIz = {}

def bPzO(QMPH, ulkE, ASCF):
    global JdWu, DmcN, YQNQ, hpFP, ZHJi, WSDh, nxUq, bFnk, rGgO, rWGZ, nShD, mIoQ, ZNjC, COYH, yqiG, TTSh
    JdWu, DmcN = (QMPH, ulkE)
    YQNQ = ASCF
    hpFP = int(ASCF * ulkE * XIlf / QMPH) // 2 * 2
    YQNQ = YQNQ // 2 * 2
    ZHJi, WSDh = (hpFP * JdWu, YQNQ * DmcN)
    nxUq, bFnk = (hpFP * zGLb, YQNQ * zGLb)
    YilM = (np.arange(nxUq, dtype=np.float32) + 0.5) * (JdWu / zGLb)
    Hcet = (np.arange(bFnk, dtype=np.float32) + 0.5) * (DmcN / zGLb)
    rGgO = (((YilM - ZHJi / 2) / WSDh)[None, :] * np.ones((bFnk, 1), np.float32)).astype(np.float32)
    rWGZ = (((Hcet - WSDh / 2) / WSDh)[:, None] * np.ones((1, nxUq), np.float32)).astype(np.float32)
    nShD = np.sqrt(rGgO * rGgO + rWGZ * rWGZ)
    IoBp = (np.arange(hpFP, dtype=np.float32) + 0.5) * JdWu
    tWhj = (np.arange(YQNQ, dtype=np.float32) + 0.5) * DmcN
    mIoQ = (((IoBp - ZHJi / 2) / WSDh)[None, :] * np.ones((YQNQ, 1), np.float32)).astype(np.float32)
    ZNjC = (((tWhj - WSDh / 2) / WSDh)[:, None] * np.ones((1, hpFP), np.float32)).astype(np.float32)
    COYH = np.sqrt(mIoQ * mIoQ + ZNjC * ZNjC)
    omNe, ZXOU = np.mgrid[0:YQNQ, 0:hpFP]
    yqiG = ((omNe * 73856093 ^ ZXOU * 19349663 ^ 1540483477) % 1009 / 1009.0).astype(np.float32)
    YwOp()

def wkot(YlSF, vSeE=VJWJ):
    Fblq = YlSF - vSeE
    if Fblq < 0 or Fblq > 0.36:
        return 0.0
    if Fblq < 0.09:
        return IwWo(Fblq / 0.09)
    if Fblq < 0.12:
        return 1.0
    return 1 - IwWo((Fblq - 0.12) / 0.24)

def GIDD(YlSF):
    APkY = IwWo((YlSF - pVqB) / njIx)
    APkY = APkY * (1 + 0.035 * m.sin(m.pi * APkY))
    return min(1.0, APkY) * (1 - 0.985 * wkot(YlSF))

def VaHH(YlSF, laEg):
    HAhi = (0.0, 0.0)
    Mdik = (0.0, 0.0)
    NTsg = 0.0
    for DciA, YNQO, EWLp in bPvc:
        if DciA <= YlSF:
            HAhi = Mdik
            Mdik = (YNQO, EWLp)
            NTsg = DciA
        else:
            break
    APkY = IwWo((YlSF - NTsg) / 0.09)
    hoPy = HAhi[0] + (Mdik[0] - HAhi[0]) * APkY
    wXgZ = HAhi[1] + (Mdik[1] - HAhi[1]) * APkY
    hoPy += 0.003 * m.sin(YlSF * 1.3)
    wXgZ += 0.002 * m.sin(YlSF * 1.1 + 1)
    GKIi = 1 - IwWo((YlSF - SkoB) / 2.5)
    wXgZ -= 0.03 * wkot(YlSF)
    return (hoPy * GKIi, wXgZ * GKIi)

def YLMW(kcjw, ZUQr):
    JoNU = kcjw / PHPS
    EXVc = 0.88 if JoNU < -0.12 else 1.12
    ADla = max(0.0, 1 - ((JoNU + 0.12) / EXVc) ** 2) ** 0.8
    JkeN = max(0.0, 1 - (JoNU - 0.08) ** 2) ** 0.9
    rTHb = 0.03 * JkeN
    eTLJ = rTHb + (WDcV * JkeN - rTHb) * (0.35 + 0.65 * ZUQr)
    Rixe = eTLJ + (-uyvx * ADla - eTLJ) * ZUQr
    return (Rixe, eTLJ, ADla, JkeN)

def Jirg(YilM, Hcet, NmOQ, Djiu, YlSF):
    SGcE = YilM / NmOQ
    PIZS = -Hcet / NmOQ
    sRpD = RnEl(mYep, SGcE * 16 + 400, PIZS * 16 + 100)
    zJpt = RnEl(mYep, SGcE * 16 + 90, PIZS * 16 + 530)
    SwaR = RnEl(mYep, SGcE * 42 + 300, PIZS * 42 + 700 + YlSF * 0.8)
    nXTN = RnEl(mYep, SGcE * 110 + 80, PIZS * 110 + 200)
    rQws = 1 - 0.65 * Djiu
    AcDL = SGcE + rQws * 0.4 * (sRpD - 0.5) + 0.05 * (SwaR - 0.5)
    YGYD = PIZS + rQws * 0.4 * (zJpt - 0.5) + 0.05 * (SwaR - 0.5)
    APzS = np.sqrt(AcDL * AcDL + YGYD * YGYD) / 0.8 - 1.0
    nWfa = YGYD + 0.12
    anXr = (AcDL * AcDL + nWfa * nWfa - 1.0) ** 3 - AcDL * AcDL * nWfa ** 3
    yTNZ = 0.5 * np.cbrt(anXr)
    gHPD = APzS * (1 - Djiu) + yTNZ * Djiu
    LdUS = np.clip(-gHPD / (0.8 - 0.35 * Djiu), 0, 1)
    APkY = 3.0 + 2.5 * Djiu
    VPXe = np.where(gHPD < 0, 0.5 + 0.5 * np.sqrt(LdUS), np.exp(-np.clip(gHPD, 0, 10) * APkY) * 0.5)
    fogL = 1 + (0.62 + 0.8 * nXTN - 1) * 0.8
    FTRv = np.array([0.92, 0.16, 0.4], np.float32)
    dUQd = np.array([1.0, 0.58, 0.78], np.float32)
    MbXA = MkuP(FTRv, dUQd, (LdUS ** 0.8)[..., None])
    UweE = (VPXe * fogL)[..., None] * MbXA
    VGqF = np.exp(-np.clip(gHPD, 0, 10) * 1.6) * 0.2 * (0.5 + SwaR) * (gHPD > 0)
    UweE = UweE + VGqF[..., None] * np.array([0.78, 0.1, 0.3], np.float32)
    eosi = np.exp(-((gHPD + 0.04) / 0.14) ** 2)
    uOUy = np.clip((RnEl(bjkj, AcDL * 120 + 50, YGYD * 120 + 300 + YlSF * 0.6) - 0.86) * 7, 0, 1)
    BDcQ = np.array([0.95, 0.16, 0.34], np.float32)
    UweE = UweE + (eosi * (0.2 + 0.9 * uOUy) * (0.5 + SwaR))[..., None] * BDcQ
    UweE = UweE + (uOUy * np.clip(-gHPD, 0, 1) * 0.25)[..., None] * BDcQ
    return UweE.astype(np.float32)

def gsqS(YlSF, iUSY, ZUQr, hoPy, wXgZ, QIWj, ngRF):
    FFYr = 1.0 / iUSY
    thOW = FFYr / bFnk
    QkYw = rGgO * FFYr
    AKKs = rWGZ * FFYr
    znkg = iUSY < 3.4
    EubL = QkYw - hoPy
    oKSh = AKKs - wXgZ
    qWGn = np.sqrt(EubL * EubL + oKSh * oKSh)
    MQIZ = None
    if znkg:
        JoNU = QkYw / PHPS
        dmwr = np.clip(JoNU, -1.3, 1.3)
        EXVc = np.where(dmwr < -0.12, 0.88, 1.12)
        ADla = np.clip(1 - ((dmwr + 0.12) / EXVc) ** 2, 0, 1) ** 0.8
        JkeN = np.clip(1 - (dmwr - 0.08) ** 2, 0, 1) ** 0.9
        mRio = AKKs + 0.055 * JoNU
        rTHb = 0.03 * JkeN
        eTLJ = rTHb + (WDcV * JkeN - rTHb) * (0.35 + 0.65 * ZUQr)
        Rixe = eTLJ + (-uyvx * ADla - eTLJ) * ZUQr
        kXGt = mRio - Rixe
        itGN = eTLJ - mRio
        MQIZ = np.minimum(kXGt, itGN)
        Wfpg = np.clip(MQIZ / (1.6 * thOW) + 0.5, 0, 1)[..., None]
    QiBD = (np.arctan2(oKSh, EubL) / (2 * m.pi) % 1.0 * MOLv).astype(np.int32) % MOLv
    CIlN = np.clip((qWGn - QIWj) / (YNCj - QIWj), 0, 1.3)
    YoLX = CIlN * 14
    MmEL = np.floor(YoLX).astype(np.int32)
    QYdy = YoLX - MmEL
    RijA = 0.55 * Bfgh[QiBD] + 0.45 * (VWZC[(QiBD + MmEL * 131) % MOLv] * (1 - QYdy) + VWZC[(QiBD + (MmEL + 1) * 131) % MOLv] * QYdy)
    DpBH = np.arctan2(oKSh, EubL) / (2 * m.pi) % 1.0
    hmEj = np.abs(DpBH * 34 % 1.0 - 0.5) * 2 - 0.5
    ujMI = 0.34 + 0.2 * (tuLQ[QiBD] - 0.5) + 0.035 * hmEj
    KBDh = sJiA(-0.1, 0.22, CIlN - ujMI)[..., None]
    mhms = np.array([0.8, 0.45, 0.1], np.float32)
    aeVo = np.array([0.42, 0.2, 0.06], np.float32)
    ILZm = MkuP(mhms, aeVo, KBDh)
    ILZm = ILZm * (0.45 + 1.05 * RijA)[..., None]
    ILZm += np.array([0.22, 0.11, 0.0], np.float32) * (np.exp(-((CIlN - ujMI) / 0.07) ** 2) * (0.2 + RijA))[..., None]
    ZxTM = (nGDT[QiBD] > 0.72) * sJiA(0.65, 0.18, CIlN)
    ILZm *= (1 - 0.55 * ZxTM)[..., None]
    ILZm *= (1 - 0.82 * sJiA(0.62, 1.0, CIlN))[..., None]
    ILZm *= (0.55 + 0.45 * sJiA(0, 0.07, CIlN))[..., None]
    if znkg:
        ILZm *= (0.3 + 0.7 * sJiA(0, 0.16, kXGt))[..., None]
    if znkg:
        QMPH = sJiA(0.4, 0.95, np.abs(JoNU))
        tlob = (0.38 + 0.62 * sJiA(0, 0.22, kXGt)) * (0.72 + 0.28 * sJiA(0, 0.1, itGN)) * (1 - 0.3 * QMPH)
        pblI = np.array([0.8, 0.82, 0.86], np.float32) * tlob[..., None]
        pblI = MkuP(pblI, np.array([0.86, 0.5, 0.46], np.float32) * tlob[..., None], (QMPH * 0.35)[..., None])
        sGfC = np.clip((RnEl(FFHF, QkYw * 85 + 40, AKKs * 85 + 70) - 0.925) * 14, 0, 1) * (0.25 + 0.75 * QMPH) * sJiA(0.12, 0.32, np.abs(EubL))
        pblI = MkuP(pblI, np.array([0.62, 0.15, 0.14], np.float32), (sGfC * 0.65)[..., None])
        WYJv = np.clip((YNCj - qWGn) / (1.6 * thOW) + 0.5, 0, 1)[..., None]
        HkJe = MkuP(pblI, ILZm, WYJv)
    else:
        HkJe = ILZm
    McWW = QIWj * iUSY
    zfps = 0.25 + 0.75 * sJiA(0, 0.3 * McWW, McWW - nShD)
    YSdg = np.clip((QIWj - qWGn) / (1.6 * thOW) + 0.5, 0, 1)
    HkJe = MkuP(HkJe, ngRF * zfps[..., None], YSdg[..., None])
    ZEux = max(0.0, min(1.0, 1 - (iUSY - 1.6) / 2.4))
    if ZEux > 0:
        HNts = np.sqrt((EubL - 0.075) ** 2 + (oKSh + 0.04) ** 2)
        ilNq = np.clip(1 - (HNts - 0.03) / (1.4 * thOW + 0.004), 0, 1)
        toYn = np.sqrt((EubL + 0.045) ** 2 + (oKSh - 0.05) ** 2)
        CFck = np.clip(1 - (toYn - 0.009) / (1.4 * thOW + 0.003), 0, 1) * 0.5
        HkJe = HkJe + ((ilNq + CFck) * ZEux)[..., None] * np.array([1.0, 0.98, 0.95], np.float32) * 1.4
    if not znkg:
        return (HkJe, YSdg)
    if iUSY < 2.6:
        iten = 0.5 * (Rixe + eTLJ)
        belw = mRio < iten
        EJKq = np.maximum(Rixe - mRio, 0)
        BBke = np.maximum(mRio - eTLJ, 0)
        HNts = np.where(belw, EJKq, BBke)
        YcZu = RnEl(wkiD, QkYw * 120 + 100, AKKs * 120 + 100)
        WaAQ = np.array([0.62, 0.4, 0.29], np.float32)
        VFrt = WaAQ * (0.9 + 0.2 * YcZu)[..., None]
        tlob = 0.5 + 0.5 * sJiA(0, 0.3, HNts)
        tlob *= 1 + 0.1 * np.exp(-((AKKs + 0.2) / 0.09) ** 2)
        RRPn = 0.075 + 0.03 * (1 - ZUQr)
        tlob *= 1 - 0.42 * np.exp(-((EJKq - RRPn) / 0.02) ** 2) * belw
        tlob *= 1 + 0.08 * np.exp(-((BBke - 0.09) / 0.04) ** 2) * ~belw
        VFrt = VFrt * tlob[..., None]
        qFdV = sJiA(RRPn, RRPn * 0.4, EJKq) * belw
        VFrt = MkuP(VFrt, np.array([0.68, 0.4, 0.31], np.float32) * tlob[..., None], (qFdV * 0.5)[..., None])
        ZseZ = np.clip(1 - np.abs(JoNU), 0, 1)
        XFtP = np.exp(-((mRio + 0.42 + 0.1 * JoNU * JoNU) / (0.04 + 0.012 * ZseZ)) ** 2)
        iXIG = 0.55 + 0.9 * RnEl(LKPK, QkYw * 90, AKKs * 30)
        VFrt = MkuP(VFrt, np.array([0.1, 0.06, 0.04], np.float32), np.clip(XFtP * iXIG, 0, 0.92)[..., None])
        USBG = np.exp(-(EJKq / 0.01) ** 2) * belw
        VFrt = MkuP(VFrt, np.array([0.05, 0.03, 0.022], np.float32), np.clip(USBG * (1.0 - 0.3 * ZUQr) * 0.9, 0, 1)[..., None])
        sGji = sJiA(0.014, 0.0, BBke) * ~belw
        VFrt = MkuP(VFrt, np.array([0.74, 0.34, 0.3], np.float32), (sGji * 0.7)[..., None])
        bBNw = np.exp(-((BBke - 0.016) / 0.006) ** 2) * ~belw * (0.35 + 0.65 * RnEl(LKPK, QkYw * 60, AKKs * 60))
        VFrt = VFrt + (bBNw * 0.55)[..., None] * np.array([1.0, 0.85, 0.75], np.float32) * sJiA(0.12, 0.5, ZUQr)
        sVBR = (RnEl(LKPK, QkYw * 150 + 7, AKKs * 150 + 3) > 0.985) * 0.35 * (0.4 + YcZu) * sJiA(0.0, 0.3, HNts)
        VFrt = VFrt + sVBR[..., None] * np.array([1.0, 0.9, 0.8], np.float32)
        UweE = MkuP(VFrt, HkJe, Wfpg)
        YboB = np.exp(-(((QkYw + PHPS * 0.9) / 0.045) ** 2 + ((mRio - 0.025) / 0.032) ** 2)) * sJiA(0.1, 0.5, ZUQr)
        UweE = MkuP(UweE, np.array([0.82, 0.42, 0.38], np.float32), (YboB * 0.85)[..., None])
        return (UweE, YSdg)
    return (HkJe, YSdg)
OHbg = []
PxTP = {'last': 0.0, 'next_shoot': 1000000000.0, 'comet': False}

class Esgq:

    def __init__(AzMx, RXcw, eImK, ZrxP, aCZN, mkDv, CXnC, UweE, DRaR=False):
        AzMx.x, AzMx.y, AzMx.vx, AzMx.vy = (RXcw, eImK, ZrxP, aCZN)
        AzMx.life, AzMx.tail, AzMx.col, AzMx.soft = (mkDv, CXnC, UweE, DRaR)
        AzMx.age = 0.0

def YwOp():
    PxTP.update(last=0.0, next_shoot=1000000000.0, comet=False)
    OHbg.clear()
    FJva[:] = hMYz.uniform(0.06, 1.0, MqHW).astype(np.float32)

def dcRc(YlSF, eQfL, laEg):
    JBPk = 0.01 + 0.05 * laEg + (0.015 if YlSF > BHXs else 0.0)
    FJva[:] -= JBPk * eQfL
    swKG = FJva < 0.06
    if swKG.any():
        FJva[swKG] += 0.94
        iulD = int(swKG.sum())
        eZks[swKG] = hMYz.uniform(-1, 1, iulD)
        gwlf[swKG] = hMYz.uniform(-1, 1, iulD)
    if PxTP['next_shoot'] > 100000000.0 and YlSF > BHXs - 4.0:
        PxTP['next_shoot'] = YlSF + 1.0
    if YlSF > PxTP['next_shoot']:
        PxTP['next_shoot'] = YlSF + FKhC.uniform(2.2, 4.5)
        DpBH = m.radians(FKhC.uniform(18, 62))
        Xewc = FKhC.choice((-1, 1))
        UJiW = FKhC.uniform(0.7, 1.2)
        OHbg.append(Esgq(FKhC.uniform(-0.7, 0.7), FKhC.uniform(-0.45, -0.15), Xewc * m.cos(DpBH) * UJiW, m.sin(DpBH) * UJiW, FKhC.uniform(0.9, 1.4), FKhC.uniform(0.14, 0.26), np.array([0.88, 0.94, 1.0], np.float32)))
    if YlSF > BHXs + 1.5 and (not PxTP['comet']):
        PxTP['comet'] = True
        OHbg.append(Esgq(-0.95, -0.28, 0.03, 0.008, 70.0, 0.22, np.array([0.7, 0.86, 1.0], np.float32), soft=True))
    for lckv in OHbg:
        lckv.age += eQfL
    OHbg[:] = [lckv for lckv in OHbg if lckv.age < lckv.life]

def ypCJ(Bcrd, VHGA, qWGn, Ogvl, ulkE, tEWP, TpFB=1.0):
    if 0 <= qWGn < YQNQ and 0 <= Ogvl < hpFP:
        Bcrd[qWGn, Ogvl] = hnxe[ulkE]
        VHGA[qWGn, Ogvl] = tEWP * TpFB

def gCEr(lckv, Bcrd, VHGA, UDiL, DPqc):
    SGcE = lckv.x + lckv.vx * lckv.age
    PIZS = lckv.y + lckv.vy * lckv.age
    ngRF = m.hypot(lckv.vx, lckv.vy)
    fRab, legl = (lckv.vx / ngRF, lckv.vy / ngRF)
    ZEux = m.sin(m.pi * min(1.0, lckv.age / lckv.life)) ** 0.7
    if ZEux < 0.02:
        return
    if abs(legl) < 0.38 * abs(fRab):
        fJUU = '-'
    elif abs(fRab) < 0.38 * abs(legl):
        fJUU = '|'
    elif fRab * legl > 0:
        fJUU = '\\'
    else:
        fJUU = '/'
    iulD = max(6, int(lckv.tail * WSDh / (JdWu * 0.8)))
    for APkY in range(iulD):
        irnb = APkY / iulD
        Ogvl = int((ZHJi / 2 + (SGcE - fRab * lckv.tail * irnb) * WSDh) / JdWu)
        qWGn = int((WSDh / 2 + (PIZS - legl * lckv.tail * irnb) * WSDh) / DmcN)
        jJzp = (1 - irnb) ** 1.3 * ZEux
        if jJzp < 0.08 or not (0 <= qWGn < YQNQ and 0 <= Ogvl < hpFP) or UDiL[qWGn, Ogvl] < 0.5:
            continue
        if APkY == 0:
            ulkE = '@' if not lckv.soft else '*'
        elif lckv.soft:
            ulkE = ':' if jJzp > 0.35 else '.'
        else:
            ulkE = fJUU if jJzp > 0.3 else '.'
        ypCJ(Bcrd, VHGA, qWGn, Ogvl, ulkE, lckv.col, min(1.0, 0.3 + jJzp) * DPqc[qWGn, Ogvl])

def xAjD(Bcrd, VHGA, saat, YlSF, sNOL, sPGM, UDiL, DPqc, gWBl, ZSFU):
    if sPGM <= 0.003:
        return
    Fblq = FJva
    Ogvl = ((ZHJi * 0.5 + (eZks * sNOL / Fblq + gWBl) * WSDh) / JdWu).astype(np.int32)
    qWGn = ((WSDh * 0.5 + (gwlf * sNOL / Fblq + ZSFU) * WSDh) / DmcN).astype(np.int32)
    ICuP = sJiA(1.0, 0.82, Fblq) * (0.8 + 0.2 * np.sin(YlSF * ZpYX + HUGm)) * sPGM
    cCaD = (Ogvl >= 0) & (Ogvl < hpFP) & (qWGn >= 0) & (qWGn < YQNQ) & (ICuP > 0.04)
    if not cCaD.any():
        return
    vuqZ = np.flatnonzero(cCaD)
    Ogvl, qWGn = (Ogvl[vuqZ], qWGn[vuqZ])
    jJzp = YmtX[vuqZ] * ICuP[vuqZ] * (1 + 0.05 / Fblq[vuqZ])
    HCBP = UDiL[qWGn, Ogvl] > 0.5
    vuqZ, Ogvl, qWGn, jJzp = (vuqZ[HCBP], Ogvl[HCBP], qWGn[HCBP], jJzp[HCBP])
    nuAz = jJzp > saat[qWGn, Ogvl] * 0.7
    vuqZ, Ogvl, qWGn, jJzp = (vuqZ[nuAz], Ogvl[nuAz], qWGn[nuAz], jJzp[nuAz])
    if len(jJzp) == 0:
        return
    ulkE = np.where(jJzp < 0.2, hnxe['.'], np.where(jJzp < 0.42, hnxe['+'], hnxe['*']))
    Bcrd[qWGn, Ogvl] = ulkE
    VHGA[qWGn, Ogvl] = oVqb[vuqZ] * np.clip(0.35 + 0.9 * jJzp, 0, 1)[:, None] * DPqc[qWGn, Ogvl][:, None]
    fpaf = np.flatnonzero(jJzp > 0.55)
    for MFxG in fpaf[:40]:
        FlRi, NnCg, fncS = (int(Ogvl[MFxG]), int(qWGn[MFxG]), float(jJzp[MFxG]))
        UweE = oVqb[vuqZ[MFxG]] * DPqc[NnCg, FlRi]
        Bcrd[NnCg, FlRi] = hnxe['@'] if fncS > 0.85 else hnxe['*']
        UrLv = int(2 + 6 * (fncS - 0.5))
        for APkY in range(1, UrLv + 1):
            TpFB = (1 - APkY / (UrLv + 1)) * fncS
            for rvRo, qRTW, dENC in ((0, APkY, '-'), (0, -APkY, '-'), (APkY // 2 + (1 if APkY > 2 else 0), 0, '|'), (-(APkY // 2 + (1 if APkY > 2 else 0)), 0, '|')):
                if rvRo == 0 and qRTW == 0:
                    continue
                hLjZ, VJev = (NnCg + rvRo, FlRi + qRTW)
                if 0 <= hLjZ < YQNQ and 0 <= VJev < hpFP and (UDiL[hLjZ, VJev] > 0.5) and (saat[hLjZ, VJev] < TpFB * 0.8):
                    Bcrd[hLjZ, VJev] = hnxe[dENC if TpFB > 0.18 else '.']
                    VHGA[hLjZ, VJev] = UweE * min(1.0, 0.25 + TpFB)

def HAAA(Bcrd, VHGA, YlSF, iUSY, ZUQr, hoPy, wXgZ):
    if iUSY > 2.6 or ZUQr < 0.0:
        return
    JkeN = 1 - ZUQr ** 0.8

    def uAgR(YloR, qHJo):
        return (int((ZHJi / 2 + YloR * iUSY * WSDh) / JdWu), int((WSDh / 2 + qHJo * iUSY * WSDh) / DmcN))

    def hlKA(BPjg):
        DpBH = m.degrees(m.atan2(-m.sin(BPjg), m.cos(BPjg))) % 180
        if DpBH < 25 or DpBH >= 155:
            return '-'
        if DpBH < 70:
            return '/'
        if DpBH < 110:
            return '|'
        return '\\'

    def mbOC(yrNN, zwRw, LeBI, saat, kOLn, dofN, fOim, MIuS, LrWO):
        iulD = int(max(2, min(MIuS, saat * iUSY * WSDh / (JdWu * 0.85))))
        Nihf = saat / iulD
        YloR, qHJo = (yrNN, zwRw)
        for APkY in range(iulD):
            RlZB = APkY / max(1, iulD - 1)
            BPjg = LeBI + kOLn * RlZB * RlZB
            YloR += m.cos(BPjg) * Nihf
            qHJo += m.sin(BPjg) * Nihf
            Ogvl, qWGn = uAgR(YloR, qHJo)
            if not (0 <= qWGn < YQNQ and 0 <= Ogvl < hpFP):
                continue
            ulkE = LrWO if APkY == iulD - 1 and iulD >= 4 else hlKA(BPjg)
            Bcrd[qWGn, Ogvl] = hnxe[ulkE]
            VHGA[qWGn, Ogvl] = dofN + (fOim - dofN) * RlZB
    NsXc = np.array([0.16, 0.1, 0.07], np.float32)
    sLcr = np.array([0.3, 0.19, 0.13], np.float32)
    IHiz = np.array([0.17, 0.11, 0.08], np.float32)
    lzBw = np.array([0.3, 0.2, 0.14], np.float32)
    for tmUO, reiZ, LgTV, mEVr in KTvu:
        kcjw = tmUO * PHPS
        Rixe, eTLJ, ADla, xEjr = YLMW(kcjw, ZUQr)
        Xeyo = Rixe - 0.055 * tmUO
        sQCG = m.radians(-90 + 26 * tmUO)
        RxuC = m.radians(90 - 20 * tmUO) if tmUO >= 0 else m.radians(-270 - 20 * tmUO)
        LeBI = sQCG + (RxuC - sQCG) * JkeN
        UteZ = m.sqrt(max(0.0, 1 - tmUO * tmUO))
        iPDF = (0.07 + 0.05 * UteZ) * reiZ
        kOLn = m.radians(-22 * tmUO) * (1 - JkeN)
        mbOC(kcjw, Xeyo, LeBI, iPDF, kOLn, NsXc, sLcr, 14, "'")
    for tmUO, reiZ, LgTV, mEVr in Mdfo:
        kcjw = tmUO * PHPS
        Rixe, eTLJ, ADla, xEjr = YLMW(kcjw, ZUQr)
        Xeyo = eTLJ - 0.055 * tmUO
        LeBI = m.radians(90 - 20 * tmUO)
        iPDF = 0.034 * (0.5 + 0.8 * xEjr) * reiZ
        mbOC(kcjw, Xeyo, LeBI, iPDF, m.radians(12 * (1 if tmUO > 0 else -1)), IHiz, lzBw, 6, '.')

def Xtmm(GOLX):
    jJzp = np.clip(GOLX - 0.45, 0, None)
    MxLx = GOLX
    for irnb, bOem in ((2, 0.4), (4, 0.3)):
        lckv = jJzp.reshape(bFnk // irnb, irnb, nxUq // irnb, irnb, 3).mean((1, 3))
        for zLEl in range(2):
            lckv = (lckv * 2 + np.roll(lckv, 1, 0) + np.roll(lckv, -1, 0) + np.roll(lckv, 1, 1) + np.roll(lckv, -1, 1)) / 6
        MxLx = MxLx + bOem * np.repeat(np.repeat(lckv, irnb, 0), irnb, 1)
    return MxLx

def eiQz(YlSF, eQfL):
    PxTP['last'] = YlSF
    laEg = gQyV(YlSF)
    KWhk = IwWo(YlSF / SkoB)
    iUSY = m.exp(m.log(mmqE) * laEg) * (1 + 0.05 * KWhk + 0.004 * m.sin(YlSF * 0.9))
    bsCb = iUSY if YlSF < BHXs else mmqE * m.exp(0.03 * (YlSF - BHXs))
    sNOL = min(6.0, yGSo * bsCb ** 1.25)
    frfb = min(1.15, yGSo * iUSY ** 1.25)
    ZUQr = GIDD(YlSF)
    hoPy, wXgZ = VaHH(YlSF, laEg)
    QIWj = Vjlg * (0.76 + 0.24 * IwWo((YlSF - 1.8) / 3.5)) * (1 + 0.025 * m.sin(1.9 * YlSF)) * (1 + 0.3 * laEg)
    McWW = QIWj * iUSY
    VIbs = McWW * 0.72 > 1.03
    UTgP = IwWo((YlSF - (SkoB + 1.5)) / 4.5)
    fctJ = IwWo((YlSF - (SkoB + 3.5)) / 8.0)
    dcRc(YlSF, eQfL, laEg)
    gWBl, ZSFU = (hoPy * iUSY, wXgZ * iUSY)
    ngRF = np.empty((bFnk, nxUq, 3), np.float32)
    ngRF[:] = (0.004, 0.005, 0.012)
    if fctJ > 0.002:
        vnFJ = IwWo((YlSF - BHXs) / 20.0)
        Djiu = IwWo((YlSF - TIiq) / gLCF)
        BIBJ = 1 + 0.03 * m.sin(YlSF * 2.6) * Djiu * Djiu
        ngRF += Jirg(rGgO - gWBl - 0.03 * vnFJ * m.sin(YlSF * 0.07), rWGZ - ZSFU, 0.17 * frfb * BIBJ, Djiu, YlSF) * (1.25 * fctJ ** 1.3)
    if VIbs:
        GOLX = ngRF
        UDiL = np.ones((YQNQ, hpFP), np.float32)
        fJIl = np.zeros((YQNQ, hpFP), bool)
    else:
        GOLX, YSdg = gsqS(YlSF, iUSY, ZUQr, hoPy, wXgZ, QIWj, ngRF)
        UDiL = YSdg.reshape(YQNQ, zGLb, hpFP, zGLb).mean((1, 3))
        fJIl = UDiL < 0.5
    GOLX = Xtmm(GOLX)
    GOLX = 1 - np.exp(-2.0 * np.clip(GOLX, 0, None))
    GOLX = GOLX * (1 - 0.3 * sJiA(0.4, 1.0, nShD))[..., None] * IwWo(YlSF / 1.2)
    qwPO = GOLX.reshape(YQNQ, zGLb, hpFP, zGLb, 3).mean((1, 3))
    cTLs = 0.3 * qwPO[..., 0] + 0.6 * qwPO[..., 1] + 0.1 * qwPO[..., 2]
    MsAI = np.clip(cTLs, 0, 1) ** 0.72
    YkXh = np.clip((MsAI + (yqiG - 0.5) * 0.07) * DWSw, 0, DWSw).astype(np.int32)
    YkXh = np.where(fJIl, np.maximum(YkXh, 3), YkXh)
    Bcrd = YkXh.astype(np.int32)
    VHGA = np.clip(qwPO * 1.15, 0, 1).astype(np.float32)
    DPqc = (0.25 + 0.75 * sJiA(0, 0.3 * McWW, McWW - COYH)).astype(np.float32)
    xAjD(Bcrd, VHGA, MsAI, YlSF, sNOL, UTgP, UDiL, DPqc, gWBl, ZSFU)
    for lckv in OHbg:
        gCEr(lckv, Bcrd, VHGA, UDiL, DPqc)
    if not VIbs:
        HAAA(Bcrd, VHGA, YlSF, iUSY, ZUQr, hoPy, wXgZ)
    gHPD = np.clip((np.clip(VHGA, 0, 1) * (vNdd - 0.01)).astype(np.int16), 0, vNdd - 1)
    return (Bcrd, gHPD)

def YTRx(Bcrd, gHPD, kxCV, vrRT, SLmn):
    REyJ = Bcrd == kxCV
    wGYi = np.abs(gHPD - vrRT).max(axis=2)
    yGMC = (Bcrd == 0) & (kxCV == 0)
    CDbz = ~yGMC & (~REyJ | (wGYi >= 2))
    qwPO = np.flatnonzero(CDbz)
    if len(qwPO) > SLmn:
        cnHo = ((~REyJ).astype(np.int16) * 6 + wGYi).ravel()[qwPO]
        LMZb = np.argpartition(-cnHo, SLmn)[:SLmn]
        qwPO = qwPO[LMZb]
    return qwPO

def qwiC():
    import tkinter as tk
    import tkinter.font as tkf
    rsEi = tk.Tk()
    rsEi.title('Eye -> Space')
    rsEi.resizable(False, False)
    rsEi.bind('<Escape>', lambda DTAl: rsEi.destroy())
    GDlz = set(tkf.families())
    yRSK = next((irnb for irnb in ('Cascadia Mono', 'Consolas', 'Courier New', 'DejaVu Sans Mono', 'Courier') if irnb in GDlz), 'Courier')
    LvUl = rsEi.winfo_screenheight()
    uepT = tkf.Font(root=rsEi, family=yRSK, size=qXkV, weight='bold')
    yKMD = uepT.metrics('linespace')
    VuAb = uepT.measure('M')
    ASCF = min(QcTA, (LvUl - 110) // yKMD)
    bPzO(VuAb, yKMD, ASCF)
    rsEi.geometry(f'{ZHJi}x{WSDh}+{(rsEi.winfo_screenwidth() - ZHJi) // 2}+{max(0, (LvUl - WSDh) // 2 - 20)}')
    YsxK = tk.Canvas(rsEi, width=ZHJi, height=WSDh, bg='#010203', highlightthickness=0)
    YsxK.pack()
    jxeg = np.zeros((YQNQ, hpFP), dtype=object)
    jxeg[:] = 0
    kxCV = np.zeros((YQNQ, hpFP), np.int32)
    vrRT = np.zeros((YQNQ, hpFP, 3), np.int16)
    seen = {}
    YYVz = {'t0': time.perf_counter(), 'budget': 2500, 'cost': 0.012}

    def SGcE(utIv):
        APkY = (int(utIv[0]), int(utIv[1]), int(utIv[2]))
        lckv = seen.get(APkY)
        if lckv is None:
            lckv = '#%02x%02x%02x' % tuple((AKKs * 255 // (vNdd - 1) for AKKs in APkY))
            seen[APkY] = lckv
        return lckv

    def GtEO(zLEl=None):
        YYVz['t0'] = time.perf_counter()
        YwOp()
    rsEi.bind('r', GtEO)
    rsEi.bind('R', GtEO)

    def BigW():
        iYiN = time.perf_counter()
        YlSF = iYiN - YYVz['t0']
        eQfL = min(max(YlSF - PxTP['last'], 0.0), 0.1)
        Bcrd, gHPD = eiQz(YlSF, eQfL)
        qwPO = YTRx(Bcrd, gHPD, kxCV, vrRT, YYVz['budget'])
        YDas = time.perf_counter()
        for irnb in qwPO:
            rDom, zzLH = divmod(int(irnb), hpFP)
            ulkE = YRBb[Bcrd[rDom, zzLH]]
            zfAe = SGcE(gHPD[rDom, zzLH])
            HHhi = jxeg[rDom, zzLH]
            if HHhi == 0:
                if ulkE == ' ':
                    kxCV[rDom, zzLH] = 0
                    vrRT[rDom, zzLH] = gHPD[rDom, zzLH]
                    continue
                jxeg[rDom, zzLH] = YsxK.create_text((zzLH + 0.5) * JdWu, (rDom + 0.5) * DmcN, text=ulkE, fill=zfAe, font=uepT, anchor='center')
            else:
                YsxK.itemconfig(HHhi, text=ulkE, fill=zfAe)
            kxCV[rDom, zzLH] = Bcrd[rDom, zzLH]
            vrRT[rDom, zzLH] = gHPD[rDom, zzLH]
        if len(qwPO) > 50:
            xihF = (time.perf_counter() - YDas) / len(qwPO)
            YYVz['cost'] = 0.7 * YYVz['cost'] + 0.3 * xihF
            YYVz['budget'] = int(min(12000, max(400, akga / 1000.0 / max(YYVz['cost'], 1e-06))))
        zajj = (time.perf_counter() - iYiN) * 1000
        rsEi.after(max(1, int(1000 / MnPj - zajj)), BigW)
    rsEi.after(100, BigW)
    rsEi.mainloop()
if __name__ == '__main__':
    qwiC()