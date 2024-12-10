from rich import print
from rich.panel import Panel
from rich.box import DOUBLE, SIMPLE, ROUNDED, SQUARE

# Створимо панель з різними стилями обрамлення
panel_content = "Це вміст панелі"

# Панель з подвійним обрамленням
panel_double = Panel(panel_content, title="Подвійне обрамлення", box=DOUBLE)

# Панель з простим обрамленням
panel_simple = Panel(panel_content, title="Просте обрамлення", box=SIMPLE)

# Панель із закругленим обрамленням
panel_rounded = Panel(panel_content, title="Закруглене обрамлення", box=ROUNDED)

# Панель з квадратним обрамленням
panel_square = Panel(panel_content, title="Квадратне обрамлення", box=SQUARE)

# Виводимо панелі
print(panel_double)
print(panel_simple)
print(panel_rounded)
print(panel_square)
