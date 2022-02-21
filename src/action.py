import sys, os
from src.command import Command
from src.helper import HelperBash as bash

class Action:
	proyectConfig={}
	ROOT_PATH=''
	
	def __init__(self, CommandInstance:Command) -> None:
		Action.proyectConfig= CommandInstance.getProyectConfig()
		Action.ROOT_PATH		= Action.proyectConfig['root_path']
		self.process(CommandInstance.getCommand(), CommandInstance.getProyect())
		pass

	def process(self, command:str, proyect:str=""):
		bash.pushdir(Action.ROOT_PATH)
		extraParam	=""
		try:
			directory			=Action.proyectConfig['proyects'][proyect]['directory']
			composer_file	=Action.proyectConfig['proyects'][proyect]['composer_file']
		except:
			bash.popdir()
			sys.exit()
		
		# Si proyecto base, agregar parametros extra
		if proyect == "base":
			extraParam="-p vps"

		if command == "cd":
			print(f"{Action.ROOT_PATH}/{directory}")
			bash.newBashInDir(f"{Action.ROOT_PATH}/{directory}")
		else:
			# Ejecutar docker-compose con ruta y parametros
			os.system(f"docker-compose -f {Action.ROOT_PATH}/{directory}/{composer_file} {extraParam} {command}")
		# investigar diferencia con:
		# subprocess.run(f"docker-compose -f {pathProyect[stringProyecto]} {extraParam} {stringComando} ")
		# https://stackabuse.com/executing-shell-commands-with-python/
		# os.system("popd")
		bash.popdir()
		sys.exit()