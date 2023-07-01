from textual.app import App
from textual.widgets import Header, Footer, Placeholder
from textual.containers import Horizontal, Container
from textual.binding import Binding

from .debug.inspector import Inspector


class ILNApp(App[None]):
    BINDINGS = [
        Binding("q", "quit", "Quit"),
    ]

    TITLE = "ilo lawa nimi"

    def compose(self) -> None:
        yield Horizontal(
            Container(
                Header(),
                Placeholder(label="Hello, world!"),
                Footer(),
            ),
            # Inspector(),
        )


def main() -> None:
    ILNApp().run()


if __name__ == "__main__":
    main()