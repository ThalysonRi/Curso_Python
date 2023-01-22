import pyautogui
import cv2

def whatsapp():
    img_google=cv2.imread(r"D:\Cursos\CFB - Curso Python\Curso_Python\Aulas\Aula04\google.png")
    img_google = pyautogui.locateCenterOnScreen(img_google,confidence=0.7)
    pyautogui.click(img_google)
    img_sitewhatsapp = cv2.imread(r"D:\Cursos\CFB - Curso Python\Curso_Python\Aulas\Aula04\pesquisa2.png")
    img_sitewhatsapp = pyautogui.locateCenterOnScreen(img_sitewhatsapp, confidence=2)
    if img_sitewhatsapp!=None:
        for coordinates in img_sitewhatsapp:
            pyautogui.click(img_sitewhatsapp)
            pyautogui.write("https://web.whatsapp.com")
            pyautogui.sleep(1)
            pyautogui.press('enter')
    else:
        print("Nao encontra imagem")
    img_whatsapp=cv2.imread(r"D:\Cursos\CFB - Curso Python\Curso_Python\Aulas\Aula04\whatsapp_web.png")
    img_whatsapp = pyautogui.locateCenterOnScreen(img_whatsapp,confidence=0.7)
    if img_whatsapp==None:
        pyautogui.sleep(13)
    img_mensagem=cv2.imread(r"D:\Cursos\CFB - Curso Python\Curso_Python\Aulas\Aula04\pesquisa.png")
    img_mensagem = pyautogui.locateCenterOnScreen(img_mensagem, confidence=0.7)
    if img_mensagem!=None:
        pyautogui.click(img_mensagem)
        pyautogui.write("Thalyson")
        pyautogui.press('enter')
        pyautogui.sleep(1)
        pyautogui.write("Aprenda programacao")
        pyautogui.press('enter')
        pyautogui.sleep(1)
        pyautogui.press('esc')
        pyautogui.sleep(1)
        pyautogui.hotkey('ctrl','shift','W')

while True:
    try:
        whatsapp()
        break
    except:
        print("Erro")

#Eu adicionei um loop "for" para iterar sobre o objeto gerador retornado pela função 'locateAllOnScreen()' e passar cada conjunto de coordenadas para a função 'click()', assim o erro é corrigido e o programa deve funcionar corretamente.
