import flet as ft
from flet import colors
from decimal import Decimal as dc

botoes = [
        {'operador': 'AC', 'fonte': colors.WHITE, 'fundo': '#323232'},
        {'operador': '±', 'fonte': colors.WHITE, 'fundo': '#323232'},
        {'operador': '%', 'fonte': colors.WHITE, 'fundo': '#323232'},
        {'operador': '/', 'fonte': colors.WHITE, 'fundo': '#323232'},
        {'operador': '7', 'fonte': colors.WHITE, 'fundo': '#3b3b3b'},
        {'operador': '8', 'fonte': colors.WHITE, 'fundo': '#3b3b3b'},
        {'operador': '9', 'fonte': colors.WHITE, 'fundo': '#3b3b3b'},
        {'operador': '*', 'fonte': colors.WHITE, 'fundo': '#323232'},
        {'operador': '4', 'fonte': colors.WHITE, 'fundo': '#3b3b3b'},
        {'operador': '5', 'fonte': colors.WHITE, 'fundo': '#3b3b3b'},
        {'operador': '6', 'fonte': colors.WHITE, 'fundo': '#3b3b3b'},
        {'operador': '-', 'fonte': colors.WHITE, 'fundo': '#323232'},
        {'operador': '1', 'fonte': colors.WHITE, 'fundo': '#3b3b3b'},
        {'operador': '2', 'fonte': colors.WHITE, 'fundo': '#3b3b3b'},
        {'operador': '3', 'fonte': colors.WHITE, 'fundo': '#3b3b3b'},
        {'operador': '+', 'fonte': colors.WHITE, 'fundo': '#323232'},
        {'operador': '0', 'fonte': colors.WHITE, 'fundo': '#3b3b3b'},
        {'operador': '.', 'fonte': colors.WHITE, 'fundo': '#3b3b3b'},
        {'operador': '=', 'fonte': '#3b3b3b', 'fundo': '#4cc2ff'}
    ]

def main(page: ft.Page):
    # Window configs
    page.window_resizable=False
    page.window_maximizable=False
    page.window_width=345
    page.window_height=450
    page.window_always_on_top=True

    # Page configs
    page.title='Calculator'
    page.bgcolor='#202020'

    # Theme configs
    page.fonts={
        "JetBrains": "fonts/jetbrains.TTF"
    }
    page.theme = ft.Theme(font_family='JetBrains')
    
    result = ft.Text(value='0', color=colors.WHITE, size=48)

    def calculate(op, valueAt):
        try:
            value = eval(valueAt)

            if op == '%':
                value = value/100
            elif op == '±':
                value = value*(-1)
        except:
            return 'Error!'
        
        digits = min(abs(dc(value).as_tuple().exponent), 5)
        return format(value, f'.{digits}f')

    def select(e):
        valueAt = result.value if result.value not in ('0','Error!') else ''
        value = e.control.content.value

        if value.isdigit():
            value = valueAt + value
        elif value == 'AC':
            value = '0'
        else:
            if valueAt and valueAt[-1] in ('/','*','+','-','.'):
                valueAt = valueAt[:-1]

            value = valueAt + value

            if value[-1] in ('=','%','±'):
                value = calculate(op=value[-1],valueAt=valueAt)

        result.value = value
        result.update()

    screen = ft.Row(
        width=300,
        height=120,
        controls=[result],
        alignment='end'
    )

    btn = [ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte'], size=16),
        width=75,
        height=50,
        border_radius=7,
        bgcolor=btn['fundo'],
        alignment=ft.alignment.center,
        on_click=select
    ) for btn in botoes]

    keyboard = ft.Row(
        spacing=2,
        run_spacing=2,
        width=345,
        wrap=True,
        controls=btn,
        alignment='end'
    )

    page.add(screen, keyboard)

ft.app(target=main)