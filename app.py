from flask import Flask, render_template_string

app = Flask(__name__)

# Plantilla HTML con CSS embebido y favicon vacío
html_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página Bonita con Flask</title>
    <!-- Favicon vacío para evitar 404 -->
    <link rel="icon" href="data:,">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(to right, #6a11cb, #2575fc);
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }
        header {
            font-size: 3em;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.5em;
            text-align: center;
            max-width: 600px;
        }
        button {
            padding: 10px 25px;
            margin-top: 20px;
            font-size: 1.2em;
            background-color: #fff;
            color: #2575fc;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        button:hover {
            background-color: #f0f0f0;
            transform: scale(1.1);
        }
        footer {
            position: absolute;
            bottom: 10px;
            font-size: 0.9em;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <header>¡Bienvenido a mi Página!</header>
    <p>Esta página está construida completamente en Flask con HTML y CSS embebidos en un solo archivo <strong>app.py</strong>.</p>
    <button onclick="alert('¡Hola! Gracias por visitar.')">Haz clic aquí</button>
    <footer>© 2025 Mi Página Flask</footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template)

if __name__ == "__main__":
    # Levanta la app en el puerto 80
    app.run(host="0.0.0.0", port=80, debug=True)
