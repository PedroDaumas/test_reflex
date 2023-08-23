"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import json
import reflex as rx

from app.views.home.main import HomePage
from app.views.home.state import HomeState
from app.views.utils.main_state import MainState


async def healthcheck():
    """Check if the endpoint is on. Used by container orchestration system."""

    version_info = None

    with open("./version.json", encoding="utf-8") as json_file:
        version_info = json.load(json_file)

    return {"status": "pass", **version_info}


# Add state and page to the app.
app = rx.App(state=MainState)

##################################################################################################
# API Routes
##################################################################################################

app.api.add_api_route("/", healthcheck)
app.api.add_api_route("/healthcheck", healthcheck)
app.api.add_api_route("/health_check", healthcheck)


##################################################################################################
# UI Routes
##################################################################################################

app.add_page(
    HomePage().build,
    route="/",
    on_load=HomeState.update_users,
    title="APP",
)

app.compile()
