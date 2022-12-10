## Este script é executado ao iniciar o sistema
## O comando está em .config/autostart/monitor_bateria.desktop

import psutil
from plyer import notification
import time
import playsound

while(True):
	bateria = psutil.sensors_battery()
	nivel = bateria.percent
	carregando = bateria.power_plugged

	if nivel < 15 and not carregando:
		notification.notify(
			title = "Nível de bateria",
			message = (f'{nivel:,.0f}% restantes\nCarregue a bateria!'),
			timeout = 10
		)

		playsound.playsound('/Endereço/completo/do/seu/mp3.mp3')

		time.sleep(10)

	continue
