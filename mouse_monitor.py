import pyautogui
import time
import os

try:
    while True:
        x, y = pyautogui.position()
        # Limpa o terminal para não poluir
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Posição atual do mouse: X={x}, Y={y}")
        time.sleep(0.05)  # Atualiza a cada 50ms (ajuste se quiser)
except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")

