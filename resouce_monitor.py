import psutil 
import time 

def monitor_resources():
	while True:
		cpu_percent = psutil.cpu_percent(interval=1)
		mem_percent = psutil.virtual_memory().percent

		print(f"CPU USADA: {cpu_percent}% | Memoria Usada: {mem_percent}%")
		time.sleep(1)
if __name__ == "__main__":
	monitor_resources ()
