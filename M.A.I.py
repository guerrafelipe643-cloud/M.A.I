# ===============================================================================
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
"""
Parte 1
O algoritmo consiste em uma IA totalmente focada em memorização, após um treino longo chega a ter latência baixa mesmo após 200 informações guardadas(dados do teste:
 Recuperação: 2917 ns
Recuperação: 1666 ns
Recuperação: 1042 ns
Recuperação: 990 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 937 ns
Recuperação: 885 ns
Recuperação: 834 ns
Recuperação: 886 ns
Recuperação: 2396 ns
Recuperação: 1042 ns
Recuperação: 938 ns
Recuperação: 885 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 885 ns
Recuperação: 938 ns
Recuperação: 886 ns
Recuperação: 885 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 937 ns
Recuperação: 886 ns
Recuperação: 885 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 834 ns
Recuperação: 938 ns
Recuperação: 833 ns
Recuperação: 885 ns
Recuperação: 937 ns
Recuperação: 938 ns
Recuperação: 938 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 938 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 937 ns
Recuperação: 885 ns
Recuperação: 885 ns
Recuperação: 885 ns
Recuperação: 990 ns
Recuperação: 833 ns
Recuperação: 885 ns
Recuperação: 885 ns
Recuperação: 937 ns
Recuperação: 886 ns
Recuperação: 938 ns
Recuperação: 937 ns
Recuperação: 885 ns
Recuperação: 885 ns
Recuperação: 885 ns
Recuperação: 833 ns
Recuperação: 1354 ns
Recuperação: 990 ns
Recuperação: 886 ns
Recuperação: 834 ns
Recuperação: 885 ns
Recuperação: 886 ns
Recuperação: 885 ns
Recuperação: 833 ns
Recuperação: 886 ns
Recuperação: 885 ns
Recuperação: 833 ns
Recuperação: 886 ns
Recuperação: 833 ns
Recuperação: 886 ns
Recuperação: 834 ns
Recuperação: 937 ns
Recuperação: 833 ns
Recuperação: 886 ns
Recuperação: 885 ns
Recuperação: 834 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 833 ns
Recuperação: 886 ns
Recuperação: 833 ns
Recuperação: 886 ns
Recuperação: 885 ns
Recuperação: 886 ns
Recuperação: 885 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 885 ns
Recuperação: 885 ns
Recuperação: 834 ns
Recuperação: 885 ns
Recuperação: 834 ns
Recuperação: 833 ns
Recuperação: 834 ns
Recuperação: 833 ns
Recuperação: 885 ns
Recuperação: 833 ns
Recuperação: 885 ns
Recuperação: 833 ns
Recuperação: 886 ns
Recuperação: 938 ns
Recuperação: 833 ns
Recuperação: 938 ns
Recuperação: 938 ns
Recuperação: 833 ns
Recuperação: 886 ns
Recuperação: 885 ns
Recuperação: 885 ns
Recuperação: 937 ns
Recuperação: 886 ns
Recuperação: 833 ns
Recuperação: 833 ns
Recuperação: 833 ns
Recuperação: 833 ns
Recuperação: 885 ns
Recuperação: 833 ns
Recuperação: 833 ns
Recuperação: 886 ns
Recuperação: 833 ns
Recuperação: 938 ns
Recuperação: 834 ns
Recuperação: 1458 ns
Recuperação: 990 ns
Recuperação: 937 ns
Recuperação: 937 ns
Recuperação: 886 ns
Recuperação: 937 ns
Recuperação: 938 ns
Recuperação: 886 ns
Recuperação: 833 ns
Recuperação: 886 ns
Recuperação: 938 ns
Recuperação: 937 ns
Recuperação: 937 ns
Recuperação: 833 ns
Recuperação: 937 ns
Recuperação: 886 ns
Recuperação: 886 ns
Recuperação: 886 ns


{Feito em um redimi note 13 4G}
) em absolutamente todas as respostas, é um algoritmo totalmente modular e baseado no funcionamento do corpo humano misturado com algoritmos antigos, apesar disso nos testes realizados, a MAI apresentou desempenho superior a modelos neurais tradicionais em tarefas de memorização e recuperação de padrões previamente aprendidos. todavia acaba perdendo muito em capacidade de raciocínio.
Parte 2
Organização modular / hierarquia:
Células
Tecidos 
Sistemas 
________________________________.
Organização por neurônios:
Nd: neurônio de dígito: usa apenas um carácter 
Np: neurônio de palavra: usa só uma palavra
Ns: neurônio de sintaxe: organiza as palavras 
________________________________.
Explicações:
Células: conjunto básico e mínimo formado por apenas um ND
Tecido: conjunto de mínimo de organização entre um ND, um np e um ns
Sistema: conjunto mínimo e básico da IA completa
_______________________________.
Base descompactada:
Cada neurônio tem sua memória isolada, que representa a capacidade de armazenamento e o armazenamento dele, basicamente cada neurônio acaba tendo uma porta and com as entradas sendo: ent(entrada normal se ela existe uma entrada da porta and = 1) e memória (se ent está na memória a outra entrada é = 0 e puxa o resultado diretamente da memória), se a porta and ativar sendo 1,1 a saída= 1, o neurônio acaba ativando (obs: essa base vale para apenas para ND)
________________________.
Cálculos de um ND isolado:
Variáveis mínimas:
Mem: (memória interna)
Memg: (memória global)
Err: (erro)
Ta: (taxa de aprendizagem)
VN: (valor do neurônio)
VNA: (valor atual do neurônio)
VAN: (valor de ativação do neurônio)
VAMN: (valor de ativação da memória → neurônio(
VAE: (valor de ativação entrada)
Ent: (entrada)
↓
Cálculos mínimos:
Cálculo do erro: ERR = ENT - VN
Cálculo do ajuste: VNA = (mínimo: -1, máximo: 1)TA . ERR
Cálculo de soma: VN = VN + VNA
Cálculo de busca memória: se ENT está na memória: VN = MEM(ENT)
_______________________________.
Cada neurônio restante exemplo np e na tem um funcionamento praticamente igual ao ND porém mais otimizado para sua função por isso não falei deles.
_____________________________.
Testes mentais:
Se os ND's souberem o valor de cada algarismo como vai estar salvo em Mem eles vão conseguir copiar qualquer número com latência quase 0
____________________________.
O funcionamento da IA se baseia apenas nos ND sendo os NP e NS apenas acessórios para caso alguém queira implementar raciocínio(muito mal otimizada para isso)
__________________________.
Usos: detectar padrões e demonstra-los, exemplo: comportamento de animais
Implantação em aceleradores de partículas para descobrir novos átomos
__________________________.
Exemplo python:"""
import random
import time
mem = {}
memg = {}
ta = 0.1
vamn = 1
van = 1
vae = 1
vn = random.randint(0,9)
vna = 0
err = 0
tenta = 0
def treinocelula(mem,memg,vamn,van,vae,ent,vn,vna,err,ta,tenta):
    if ent is None:
        vae = 0
        vamn = 0
    else:
        vae = 1
    if ent in mem and vae == 1:
        vamn = 0
        vae = 1
        vna = mem[ent]
    else:
        vae = 1
        vamn = 1
    if vae == 1 and vamn == 1:
        van = 1
    if van == 1:
        err = ent - vn
        vna = max(-1,min(1,err * ta))
        vn = vn + vna
        tenta += 1
        if abs(err) < 1e-2 or tenta > 1e8:
            vn = round(vn)
            if vn == ent:
                mem[ent] = vn
                if ent in mem:
                    memg[ent] = vn
    return mem,memg,vamn,van,vae,ent,vn,vna,err,ta,tenta
