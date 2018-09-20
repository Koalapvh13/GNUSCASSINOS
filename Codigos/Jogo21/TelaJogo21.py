from Codigos.Jogo21.baralho import Baralho
import random
#import time
from pygame  import mixer
from tkinter import *

#fodasticamente by:grupomaisfodadoBrasil <"G'NUS DIGITAIS"> não ouse tocar nesta linha!>>risco de morte
#melhor team: "G'NUS DIGITAIS"> Matheus Dias, Bruno Felipe, Rodrigo Rocca e Igor Ramos(6998121-0671)..

def limpaMeio():
    logo['image']=''
    medalha['image']=''
    perdeuimg['image']=''
    empateimg['image']=''
    logo.place(x=0,y=0)
    medalha.place(x=0, y=0)
    perdeuimg.place(x=0, y=0)
    empateimg.place(x=0,y=0)
    resultadoTela("não")


def resultadoTela(s):
    if s == 'sim':
        lbResultadoMaquina.place(x=360, y=160)
        lbPontuacaoMaquina.place(x=472, y=168)

        lbResultadoJogador.place(x=360, y=410)
        lbPontuacaoJogador.place(x=472, y=418)

        lbResultadoMaquina['image']=pontoMaquina
        lbResultadoJogador['image']=pontoJogador
        lbPontuacaoMaquina['text'] = valorMaquina
        lbPontuacaoJogador['text'] = valorJogador

    else:

        lbPontuacaoMaquina['text'] = ""
        lbPontuacaoJogador['text'] = ""
        lbPontuacaoMaquina.place(x=1000,y=650)
        lbPontuacaoJogador.place(x=1000,y=650)
        lbResultadoJogador['image']=''
        lbResultadoMaquina['image']=''


def empatou():
    mixer.init()
    #mixer.music.load(r'C:\Users\Igor\Pictures\sounds\uhoh.mp3')  # emb 3 é o som mais lento.
    mixer.music.load(r'sounds/uhoh.mp3')
    mixer.music.play()
    limpaMeio()
    resultadoTela("sim")
    logo['image'] = ''
    empateimg['image']=imgEmpate
    empateimg.place(x=350,y=220)

    logo.place(x=0, y=0)
def ganhou():
    #musica ganhou
    mixer.init()
    #mixer.music.load(r'C:\Users\Igor\Pictures\sounds\ganhou.mp3')  # emb 3 é o som mais lento.
    mixer.music.load(r'sounds/ganhou.mp3')
    mixer.music.play()
    limpaMeio()
    resultadoTela("sim")
    logo['image'] = ''
    medalha['image']=imgMedalha
    medalha.place(x=350, y=220)
    logo.place(x=0,y=0)

def perdeu():
    #musica perdeu
    mixer.init()
    #mixer.music.load(r'C:\Users\Igor\Pictures\sounds\uhoh.mp3')  # emb 3 é o som mais lento.
    mixer.music.load(r'sounds/uhoh.mp3')
    mixer.music.play()
    limpaMeio()
    resultadoTela("sim")
    logo['image'] = ''
    perdeuimg['image'] = imgPerdeu
    perdeuimg.place(x=350, y=220)
    logo.place(x=0, y=0)

def play():
    #time.sleep(1)
    limpaMeio()
    jogar()
    inicio['image']=''
    logo['image']=imglogo
    medalha['image']=''
    medalha.place(x=0,y=0)
    perdeuimg['image']=''
    perdeuimg.place(x=0,y=0)
    inicio.place(x=0,y=0)
    limpar.place(x=680, y=500)
    logo.place(x=340, y=250)
    AtualizaPlay()
def AtualizaPlay():
    reinicio.place(x=748,y=500)


def Embaralhar():
    mixer.init()
    #mixer.music.load(r'C:\Users\Igor\Pictures\sounds\emb3.wav')#emb 3 é o som mais lento.
    mixer.music.load(r'sounds/emb3.wav')
    mixer.music.play()

