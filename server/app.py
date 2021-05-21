from starlette.applications import Starlette
import asyncio
import sys
import subprocess


async def shutdown():
    print("sleeping for 5 seconds")
    await asyncio.sleep(5)
    print("Continuing to cancel")


app = Starlette(on_shutdown=[shutdown])

if __name__ == "__main__":
    uvicorn_cmd = "uvicorn server.app:app --log-level trace --lifespan on"
    uvicorn_cmd = uvicorn_cmd.split()
    sys.exit(subprocess.run(uvicorn_cmd, check=False).returncode)
