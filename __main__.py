import sys, os, json
from src.command import Command
from src.action import Action

localm_dir= os.path.dirname(__file__)
config={}
try:
	with open(f"{localm_dir}/localm.json") as f:
			config = json.load(f)
except:
  print(f"Debe existir el archivo de configuracion en {localm_dir}/localm.json")
  sys.exit()

Command.setProyectConfig(config)
Action(Command())
sys.exit()

