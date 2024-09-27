import psutil
import logging
import time

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # CPU usage percentage
MEMORY_THRESHOLD = 80  # Memory usage percentage
DISK_THRESHOLD = 90  # Disk usage percentage

def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')

    # Check memory usage
    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory_info.percent}%')

    # Check disk usage
    disk_info = psutil.disk_usage('/')
    if disk_info.percent > DISK_THRESHOLD:
        logging.warning(f'High disk usage detected: {disk_info.percent}%')

    # List running processes
    running_processes = [p.info for p in psutil.process_iter(['pid', 'name'])]

    return {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_info.percent,
        'disk_usage': disk_info.percent,
        'running_processes': running_processes
    }

if __name__ == "__main__":
    while True:
        health = check_system_health()
        print(f"CPU: {health['cpu_usage']}%, Memory: {health['memory_usage']}%, Disk: {health['disk_usage']}%")
        time.sleep(60)  # Check every minute
