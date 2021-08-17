#pip install instabot

# importar la clase a utilizar
from instabot import Bot
# crear el nuevo objeto
mi_bot = Bot()

mi_bot.login(username='mi_nombre_de_usuario', password='mi_password')

mi_bot.follow_followers('cuenta_objetivo')
