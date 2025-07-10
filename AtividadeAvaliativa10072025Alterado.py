def avaliar_maquiagem():
    print("===Avaliando a Maquiagem===")
    input(" Qual é o nome do produto? ")
    input(" Qual é a marca do produto? ")
    input(" Qual é o preço do produto? ")
    nota=int(input(" Qual é a sua avaliação de 1 a 5? "))
    while nota != 1 and nota != 2 and nota != 3 and nota != 4 and nota != 5:
        print(" Avaliação inválida. Por favor, insira um número de 1 a 5.")
        nota = int(input(" Qual é a sua avaliação de 1 a 5? "))
    input(" Deixe um comentário sobre o produto: ")
    print(" Avaliação Concluída")

def avaliar_cabelo():
    print("===Avaliando Produtos de Cabelo===")
    input(" Qual é o nome do produto? ")
    input(" Qual é a marca do produto? ")
    input(" Para que tipo de cabelo é indicado? ")
    input(" Qual é o preço do produto? ")
    nota=int(input(" Qual é a sua avaliação de 1 a 5? "))
    while nota != 1 and nota != 2 and nota != 3 and nota != 4 and nota != 5:
        print(" Avaliação inválida. Por favor, insira um número de 1 a 5.")
        nota = int(input(" Qual é a sua avaliação de 1 a 5? "))
    input(" Deixe um comentário sobre o produto: ")
    print(" Avaliação Concluída")

def avaliar_produtosdeunhas():
    print("===Avaliando Produtos de Unha===")
    input(" Qual é o nome do produto? ")
    input(" Qual é a marca do produto? ")
    input(" Qual a cor do produto? ")
    input(" Qual é o preço do produto? ")
    nota=int(input(" Qual é a sua avaliação de 1 a 5? "))
    while nota != 1 and nota != 2 and nota != 3 and nota != 4 and nota != 5:
      print(" Avaliação inválida. Por favor, insira um número de 1 a 5.")
      nota = int(input(" Qual é a sua avaliação de 1 a 5? "))
    input(" Deixe um comentário sobre o produto: ")
    print(" Avaliação Concluída")

print("===Bem-Vindo ao Mundo da Beleza Compartilhado, onde você fala sua opinião sobre os produtos de beleza===")
nome= input(" Qual é o seu nome? ")
print(f" Olá, {nome}! Vamos começar a sua jornada de compartilhar a sua beleza.")
escolha_maquiagem = input(" Você que avaliar um produto de maquiagem? (Sim/Não): ")
if escolha_maquiagem == "Sim" or escolha_maquiagem == "sim" or escolha_maquiagem == "S" or escolha_maquiagem == "s":
   avaliar_maquiagem()
   loop= input(" Você gostaria de avaliar outro produto de maquiagem? (Sim/Não): ")
   while loop == "Sim" or loop == "sim" or loop == "S" or loop == "s":
         avaliar_maquiagem()
         loop = input(" Você gostaria de avaliar outro produto de maquiagem? (Sim/Não): ")
else:
    print(" Você escolheu não avaliar maquiagem. Vamos para a próxima etapa.")
escolha_cabelo= input(" Você quer avaiar um produto de cabelo? (Sim/Não): ")
if escolha_cabelo == "Sim" or escolha_cabelo == "sim" or escolha_cabelo== "S" or escolha_cabelo == "s":
   avaliar_cabelo()
   loop= input(" Você gostaria de avaliar outro produto de maquiagem? (Sim/Não): ")
   while loop == "Sim" or loop == "sim" or loop == "S" or loop == "s":
         avaliar_cabelo()
         loop = input(" Você gostaria de avaliar outro produto de cabelo? (Sim/Não): ")
else:
    print(" Você escolheu não avaliar os produtos de cabelos. Vamos para a próxima etapa.")
escolha_unhas = input(" Você quer avaliar um produto de unhas? (Sim/Não): ")
if escolha_unhas == "Sim" or escolha_unhas == "sim" or escolha_unhas == "S" or escolha_unhas == "s":
   avaliar_produtosdeunhas()
   loop= input(" Você gostaria de avaliar outro produto de unhas? (Sim/Não): ")
   while loop == "Sim" or loop == "sim" or loop == "S" or loop == "s":
         avaliar_produtosdeunhas()
         loop = input(" Você gostaria de avaliar outro produto de unhas? (Sim/Não): ")
else:
    print(" Você escolheu não avaliar produtos de unhas. Vamos para a próxima etapa.")

continuar = input(" Você gostaria de conhecer a nossa Loja online? (Sim/Não): ")
if continuar == "Sim" or continuar == "sim" or continuar == "S" or continuar == "s":
    print(f"{nome}, que bom que você quiz ver a nossa loja, aqui abaixo estão os produtos que vendemos:")
    print("===Produtos de Maquiagem===")
    print("1. Batom - R$ 25,00")
    print("2. Máscara de Cílios - R$ 30,00")
    print("2. Base - R$ 50,00")
    print("3. Pó Compacto - R$ 45,00")
    print("4. Blush - R$ 20,00")
    print("5. Delineador - R$ 30,00")
    print("\n")
    print("===Produtos de Cabelo===")
    print("3. Escova para pentear- R$ 20,00")
    print("4. Shampoo - R$ 35,00")
    print("5. Condicionador - R$ 35,00")
    print("6. Máscara de Hidratação - R$ 50,00")
    print("7. Óleo Capilar - R$ 45,00")
    print("\n")
    print("===Produtos de Unhas===")
    print("1. Base para Unhas - R$ 20,00")
    print("6. Esmalte - R$ 15,00")
    print("7. Removedor de Esmalte - R$ 10,00")
    print("8. Lixa de Unhas - R$ 5,00")
    print("9. Spray de unhas- R$ 30,00")
    print(" Para mais informações, visite nosso site oficial Beleza.é.saber.se.cuidar.com ou atravéz do nosso Instagram @Belezaesabersecuidar ou por whatsapp (31) 97940-8959.")

else:
    print(" Você escolheu não conhecer a nossa loja online. Esperamos que tenha gostado da sua experiência de avaliação de produtos de beleza.")
print(" Obrigado por participar! Até a próxima!")
    
    
    
