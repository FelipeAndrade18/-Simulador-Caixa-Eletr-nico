print('{:=^80}'.format('\033[1;30mSIMULADOR DE CAIXA ELETRÔNICO\033[m'))
valor = int(input('Qual valor deseja levantar : \N{euro sign} '))
print('='*80)
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
           print('Total de {} cedulas de \N{euro sign} {}'.format(totced, ced))
        if ced == 50:
            ced =20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*80)
