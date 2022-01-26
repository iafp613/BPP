'''
ASIGNATURA: Programación de Aplicaciones con Python
ALUMNO: Ignacio A. Fontal Patac
FECHA: 01/01/2022
ACTIVIDAD: Tema 12 - Dash
'''

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

data = px.data.iris()
figura = px.scatter(data, x="sepal_width", y="sepal_length", color="species")

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children='Gráfica de iris para el sépalo'),
    dcc.Graph(figure=figura)])


if __name__ == '__main__':
    app.run_server(debug=True)