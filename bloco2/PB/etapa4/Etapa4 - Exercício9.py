import subprocess, psutil, time
# Apenas cria um processo (calculadora) para testar
pid = subprocess.Popen("bc").pid
p = psutil.Process(pid)
print("Nome:", p.name())
print("Executável:", p.exe())
print("Tempo de criação:", time.ctime(p.create_time()))
print("Tempo de usuário:", p.cpu_times().user, "s")
print("Tempo dte sistema:", p.cpu_times().system, "s")
print("Percentual de uso de CPU:", p.cpu_percent(interval=1.0), "%")
perc_mem = '{:.2f}'.format(p.memory_percent())
print("Percentual de uso de memória:", perc_mem, "%")
# RSS: Resident set size e VMS: Virtual Memory Size
mem = '{:.2f}'.format(p.memory_info().rss/1024/1024)
print("Uso de memória:", mem, "MB")
print("Número de threads:", p.num_threads())