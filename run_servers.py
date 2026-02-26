import os
import sys
import time
import subprocess

def run_asgi():
    print("\n[ASGI] Starting Uvicorn (Asynchronous) on Port 8002...")
    # Using python -m uvicorn to ensure it uses the correct environment
    return subprocess.Popen([sys.executable, "-m", "uvicorn", "core.asgi:application", "--host", "127.0.0.1", "--port", "8002"])

def run_dev_server():
    print("\n[DEV] Starting Django Dev Server on Port 8001...")
    return subprocess.Popen([sys.executable, "manage.py", "runserver", "127.0.0.1:8001", "--noreload"])

if __name__ == "__main__":
    print("Django WSGI vs ASGI Deployment Service")
    print("---------------------------------------")
    
    processes = []
    try:
        # On Windows, Gunicorn isn't available, so we use runserver for the 'sync' side demonstration
        p1 = run_dev_server()
        p2 = run_asgi()
        processes.extend([p1, p2])
        
        print("\nServices are booting up...")
        time.sleep(3)
        
        print("\nReady:")
        print("-> Sync Side (Dev Server): http://127.0.0.1:8001/sync/")
        print("-> Async Side (Uvicorn):    http://127.0.0.1:8002/async/")
        print("-> WebSocket Endpoint:      ws://127.0.0.1:8002/ws/chat/")
        print("\nPress Ctrl+C to stop.")
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping services...")
        for p in processes:
            p.terminate()
        sys.exit(0)
