def pifagor(a,b,type='гипотенуза'):
    if type == 'гипотенуза':
        return (a**2+b**2)**0.5
    else:
        return (max(a,b)**2-min(a,b)**2)**0.5