import os
import sys
import time
import subprocess

def run_wsgi():
    print("\n[WSGI] Starting Gunicorn (Synchronous)...")
    # Command: gunicorn core.wsgi:application --bind 0.0.0.0:8001
    subprocess.Popen(["gunicorn", "core.wsgi:application", "--bind", "127.0.0.1:8001"])

def run_asgi():
    print("\n[ASGI] Starting Uvicorn (Asynchronous)...")
    # Command: uvicorn core.asgi:application --host 127.0.0.1 --port 8002
    subprocess.Popen(["uvicorn", "core.asgi:application", "--host", "127.0.0.1", "--port", "8002"])

if __name__ == "__main__":
    print("Django WSGI vs ASGI Deployment Service")
    print("---------------------------------------")
    
    try:
        run_wsgi()
        run_asgi()
        
        print("\nServices are running:")
        print("-> WSGI App: http://127.0.0.1:8001/sync/")
        print("-> ASGI App: http://127.0.0.1:8002/async/")
        print("-> WebSocket: ws://127.0.0.1:8002/ws/chat/")
        print("\nPress Ctrl+C to stop both services.")
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutting down services...")
        sys.exit(0)
