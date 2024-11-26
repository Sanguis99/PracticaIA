metro_times = {
    "A": {
        "Plaza de Mayo - Perú": 1,
        "Perú - Piedras": 1,
        "Piedras - Lima": 1,
        "Lima - Sáenz Peña": 1,
        "Sáenz Peña - Congreso": 1,
        "Congreso - Pasco": 1,
        "Pasco - Alberti": 1,
    },
    "B": {
        "Leandro N. Alem - Florida": 1,
        "Florida - Carlos Pellegrini": 1,
        "Carlos Pellegrini - Uruguay": 1,
        "Uruguay - Callao Norte": 1,
        "Callao Norte - Pasteur": 1,
    },
    "C": {
        "Retiro - General San Martín": 1,
        "General San Martín - Lavalle": 2,
        "Lavalle - Diagonal Norte": 1,
        "Diagonal Norte - Avenida de Mayo": 2,
        "Avenida de Mayo - Moreno": 1,
        "Moreno - Independencia Este": 1,
        "Independencia Este - San Juan": 1,
        "San Juan - Constitución": 2,
    },
    "D": {
        "Catedral - 9 de Julio": 1,
        "9 de Julio - Tribunales": 1,
        "Tribunales - Callao Sur": 2,
        "Callao Sur - Facultad de Medicina": 1,
    },
    "E": {
        "Bolívar - Belgrano": 2,
        "Belgrano - Independencia Oeste": 2,
        "Independencia Oeste - San José": 2,
        "San José - Entre Ríos": 2,
        "Entre Ríos - Pichincha": 1,
    },
    "T": {
        "Lima - Avenida de Mayo": 5,
        "Perú - Catedral": 2,
        "Perú - Bolívar": 3,
        "Carlos Pellegrini - 9 de Julio": 2,
        "Diagonal Norte - 9 de Julio": 1,
        "Independencia Oeste - Independencia Este": 3,
        "Catedral - Bolívar": 5,
        "Callao Norte - Callao Sur": 1,
        "Independencia Este - Independencia Oeste": 1
    },
}

lines = {
	'A': ['Plaza de Mayo', 'Perú', 'Piedras', 'Lima', 'Sáenz Peña', 'Congreso', 'Pasco', 'Alberti'],
	'B': ['Leandro N. Alem', 'Florida', 'Carlos Pellegrini', 'Uruguay', 'Callao Norte', 'Pasteur'],
	'C': ['Retiro', 'General San Martín', 'Lavalle', 'Diagonal Norte', 'Avenida de Mayo', 
        'Moreno', 'Independencia Este', 'San Juan', 'Constitución'],
	'D': ['Catedral', '9 de Julio', 'Tribunales', 'Callao Sur', 'Facultad de Medicina'],
	'E': ['Bolívar', 'Belgrano', 'Independencia Oeste', 'San José', 'Entre Ríos', 'Pichincha'],
}

metro_node_coord = {
    'Plaza de Mayo': (4.2,0.7),
    'Perú': (3,0.7),
    'Piedras': (1.69,0.7),
    'Lima': (0,0.7),
    'Sáenz Peña': (-1,0.7),
    'Congreso': (-2.08,0.7),
    'Pasco': (-3.23,0.7),
    'Alberti': (-4.26,0.7),

    'Leandro N. Alem': (3.95,2.35),
    'Florida': (2.75,2.35),
    'Carlos Pellegrini': (1.55,2.35),
    'Uruguay': (-1.2,2.35),
    'Callao Norte': (-2.1,2.35),
    'Pasteur': (-3.69,2.35),
    
    'Retiro': (3.83,4.63),
    'General San Martín': (2.8,4.1),
    'Lavalle': (1.89,2.82),
    'Diagonal Norte': (1.52,1.4),
    'Avenida de Mayo': (0.68,0.69),
    'Moreno': (0.68,-0.53),
    'Independencia Este': (0.68,-1.86),
    'San Juan': (0.68,-3.36),
    'Constitución': (0.68,-4.88),

    'Catedral': (2.7,1.6),
    '9 de Julio': (0.7,2),
    'Tribunales': (-0.64,2.94),
    'Callao Sur': (-2.1,3.6),
    'Facultad de Medicina': (-3.9,3.6),

    'Bolívar': (2.7,-0.15),
    'Belgrano': (1.2,-0.57),
    'Independencia Oeste': (-0.36,-1.86),
    'San José': (-1.0,-3.14),
    'Entre Ríos': (-2.1,-3.14),
    'Pichincha': (-3.74,-3.14),
}

metro_coord_geodesic = {
    'Plaza de Mayo': (-34.60852336525573, -58.37099647736891),
    'Perú': (-34.60841740052505, -58.37424731475452),
    'Piedras': (-34.60868231209738, -58.3782706282344),
    'Lima': (-34.60899936126676, -58.38223798242305),
    'Sáenz Peña': (-34.60930642035077, -58.38642070055631),
    'Congreso': (-34.60909205349264, -58.39239405734514),
    'Pasco': (-34.60943212397035, -58.398124817661504),
    'Alberti': (-34.609737510219716, -58.40065898341956),

    'Leandro N. Alem': (-34.60281575311817, -58.369699552240384),
    'Florida': (-34.603168992189694, -58.374205663467976),
    'Carlos Pellegrini': (-34.603515609413634, -58.38091914892496),
    'Uruguay': (-34.603876515306226, -58.38648778697883),
    'Callao Norte': (-34.60428051748904, -58.391901606970926),
    'Pasteur': (-34.60447816473591, -58.39891966425801),
    
    'Retiro': (-34.59102559582136, -58.37459659456844),
    'General San Martín': (-34.59542282799334, -58.37703420805947),
    'Lavalle': (-34.60196300063525, -58.37785934938813),
    'Diagonal Norte': (-34.60421016183624, -58.37767915586964),
    'Avenida de Mayo': (-34.60836625694821, -58.37838785470674),
    'Moreno': (-34.61191577252951, -58.379483040138766),
    'Independencia Este': (-34.617505429647466, -58.37847215489829),
    'San Juan': (-34.621956046240555, -58.37929951603437),
    'Constitución': (-34.6273143709629, -58.380378469073364),

    'Catedral': (-34.60746965446476, -58.373881894567646),
    '9 de Julio': (-34.604374394134, -58.37987593524887),
    'Tribunales': (-34.60167148679957, -58.384128779029666),
    'Callao Sur': (-34.59949557978796, -58.39195888279371),
    'Facultad de Medicina': (-34.59969268410233, -58.39749535538687),

    'Bolívar': (-34.609429858008006, -58.3735886638776),
    'Belgrano': (-34.61270583182017, -58.37760124862716),
    'Independencia Oeste': (-34.618041135928785, -58.38121954864429),
    'San José': (-34.62220323205144, -58.384870612201205),
    'Entre Ríos': (-34.62261344500609, -58.39116573363126),
    'Pichincha': (-34.623049298114374, -58.3967793357254),
}