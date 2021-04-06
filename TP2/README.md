# Algoritmos Genéticos

### Sistemas de Inteligencia Artificial - Grupo 7

## Instalación

### En Linux/Mac

El sistema necesitará un herramienta para el correcto uso de los graficos.

Correr en la terminal elsiguiente comando para descargarlo:
$>`sudo apt-get install python3-tk`

### Ejecución

Para ejecutar el programa, debe abrir en su IDE/pararse en la terminal sobre la carpeta del proyecto ("SIA/TP2/"), y correr el siguiente archivo con python:
`python3 main.py`

### Configuración

El programa cuenta con varios parámetros que pueden ser seteados por el usuario. Ese proceso se realiza editando el archivo `config.json`
En el mismo, se cuenta con los siguientes valores:


- player_class
- dataset
- population_size
- max_height
- min_height
- height_decimals
- genome_size
- fill
- cross
    - method
    - annular_length
    - uniform_prob
- mutation
     - method
     - probability
- select_parents
    - method_1
    - method_2
    - percent_1
    - amount
    - boltzmann_tc
    - boltzmann_t0
    - boltzmann_k
    - tournament_group
    - tournament_threshold
- select_children
    - method_1
    - method_2
    - percent_1
    - boltzmann_tc
    - boltzmann_t0
    - boltzmann_k
    - tournament_group
    - tournament_threshold
- cut
    - method
    - time_limit
    - acceptable_fitness
    - structure_percent
    - generations_limit
    - fitness_decimals
- live_graph
- diversity_graph
- last_diversity_graph
- items_div_graph

## Ejemplos Configuraciónes



### Ejemplo 10000 poblacion - sin gráficos

{
    "player_class": "warrior",
    "dataset": "data",
    "population_size": 10000,
    "max_height": 2.0,
    "min_height": 1.3,
    "height_decimals": 2,
    "genome_size": 6,
    "fill": "fill_all",
    "cross": {
        "method": "annular",
        "annular_length": 3,
        "uniform_prob": 0.5
    },
    "mutation": {
        "method": "gen",
        "probability": 0.5
    },
    "select_parents": {
        "method_1": "elite",
        "method_2": "ranking",
        "percent_1": 0.7,
        "amount": 10000,
        "boltzmann_tc": 1,
        "boltzmann_t0": 20,
        "boltzmann_k": 0.1,
        "tournament_group": 50,
        "tournament_threshold": 0.7
    },
    "select_children": {
        "method_1": "elite",
        "method_2": "ranking",
        "percent_1": 1,
        "boltzmann_tc": 1,
        "boltzmann_t0": 20,
        "boltzmann_k": 0.1,
        "tournament_group": 50,
        "tournament_threshold": 0.7
    },
    "cut": {
        "method": "content_cut",
        "time_limit": 10,
        "acceptable_fitness": 19,
        "structure_percent": 0.5,
        "generations_limit": 10,
        "fitness_decimals": 4
    },
    "live_graph": false,
    "diversity_graph": false,
    "last_diversity_graph": false,
    "items_div_graph": false
}

### Ejemplo 1000 poblacion - con gráficos

{
    "player_class": "warrior",
    "dataset": "data",
    "population_size": 1000,
    "max_height": 2.0,
    "min_height": 1.3,
    "height_decimals": 2,
    "genome_size": 6,
    "fill": "fill_all",
    "cross": {
        "method": "annular",
        "annular_length": 3,
        "uniform_prob": 0.5
    },
    "mutation": {
        "method": "gen",
        "probability": 0.5
    },
    "select_parents": {
        "method_1": "boltzmann",
        "method_2": "ranking",
        "percent_1": 0.7,
        "amount": 1000,
        "boltzmann_tc": 1,
        "boltzmann_t0": 20,
        "boltzmann_k": 0.1,
        "tournament_group": 50,
        "tournament_threshold": 0.7
    },
    "select_children": {
        "method_1": "boltzmann",
        "method_2": "ranking",
        "percent_1": 1,
        "boltzmann_tc": 1,
        "boltzmann_t0": 20,
        "boltzmann_k": 0.1,
        "tournament_group": 50,
        "tournament_threshold": 0.7
    },
    "cut": {
        "method": "structure_cut",
        "time_limit": 10,
        "acceptable_fitness": 19,
        "structure_percent": 0.7,
        "generations_limit": 10,
        "fitness_decimals": 4
    },
    "live_graph": true,
    "diversity_graph": true,
    "last_diversity_graph": true,
    "items_div_graph": true
}