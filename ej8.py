nombres1= """
    'Agustin',
    'Alan',
    'Andrés',
    'Ariadna',
    'Bautista',
    'CAROLINA',
    'CESAR',
    'David',
    'Diego',
    'Dolores',
    'DYLAN',
    'ELIANA',
    'Emanuel',
    'Fabián',
    'Facundo',
    'Facundo',
    'FEDERICO',
    'FEDERICO',
    'GONZALO',
    'Gregorio',
    'Ignacio',
    'Jonathan',
    'Jonathan',
    'Jorge',
    'JOSE',
    'JUAN',
    'Juan',
    'Juan',
    'Julian',
    'Julieta',
    'LAUTARO',
    'Leonel',
    'LUIS',
    'Luis',
    'Marcos',
    'María',
    'MATEO',
    'Matias',
    'Nicolás',
    'NICOLÁS',
    'Noelia',
    'Pablo',
    'Priscila',
    'TOMAS',
    'Tomás',
    'Ulises',
    'Yanina' """

nombres2 = """
    'Agustin',
    'AGUSTIN',
    'Agustín',
    'Ailen',
    'Alfredo',
    'Amalia',
    'Ariana',
    'Bautista',
    'Braian',
    'Carla',
    'CESAR',
    'Daniel',
    'Diego',
    'ELIANA',
    'Facundo',
    'Facundo',
    'Facundo',
    'Facundo',
    'Federico',
    'Federico',
    'Flavia',
    'Francisco',
    'Germán',
    'Guido',
    'GUSTAVO',
    'Hilario',
    'Ignacio',
    'IVAN',
    'Jimmy',
    'Joaquín',
    'Jose',
    'Josue',
    'JUAN',
    'Juan',
    'Laura',
    'LAURA',
    'Lautaro',
    'Lautaro',
    'Ludmila',
    'Marcos',
    'Marcos',
    'MARIANELA',
    'MARTIN',
    'MATEO',
    'Mateo',
    'Matias',
    'MAURO',
    'Maximiliano',
    'NESTOR',
    'Nicolas',
    'Pedro',
    'Ramiro',
    'Sofía',
    'Tobias',
    'Tomás',
    'Tomás',
    'Ulises',
    'Yanina' """

notas1= """81,
    60,
    72,
    24,
    15,
    91,
    12,
    70,
    29,
    42,
    16,
    3,
    35,
    67,
    10,
    57,
    11,
    69,
    12,
    77,
    13,
    86,
    48,
    65,
    51,
    41,
    87,
    43,
    10,
    87,
    91,
    15,
    44,
    85,
    73,
    37,
    42,
    95,
    18,
    7,
    74,
    60,
    9,
    65,
    93,
    63,
    74"""

notas2 = """30,
    95,
    28,
    84,
    84,
    43,
    66,
    51,
    4,
    11,
    58,
    10,
    13,
    34,
    96,
    71,
    86,
    37,
    64,
    13,
    8,
    87,
    14,
    14,
    49,
    27,
    55,
    69,
    77,
    59,
    57,
    40,
    96,
    24,
    30,
    73,
    95,
    19,
    47,
    15,
    31,
    39,
    15,
    74,
    33,
    57,
    10"""

nombres1 = nombres1.replace(',',"").replace("'", "")
nombres1 = (nombres1.split())
#print(nombres1)

nombres2 = nombres2.replace(',',"").replace("'", "")
nombres2 = (nombres2.split())
#print(nombres2)

notas1 = notas1.replace(',',"")
notas1 = notas1.split()

notas2 = notas2.replace(',',"")
notas2 = notas2.split()


#Indicar los nombres que se encuentran en ambas listas.

nombres_repetidos = [nombre for nombre in dict([(nombre, '') for nombre in nombres1 if nombres1 if nombre in nombres2])]

print('Nombres repetidos en ambas listas:')
print(nombres_repetidos)

print()

#imprimir con formato los nombres de los estudiantes con las correspondientes nota y la suma

formato = "{:4} {:15} {:8} {:8} {:8}"

print(formato.format('','Nombre','Eval1','Eval2','Total'))

for line in range(len(nombres1)):
    print(formato.format(line, nombres1[line], notas1[line], notas2[line], int(notas1[line])+int(notas2[line])))
