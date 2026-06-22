
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
class ND:
    def __init__(self, name):
        self.name = name
        self.mem = {}
        self.memg = {}
        self.ta = 0.1
        self.vn = random.randint(0,9)
        self.tenta = 0
    def detectar(self, ent):
        if ent in self.mem:
            return self.mem[ent], "Conhecido"
        else:
            return None, "Novo"
    def aprender(self, entrada):
        tenta = 0
        vn = self.vn  # começa com o valor atual do neurônio
        while True:
            err = entrada - vn           # recalcula o erro a cada iteração
            if abs(err) < 1e-2 or tenta > 1e8:   # condição de parada
                break
            vna = max(-1, min(1, err * self.ta))
            vn += vna
            tenta += 1
        vn = round(vn)
        if vn == entrada:
            self.mem[entrada] = vn
            if entrada in self.mem:         
                self.memg[entrada] = vn
            self.vn = vn                     
        self.tenta = tenta                   
class NP:
    def __init__(self, name):
        self.name = name
        self.mem = {}
    def comparar(self, ents):
        if ents in self.mem:
            return "Conhecido"
        else:
            self.mem[ents] = ents
            return "Novo! e salvo!"
class NS:
    def __init__(self, name):
        self.name = name
        self.mem = {}
    def comparar(self, ents):
        if ents in self.mem:
            return "Padrão geral: Conhecido"
        else:
            self.mem[ents] = ents
            return "Padrão geral: Novo e aprendido"
ciclo = 0
while True:
    
    ciclo = 0
    nds = []
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
        if "s" in use:
            numnp = numerond // num
            for i in range(numnp):
                nps.append(NP(f"np.{i}"))
        for i in range(numerond):
            nds.append(ND(f"nd.{i}"))
        ns = NS("NS")
        print(f"{len(nds)} nds criados!")
        resultados = []
        memoriaglobal = []
        ciclo = 0
        valores_nds = []
        while ciclo < numerociclos:
            resultado = []
            resultadotodo = []
            valores_nds = []
            conhecidosn = 0
            resultados = []
            if opcao1 == 1:
                text = "".join(random.choices(string.ascii_letters + string.digits, k=len(nds)))
            if opcao1 == 2:
                text = input("Digite a entrada: ")
            if len(text) > len(nds):
                print(f"Muitos caracteres!, o texto tem {len(text)} caracteres, o máximo é {len(nds)}!")
                continue
            inicio1 = time.perf_counter_ns()
            for i, char in enumerate(text):
                if char.isdigit():
                    ent = int(char)
                else:
                    ent = ord(char)
                nd = nds[i]
                inicio = time.perf_counter_ns()
                valor,status = nd.detectar(ent)
                fim = time.perf_counter_ns()
                print(f"latência de detecção: {fim-inicio} ns")
                if status == "Novo":
                    inicio2 = time.perf_counter_ns()
                    nd.aprender(ent)
                    fim2 = time.perf_counter_ns()
                    print(f"latência de cáculo do {nd.name}: {fim2-inicio2} ns")
                    print(f"memória atual: {nd.mem}")
                else:
                    conhecidosn += 1
                valores_nds.append(nd.vn)
            if "s" in use:
                for i, np in enumerate(nps):
                    inicio = i * num
                    fim = inicio + num
                    ents = tuple(valores_nds[inicio:fim])
                    resultadotodo.append(np.comparar(ents))
            compreensaogeral = ns.comparar(tuple(valores_nds))
            fim1 = time.perf_counter_ns()
            print(f"latência total: {fim1-inicio1} ns")
            print(f'número de conhecidos (ND) detectados: {conhecidosn}')
            print(f"Esse padrão é: {resultadotodo}")
            print(f"RESULTADO NS: {compreensaogeral}")
            time.sleep(tempo)
            ciclo += 1
