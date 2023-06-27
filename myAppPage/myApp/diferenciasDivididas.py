import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

class diferencias_divididas:
    x = []
    fx = []
    px = None
    verificarResp = []
    cadaiteracio = []

    def insercion_datos(self, valoresx, valoresy):  
        self.x = np.array(valoresx)
        self.fx = np.array(valoresy)

    def calcular_polinomio(self):
        cantidad_x = len(self.x)

        # expresión del polinomio con Sympy
        x = sym.Symbol('x')
        polinomio = self.fx[0]
        for j in range(1, cantidad_x, 1):
            factor = self.dDividida[j - 1]
            termino = 1
            for k in range(0, j, 1):
                termino = termino * (x - self.x[k])
            polinomio = polinomio + termino * factor

        # simplifica multiplicando entre (x-xi)
        self.polisimple = polinomio.expand()
        self.px = sym.lambdify(x, self.polisimple)
        polisimplex = self.polisimple
        
        self.polisimple = self.mostrarcadena(str(polisimplex))

        return self.titulo_tabla, self.tabla, self.dDividida, polinomio, self.polisimple


    def formatear_exponente(self, exponente):
        # Verificar si el exponente es un número entero
        if exponente.is_integer():
            return str(int(exponente))
        else:
            return str(exponente)

    def mostrarcadena(self, funcion):
        # Expresión original
        expresion_original = funcion

        # Reemplazar "**" por "^" para los exponentes
        expresion_reemplazada = expresion_original.replace("**", "^").replace('*', '')

        # Formatear los exponentes utilizando la función formatear_exponente
        expresion_formateada = ""
        i = 0
        while i < len(expresion_reemplazada):
            if expresion_reemplazada[i] == "^":
                j = i + 1
                while j < len(expresion_reemplazada) and (expresion_reemplazada[j].isdigit() or expresion_reemplazada[j] == "-" or expresion_reemplazada[j] == "."):
                    j += 1
                exponente = expresion_reemplazada[i+1:j]
                exponente_formateado = self.formatear_exponente(float(exponente))
                expresion_formateada += "<sup>" + exponente_formateado + "</sup>"
                i = j
            else:
                expresion_formateada += expresion_reemplazada[i]
                i += 1
        return expresion_formateada
    
    def mostrar_resultados(self):
        self.titulo_tabla = ['i', 'x', 'fx']
        cantidad_x = len(self.x)

        item = np.arange(0, cantidad_x, 1)
        self.tabla = np.concatenate(([item], [self.x], [self.fx]), axis=0)
        self.tabla = np.transpose(self.tabla)

        # diferencias divididas vacia
        dfinita = np.zeros(shape=(cantidad_x, cantidad_x), dtype=float)
        self.tabla = np.concatenate((self.tabla, dfinita), axis=1)

        # Calcula tabla, inicia en columna 3
        [cantidad_x, m] = np.shape(self.tabla)
        diagonal = cantidad_x - 1
        diferenciaActual = 1
        j = 3
        # if mostrarpasos:
        #     print('A continuacion veras que datos son tomados para realizar cada diferencia divididas')
        while j < m:
            # Añade título para cada columna
            self.titulo_tabla.append(f'{j - 2}ᵃ D. D.')
            # cada fila de columna
            i = 0
            
            # if mostrarpasos and j < (m-1):
            #     print(f'\nDiferencias actual: {diferenciaActual}')

            paso = j - 2  # inicia en 1
            while i < diagonal:
                numerador = self.tabla[i + 1, j - 1] - self.tabla[i, j - 1]
                denominador = (self.x[i + paso] - self.x[i])
                self.tabla[i, j] = numerador / denominador
                # if mostrarpasos:
                self.cadaiteracio.append({
                    'titulo': f'{diferenciaActual}ª Diferencia Dividida',
                    'primerDato':f'Tomamos {self.tabla[i + 1, j - 1]} y le restamos {self.tabla[i, j - 1]} asi obtenemos el numerador',
                    'segundoDato': f'Tomamos {self.x[i + paso]} y le restamos {self.x[i]} asi obtenemos el denominador',
                    'resultado': f'Ahora dividimos el numerador entre el denominador osea {numerador}/{denominador} dando asi: {self.tabla[i, j]} ahora este dato lo agregamos a la tabla',
                })
                # print(f'{diferenciaActual}ª Diferencia Dividida')    
                # print(f'Tomamos {self.tabla[i + 1, j - 1]} y le restamos {self.tabla[i, j - 1]} asi obtenemos el numerador')
                # print(f'Tomamos {self.x[i + paso]} y le restamos {self.x[i]} asi obtenemos el denominador')
                # print(f'Ahora dividimos el numerador entre el denominador osea {numerador}/{denominador} dando asi:')
                # print(f'[{self.tabla[i, j]}] ahora este dato lo agregamos a la tabla')
                
                i = i + 1    
            diagonal = diagonal - 1
            j = j + 1
            diferenciaActual += 1

        self.dDividida = self.tabla[0, 3:]

        datos = self.calcular_polinomio()
        for i in range(len(self.x)):
            self.verificarResp.append(f'Evaluando la funcion obtenida en el punto {self.x[i]} da como resultado: {self.px(self.x[i])}')
        return datos
    
    def mostrar_grafica(self):
        if self.px is None:
            print('Debe calcular el polinomio antes de mostrar la gráfica.')
            return False

        # Puntos para la gráfica
        muestras = 101
        a = np.min(self.x)
        b = np.max(self.x)
        pxi = np.linspace(a, b, muestras)
        pfi = self.px(pxi)

        # Gráfica
        plt.close()
        plt.plot(self.x, self.fx, 'o', label='Puntos')
        plt.plot(pxi, pfi, label='Polinomio')
        plt.legend()
        plt.xlabel('xi')
        plt.ylabel('fi')
        plt.title('Diferencias Divididas - Newton')
        return plt