def puxarcarta():
    mixer.init()
    #mixer.music.load(r'C:\Users\Igor\Pictures\sounds\DEAL1.wav')# deal1 é o mais rapido e agradavel.
    mixer.music.load(r'sounds/DEAL1.wav')
    mixer.music.play()
    global estado
    global valorJogador
    global valorMaquina

    cartasJogador.append(bara.topo_da_pilha())
    #url1 = criaString(descobreCarta(cartasJogador)) add imagem
    jogador = Trata(cartasJogador)
    valorJogador = placarJogador(jogador)
    lbJogador['text']=valorJogador

    if valorJogador>21:
        perdeu()
        print("1-perdeu")
        reconfigura()
        lbJogador['text']='00'
        lbMaquina['text']='00'
        estado=1
    elif valorJogador==21 and valorMaquina==21:
        empatou()
        print("1-Empate com a maquina!")
        #desvira cartas viradas e espera 2 segundos
        reconfigura()
        #zerarPartida()
    elif valorJogador==21:
        ganhou()
        print("1-ganhou de cara21!")
        # desvira cartas viradas e espera 2 segundos
        reconfigura()
        #zerarPartida()
    elif(valorMaquina==21):
        perdeu()
        print("1-perdeu, maquina ganhou de cara21!")
        #lbalperdeu se mostra visivel
        # desvira cartas viradas e espera 2 segundos
        reconfigura()
        #zerarPartida()
    elif valorMaquina>21:
        ganhou()
        print("1-ganhou! maquina estourou21")
        # desvira cartas viradas e espera 2 segundos
        reconfigura()
        #zerarPartida()

def zerarPartida():
    mixer.init()
    #mixer.music.load(r'C:\Users\Igor\Pictures\sounds\stop.wav')  # deal1 é o mais rapido e agradavel.
    mixer.music.load(r'sounds/stop.wav')
    mixer.music.play()
    limpaMeio()
    reconfigura()
    logo['image'] = imglogo
    logo.place(x=340, y=250)


def pararcarta():

    global valorJogador
    global valorMaquina


    if valorMaquina>valorJogador:
        perdeu()
        print("2-perdeu, maquina tinha valor maior!")
        # desvira cartas viradas e espera 2 segundos
        reconfigura()
        #zerarPartida()
    else:
        # maquina joga!@@@
        while (valorMaquina<valorJogador):
            cartasMaquina.append(bara.topo_da_pilha())
            maquina = Trata(cartasMaquina)
            valorMaquina = placarMaquina(maquina)
            lbMaquina['text']=valorMaquina

        if valorMaquina==valorJogador:
            empatou()
            print("2-empate! maquina decidiu empatar com vc!")
            # desvira cartas viradas e espera 2 segundos
            reconfigura()
            #zerarPartida()
        elif valorMaquina>21:
            ganhou()
            print("2-ganhou! maquina estourou valor!")
            # desvira cartas viradas e espera 2 segundos
            reconfigura()
            #zerarPartida()
        elif valorMaquina==21:
            perdeu()
            print("2-perdeu, maquina fez exatamente21!")
            # desvira cartas viradas e espera 2 segundos
            reconfigura()
            #zerarPartida()
        else:
            perdeu()
            print("2-perdeu! maquina venceu abaixo de 21!")
            # desvira cartas viradas e espera 2 segundos
            reconfigura()
            #zerarPartida()


def parar():
    musica_atual = mixer.music.stop()

def pausar():
    musica_atual = mixer.music.pause()

def sair():
    janela.destroy()

def placarMaquina(v):
    #inicio do print de placar da maquina
    tex="Máquina cards:. "
    t=''
    soma=0
    for i in range(len(v)):
        soma=soma+v[i]
        t=t+str(v[i])+", "
    print(tex+t+" PTs: "+str(soma))
    return soma

def placarJogador(v):
    #inicio do print de placar da maquina
    tex="Jogador cards:. "
    t=''
    soma=0
    for i in range(len(v)):
        soma=soma+v[i]
        t=t+str(v[i])+", "
    print(tex+t+" PTs: "+str(soma))
    return soma

def Trata(cartas):
    vet=[]
    #vetP=[]
    for i in range(len(cartas)):
        carM=0
        if cartas[i][0] == 'A':
            carM = 11
        elif cartas[i][0] == 'J' or cartas[i][0] == 'Q' or cartas[i][0] == 'K':
            carM = 10
        else:
            carM = int(cartas[i][0])
        vet.append(carM)
    return vet

