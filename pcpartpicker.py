def chooseCase(w):
    cases = ["Um", "dois", "tres"]

    print("Vamos escolher um gabinete!")
    for idx, case in enumerate(cases):
        print("{}) {}".format(idx + 1, case))

    choice = input("Digite o número do gabinete desejado, digite 0 caso não queira nenhum: ")
    choice = int(choice)

    while not(choice >= 0 and choice <= len(cases)):
        choice = input("Escolha inválida, digite o número do gabinete desejado: ")
        choice = int(choice)
    
    if choice != 0:
        w.append(cases[choice - 1])

def chooseMotherboard(w):
    mbs = ["Um", "dois", "tres"]

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

def chooseCPU(w):
    cpus = ["Um", "dois", "tres"]

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

def chooseCooler(w):
    coolers = ["Um", "dois", "tres"]

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

def chooseRAM(w):
    rams = ["Um", "dois", "tres"]

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

def chooseGPU(w):
    gpus = ["Um", "dois", "tres"]

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

def chooseMemory(w):
    mems = ["Um", "dois", "tres"]

    print("Vamos escolher o armazenamento!")
    for idx, mem in enumerate(mems):
        print("{}) {}".format(idx + 1, mem))

    choice = input("Digite o número do armazenamento, digite 0 caso não queira nenhum: ")
    choice = int(choice)

    while choice != 0:
        while not(choice >= 0 and choice <= len(mems)):
            choice = input("Escolha inválida, por favor digite o número do armazenamento desejado: ")
            choice = int(choice)

        if choice != 0:
            w.append(mems[choice - 1])
            choice = input("Deseja adicionar mais armazenamento ? Se sim, digite o número do armazenamento desejado, se não, digite 0: ")
            choice = int(choice)

def choosePowerSupply(w):
    pss = ["Um", "dois", "tres"]

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

def testAfd(w):
    δ = {
    }

    M = δ, 'q1', ['q2']

    return afd(M, w)

def afd(M, w):
    δ, q, F = M

    for s in w:
        q = δ[(q, s)]

    return q in F


def main():
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

    print(word)

    if (testAfd):
        print("Este computador é funcional!")
    else:
        print("Este computador possui incompatiblidades, por favor tente novamente.")

if __name__ == "__main__":
    main()