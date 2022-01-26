'''
NOMBRE: Ignacio A. Fontal Patac
ASIGNATURA: Buenas prácticas de programación
FECHA: 18/01/2022
TEMA 1: Control de errores, pruebas y validación de datos.
'''

import pandas as pd
import matplotlib.pyplot as plt

def abrir_fichero():
    '''Función que abre un fichero .csv

    Parámetros:
    -----------
    Ninguno

    Devuelve:
    --------
    pandas dataframe
    
    ''' 
    try: 
        df = pd.read_csv('finanzas2020[1].csv', sep='\t')
        print('Fichero abierto correctamente')
        return df
    except FileNotFoundError:
        print('No se ha encontrado el fichero')

def comprobar_columnas(datos):
    '''Función que comprueba que el número de columnas del fichero es igual a 12.
    
    Parámetros:
    -----------
    pandas dataframe

    Devuelve:
    --------
    print(si es correcto o no)
    '''

    try:
        if len(datos.columns) == 12:
            return 'El número de columnas es correcto.'
        else:
            return 'El número de columnas no es correcto.'
    except:
        return 'Algo ha ido mal'

def comprobar_valores(datos):
    '''Función que comprueba que no hay números nan o valores vacíos.
    
    Parámetros:
    -----------
    pandas dataframe

    Devuelve:
    --------
    print(si hay valores NaN o vacíos o no.)
    '''

    try:
        if datos.isnull().values.any():
            print('Hay nan')
        else:
            print('No hay nan')
        if datos.isna().values.any():
            print('Hay valores vacíos')
        else:
            print('No hay valores vacíos')
            return 'No hay valores vacíos ni nan'
    except:
        print('Algo ha ido mal')

def comprobar_datos(datos):
    '''Función que comprueba que todos los datos son números enteros o flotantes y si no es así, los transforma.
        Además Crea un nuevo dataframe con los totales de cada mes.

    Parámetros:
    -----------
    pandas dataframe

    Devuelve:
    --------
    print(Si todos los valores son numéricos o no)
    pandas dataframe con los totales de cada mes.
    '''

    try:
        if datos.dtypes.any() == 'int64' or datos.dtypes.any() == 'float64':
            print('Los datos son correctos. Todos los datos son números enteros o flotantes.')
        else:
            print('Hay valores no numéricos')
            totales = []
            for col in finanzas.columns:
                finanzas[col] = finanzas[col].replace("'", "") # Elimina comillas simples
                finanzas[col] = pd.to_numeric(finanzas[col], errors='coerce') # Convierte a número las columnas object
                finanzas[col] = finanzas[col].fillna(axis=0, method='ffill') # Rellena los NaN con el valor anterior
                totales.append(finanzas[col].sum()) # Suma los valores de cada columna
            print('Los datos no eran correctos y han sido corregidos')
            try:
                finanzasNew = pd.DataFrame(totales, columns=['Total'], index=[
                                                            'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 
                                                            'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
                                                            ])
                return finanzasNew
            except:
                print('No se ha podido crear el fichero')
    except:
        print('Algo ha ido mal')

def analisis_datos(datos):
    '''Función que proporciona información del archivo original y sus valores estadísticos.

    Parámetros:
    -----------
    pandas dataframe

    Devuelve:
    --------
    print(información del archivo original y sus valores estadísticos)
    '''
    try:
        print('Información del archivo:')
        print(datos.info())
        print('------------------------------------------------------------------------------------------------------------------')
        print('\nValores estadísticos del archivo:')
        print(datos.describe())
        print('------------------------------------------------------------------------------------------------------------------')
        return 'OK'
    except:
        print('Algo ha ido mal: No se ha podido mostrar la información')


def gasto(datos):
    '''Función que devuelve el mes que se ha gastado más.
    
    Parámetros:
    -----------
    pandas dataframe

    Devuelve:
    --------
    Mes que se ha gastado más
    '''

    return datos.idxmin()

def ahorro(datos):
    '''Función que devuelve el mes que se ha ahorrado más.
    
    Parámetros:
    -----------
    pandas dataframe

    Devuelve:
    --------
    Mes que se ha ahorrado más
    '''

    return datos.idxmax()

def media(datos):
    '''Función que devuelve la media de gastos.
    
    Parámetros:
    -----------
    pandas dataframe

    Devuelve:
    --------
    Media de gastos
    '''

    return datos.mean()

def gastototal(datos):
    '''Función que devuelve el gasto total.
    
    Parámetros:
    -----------
    pandas dataframe

    Devuelve:
    --------
    Gasto total anual
    '''

    gastos = []
    gastosTotales = 0
    for i in datos.Total:
        if i < 0:
            gastos.append(i)
    for i in gastos:
        gastosTotales += i

    return gastosTotales

def ingresototal(datos):
    '''Función que devuelve el ingreso total.
    
    Parámetros:
    -----------
    pandas dataframe

    Devuelve:
    --------
    Ingreso total anual
    '''

    ingresos = []
    ingresosTotales = 0
    for i in datos.Total:
        if i > 0:
            ingresos.append(i)
    for i in ingresos:
        ingresosTotales += i

    return ingresosTotales

def lineplot(datos):
    '''Función que crea y guarda una gráfica con los gastos y los ingresos por meses
    
    Parámetros:
    -----------
    pandas dataframe

    Devuelve:
    --------
    Gráfica con los gastos y los ingresos por meses en .jpg
    '''

    mes = finanzas.columns

    fig = plt.figure()
    rect = (0,0, 2, 1)
    axes = fig.add_axes(rect)
    plt.title('Ingresos/Gastos')
    plt.plot(mes, datos.Total)
    axes.set_ylim(-20000, 20000)
    plt.ylabel('Ingresos / Gastos')
    plt.xlabel('Mes')
    plt.legend()
    plt.grid(True)
    plt.savefig('Grafico.jpg', bbox_inches='tight')

    
finanzas = abrir_fichero()
print('\n------------------------------------------------------------------------------------------------------------------')
comprobar_columnas(finanzas)
print('\n------------------------------------------DATOS ANTES DE LIMPIAR--------------------------------------------------')
analisis_datos(finanzas)
print('\n--------------------------------------------LIMPIEZA DE DATOS-----------------------------------------------------')
comprobar_valores(finanzas)
print('\n------------------------------------------------------------------------------------------------------------------')
finanzasNew = comprobar_datos(finanzas)
print('\n-----------------------------------------DATOS DESPUÉS DE LIMPIAR-------------------------------------------------')
analisis_datos(finanzas)
print('\n------------------------------------------------------------------------------------------------------------------')

print('Se ha gastado más en: ' + gasto(finanzasNew))
print('\n------------------------------------------------------------------------------------------------------------------')
print('Se ha ahorrado más en: ' + ahorro(finanzasNew))
print('\n------------------------------------------------------------------------------------------------------------------')
print('La media de gastos anual es: ' + str(media(finanzasNew)))
print('\n------------------------------------------------------------------------------------------------------------------')
print('El gasto total es: ' + str(gastototal(finanzasNew)))
print('\n------------------------------------------------------------------------------------------------------------------')
print('El ingreso total es: ' + str(ingresototal(finanzasNew)))
print('\n------------------------------------------------------------------------------------------------------------------')
lineplot(finanzasNew)