def maquinaPensa(): #inteligencia não artificial :by gnu-digitail
    vet=[13,14,15,16,17,18,19]
    pensou=random.choice(vet)
    return pensou


def destroi(img):
    img.destroy()

def criaString(entrada):
    s=r"image\Baralho\ "+str(entrada)+".png"
    return s.replace(" ","")

def descobreCarta(mat):
    ultima=mat[-1]
    valor=''
    valor=ultima[1]+ultima[2][0]
    return valor
def reconfigura():
    #limpaMeio()
    global valorJogador
    global valorMaquina
    global cartasMaquina
    global cartasJogador
    img1['file']=r"image\cartasSlot.png"
    img2['file']=r"image\cartasSlot.png"
    img3['file']=r"image\cartasSlot.png"
    img4['file']=r"image\cartasSlot.png"
    lbMaquina['text']='00'
    lbJogador['text']='00'
    valorMaquina=0
    valorJogador=0
    cartasJogador=[]
    cartasMaquina=[]
    print("Máquina cards:. "+str(cartasMaquina)+" Pts: "+str(valorMaquina))
    print("Jogador cards:. "+str(cartasJogador)+" Pts: "+str(valorJogador))

def jogar():

    Embaralhar()
    urlFechada=r"image\cartafechada.png"
    global cartasMaquina
    cartasMaquina= []
    global cartasJogador
    cartasJogador= []
    global valorJogador
    valorJogador= 0
    global valorMaquina
    valorMaquina= 0

    bara.gerar_baralho()
    bara.pilha_embaralhar()

    cartasMaquina.append(bara.topo_da_pilha())
    url1 = criaString(descobreCarta(cartasMaquina))

    cartasJogador.append(bara.topo_da_pilha())
    url3 = criaString(descobreCarta(cartasJogador))

    cartasMaquina.append(bara.topo_da_pilha())
    #este n possui URL pois esta carta esta virada para baixo.

    cartasJogador.append(bara.topo_da_pilha())
    url4 = criaString(descobreCarta(cartasJogador))

    img1['file'] = url1
    img2['file'] = urlFechada
    img3['file'] = url3
    img4['file'] = url4

    maquina = Trata(cartasMaquina)
    print(maquina)

    jogador = Trata(cartasJogador)
    print(jogador)

    valorMaquina = placarMaquina(maquina)
    valorJogador = placarJogador(jogador)
    lbMaquina['text']=maquina[0]
    lbJogador['text']=valorJogador




'''codigo principal'''

janela = Tk()
janela.title("G'nus Cassinos")
bara = Baralho()
cartasMaquina=[]
cartasJogador=[]
valorJogador=0
valorMaquina=0
estado=0

'''fim codigo principal aplicacao'''

"""FIX-ME""" #da maquina
"""algumas imagens reservas em slots invisiveis que ficarão do lado direito do user: """

imag1 = Label(janela)
#carta1 = PhotoImage(file=)
#imag1['image'] = carta1
imag1['bg'] = '#006400'


imag2 = Label(janela)
#carta2 = PhotoImage(file=r"image\cartafechada.png")
#imag2['image'] = carta2
imag2['bg'] = '#006400'


imag3 = Label(janela)
#carta3 = PhotoImage(file=r"image\Baralho\Ao.png")
#imag3['image'] = carta3
imag3['bg'] = '#006400'

imag4 = Label(janela)
#carta4 = PhotoImage(file=r"image\Baralho\2o.png")
#imag4['image'] = carta4
imag4['bg'] = '#006400'


imag5 = Label(janela)
#carta5 = PhotoImage(file=r"image\Baralho\Ao.png")
#imag5['image'] = carta5
imag5['bg'] = '#006400'

imag6 = Label(janela)
#carta6 = PhotoImage(file=r"image\Baralho\2o.png")
#imag6['image'] = carta6
imag6['bg'] = '#006400'

