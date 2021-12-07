import subprocess
import os

input_name = ("Digite o nome do arquivo que deseja abrir: ")
# nao uso windows nem notepad
subprocess.Popen(["subl.exe", input_name])