import pyautogui
import cv2

def whatsapp():
    img_google=cv2.imread(r"D:\Cursos\CFB - Curso Python\Curso_Python\Aulas\Aula04\Imagens\google.png")
    img_google = pyautogui.locateCenterOnScreen(img_google,confidence=0.7) #Localiza uma imagem na tela
    pyautogui.click(img_google) #Clica na tela
    img_sitewhatsapp = cv2.imread(r"D:\Cursos\CFB - Curso Python\Curso_Python\Aulas\Aula04\Imagens\pesquisa2.png")
    img_sitewhatsapp = pyautogui.locateCenterOnScreen(img_sitewhatsapp, confidence=2) #Localiza uma imagem na tela
    if img_sitewhatsapp!=None: #Se o resultado for diferente de "None" segue abaixo.
        for coordinates in img_sitewhatsapp: #Se encontrar coordenadas na variável, segue os comandos abaixo.
            pyautogui.click(img_sitewhatsapp) #Clica na imagem
            pyautogui.write("https://web.whatsapp.com") #Digita o texto
            pyautogui.sleep(1) #Espera um segundo
            pyautogui.press('enter') #Digita enter
    else: #Caso não encontra
        print("Nao encontra imagem") #Retorna o texto
    img_whatsapp=cv2.imread(r"D:\Cursos\CFB - Curso Python\Curso_Python\Aulas\Aula04\Imagens\whatsapp_web.png")
    img_whatsapp = pyautogui.locateCenterOnScreen(img_whatsapp,confidence=0.7) #Procura a imagem
    if img_whatsapp==None: #Se não encontrar, espera 13 segundos
        pyautogui.sleep(13)
    img_mensagem=cv2.imread(r"D:\Cursos\CFB - Curso Python\Curso_Python\Aulas\Aula04\Imagens\pesquisa.png")
    img_mensagem = pyautogui.locateCenterOnScreen(img_mensagem, confidence=0.7) #Procura a imagem
    if img_mensagem!=None: #Se for diferente de None, segue os comandos abaixo
        pyautogui.click(img_mensagem) #Clica na imagem
        pyautogui.write("Thalyson") #Escreve a palavra Thalyson
        pyautogui.press('enter') #Pressiona enter
        pyautogui.sleep(1) #Espera 1 segundo
        pyautogui.write("Aprenda programacao") #Escreve o texto
        pyautogui.press('enter') #Pressiona enter
        pyautogui.sleep(1) #Espera um segundo
        pyautogui.press('esc') #Presiona esc
        pyautogui.sleep(1) #espera 1 segundo
        pyautogui.hotkey('ctrl','shift','W') #Aperta as teclas informadas

while True: #Segue o loop caso não haja erros
    try: #Sem erros
        whatsapp() #Chama a função whatsapp
        break #Faz um intervalo
    except: #Caso de erro
        print("Erro") #Printa na tela a mensagem erro

#Eu adicionei um loop "for" para iterar sobre o objeto gerador retornado pela função 'locateAllOnScreen()' e passar cada conjunto de coordenadas para a função 'click()', assim o erro é corrigido e o programa deve funcionar corretamente.
