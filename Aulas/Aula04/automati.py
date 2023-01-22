import pyautogui
import cv2


def localizar_imagem():
    img = cv2.imread(r"D:\Cursos\CFB - Curso Python\Curso_Python\Aulas\Aula04\thalyson.png")
    y = pyautogui.locateCenterOnScreen(img, confidence=0.7)
    pyautogui.sleep(1)
    if y==None:
        print("Imagem nao encontrada")
    else:
        pyautogui.click(y) 
    return "Ok" 

contador = 1
while (contador<=5):
    localizar_imagem()
    contador = contador + 1
else:
    print("Ja cliquei 5 vezes na tela")