imag7 = Label(janela)
#carta7 = PhotoImage(file=r"image\Baralho\Ao.png")
#imag7['image'] = carta7
imag7['bg'] = '#006400'

imag8 = Label(janela)
#carta8 = PhotoImage(file=r"image\Baralho\Ao.png")
#imag8['image'] = carta8
imag8['bg'] = '#006400'

#[1,2,3,4,***5,6,7***]: exemplo.
#3 é mais que o sufuciente!

#FIX-ME FIM"""

#botao comecar partida!
inicio=Button(janela)
imgInicio=PhotoImage(file=r"image\play2.png")
inicio['image']=imgInicio
inicio['relief']=FLAT
inicio['command']=play
inicio['bg']='#006400'
inicio.place(x=400,y=180)
#fim botao comecar partida!
#inicio botao reinicio
reinicio=Button(janela)
reinicioimg=PhotoImage(file=r"image\restart2.png")
reinicio['image']=reinicioimg
reinicio['relief']=FLAT
reinicio['command']=play
reinicio['bg']='#006400'
#fim reincio
#inicio limpar
limpar=Button(janela)
limparimg=PhotoImage(file=r"image\limpar.png")
limpar['image']=limparimg
limpar['relief']=FLAT
limpar['command']=zerarPartida
limpar['bg']='#006400'
#fim limpar
#LOGOgnus
logo=Label(janela)
imglogo=PhotoImage(file=r"image\meio.png")
logo['image']=imglogo
logo['bg']='#006400'
logo.place(x=340,y=250)

#MAQUINA SLOT CARTAS
#perfil label img MAQUINA gnu
imagemperfil=Label(janela)
imgperfil=PhotoImage(file=r"image\gnu.png")
imagemperfil['image']=imgperfil
imagemperfil['bg']='#006400'
imagemperfil.place(x=160,y=10)
#fim perfil gnu
#soma, placar da maquina gnu
imagemsomam=Label(janela)
imgsomam=PhotoImage(file=r"image\SOMA.png")
imagemsomam['image']=imgsomam
imagemsomam['bg']='#006400'
imagemsomam.place(x=160,y=130)
#fim placar maquina soma, GNU

#slot 1 para cartas
imagem=Label(janela)
img1=PhotoImage(file="image/cartasSlot.png")
imagem['image']=img1
imagem['bg']='#006400'
imagem.place(x=350,y=30)
#fim slot 1 para cartas
#slot 2 para cartas
imagem2=Label(janela)
img2=PhotoImage(file=r"image\cartasSlot.png")
imagem2['image']=img2
imagem2['bg']='#006400'
imagem2.place(x=443,y=30)
#fim do slot 2 para cartas maquina
#fim maquina !

#JOGADOR SLOT CARTAS
#img personagem jogador perfil
imagemPer=Label(janela)
imgPer=PhotoImage(file=r"image\user.png")
imagemPer['image']=imgPer
imagemPer['bg']='#006400'
imagemPer.place(x=160,y=430)
#fim perfil jogador img
#soma label img placar jogador
imagemsoma=Label(janela)
imgsoma=PhotoImage(file=r"image\SOMA.png")
imagemsoma['image']=imgsoma
imagemsoma['bg']='#006400'
imagemsoma.place(x=160,y=550)
#fim label soma, placar do jogador
#slot3, jogador
imagem3=Label(janela)
img3=PhotoImage(file=r"image\cartasSlot.png")
imagem3['image']=img3
imagem3['bg']='#006400'
imagem3.place(x=350,y=460)
#fim slot3 jogador
#slot4 jogador
imagem4=Label(janela)
img4=PhotoImage(file=r"image\cartasSlot.png")
imagem4['image']=img4
imagem4['bg']='#006400'
imagem4.place(x=443,y=460)
#fim slot4 jogador

#botao de parar
btnParar=Button(janela)
btnParar['bg']='#006400'
btnParar['relief']=FLAT
btnParar['command']=pararcarta
imgbtnP=PhotoImage(file=r"image\btnP.png")
btnParar['image']=imgbtnP
btnParar.place(x=550,y=500)
#fim botao parar

