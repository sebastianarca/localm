# Version Python de localm.sh, escrito en bash.

## Dependencia para compilador

pip install pyinstaller

## Para compilar
```python3.9 ~/.local/bin/pyinstaller -n localm __main__.py```

## Para instalar
```sudo rm -rf /opt/localm; sudo cp -r localm.python/dist/localm /opt/; sudo rm  /usr/local/bin/localm; sudo ln -s /opt/localm/localm /usr/local/bin/localm```



 
## Recursos
 - https://github.com/Akuli/python-tutorial/blob/master/basics/the-way-of-the-program.md
 - https://github.com/Akuli/python-tutorial/blob/master/basics/modules.md
 - https://docs.python.org/3.9/reference/index.html
 - https://www.w3schools.com/python/python_for_loops.asp
 - https://pyinstaller.readthedocs.io/en/stable/
