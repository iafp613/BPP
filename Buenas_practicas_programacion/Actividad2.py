import pytest
import pandas as pd
import FONTAL_PATAC_IGNACIO_Act1_BPP as act1

def test_comprobar_columnas():
    datos = pd.read_csv('finanzas2020[1].csv', sep='\t')
    assert act1.comprobar_columnas(datos) == 'El número de columnas es correcto.'

def test_comprobar_valores():
    datos = pd.read_csv('finanzas2020[1].csv', sep='\t')
    assert act1.comprobar_valores(datos) == 'No hay valores vacíos ni nan'

def test_analisis_datos():
    datos = pd.read_csv('finanzas2020[1].csv', sep='\t')
    assert act1.analisis_datos(datos) == 'OK'