## Este script é executado ao iniciar o sistema
## O comando está em .config/autostart/monitor_bateria.desktop e seu conteúdo está descrito no arquivo leia.txt

# certifique-se que tenha instalados esses módulos. Caso não tenha, execute no terminal: pip install nomeDoMóduloDesejado
import psutil
from plyer import notification
import time
import playsound

# executará infinitamente
while(True):
	bateria = psutil.sensors_battery() # definindo a bateria
	nivel = bateria.percent # porcentagem da bateria
	carregando = bateria.power_plugged # se está carregando(true ou false)

	# Se estiver com menos de 15 e 'carregando' for false
	if nivel < 15 and not carregando:
		# chamando a notificação
		notification.notify(
			title = "Nível de bateria",
			message = (f'{nivel:,.0f}% restantes\nCarregue a bateria!'), # mostrando a mensagem com o nível de bateria sem casas decimais
			timeout = 10 # tempo de exibição da notificação
		)

		# tocando o som(opcional)
		playsound.playsound('/Endereço/completo/do/seu/mp3.mp3')

		time.sleep(10)

	continue
