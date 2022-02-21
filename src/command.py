import sys, os
import argparse

# Implementar interfaz para los comandos:
# getProyect() getCommand() getProyectConfig()

class Command:
	proyectConfig={}
	proyectSelected=''
	commandSelected=''
	def setProyectConfig(conf:dict) -> None:
		Command.proyectConfig=conf
		pass
	
	def getProyectConfig(self) -> dict:
		return Command.proyectConfig

	def getProyect(self) -> str:
		return Command.proyectSelected

	def setProyect(self, name:str) -> None:
		Command.proyectSelected = name
		pass

	def getCommand(self) -> str:
		return Command.commandSelected

	def setCommand(self, name:str) -> None:
		Command.commandSelected = name
		pass

	def listProyects(self) -> str:
		descript	= ''
		for proyect in Command.proyectConfig['proyects']:
			proyect_descript	= Command.proyectConfig['proyects'][proyect]['descripcion']
			descript+= f"{proyect}:		{proyect_descript}"+'\n'
		# return descript.format(length='multi-line', ordinal='second')
		return descript

	def __init__(self) -> None:
		parser = argparse.ArgumentParser(
			prog='localm', 
			description='localm, es un gestor de proyectos para localhost. (Localhost Manager)',
			epilog=self.listProyects(),
			formatter_class=argparse.RawTextHelpFormatter
		)
		parser.add_argument('-s', '--start', 
			action='store_true', 
			help="Aplica el comando de docker-compose 'up -d'")
		parser.add_argument('--stop', 
			action='store_true', 
			help="Aplica el comando de docker-compose 'down --remove-orphans'")
		parser.add_argument('--logs', 
			action='store_true', 
			help="Aplica el comando de docker-compose 'logs -f'")
		parser.add_argument('--build', 
			action='store_true', 
			help="Aplica el comando de docker-compose 'build --force-rm'")
		parser.add_argument('--monit', 
			action='store_true', 
			help="Aplica el comando 'docker stats'")
		parser.add_argument('--dir', '--cd', 
			action='store_true', 
			help="Ir al directorio de la aplicacion")
		parser.add_argument('proyect', 
			help='Proyecto disponible del listado', 
			default="")

		dict_selected_arguments	= vars(parser.parse_args())
		selected_first_arg			= ''
		proyect									= dict_selected_arguments['proyect']
		for arg in dict_selected_arguments:
			if dict_selected_arguments[arg] == True:
				selected_first_arg='--'+arg
				break
		self.setProyect(proyect)
		self.setCommand(self.process(selected_first_arg))

	def process(self, comando="") -> str:
		if (comando == "--start"):
			Command.commandSelected	= "up -d"
			return Command.commandSelected
		elif (comando == "--stop"):
			Command.commandSelected	= "down --remove-orphans"
			return Command.commandSelected
		elif (comando == "--logs"):
			Command.commandSelected	= "logs -f"
			return Command.commandSelected
		elif (comando == "--build"):
			Command.commandSelected	= "build --force-rm"
			return Command.commandSelected
		elif (comando in ("--dir", "--cd")):
			Command.commandSelected	= "cd"
			return Command.commandSelected
		elif (comando == "--monit"):
			self.monitor()
		else:
			print("Ningun parametro encontrado")
			sys.exit()

	def monitor(self) -> None:
		os.system("docker stats; exit 1")
		sys.exit()