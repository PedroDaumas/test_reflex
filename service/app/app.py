"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
import json
import io
import pandas as pd
import reflex as rx

from datetime import datetime
from starlette.responses import StreamingResponse

from app.views.home.main import HomePage
from app.views.home.state import HomeState
from app.views.utils.main_state import MainState


async def healthcheck():
    """Check if the endpoint is on. Used by container orchestration system."""

    version_info = None

    with open("./version.json", encoding="utf-8") as json_file:
        version_info = json.load(json_file)

    return {"status": "pass", **version_info}

async def export():
    """
    Exports a user`s CSV
    """

    export_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    data = {'col_1': [3, 2, 1, 0], 'col_2': ['a', 'b', 'c', 'd']}
    dataframe = pd.DataFrame(data=data)

    stream = io.StringIO()
    dataframe.to_csv(stream, index=False)

    response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
    response.headers["Content-Disposition"] = f"attachment; filename=Export_{export_time}.csv"

    return response

# Add state and page to the app.
app = rx.App(state=MainState)

##################################################################################################
# API Routes
##################################################################################################

app.api.add_api_route("/", healthcheck)
app.api.add_api_route("/healthcheck", healthcheck)
app.api.add_api_route("/health_check", healthcheck)
app.api.add_api_route("/export", export)

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
