import pyautogui as pag
import pyperclip
import time

#abrindo chrome.
pag.hotkey("win","s")
pag.write("chrome")
pag.press("enter")

#tempo de espera.
time.sleep(2)

#abrindo whatsapp.
pag.write("https://web.whatsapp.com/")
pag.press("enter")

#ir no botao pesquisar o contato.
time.sleep(5)
pag.click(x=249, y=172, clicks=2, interval=0.25)


pyperclip.copy("gonçalo")
pag.hotkey("ctrl", "v")

#entrando na conversa.
pag.press("enter")

#mandando mensagem.
pyperclip.copy("Olá, essa mensagem esta sendo mandada por uma automatizaçao em python.")
pag.hotkey("ctrl", "v")
pag.press("enter")
