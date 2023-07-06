from textual.widgets import DataTable


def onerrmt(dict: dict, key: str) -> str:
    try:
        return dict[key]
    except KeyError:
        return ""


def gen_table(data: dict, config: None) -> DataTable:
    d = DataTable()
    d.add_columns("nimi", "lipu", "tenpo", "jan")

    for nimi in data["data"].values():
        word = nimi["word"]
        d.add_row(
            onerrmt(nimi, "word"),
            onerrmt(nimi, "book"),
            onerrmt(nimi, "coined_era"),
            onerrmt(nimi, "creator"),
        )

    return d
