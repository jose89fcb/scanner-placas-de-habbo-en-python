import requests

# Input de usuario
HabboID_input = input("Escribe el nombre del keko: ") 
print("Elige el hotel: es/com/fi/com.br/fr/nl/de/it/com.tr")
Hotel = input("hotel: ")

# Petición a la API para obtener datos del usuario
response = requests.get(f'https://www.habbo.{Hotel}/api/public/users?name={HabboID_input}')
try:
    user_data = response.json()
except ValueError:
    print("❌ Error: la respuesta de la API no es JSON")
    exit()

# Comprobar si el usuario existe
if 'uniqueId' not in user_data:
    print("❌ Usuario no encontrado en este hotel.")
    
    exit()

HabboID = user_data['uniqueId']
username = user_data.get('name', HabboID_input)

# Obtener placas del usuario
url = f'https://www.habbo.{Hotel}/api/public/users/{HabboID}/badges'
print("Scaneando placas...Espera un momento")
badges_response = requests.get(url)
try:
    badges = badges_response.json()
except ValueError:
    print("❌ Error: la respuesta de la API de badges no es JSON")
    exit()

filename = f"{HabboID}.html"
print(f"Fichero creado: {filename}")

# Crear HTML con diseño moderno y buscador rápido
with open(filename, "w", encoding="utf-8") as archivo:
    archivo.write(f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Placas de {username}</title>
<style>
    body {{
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: linear-gradient(135deg, #1c1c1c, #2d2d2d);
        color: #f1f1f1;
        margin: 0;
        padding: 20px;
    }}
    h1 {{
        text-align: center;
        color: #ffcc00;
        margin-bottom: 20px;
    }}
    .buscador {{
        text-align: center;
        margin-bottom: 20px;
    }}
    .buscador input {{
        padding: 10px;
        width: 50%;
        border-radius: 10px;
        border: none;
        outline: none;
        font-size: 16px;
    }}
    #contador {{
        margin-top: 5px;
        color: #aaa;
        font-size: 14px;
    }}
    .grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
    }}
    .item {{
        background: #2a2a2a;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.5);
        transition: transform 0.2s, box-shadow 0.2s;
    }}
    .item:hover {{
        transform: translateY(-5px);
        box-shadow: 0 6px 15px rgba(0,0,0,0.7);
    }}
    .texto p {{
        margin: 5px 0;
        font-size: 14px;
    }}
    .imagenPlaca img {{
        display: block;
        margin: 10px auto;
        border-radius: 8px;
        background: #111;
        padding: 5px;
    }}
    .codigoPlaca {{
        display: block;
        text-align: center;
        font-size: 13px;
        margin-top: 5px;
        color: #ffcc00;
        font-weight: bold;
    }}
    footer {{
        margin-top: 30px;
        text-align: center;
        color: #aaa;
        font-size: 14px;
    }}
</style>
<script>
    function filtrarPlacas() {{
        const input = document.getElementById("buscador");
        const filter = input.value.toLowerCase();
        const items = document.getElementsByClassName("item");
        let count = 0;

        Array.from(items).forEach(item => {{
            const nombre = item.dataset.name.toLowerCase();
            const desc = item.dataset.desc.toLowerCase();
            const code = item.dataset.code.toLowerCase();

            if(nombre.includes(filter) || desc.includes(filter) || code.includes(filter)) {{
                item.style.display = "";
                count++;
            }} else {{
                item.style.display = "none";
            }}
        }});

        document.getElementById("contador").innerText = `Placas encontradas: ${{count}}`;
    }}
</script>
</head>
<body>

<h1>Placas de {username}</h1>

<div class="buscador">
    <input id="buscador" onkeyup="filtrarPlacas()" placeholder="🔍 Buscar placa...">
    <p id="contador">Placas encontradas: {len(badges)}</p>
</div>

<div class="grid">
""")

    # Escribir cada badge como tarjeta con data-attributes
    for badge in badges:
        nombre = badge.get('name','').replace('"', '&quot;')
        desc = badge.get('description','').replace('"', '&quot;')
        code = badge.get('code','')
        archivo.write(f"""
        <div class="item" data-name="{nombre}" data-desc="{desc}" data-code="{code}">
            <div class="texto">
                <p><b>Nombre:</b> {nombre}</p>
                <p><b>Descripción:</b> {desc}</p>
            </div>
            <div class="imagenPlaca">
                <img src="https://images.habbo.com/c_images/album1584/{code}.gif" alt="{code}">
            </div>
            <span class="codigoPlaca">{code}</span>
        </div>
        """)

    archivo.write(f"""
</div>

<footer>
    <p>Generado para <b>{username}</b> en habbo.{Hotel}</p>
</footer>

</body>
</html>
""")

print("✅ Archivo HTML generado con buscador rápido y contador en vivo.")
