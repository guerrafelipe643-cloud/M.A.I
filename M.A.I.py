# =============================================================================
#   MAI - Memory Architecture for AI (Arquitetura Modular para IA)
#   Copyright (C) 2026  Felipe Guerra Rodrigues Athaydes
#
#   Este programa é um software livre: você pode redistribuí-lo e/ou modificá-lo
#   sob os termos da Licença Pública Geral GNU conforme publicada pela
#   Free Software Foundation, tanto a versão 3 da Licença, ou (a seu critério)
#   qualquer versão posterior.
#
#   Este programa é distribuído na expectativa de que seja útil, mas
#   SEM NENHUMA GARANTIA; sem mesmo a garantia implícita de
#   COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM PROPÓSITO ESPECÍFICO. Veja a
#   Licença Pública Geral GNU para mais detalhes.
#
#   Você deve ter recebido uma cópia da Licença Pública Geral GNU junto com
#   este programa. Se não, veja <https://gnu.org>.
# ==============================================================================
import random, string
import time
#ND: neurônio de digíto
#NP: neurônio de palavra/padrão
#NS: neurônio de "sintaxe" focado em decisões gerais de reconhecimentos de padrões
#ta: taxa de aprendizado
#mem: memória
#ent: entrada
#vn: valor neurônio
#vna: valor atual do neurônio
#err: erro
class ND:
    
    def __init__(self, name):
        self.name = name
        self.mem = {}
        self.vn = 0
    
    def detectar(self, ent): #verifica se ent está em mem
        if ent in self.mem:
            return self.mem[ent], "Conhecido"
        else:
            return None, "Novo"
    def aprender(self, entrada):
        ta = 0.1
        vn = self.vn  # começa com o valor atual do neurônio
        err = vn - entrada 
        while True: #cálculos para aproximação da entrada
            if abs(err) < 1e-2:   
                break
            err = entrada - vn          
            vna = max(-1, min(1, err * ta))
            vn += vna
        vn = round(vn)
        if vn == entrada:
            self.mem[entrada] = vn     
class NP:
    def __init__(self, name): 
        self.name = name
        self.mem = {}
    def comparar(self, ents): #verifica se ent é ou não conhecido
        if ents in self.mem:
            return "Conhecido"
        else:
            self.mem[ents] = ents
            return "Novo! e salvo!"

while True:
    ciclo = 0
    nds = []
    #menu
    print("=================:MENU M.A.I:=================")
    print("Selecione a opção desejada: ")
    print("1 para sair")
    print("2 para treinamento")
    try:
        opcao = int(input(":   "))
    except ValueError:
        print("Digite somente números")
    if opcao == 1:
        break
    if opcao == 2:
        nps = []
        use = input("Você deseja usar NP?: ").lower()
            
        if "s" in use:
            num = int(input("Quantos nds cada NP deve agrupar? "))
        print("Digite o tipo de entrada: ")
        try:
            opcao1 = int(input("1 para entrada aleatória    |    2 para entrada digitada: "))
        except ValueError:
            continue
        print("")
        try:
            numerociclos = int(input("Digite o número de ciclos: "))
        except ValueError:
            continue
        print("")
        try:
            tempo = float(input("Digite o tempo entre cada ciclo: "))
        except ValueError:
            continue
        print("")
        try:
            numerond = int(input("Digite o número de ND's: "))
        except ValueError:
            continue
        #criação dos neurônios
        if "s" in use:
            numnp = numerond // num
            for i in range(numnp):
                nps.append(NP(f"np.{i}"))
        for i in range(numerond):
            nds.append(ND(f"nd.{i}"))
        ns = NP("NS")
        print(f"{len(nds)} nds criados!")
        resultados = []
        memoriaglobal = []
        ciclo = 0
        valores_nds = []
        #ciclo principal
        while ciclo < numerociclos:
            resultado = []
            resultadotodo = []
            valores_nds = []
            conhecidosn = 0
            resultados = []
            #menu de texto aleatório(apenas para entradas gigantescas como de 2.000.000 de dígitos
            if opcao1 == 1:
                text = "".join(random.choices(string.ascii_letters + string.digits, k=len(nds)))
            if opcao1 == 2:
                text = input("Digite a entrada: ")
            if len(text) > len(nds):
                print(f"Muitos caracteres!, o texto tem {len(text)} caracteres, o máximo é {len(nds)}!")
                continue
            #loop para os cáculos corretos
            for i, char in enumerate(text):
                #transformações de cada digíto do texto
                if char.isdigit():
                    ent = int(char)
                else:
                    ent = ord(char)
                nd = nds[i]
                valor,status = nd.detectar(ent)
                #roda função aprender
                if status == "Novo":
                    nd.aprender(ent)
                else:
                    conhecidosn += 1
                valores_nds.append(nd.vn)
            if "s" in use:
                #fala de quando até quando da lista os nps irão pegar as saídas
                for i, np in enumerate(nps):
                    inicio = i * num
                    fim = inicio + num
                    ents = tuple(valores_nds[inicio:fim])
                    resultadotodo.append(np.comparar(ents))
            #prints
            compreensaogeral = ns.comparar(tuple(valores_nds))
            print(f'número de conhecidos (ND) detectados: {conhecidosn}')
            print(f"Esse padrão é: {resultadotodo}")
            print(f"RESULTADO NS: {compreensaogeral}")
            time.sleep(tempo)
            ciclo += 1
