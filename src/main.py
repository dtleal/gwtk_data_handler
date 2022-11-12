import logging
import sys

import application

logging.basicConfig(
    stream=sys.stdout,
    format="%(asctime)s %(filename)s %(funcName)s: %(message)s",
    level=logging.INFO,
)

app = application.initialize()


@app.on_event("startup")
async def startup_event() -> None:
    """FastAPI App startup hook."""
    logging.info("FastAPI startup")


@app.on_event("shutdown")
def shutdown_event() -> None:
    """FastAPI App shutdown hook."""
    logging.info("FastAPI shutdown")
