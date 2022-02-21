import os

class HelperBash:
	_pushstack = list()
	def __init__(self) -> None:
		pass

	def newBashInDir(directory:str=""):
		"""Lanza una subshell en el directorio actual.
		Corta la ejecucion
		https://stackoverflow.com/a/34094966
		Args:
			directory (str): Ruta a donde ir
		"""
		os.chdir(directory)
		shell = os.environ.get('SHELL', '/bin/sh')
		os.execl(shell, shell)

	def pushdir(dirname:str):
		HelperBash._pushstack.append(os.getcwd())
		os.chdir(dirname)
	#   os.system(f"cd {dirname}")

	def popdir():
		os.chdir(HelperBash._pushstack.pop())
	#   dirname=_pushstack.pop()
	#   os.system(f"cd {dirname}")