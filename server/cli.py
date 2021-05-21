import click
import asyncio
import signal
import sys
import subprocess


@click.group()
def cli() -> None:
    """CLI for cloud-kws-server."""
    pass


@cli.command()
def serve():
    # --------------- NEEDED SECTION -------------
    # loop = asyncio.get_event_loop()
    # loop.add_signal_handler(signal.SIGTERM, signal.SIG_IGN, signal.SIGTERM)
    # loop.add_signal_handler(signal.SIGINT, signal.SIG_IGN, signal.SIGINT)
    # --------------- NEEDED SECTION -------------

    uvicorn_cmd = "uvicorn server.app:app --log-level trace --lifespan on"
    uvicorn_cmd = uvicorn_cmd.split()
    sys.exit(subprocess.run(uvicorn_cmd, check=False).returncode)


@cli.command()
def servewrapper():
    # https://click.palletsprojects.com/en/8.0.x/exceptions/#what-if-i-don-t-want-that
    # This didn't work
    serve.main([], standalone_mode=False)


if __name__ == "__main__":
    # This works, but it doesn't solve our issue!
    try:
        serve.main([], standalone_mode=False)
    except click.Abort:
        pass
