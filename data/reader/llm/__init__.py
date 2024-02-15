import structlog
from modal import Image, NetworkFileSystem, Stub

APP_NAME = "readwise-llm"

log = structlog.get_logger()

image = Image.debian_slim().pip_install(["structlog"])

stub = Stub(APP_NAME)
