def montante(c:float, i:float, t:float):
    m=c*(1+i*t)
    return m

def mf(c:float, i:float, t:float ):
    m=c*(1+i)**t
    return m

def mfj(vi:float, d:float):
    Vf=vi*(1-d/100)
    return Vf

def valor_final(vi:float, a:float):
    Vf=vi*(1+a/100)
    return Vf

def financiamento(v:float, n:float):
    p=v/n
    return p
