import sys
import httpx
import json
import click

from textual.app import App, ComposeResult
from textual.widgets import (
    Placeholder,
    Header,
    Footer,
    DataTable,
    LoadingIndicator,
    Label,
)
from textual.containers import Container, ScrollableContainer
from textual.binding import Binding

from .debug.inspector import Inspector
from .jasima import gen_table


LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


class Sidebar(Container):
    def compose(self) -> ComposeResult:
        yield Placeholder("Sidebar")


class Main(ScrollableContainer):
    def compose(self) -> ComposeResult:
        yield Label(
            LOREM_IPSUM,
            id="test",
        )
        yield DataTable()
    
    def reload_data(self) -> None:
        self.query_one(DataTable).remove()
        self.mount(gen_table(self.app.jasima_linku, None))


class ksliln(App[None]):
    BINDINGS = [
        Binding("q", "quit", "o weka"),
        Binding("s", "toggle_sidebar", "ilo Sidebar"),
    ]

    TITLE = "ksliln"
    CSS_PATH = "styles.css"

    jasima_linku = None

    def compose(self) -> ComposeResult:
        yield Sidebar(classes="hidden")
        yield Header()
        yield Footer()

        # yield Inspector()

        yield Container(
            LoadingIndicator(id="loading"),
            Main(),
        )

    async def on_mount(self) -> None:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://linku.la/jasima/data.json")
            self.jasima_linku = json.loads(response.text)

            self.query_one("#loading").remove()
            self.query_one("Main").reload_data()

    def action_toggle_sidebar(self) -> None:
        self.query_one("Sidebar").toggle_class("hidden")


@click.command()
@click.argument("name", default="world")
def cli(name) -> None:
    click.echo(f"Hello {name}!")


def main() -> None:
    if len(sys.argv) > 1:
        cli()
    else:
        ksliln().run()


if __name__ == "__main__":
    main()
