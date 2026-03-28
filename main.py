import random
import pandas as pd

# ---------- Tablas relacionadas (simulan FK) ----------

paises = {
    1: "México",
    2: "España",
    3: "Argentina",
    4: "Colombia",
    5: "Chile"
}

deportes = {
    1: "Fútbol",
    2: "Baloncesto",
    3: "Tenis",
    4: "Natación",
    5: "Atletismo"
}

nombres = [
    "Juan", "María", "Luis", "Ana", "Carlos", "Laura",
    "Pedro", "Sofía", "Diego", "Valeria", "Jorge", "Camila"
]

apellidos = [
    "García", "Martínez", "López", "Hernández",
    "González", "Pérez", "Sánchez", "Ramírez"
]

estados_civiles = ["Soltero", "Casado", "Divorciado", "Viudo"]

# ---------- Generación del dataset ----------

data = []

for i in range(1, 101):
    pais_id = random.choice(list(paises.keys()))
    deporte_id = random.choice(list(deportes.keys()))

    nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)}"

    fila = {
        "id": i,  # PRIMARY KEY
        "nombre": nombre_completo,
        "edad": random.randint(18, 70),
        "pais_id": pais_id,  # FOREIGN KEY
        "nacionalidad": paises[pais_id],
        "deporte_id": deporte_id,  # FOREIGN KEY
        "deporte_favorito": deportes[deporte_id],
        "estado_civil": random.choice(estados_civiles)
    }

    data.append(fila)

df = pd.DataFrame(data)

# ---------- Guardar a CSV ----------
df.to_csv("usuarios_dataset.csv", index=False)

# ---------- Mostrar preview ----------
print(df.head())