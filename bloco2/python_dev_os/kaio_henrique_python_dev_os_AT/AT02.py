import subprocess
import os

input = ("Digite o nome do arquivo que deseja abrir: ")
# nao uso windows nem notepad
subprocess.Popen(["subl.exe", input])
# subprocess.Popen(["subl", input])