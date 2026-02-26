import os
import sys
import time
import subprocess

def run_unified_server():
    print("\n[DEPLOYMENT MODE] Starting Daphne ASGI Server on Port 8000...")
    print("This server handles BOTH HTTP and WebSockets on the same port.")
    # Command: python -m daphne -p 8000 core.asgi:application
    return subprocess.Popen([sys.executable, "-m", "daphne", "-p", "8000", "core.asgi:application"])

if __name__ == "__main__":
    print("Django Unified Chat Service (WhatsApp Style)")
    print("--------------------------------------------")
    
    try:
        p = run_unified_server()
        
        print("\n🚀 App is running at: http://127.0.0.1:8000/")
        print("Press Ctrl+C to stop.")
        
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping services...")
        p.terminate()
        sys.exit(0)
