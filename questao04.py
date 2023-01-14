SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

faturamento_total = SP + RJ + MG + ES + Outros

SP_porcent = (SP / faturamento_total) * 100
RJ_porcent = (RJ / faturamento_total) * 100
MG_porcent = (MG / faturamento_total) * 100
ES_porcent = (ES / faturamento_total) * 100
Outros_porcent = (Outros / faturamento_total) * 100

print(f"SP: {SP_porcent:.2f}%")
print(f"RJ: {RJ_porcent:.2f}%")
print(f"MG: {MG_porcent:.2f}%")
print(f"ES: {ES_porcent:.2f}%")
print(f"Others: {Outros_porcent:.2f}%")
