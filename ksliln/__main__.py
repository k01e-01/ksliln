import sys

import click

from textual.app import App
from textual.widgets import Header, Footer, Placeholder
from textual.containers import Horizontal, Container
from textual.binding import Binding

from .debug.inspector import Inspector


class ILNApp(App[None]):
    BINDINGS = [
        Binding("q", "quit", "Quit"),
    ]

    TITLE = "ksliln"

    def compose(self) -> None:
        yield Horizontal(
            Container(
                Header(),
                Placeholder(label="Hello, world!"),
                Footer(),
            ),
            # Inspector(),
        )


@click.command()
@click.argument("name", default="world")
def cli(name) -> None:
    click.echo(f"Hello {name}!")


def main() -> None:
    if len(sys.argv) > 1:
        cli()
    else:
        ILNApp().run()


if __name__ == "__main__":
    main()
