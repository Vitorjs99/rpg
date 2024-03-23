import random

personagens = {}

while True:
    nome = input("Digite o nome do personagem (ou 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        break
    
    if nome in personagens:
        # Se o nome já existe no dicionário, use os valores existentes
        força, destreza, inteligencia, sabedoria, carisma, resistencia, agilidade, sorte = personagens[nome]
    else:
        # Caso contrário, gere novos valores aleatórios
        força = random.randint(1, 10)
        destreza = random.randint(1, 10)
        inteligencia = random.randint(1, 10)
        sabedoria = random.randint(1, 10)
        carisma = random.randint(1, 10)
        resistencia = random.randint(1, 10)
        agilidade = random.randint(1, 10)
        sorte = random.randint(1, 10)
        
        # Armazene os valores no dicionário
        personagens[nome] = (força, destreza, inteligencia, sabedoria, carisma, resistencia, agilidade, sorte)
    
    total = força + destreza + inteligencia + sabedoria + carisma + resistencia + agilidade + sorte

    print("\nNome do personagem:", nome)
    print("Sua força é:", força)
    print("Sua destreza é:", destreza)
    print("Sua inteligência é:", inteligencia)
    print("Sua sabedoria é:", sabedoria)
    print("Seu carisma é:", carisma)
    print("Sua resistência é:", resistencia)
    print("Sua agilidade é:", agilidade)
    print("Sua sorte é:", sorte)
    print("O total dos seus atributos é:", total)
    