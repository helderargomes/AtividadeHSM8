placa = input("Digite o numero da placa do veiculo:")
limite = float(input("Digite o limite de velocidade da via:"))
velocidade = float(input("Digite a velocidade registrada para o veiculo:"))

excesso = velocidade-limite
multa = 0;

print("Placa do veiculo: " + placa);

if excesso <= (limite*0.20):
    multa = 130.16;
    print("Infracao media");
elif excesso <= (limite*0.50):
    multa = 195.23;
    print("Infracao grave")
else:
    multa = 880.41;
    print("Infracao gravissima");

print(f"Multa = R${multa}")