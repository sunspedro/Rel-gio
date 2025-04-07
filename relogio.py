import flet as ft 
from datetime import datetime
import asyncio
import time

def main(page:ft.Page):
    page.window.width = 800
    page.window.max_width = 800
    page.window.min_width = 800
    page.window.height = 500
    page.window.max_height = 500
    page.window.min_height = 500
    page.window.top = 100
    page.window.left = 250
    page.window.title_bar_hidden = True
    page.padding = 0
    
    def hover_close(e):
        close.content.opacity = 1 if e.data == "true" else 0
        close.content.update()

    dias = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']
    mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    data_atual = datetime.today().weekday()

    data_formatada = f'{dias[data_atual].capitalize()}, {datetime.now().strftime("%d")} de {mes[int(datetime.now().strftime("%m")) - 1]}'

    data_texto = ft.Text(
        size=25,
        weight='w500',
        value=data_formatada
    )

    hora_atual = datetime.now().strftime('%H:%M:%S')
    hora_texto = ft.Text(
        value=hora_atual,
        size=32,
        color='white',
        weight='w900'
    )

    async def atualizar_data_hora():
        while True:
            hora_texto.value = datetime.now().strftime('%H:%M:%S')
            data_formatada = f'{dias[data_atual].capitalize()}, {datetime.now().strftime("%d")} de {mes[int(datetime.now().strftime("%m")) - 1]}'
            data_texto.value = data_formatada
            page.update()
            await asyncio.sleep(1)

    stack_main = ft.Stack(
        expand=True,
        controls=[
            ft.Container(
                content=ft.Image(
                    src='C:\\Users\\pedro.borges\\Desktop\\Aplicativos uteís\\Python\\testes\\user.png',
                    width=800,
                    height=500,
                    fit=ft.ImageFit.COVER,
                    opacity=.4
                )
            ),
            ft.Container(
                content=hora_texto,
                margin=ft.margin.only(
                    left=340,
                    top=180  
                )
            ),
            ft.Container(
                content=data_texto,
                margin=ft.margin.only(
                    left=290,
                    top=230  
                )
            ),
            ft.Container(
                expand=True,
                padding=ft.padding.only(top=380, left=100),  
                content=ft.Container(
                    width=600,
                    height=60,
                    border=ft.border.all(width=2, color='white'),
                    border_radius=16,
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.ACCESS_TIME,
                                scale=1.4,
                                icon_color='white'
                            ),
                            ft.IconButton(
                                icon=ft.icons.ALARM,
                                scale=1.4,
                                icon_color='white'
                            ),
                            ft.IconButton(
                                icon=ft.icons.CALENDAR_MONTH,
                                scale=1.4,
                                icon_color='white'
                            ),
                        ]
                    )
                ),
            ),
            ft.WindowDragArea(width=800, height=400, content=ft.Container(bgcolor='transparent')),
            close := ft.Container(
                margin=ft.margin.only(left=760, top=10),  
                content=ft.Icon(
                    ft.icons.CLOSE,
                    color='white',
                    opacity=0,
                    animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE_IN_OUT)
                ),
                ink=True,
                on_hover=hover_close,
                on_click=lambda _: page.window.close()
            ),
        ]
    )

    page.add(stack_main)
    page.run_task(atualizar_data_hora)

ft.app(target=main)
