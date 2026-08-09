# Informe: Comparación de rendimiento entre lenguajes compilados (C) e interpretados (Python)

## 1. Introducción y objetivos
El propósito de este experimento es analizar cuantitativa y cualitativamente las diferencias de rendimiento en tiempo de ejecución entre un lenguaje compilado (**C**) y un lenguaje interpretado (**Python**).

Para lograr una comparación objetiva, se implementó exactamente el mismo algoritmo numérico en ambos lenguajes: la **multiplicación directa de matrices cuadradas** ($N \times N$) utilizando bucles anidados directos ($O(N^3)$).

## 2. Fundamento teorico

### Lenguaje compilado (C)
C es un lenguaje que pasa por un proceso previo de compilación. El compilador (`gcc`) traduce el código fuente completo en un único paso directamente a **código máquina** (instrucciones binarias nativas del procesador local). 
* **Ventaja clave**: Al momento de la ejecución, el procesador ejecuta directamente las instrucciones de bajo nivel sin intermediarios ni decisiones sobre el tipo de datos.
* **Optimizaciones del compilador**: Las opciones de compilación como `-O3` reorganizan las instrucciones binarias, aprovechan los registros del procesador y desenrollan bucles para minimizar accesos a memoria.

### Lenguaje interpretado (Python)
Python no produce un archivo binario nativo ejecutable directo. En su lugar, el intérprete lee el código, lo convierte en un formato intermedio llamado *bytecode* y ejecuta este *bytecode* paso a paso mediante una máquina virtual.
* **Sobrecarga de interpretación**: En cada iteración de un bucle, el intérprete debe verificar dinámicamente los tipos de datos de las variables, gestionar referencias de objetos en memoria y el despacho de funciones.
* **Costo en bucles anidados**: En un algoritmo de complejidad $O(N^3)$, la sobrecarga de comprobación del intérprete se multiplica por millones de iteraciones, ralentizando la ejecución considerablemente en comparación con el código nativo.

## 3. Metodología
1. **Algoritmo**: Multiplicación de matrices $C_{i,j} = \sum_{k=0}^{N-1} A_{i,k} \times B_{k,j}$.
2. **Entornos probados**:
   - **Python 3.14**: Implementación nativa en Python usando bucles `for` nativos.
   - **C (GCC 14.2) -O0**: Compilación básica sin optimizaciones del compilador.
   - **C (GCC 14.2) -O3**: Compilación con optimizaciones de alto nivel activadas.
3. **Herramientas de Medición de Tiempo**:
   - En Python se utilizó la función `time.perf_counter()` del módulo nativo `time`.
   - En C se utilizó la función `clock()` de la librería nativa `<time.h>`.
4. **Procedimiento**: Se ejecutó cada tamaño de matriz $N \in \{50, 100, 150, 200, 250, 300, 350, 400\}$ un total de 3 veces y se calculó el promedio para reducir el impacto de ruido en el sistema operativo.

## 4. Resultados experimentales

A continuación se presentan los tiempos promedio obtenidos expresados en segundos:

| Tamaño Matriz ($N \times N$) | Python (s) | C (-O0) (s) | C (-O3) (s)
| :---: | :---: | :---: | :---: |
| 50x50 | 0.005701 | 0.000000 | 0.000000 |
| 100x100 | 0.047446 | 0.003000 | 0.000000 |
| 150x150 | 0.144890 | 0.008000 | 0.001000 |
| 200x200 | 0.336478 | 0.019000 | 0.004000 |
| 250x250 | 0.657364 | 0.037667 | 0.008000 |
| 300x300 | 1.188186 | 0.070333 | 0.015000 |
| 350x350 | 1.841862 | 0.105000 | 0.024333 |
| 400x400 | 2.856981 | 0.162000 | 0.036667 |

## 5. Gráfico de rendimiento

Al correr **benchmark.py**, se nos genera un archivo llamado **benchmark_results.png**, el cual contiene el grafico de rendimiento de ambos lenguajes. Al analizarlo podemos ver:
1. **Comportamiento curva**: La curva de Python crece de forma vertiginosa a medida que $N$ aumenta hacia 400. Mientras que Python requiere varios segundos para procesar una matriz de $400 \times 400$, C realiza el mismo procedimiento en una fracción de segundo.
2. **Escala logarítmica**: La gráfica muestra una separación constante entre la línea de Python y las líneas de C. Esta brecha vertical representa un factor de diferencia de orden de magnitud (C es aproximadamente entre 30 y 100 veces más rápido en este tipo de cálculo intensivo en bucles).
3. **Efecto de la optimización (`-O3`)**: La comparación entre C sin optimizar (`-O0`) y C optimizado (`-O3`) demuestra que el compilador logra reducir aún más el tiempo mediante vectorización e instrucciones especializadas de la CPU.

## 6. Conclusiones
* **Eficiencia de Ejecución**: C es sustancialmente más rápido que Python para algoritmos numéricos intensivos implementados con bucles explícitos. Esto se debe a que C ejecuta código máquina directo sin la sobrecarga del intérprete.
* **Costo de la Abstracción**: La flexibilidad de Python (tipado dinámico, gestión automática de memoria, legibilidad) tiene un costo en rendimiento computacional cuando se procesan estructuras de bajo nivel sin librerías optimizadas.
* **Uso Práctico**: En desarrollo de software real, Python se prefiere para desarrollo rápido, prototipado y lógica de alto nivel, mientras que los módulos intensivos en cálculo numérico se delegan a librerías escritas en C/C++ (como NumPy o PyTorch en Python).

## 7. Guia de ejecucion:
### Python y C

1. Abre la terminal (CMD, PowerShell, Terminal, etc.).
2. Navega a la carpeta del archivo:
   ```bash
   cd ruta/de/la/carpeta
   ```
3. Ejecuta el script:
   ```bash
   python benchmark.py
   ```
   o, en algunos sistemas:
   ```bash
   python3 benchmark.py
   ```
   En Windows también puedes usar:
   ```bash
   py benchmark.py
   ```
> **Nota:** Para esta tarea se implementaron funciones que permiten compilar y correr el codigo de Python y de C directamente desde **benchmark.py**, por lo cual no es necesario ejecutar ambos archivos por aparte.
