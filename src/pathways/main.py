from pathways.settings import Settings
import uvicorn
from fastapi import FastAPI

from pathways.graphdb import prepare_seed_database
from pathways.routes.interaction import router as interaction_router
from pathways.utils.logging import configure_logging

settings = Settings()
app = FastAPI()

app.include_router(interaction_router, prefix="/interactions")


def main():
    configure_logging(settings.log_level)

    if settings.seed_data:
        prepare_seed_database()

    uvicorn.run(
        "pathways.main:app",
        host=settings.host_address,
        port=settings.port,
        log_level=settings.log_level.lower(),
    )

if __name__ == "__main__":
    main()
