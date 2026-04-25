import random
import pandas as pd

# ---------- Tablas relacionadas (simulan FK) ----------

paises = {
    1: "México",
    2: "Panamá",
    3: "Argentina",
    4: "Colombia",
    5: "Chile",
    6: "Uruguay",
    7: "Brasil",
    8: "Costa Rica",
    9: "República Dominicana",
    10: "El Salvador",
    11: "Belice",
    12: "Canadá",
    13: "Estados Unidos",
    14: "Puerto Rico",
    15: "Alaska".
}

sports = {
    1: "Fútbol",
    2: "Baloncesto",
    3: "Tenis",
    4: "Natación",
    5: "Atletismo",
    6: "Beisbol",
    7: "Clavados",
    8: "Golf",
    9: "Volleyball"
}

nombres = [
    "Juan", "María", "Luis", "Ana", "Carlos", "Laura", "Elena", "Perla", "Samuel", "Emiliano", "Ángel",
    "Pedro", "Sofía", "Diego", "Valeria", "Jorge", "Camila", "Rene", "Marlen", "Diana"
]

apellidos = [
    "García", "Martínez", "López", "Hernández", "Sanchez", "Montero", "Velasco", "Huitron",
    "González", "Pérez", "Sánchez", "Ramírez", "Ramos", 
]

estados_civiles = ["Soltero", "Casado", "Divorciado", "Viudo"]

# ---------- Generación del dataset ----------

data = []

for i in range(1, 101):
    pais_id = random.choice(list(paises.keys()))
    sport_id = random.choice(list(sports.keys()))

    nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)}"

    fila = {
        "id": i,  # PRIMARY KEY
        "nombre": nombre_completo,
        "edad": random.randint(18, 70),
        "pais_id": pais_id,  # FOREIGN KEY in case there is other data set
        "nacionalidad": paises[pais_id],
        "deporte_id": sport_id,  # FOREIGN KEY
        "deporte_favorito": sports[sport_id],
        "estado_civil": random.choice(estados_civiles)
    }

    data.append(fila)

df = pd.DataFrame(data)

# ---------- Guardar a CSV ----------
df.to_csv("usuarios_dataset.csv", index=False)

# ---------- Mostrar preview ----------
print(df.head())
