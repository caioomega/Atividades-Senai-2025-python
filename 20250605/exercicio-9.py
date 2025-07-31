num_pessoas=int(input("Digite a quantidade de pessoas para medir a temperatura: "))
abaixo=0
normal=0
febril=0
febre=0
febre_alta=0
soma=0
abaixo_media=0
normal_media=0
febril_media=0
febre_media=0
alta_media=0
for i in range(num_pessoas):
    temp=float(input("Digite a temperatura em °C:" ))
    if temp<35.5:
        print("Temperatura abaixo do normal!")
        abaixo+=1
        soma+=temp
        abaixo_media+=temp
    elif temp>35.5 and temp<=37.2:
        print("Temperatura normal!")
        normal+=1
        soma+=temp
        normal_media+=temp
    elif temp>37.2 and temp<=38:
        print("Estado febril!")
        febril+=1
        soma+=temp
        febril_media+=0
    elif temp>38 and temp<=39:
        print("Febre!")
        febre+=1
        soma+=temp
        febre_media+=temp
    else:
        print("Febre alta!")
        febre_alta+=1
        soma+=temp
        alta_media+=1
media=soma/num_pessoas
print("Resultados: ")
if abaixo!=0:
    print(F"{abaixo} pessoas com temperatura abaixo do normal, e uma média de {abaixo_media/media:.1f}°C")
if normal!=0:
    print(F"{normal} pessoas com temperatura normal, e uma média de {normal_media/normal:.1f}°C") 
if febril!=0:
    print(F"{febril} pessoas com temperatura em estado febril, e uma média de {febril_media/febril:.1f}°C")
if febre!=0:
    print(F"{febre} pessoas com febre, e uma média de {febre_media/febre:.1f}°C")
if febre_alta!=0:
    print(F"{febre_alta} pessoas com febre alta, e uma média de {alta_media/febre_alta:.1f}°C")
print(F"A média total das temperaturas é de {media:.1f}°C")
