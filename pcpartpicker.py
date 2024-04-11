def chooseCase(w):
    cases = ["Montech AIR X ARGB",
             "Cooler Master Cosmos C700M RGB",
             "Ouro Kronii Y60"]

    print("Primeiramente vamos escolher um gabinete!")
    for idx, case in enumerate(cases):
        print("{}) {}".format(idx + 1, case))

    choice = input("Digite o número do gabinete desejado, digite 0 caso não queira nenhum: ")
    choice = int(choice)

    while not(choice >= 0 and choice <= len(cases)):
        choice = input("Escolha inválida, digite o número do gabinete desejado: ")
        choice = int(choice)
    
    if choice != 0:
        w.append(cases[choice - 1])

    print()

def chooseMotherboard(w):
    mbs = ["MSI B550M PRO-VDH WIFI", 
           "Gigabyte H510M H"
           ]

    print("Vamos escolher uma placa-mãe!")
    for idx, mb in enumerate(mbs):
        print("{}) {}".format(idx + 1, mb))

    choice = input("Digite o número da placa-mãe desejada, digite 0 caso não queira nenhuma: ")
    choice = int(choice)

    while not(choice >= 0 and choice <= len(mbs)):
        choice = input("Escolha inválida, digite o número da placa mãe desejada: ")
        choice = int(choice)
    
    if choice != 0:
        w.append(mbs[choice - 1])

    print()

def chooseCPU(w):
    cpus = ["AMD Ryzen 5 5600", 
            "Intel Core i9 11900k"
            ]

    print("Vamos escolher um processador!")
    for idx, cpu in enumerate(cpus):
        print("{}) {}".format(idx + 1, cpu))

    choice = input("Digite o número do processador desejado, digite 0 caso não queira nenhum: ")
    choice = int(choice)

    while not(choice >= 0 and choice <= len(cpus)):
        choice = input("Escolha inválida, digite o número do processador desejado: ")
        choice = int(choice)
    
    if choice != 0:
        w.append(cpus[choice - 1])

    print()

def chooseCooler(w):
    coolers = ["DeepCool Gammax 400 V2", 
               "DeepCool AK620 ZERO DARK"
               ]

    print("Vamos escolher um cooler!")
    for idx, cooler in enumerate(coolers):
        print("{}) {}".format(idx + 1, cooler))

    choice = input("Digite o número do cooler desejado, digite 0 caso não queira nenhum: ")
    choice = int(choice)

    while not(choice >= 0 and choice <= len(coolers)):
        choice = input("Escolha inválida, digite o número do cooler desejado: ")
        choice = int(choice)
    
    if choice != 0:
        w.append(coolers[choice - 1])

    print()

def chooseRAM(w):
    rams = ["2x16GB Corsair Vengeance DDR4 3200MHz", 
            "2x16GB Corsair Dominator Platinum DDR4 3600MHz"
            ]

    print("Vamos escolher a RAM!")
    for idx, ram in enumerate(rams):
        print("{}) {}".format(idx + 1, ram))

    choice = input("Digite o número da RAM desejada, digite 0 caso não queira nenhuma: ")
    choice = int(choice)

    while choice != 0:
        while not(choice >= 0 and choice <= len(rams)):
            choice = input("Escolha inválida, por favor digite o número da RAM desejada: ")
            choice = int(choice)

        if choice != 0:
            w.append(rams[choice - 1])
            choice = input("Deseja adicionar mais RAM ? Se sim, digite o número da RAM desejada, se não, digite 0: ")
            choice = int(choice)

    print()

def chooseGPU(w):
    gpus = ["Gigabyte GeForce RTX 3070 Ti", 
            "AsRock AMD Radeon RX 7900 XTX"
            ]

    print("Vamos escolher uma placa de vídeo!")
    for idx, gpu in enumerate(gpus):
        print("{}) {}".format(idx + 1, gpu))

    choice = input("Digite o número da placa de vídeo desejada, digite 0 caso não queira nenhuma: ")
    choice = int(choice)

    while not(choice >= 0 and choice <= len(gpus)):
        choice = input("Escolha inválida, digite o número da placa de vídeo desejada: ")
        choice = int(choice)
    
    if choice != 0:
        w.append(gpus[choice - 1])

    print()

