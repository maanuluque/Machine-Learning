# Sokoban
### Sistemas de Inteligencia Artificial - Grupo 7

## Instalación

## En Linux/Mac
Nuestro repositorio cuenta con un archivo `install.sh` que al ejecutarlo descarga los paquetes necesarios.
Para ejecutarlo, abra la terminal en la carpeta del proyecto y utilice el siguiente comando:
`./install.sh`

Nota: el sistema le solicitará la contraseña de administrador para instalar los paquetes.

# En Windows
Descargue python desde el [sitio oficial de python](https://www.python.org/downloads/). 
El gestor de paquetes PIP se incluirá en la misma descarga. Para corroborarlo, ejecute en la terminal el siguiente comando: 
`pip --version`

Finalmente, instale el paquete munkres mediante el comando:
`pip install munkres`


## Ejecución
Para ejecutar el programa, simplemente se debe correr en la terminal el archivo main.py:
`python3 main.py`

## Configuración
El programa cuenta con varios parámetros que pueden ser seteados por el usuario. Ese proceso se realiza editando el archivo `config.json`
En el mismo, se cuenta con los siguientes valores:
- algorithm
  - dfs
  - bfs
  - iddfs
  - globalGreedy
  - A*
  - IDA*
- heuristics
  - slb
  - slb*
  - mmlb
- map
  - Debe contener `Maps/map#.txt` (siendo "#" el numero de mapa seleccionado)
- iddfs_depth_limit
  - Selecciona el limite de profundidad del algoritmo IDDFS (solo es relevante si se seleccionó tal algoritmo)
- ida*_limit
  - Selecciona el limite del algoritmo IDA* (solo es relevante si se seleccionó tal algoritmo)