while True:
    tenta = 0
    try:
        ent = int(input("Digite uma entrada: "))
        ta = float(input("digite a taxa de aprendizado: "))
    except ValueError:
        print("digite somente números")
        continue
    while True:
        mem,memg,vamn,van,vae,ent,vn,vna,err,ta,tenta = treinocelula(mem,memg,vamn,van,vae,ent,vn,vna,err,ta,tenta)
        if abs(err) < 1e-3 or tenta > 1e8:
            print(f"valor neuronio: {vn}")
            print(f"memória: {mem}")
            print(f"tentativas: {tenta}")
            break
""""
_______________________________.
Para impedir explosões pode-se definir um máximo e um mínimo do erro e tentativas, para impedir bugs de processamento Mem já vem com o algarismo 0 incluído para não zerar VN e entrar em um ciclo infinito.
______________________________.
Cada memória tem um filtro se algo já salvo está na memória nada novo é adicionado pois não passa pelo cálculo do neurônio
_____________________________.
Sistema de interligação por ND:
Cada ND pode cuidar de um carácter e as saídas irão convergir em uma palavra na ordem crescente, cada neurônio vai ter um ID escondido/abstrato que funcionará na ordem exemplo neurônio 1 - 100 na ordem, para impedir erros custará muito processamento mas cada np terá acesso a todos os ND, para não bagunçar tudo ele só pegará uma palavra exemplo: (oi), isso custa 2 ND mas tem 100 ND, como é uma frase pela própria mente humana as palavras são separadas por espaços, ele detectara algo entre 2 espaços e irá corrigir a palavra gerada pelos ND's
_______________________________.
Np funcionamento:
Cada np funciona como uma "via", que conecta todos os np's do código, consequentemente isso afetaria a organização, por isso ele detectara uma coisa presente em toda forma de linguagem da terra os espaços, e as letras entre dois espaços seriam uma palavra, consequentemente cada np organizaria a saída dos np's conectados a ele, cada np também tem as mesmas váriaveis de um ND somente as entradas e os cálculos são diferentes, exemplo:



Certo: senhora

Gerado: snhraoe

Cada letra tem um valor e é só diminuir o valor da primeira letra gerada pela a certa e ver se está correto
____________________________________.
*Em desenvolvimento 


Made by Felipe Guerra Rodrigues Athaydes """
