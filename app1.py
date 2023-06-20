from textual.app import App
from textual.containers import Horizontal
from textual.widgets import Label, Header, Footer, Input, Button

class MyApp(App):
    TITLE = 'Meu App'

    BINDINGS = [
        ('t', 'change_theme()', 'Mudar o tema!')
    ]

    def action_change_theme(self):
        self.dark = not self.dark 

    def compose(self):
        self.lbltitulo = Label('Boas vindas')
        self.edttexto = Input('Digite um texto')
        self.btnverde = Button('Verde', variant='success')
        self.btnamarelo = Button('Amarelo', variant='warning')
        self.btnvermelho = Button('Vermelho', variant='error')

        yield Header(show_clock=True)

        yield self.lbltitulo
        yield self.edttexto

        with Horizontal():
            yield self.btnverde
            yield self.btnamarelo
            yield self.btnvermelho

        yield Footer()

        # on_btnverde_pressed(self, event: Button.Pressed):
            # self.lbltitulo.update(f'Texto: {event.button.label}')

MyApp().run()