#botao descer mais carta
btnDescer=Button(janela)
btnDescer['bg']='#006400'
btnDescer['command']=puxarcarta
btnDescer['relief']=FLAT
imgbtnD=PhotoImage(file=r"image\btnD.png")
btnDescer['image']=imgbtnD
btnDescer.place(x=615,y=500)
#fim botao descer mais carta

#inicio  botao sair sistema
sa=Label(janela,text="Sair")
sa['bg']='#006400'
#sa['fg']="#c8ab37"
sa['font']='Arial',12,"bold"
sa['bg']="#C8AB37"
sa.place(x=15,y=570)
btnExit=Button(janela)
btnExit['bg']='#006400'
btnExit['command']=sair
btnExit['relief']=FLAT
imgbtnExit=PhotoImage(file=r"image\exit.png")
btnExit['image']=imgbtnExit
btnExit.place(x=0,y=505)
#FIM BTN SAIR SISTEMA
#monte label img, imagem do monte de cartas no lado direito>>>
imagem5=Label(janela)
img5=PhotoImage(file=r"image\monteC3.png")
imagem5['image']=img5
imagem5['bg']='#006400'
imagem5['height']=300
imagem5['width']=300
imagem5.place(x=650,y=20)
#fim imagem label, monte do lado direito>>>>>>>>>>>>>>>>>>>>>>>

#label mostrador da maquina
lbMaquina=Label(janela,text='00')
lbMaquina['font']='Arial',12,"bold"
lbMaquina['bg']="#C8AB37"
lbMaquina.place(x=254,y=138)
#fim label mostrador da maquina
#label mostrador jogador
lbJogador=Label(janela,text='00')
lbJogador['font']='Arial',12,"bold"
lbJogador['bg']="#C8AB37"
lbJogador.place(x=254,y=557)
#fim label mostrador jogador

#medalha ganhou partida
medalha=Label(janela)
imgMedalha=PhotoImage(file=r"image\ganhou2.png")
medalha['image']=imgMedalha
medalha['bg']='#006400'
#fim medalha ganhou partida

#perdeu  partida
perdeuimg=Label(janela)
imgPerdeu=PhotoImage(file=r"image\perdeu1.png")
perdeuimg['image']=imgPerdeu
perdeuimg['bg']='#006400'
#fim perdeu partida

#EMPATOU partida
empateimg=Label(janela)
imgEmpate=PhotoImage(file=r"image\empate.png")
empateimg['image']=imgEmpate
empateimg['bg']='#006400'
#fim EMPATOU partida

#lbResultadoMaquina
lbResultadoMaquina=Label(janela)
lbResultadoMaquina['font']='Arial',12,"bold"
pontoMaquina=PhotoImage(file=r"image\pontoM.png")
lbResultadoMaquina['bg']='#006400'
lbResultadoMaquina['image']=pontoMaquina
#fim lbResultadoMaquina

#lbResultadoJogador
lbResultadoJogador=Label(janela)
lbResultadoJogador['font']='Arial',12,"bold"
pontoJogador=PhotoImage(file=r"image\pontoM.png")
lbResultadoJogador['bg']='#006400'
lbResultadoJogador['image']=pontoJogador
#fim lbResultadoJogador

#lbPontuacao maquina inicio
lbPontuacaoMaquina=Label(janela)
lbPontuacaoMaquina['font']='Arial',12,"bold"
lbPontuacaoMaquina['bg']='#C8AB37'
lbPontuacaoMaquina.place(x=1000, y=165)
#lbPontuacao maquina fim

#lbPontuacao Jogador inicio
lbPontuacaoJogador=Label(janela)
lbPontuacaoJogador['font']='Arial',12,"bold"
lbPontuacaoJogador['bg']="#C8AB37"
lbPontuacaoJogador.place(x=1000, y=415)
#lbPontuacao Jogador fim

#outras configurações da janela..
janela.iconbitmap(r"image\logoSistema.ico")
janela.resizable(0,0)
janela.geometry("900x600+200+50")  # largura x altura + esquerda + topo
janela['bg'] = "#006400"
#janela.overrideredirect(True)#retira bordas
janela.mainloop()
#fim configs da janela e chamada do MAINLOOP()..
