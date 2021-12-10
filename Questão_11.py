depo = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (Ex.: 3 para 3%): "))
mensal = float(input("Depósito mensal: "))
mês = 1
saldo = depo
while mês <= 24:
    saldo = saldo + (saldo * (taxa / 100)) + mensal
    print(f"Saldo do mês {mês} é de R${saldo:5.2f}.")
    mês = mês + 1
print(f"O ganho obtido com os juros foi de R${saldo-depo:8.2f}.")