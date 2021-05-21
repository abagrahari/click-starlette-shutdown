import sys
import subprocess
import asyncio
import signal

loop = asyncio.get_event_loop()
loop.add_signal_handler(signal.SIGTERM, signal.SIG_IGN, signal.SIGTERM)
loop.add_signal_handler(signal.SIGINT, signal.SIG_IGN, signal.SIGINT)

uvicorn_cmd = "uvicorn server.app:app --log-level trace --lifespan on"
uvicorn_cmd = uvicorn_cmd.split()
sys.exit(subprocess.run(uvicorn_cmd, check=False).returncode)
