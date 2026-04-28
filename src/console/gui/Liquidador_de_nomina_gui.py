import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner  
from kivy.uix.popup import Popup

from Logica.logica_liq_nom import Nomina, NominaCalculator

class NominaApp(App):
    def build(self):
        self.title = "Calculadora de Liquidación de Nómina"
        self.contenedor = GridLayout(
            cols=2, 
            padding=[20, 10, 20, 10], 
            spacing=12, 
            size_hint=(1, 1)
        )

        self.add_field("Salario Base ($):", "salario_base", "0")
        self.add_field("Días Trabajados:", "dias_trabajados", "0")
        self.add_field("Días Incapacidad:", "dias_incapacidad", "0")
        self.add_field("Horas Extra (Cant):", "horas_extra", "0")
        
        self.contenedor.add_widget(Label(text="Tipo Extra (D/N):", font_size=18))
        self.tipo_extra_spinner = Spinner(
            text='D',  
            values=('D', 'N'),
            font_size=18,
            background_color=(0.3, 0.3, 0.3, 1)
        )
        self.contenedor.add_widget(self.tipo_extra_spinner)
        
        self.add_field("Auxilio Transp. ($):", "auxilio", "0")
        self.add_field("Bonificaciones ($):", "bonificaciones", "0")
        self.add_field("Deducciones ($):", "deducciones_adicionales", "0")

        self.contenedor.add_widget(Label(text="NETO A PAGAR:", font_size=20, bold=True))
        self.resultado_label = Label(text="$ 0.00", font_size=22, bold=True, color=(1,1, 1, 1))
        self.contenedor.add_widget(self.resultado_label)

        btn_calcular = Button(
            text="CALCULAR NÓMINA", 
            font_size=22, 
            bold=True,
            background_color=(0.2, 0.5, 0.9, 1)
        )
        btn_calcular.bind(on_press=self.calcular)
        self.contenedor.add_widget(btn_calcular)

        return self.contenedor

    def add_field(self, label_text, attr_name, default):
        lbl = Label(text=label_text, font_size=18)
        self.contenedor.add_widget(lbl)
        txt_input = TextInput(text=default, multiline=False, font_size=18, padding_y=(10, 10), write_tab=False)
        setattr(self, attr_name, txt_input)
        self.contenedor.add_widget(txt_input)

    def calcular(self, instance):
        try:
            datos_nomina = Nomina(
                salario_base=float(self.salario_base.text),
                dias_trabajados=int(self.dias_trabajados.text),
                dias_incapacidad=int(self.dias_incapacidad.text),
                horas_extra=float(self.horas_extra.text),
                tipo_extra=self.tipo_extra_spinner.text,
                auxilio=float(self.auxilio.text),
                bonificaciones=float(self.bonificaciones.text),
                deducciones_adicionales=float(self.deducciones_adicionales.text)
                )

            result = NominaCalculator.calcular_nomina(datos_nomina)
            self.resultado_label.text = f"$ {result.neto:,.2f}"

        except ValueError as e:
            self.mostrar_error("Error: No se puede calcular la liquidacion. \nAsegurece de ingresar valores numéricos válidos" + "\n" + str(e))
        
        except Exception as e:
            self.mostrar_error("Error: No se pudo calcular la liquidacion. \n" + str(e)) 

    def mostrar_error(self, err):
        contenido = GridLayout(cols=1,)
        contenido.add_widget(Label(text=str(err), font_size=18))
        cerrar= Button(text="Cerrar", size_hint=(1, 0.3), font_size=18)
        contenido.add_widget(cerrar)
        popup = Popup(title="Error", content=contenido, size_hint=(0.8, 0.4))
        cerrar.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == "__main__":
    NominaApp().run()