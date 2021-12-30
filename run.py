from rich import print
from rich.layout import Layout

layout = Layout()
print(layout)

layout.split_column(
    Layout(name="upper"),
    Layout(name="lower")
)
print(layout)