def chooseMemory(w):
    mems = ["SSD Lexar NM610 500GB NVME M.2", 
            "HD Seagate SkyHawk Surveillance 3TB"]

    print("Vamos escolher o armazenamento!")
    for idx, mem in enumerate(mems):
        print("{}) {}".format(idx + 1, mem))

    choice = input("Digite o número do armazenamento desejado, digite 0 caso não queira nenhum: ")
    choice = int(choice)

    while choice != 0 and len(mems) > 0:
        while not(choice >= 0 and choice <= len(mems)):
            choice = input("Escolha inválida, por favor digite o número do armazenamento desejado: ")
            choice = int(choice)

        if choice != 0:
            qtd = input("Quantas da memória selecionada deseja adicionar?: ")
            qtd = int(qtd)
            for i in range (qtd):
                w.append(mems[choice - 1])
            if qtd > 0:
                del mems[choice - 1]
            for idx, mem in enumerate(mems):
                print("{}) {}".format(idx + 1, mem))
            if len(mems) > 0:
                choice = input("Deseja adicionar mais armazenamento ? Se sim, digite o número do armazenamento desejado, se não, digite 0: ")
            choice = int(choice)

    print()

def choosePowerSupply(w):
    pss = ["Super Flower LEGION GX PRO 750W", 
           "Redragon RGPS 1000W"
           ]

    print("Vamos escolher uma fonte!")
    for idx, ps in enumerate(pss):
        print("{}) {}".format(idx + 1, ps))

    choice = input("Digite o número da fonte desejada, digite 0 caso não queira nenhuma: ")
    choice = int(choice)

    while not(choice >= 0 and choice <= len(pss)):
        choice = input("Escolha inválida, digite o número da fonte desejada: ")
        choice = int(choice)
    
    if choice != 0:
        w.append(pss[choice - 1])

    print()

def testAfd(M, w):
    δ, q, F = M

    for s in w:
        if (q, s) in δ:
            q = δ[(q, s)]
        else:
            return False, s

    return q in F, None

