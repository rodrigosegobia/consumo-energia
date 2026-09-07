nome = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potencia do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo medio de uso diario em horas: "))
 
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * 0.75
 
print("")
print("Aparelho:", nome)
print("Consumo estimado:", round(consumo_mensal, 2), "kWh/mes")
print("Custo estimado: R$", round(custo_estimado, 2), "por mes")
 