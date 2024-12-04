print("Seja bem-vindo ao Estatísticas Marciais!")

Lista1 = [
    "1 - Karate", "2 - Judô", "3 - Taekwondo", "4 - Jiu-Jitsu", 
    "5 - Boxe", "6 - Kickboxing", "7 - Muay Thai", 
    "8 - Capoeira", "9 - Kung Fu", "10 - Ninjutsu"
]

Lista2 = [
    {"arte": "karate", "estilos": "Shotokan, Goju-Ryu, Shito-Ryu e Wado-Ryu", "golpes": "60 a 100 golpes", "contra-ataques": "30 a 50 contra-ataques", "praticantes": "aproximadamente 100 Milhões de praticantes"},
    {"arte": "judô", "estilos": "Não possui estilo", "golpes": "67 golpes", "contra-ataques": "20 a 30 contra-ataques", "praticantes": "aproximadamente 30 Milhões de praticantes"},
    {"arte": "taekwondo", "estilos": "WT (World Taekwondo) e ITF (Internacional Taekwon-Do Federation)", "golpes": "320 golpes", "contra-ataques": "50 a 100 contra-ataques", "praticantes": "aproximadamente 80 Milhões de praticantes"},
    {"arte": "jiu-jitsu", "estilos": "Jiu-Jitsu Japonês e Jiu-Jitsu Brasileiro (BJJ)", "golpes": "600 golpes", "contra-ataques": "+ de 100 contra-ataques", "praticantes": "aproximadamente 6 Milhões de praticantes"},
    {"arte": "boxe", "estilos": "Out-fighter, In-fighter e Counter-Puncher", "golpes": "12 golpes", "contra-ataques": "20 contra-ataques", "praticantes": "aproximadamente 30 Milhões de praticantes"},
    {"arte": "kickboxing", "estilos": "Kickboxing Japonês, American Kickboxing e K-1", "golpes": "40 a 50 golpes", "contra-ataques": "30 contra-ataques", "praticantes": "aproximadamente 10 Milhões de praticantes"},
    {"arte": "muay thai", "estilos": "Muay Boran, Muay Chaiya e Muay Thai", "golpes": "100 golpes", "contra-ataques": "50 contra-ataques", "praticantes": "aproximadamente 10 Milhões de praticantes"},
    {"arte": "capoeira", "estilos": "Capoeira Angola e Regional", "golpes": "100 golpes", "contra-ataques": "50 contra-ataques", "praticantes": "aproximadamente 6 Milhões de praticantes"},
    {"arte": "kung fu", "estilos": "Shaolin Kung, Wing Chun e Hung Gar", "golpes": "+ de 1000 golpes", "contra-ataques": "+ de 1000 contra-ataques", "praticantes": "aproximadamente 50 Milhões de praticantes"},
    {"arte": "ninjutsu", "estilos": "9 principais estilos", "golpes": "milhares de golpes", "contra-ataques": "milhares de contra-ataques", "praticantes": "milhares de praticantes (Japão e China Antigo)"}
]

while True:
    print("\n--------------------------------")
    P1 = input("Deseja saber as estatísticas de alguma Arte Marcial? (sim/não): ").lower()
    match P1:
        case "sim" | "s":
            P2 = input("Deseja ver a nossa lista de Artes Marciais? (sim/não): ").lower()
            if P2 in ["sim", "s"]:
                print("\nLista de Artes Marciais:")
                for arte in Lista1:
                    print(arte)
            P3 = input("Qual Arte Marcial você gostaria de saber as estatísticas? ").lower()
            encontrou = False
            for esporte in Lista2:
                if esporte["arte"].lower() in P3:
                    encontrou = True
                    print("\nEstatísticas de", esporte["arte"])
                    print(f"Estilos: {esporte['estilos']}")
                    print(f"Número de golpes: {esporte['golpes']}")
                    print(f"Número de contra-ataques: {esporte['contra-ataques']}")
                    print(f"Número de praticantes: {esporte['praticantes']}\n")
            if not encontrou:
                print("Arte marcial não encontrada. Verifique a lista e tente novamente.\n")
        case "não" | "nao" | "n":
            print("Ok, até a próxima!")
            break
        case _:
            print("Resposta inválida. Tente novamente.\n")

    continuar = input("Deseja continuar? (sim/não): ").lower()
    if continuar not in ["sim", "s"]:
        print("Ok, Até logo!")
        break