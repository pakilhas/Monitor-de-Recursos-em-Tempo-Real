import psutil 
import time 

def monitor_resources():
	while True:
		cpu_p = psutil.cpu_percent(interval=1)
		mem_p = psutil.virtual_memory().percent

		print(f"CPU USADA: {cpu_p}% | Memoria Usada: {mem_p}%")
		time.sleep(1)
if __name__ == "__main__":
	monitor_resources ()
