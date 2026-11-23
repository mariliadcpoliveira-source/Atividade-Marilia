Calcule o Índice de Massa Corporal (IMC = peso/altura^2) e 
informe se está abaixo do peso(menor que 18.5), normal (18.5 a 24.9) ou 
acima do peso (25 ou mais).

-Resposta

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5:
  status = "Abaixo do peso"
elif imc < 25:
  status = "Peso normal"
else: 
  status = "Acima do peso"

print(f"IMC: {imc:.2f} - {status}")
