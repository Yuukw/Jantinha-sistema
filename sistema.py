print("=== SISTEMA JANTINHA ===")
investimento = 2000.0

jantinhas = int(input("Quantas jantinhas vendeu hoje? "))
espetinhos = int(input("Quantos espetinhos vendeu hoje? "))
gasto = float(input("Quanto gastou hoje? R$ "))

faturamento = jantinhas * 20 + espetinhos * 12
lucro = faturamento - gasto
falta = investimento - lucro

print("\n--- RESULTADO ---")
print(f"Faturou: R$ {faturamento:.2f}")
print(f"Lucro de hoje: R$ {lucro:.2f}")

if falta > 0:
    print(f"Falta pagar do investimento: R$ {falta:.2f}")
else:
    print(f"🎉 INVESTIMENTO PAGO! Lucro extra: R$ {-falta:.2f}")