def afd(w):
    δ = {
        ('q0', 'Montech AIR X ARGB'): 'q1',
        ('q0', 'Cooler Master Cosmos C700M RGB'): 'q1',
        ('q0', 'Ouro Kronii Y60'): 'q1',
        ('q1', 'MSI B550M PRO-VDH WIFI'): 'q2',
        ('q1', 'Gigabyte H510M H'): 'q24',
        ('q2', 'AMD Ryzen 5 5600'): 'q3',
        ('q3', 'DeepCool Gammax 400 V2'): 'q4',
        ('q3', 'DeepCool AK620 ZERO DARK'): 'q4',
        ('q3', '2x16GB Corsair Vengeance DDR4 3200MHz'): 'q5',
        ('q3', '2x16GB Corsair Dominator Platinum DDR4 3600MHz'): 'q22',
        ('q4', '2x16GB Corsair Vengeance DDR4 3200MHz'): 'q5',
        ('q4', '2x16GB Corsair Dominator Platinum DDR4 3600MHz'): 'q22',
        ('q5', 'Gigabyte GeForce RTX 3070 Ti'): 'q6',
        ('q5', 'AsRock AMD Radeon RX 7900 XTX'): 'q6',
        ('q5', '2x16GB Corsair Vengeance DDR4 3200MHz'): 'q9',
        ('q6', 'SSD Lexar NM610 500GB NVME M.2'): 'q7',
        ('q6', 'HD Seagate SkyHawk Surveillance 3TB'): 'q11',
        ('q7', 'Super Flower LEGION GX PRO 750W'): 'q8', 
        ('q7', 'Redragon RGPS 1000W'): 'q8',
        ('q7', 'SSD Lexar NM610 500GB NVME M.2'): 'q10',
        ('q7', 'HD Seagate SkyHawk Surveillance 3TB'): 'q17',
        ('q9', 'Gigabyte GeForce RTX 3070 Ti'): 'q6', 
        ('q9', 'AsRock AMD Radeon RX 7900 XTX'): 'q6',
        ('q10', 'HD Seagate SkyHawk Surveillance 3TB'): 'q17',
        ('q10', 'Super Flower LEGION GX PRO 750W'): 'q8',
        ('q10', 'Redragon RGPS 1000W'): 'q8',
        ('q11', 'SSD Lexar NM610 500 GB NVME M.2'): 'q14',
        ('q11', 'HD Seagate SkyHawk Surveillance 3TB'): 'q12',
        ('q11', 'Super Flower LEGION GX PRO 750W'): 'q8',
        ('q11', 'Redragon RGPS 1000W'): 'q8',
        ('q12', 'HD Seagate SkyHawk Surveillance 3TB'): 'q13',
        ('q12', 'SSD Lexar NM610 500 GB NVME M.2'): 'q14',
        ('q12', 'Super Flower LEGION GX PRO 750W'): 'q8',
        ('q12', 'Redragon RGPS 1000W'): 'q8',
        ('q13', 'HD Seagate SkyHawk Surveillance 3TB'): 'q16',
        ('q13', 'SSD Lexar NM610 500 GB NVME M.2'): 'q14',
        ('q13', 'Super Flower LEGION GX PRO 750W'): 'q8',
        ('q13', 'Redragon RGPS 1000W'): 'q8',
        ('q14', 'SSD Lexar NM610 500 GB NVME M.2'): 'q15',
        ('q14', 'Super Flower LEGION GX PRO 750W'): 'q8',
        ('q14', 'Redragon RGPS 1000W'): 'q8',
        ('q15', 'Super Flower LEGION GX PRO 750W'): 'q8',
        ('q15', 'Redragon RGPS 1000W'): 'q8',
        ('q16', 'SSD Lexar NM610 500 GB NVME M.2'): 'q14',
        ('q16', 'Super Flower LEGION GX PRO 750W'): 'q8',
        ('q16', 'Redragon RGPS 1000W'): 'q8',
        ('q17', 'Super Flower LEGION GX PRO 750W'): 'q8',
        ('q17', 'Redragon RGPS 1000W'): 'q8',
        ('q17', 'HD Seagate SkyHawk Surveillance 3TB'): 'q18',
        ('q18', 'Super Flower LEGION GX PRO 750W'): 'q8',
        ('q18', 'Redragon RGPS 1000W'): 'q8',
        ('q18', 'HD Seagate SkyHawk Surveillance 3TB'): 'q20',
        ('q20', 'HD Seagate SkyHawk Surveillance 3TB'): 'q21',
        ('q20', 'Super Flower LEGION GX PRO 750W'): 'q8',
        ('q20', 'Redragon RGPS 1000W'): 'q8',
        ('q21', 'Super Flower LEGION GX PRO 750W'): 'q8',
        ('q21', 'Redragon RGPS 1000W'): 'q8',
        ('q22', '2x16GB Corsair Dominator Platinum DDR4 3600MHz'): 'q23',
        ('q22', 'Gigabyte GeForce RTX 3070 Ti'): 'q6',
        ('q22', 'AsRock AMD Radeon RX 7900 XTX'): 'q6',
        ('q23', 'Gigabyte GeForce RTX 3070 Ti'): 'q6',
        ('q23', 'AsRock AMD Radeon RX 7900 XTX'): 'q6',
        ('q24', 'Intel Core i9 11900k'): 'q25',
        ('q25', 'DeepCool AK620 ZERO DARK'): 'q26',
        ('q26', '2x16GB Corsair Vengeance DDR4 3200MHz'): 'q27',
        ('q26', '2x16GB Corsair Dominator Platinum DDR4 3600MHz'): 'q27',
        ('q27', 'Gigabyte GeForce RTX 3070 Ti'): 'q28',
        ('q27', 'AsRock AMD Radeon RX 7900 XTX'): 'q28',
        ('q27', 'SSD Lexar NM610 500GB NVME M.2'): 'q29',
        ('q27', 'HD Seagate SkyHawk Surveillance 3TB'): 'q35',
        ('q28', 'SSD Lexar NM610 500GB NVME M.2'): 'q29', 
        ('q28', 'HD Seagate SkyHawk Surveillance 3TB'): 'q35',
        ('q29', 'HD Seagate SkyHawk Surveillance 3TB'): 'q30',
        ('q29', 'Super Flower LEGION GX PRO 750W'): 'q34',
        ('q29', 'Redragon RGPS 1000W'): 'q34',
        ('q30', 'HD Seagate SkyHawk Surveillance 3TB'): 'q31',
        ('q30', 'Super Flower LEGION GX PRO 750W'): 'q34',
        ('q30', 'Redragon RGPS 1000W'): 'q34',
        ('q31', 'HD Seagate SkyHawk Surveillance 3TB'): 'q32',
        ('q31', 'Super Flower LEGION GX PRO 750W'): 'q34',
        ('q31', 'Redragon RGPS 1000W'): 'q34',
        ('q32', 'HD Seagate SkyHawk Surveillance 3TB'): 'q33',
        ('q32', 'Super Flower LEGION GX PRO 750W'): 'q34',
        ('q32', 'Redragon RGPS 1000W'): 'q34',
        ('q33', 'Super Flower LEGION GX PRO 750W'): 'q34',
        ('q33', 'Redragon RGPS 1000W'): 'q34',
        ('q35', 'SSD Lexar NM610 500GB NVME M.2'): 'q39',
        ('q35', 'HD Seagate SkyHawk Surveillance 3TB'): 'q36',
        ('q35', 'Super Flower LEGION GX PRO 750W'): 'q34',
        ('q35', 'Redragon RGPS 1000W'): 'q34',
        ('q36', 'SSD Lexar NM610 500GB NVME M.2'): 'q39',
        ('q36', 'HD Seagate SkyHawk Surveillance 3TB'): 'q38',
        ('q36', 'Super Flower LEGION GX PRO 750W'): 'q34',
        ('q36', 'Redragon RGPS 1000W'): 'q34',
        ('q37', 'SSD Lexar NM610 500GB NVME M.2'): 'q39',
        ('q37', 'Super Flower LEGION GX PRO 750W'): 'q34',
        ('q37', 'Redragon RGPS 1000W'): 'q34',
        ('q38', 'SSD Lexar NM610 500GB NVME M.2'): 'q39',
        ('q38', 'HD Seagate SkyHawk Surveillance 3TB'): 'q37',
        ('q38', 'Super Flower LEGION GX PRO 750W'): 'q34',
        ('q38', 'Redragon RGPS 1000W'): 'q34',
        ('q39', 'Super Flower LEGION GX PRO 750W'): 'q34',
        ('q39', 'Redragon RGPS 1000W'): 'q34',
        }

    M = δ, 'q0', ['q8', 'q34']

    return testAfd(M, w)

def pcBuilding():
    word = []
    print("Vamos montar um computador!")
    chooseCase(word)
    chooseMotherboard(word)
    chooseCPU(word)
    chooseCooler(word)
    chooseRAM(word)
    chooseGPU(word)
    chooseMemory(word)
    choosePowerSupply(word)

    return word

def main():

    word = pcBuilding()

    print("O computador que você montou foi:")
    for _, part in enumerate(word):
        print(part)
    print()

    isFunctional, incomp = afd(word)
    if (isFunctional):
        print("Parabéns! Este computador é funcional!")
    else:
        print("Este computador possui incompatiblidades, por favor tente novamente.")
        print("Problema encontrado na peça: {}".format(incomp))

if __name__ == "__main__":
    main()
