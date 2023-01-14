import json

# Lendo o arquivo JSON
with open("billing_data.json") as f:
    data = json.load(f)

# Variáveis
menor_faturamento = float("inf")
maior_faturamento = float("-inf")
dias_acima_media = 0
faturamento_total = 0
total_dias = 0

# Iteração
for dia in data:
    # Verificação
    if dia["valor"] != 0:
        total_dias += 1
        faturamento_total += dia["valor"]

        # Verificando o menor e o maior valor
        if dia["valor"] < menor_faturamento:
            menor_faturamento = dia["valor"]
        if dia["valor"] > maior_faturamento:
            maior_faturamento = dia["valor"]

media_faturamento = faturamento_total / total_dias

# Contando dias acima da média
for dia in data:
    if dia["valor"] != 0 and dia["valor"] > media_faturamento:
        dias_acima_media += 1

print("Menor valor de faturamento:", menor_faturamento)
print("Maior valor de faturamento:", maior_faturamento)
print("Número de dias com valor superior à media mensal:", dias_acima_media)
