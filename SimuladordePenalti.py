# Simulador de Penalti (Amistosos)
import random
# imports
from random import choice
from time import sleep
import keyboard
from golinit import Cantos_do_Gol





# Varíaveis inicias

times_br = [
    "Corinthians",
    "Palmeiras",
    "São Paulo",
    "Santos",
    "Flamengo",
    "Fluminense",

]



def Instrucoes():
    print("Jogo está sendo iniciado")
    sleep(2)
    print("""Instruções gerais:
    [1] Iniciar Jogo
    [2] Instruções
    [3] Sair""")
    escolha1 = int(input("Digite sua escolha: "))
    jaescolheu = False
    while jaescolheu == False:
        if escolha1 >=4:
            print("ESCOLHA INVÁLIDA! escolha a opção certa.")
            print("""Instruções gerais:
                [1] Iniciar Jogo
                [2] Instruções
                [3] Sair""")
            escolha1 = int(input("Digite sua escolha: "))
        else:
            break

    if escolha1 == 1:
        print("Iniciando jogo.")
    elif escolha1 == 2:
        print("Instruções")
    elif escolha1 == 3:
        print("Jogo finalizado!")

Instrucoes()
cantos = Cantos_do_Gol()
pos_cantos = cantos.posicoes

def Jogo_penaltis(times : list[str]):
    escolha_de_time = str(input("Digite o nome do seu time: "))
    if escolha_de_time in times:
        print("Seleção selecionada")
        times.remove(escolha_de_time)
    escolha_da_ia = choice(times)
    print(f"""
AMISTOSO
{escolha_de_time} x {escolha_da_ia}
""")
    jogo_rodando = True
    placar_cas = int(0)
    placar_for = int(0)
    def inicio_do_jogo():



        nonlocal  placar_cas, placar_for
        print("Preparado pra cobrança")
        sleep(1.5)
        print("Qual canto o jogador irá bater?")
        printar_cantos = """
        [1] Canto Superior Direito
        [2] Canto Superior Esquerdo
        [3] Canto Inferior Esquerdo
        [4] Canto Inferior Direito
        [5] Meio
        [6] Meio alto"""

        interromper = False
        goleiro = random.randint(1, 6)
        if escolha_de_time == "adm123":
            interromper = True


        for rodada in range(1, 6):
            if interromper == True:
                break
            print(f"Rodada {rodada} de 5")
            ia_ira_pular = random.randint(1, 6)
            print(printar_cantos)
            penalti = int(input("Digite o canto que você ira bater: "))
            print("JUIZ AUTORIZOU A COBRANÇA... ")
            sleep(1)
            print("COM FÉ NO PÉEEE")
            if penalti == ia_ira_pular:
                print(f"DEFENDEUUU o goleiro do {escolha_da_ia} ❌❌❌")
            else:
                print(f"GOOOOOOL DO {escolha_de_time}")
                placar_cas += 1
                print(f"{escolha_de_time} {placar_cas} x {placar_for} {escolha_da_ia}")
            ## ========= VEZ DA IA BATER O PENALTI =============
            print(f"Vez do {escolha_da_ia} Bater o penalti")
            print(printar_cantos)
            defenda = int(input("Sua vez de defender, onde você ira pular? "))
            print("AUTORIZADOOO A COBRANÇA")
            ia_chute = random.randint(1, 6)
            sleep(1.5)
            print(f"LA VEM O {escolha_da_ia}")
            sleep(2)


            if defenda == ia_chute:
                print(f"DEFENDEUUUU O {escolha_de_time} ❌❌❌")
            else:
                print(f"GOOOLLLLLLL DO {escolha_da_ia} ❌❌❌")
                placar_for += 1
                print(f"{escolha_de_time} {placar_cas} x {placar_for} {escolha_da_ia}")
            # VERIFICAR O GANHADOR!

            if rodada == 5:
                if placar_cas > placar_for:
                    print("🏅 PARABÉNSSS! VOCÊ GANHOU!!!!")
                elif placar_for > placar_cas:
                    print("VOCÊ PERDEU ❌❌❌, mais pode tentar novamente!")
                elif placar_for == placar_cas:
                    print("chegou a hora que todos temem...")
                    sleep(2)
                    print("E HORA DE COBRANÇAS ALTERNADAS!")



    inicio_do_jogo()

Jogo_penaltis(times_br)
