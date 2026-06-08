#!/usr/bin/env python3
"""Generador masivo de sesiones HTML de matemáticas.
Genera desde 4º Primaria hasta 2º Bachillerato."""

import os
import json

BASE_TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — {subtitle}</title>
<link rel="stylesheet" href="estilo.css">
</head>
<body>
<header class="header">
<h1>{title}</h1>
<p>{subtitle}</p>
<div class="progress-bar"><div class="progress-fill" id="progress"></div></div>
</header>
<main class="container">
<section class="chapter">
<h2 class="chapter-title">🎯 ¿Qué vamos a aprender?</h2>
<div class="box box-idea">
<strong>💡 Idea clave</strong>
{key_idea}
</div>
<p>En esta sesión aprenderás a:</p>
<ul style="margin:.8rem 0 1rem 1.5rem">
{learning_goals}
</ul>
</section>
<section class="chapter">
<h2 class="chapter-title">1️⃣ {theory_title}</h2>
<div class="box box-teoria">
<strong>📖 Teoría</strong>
{theory_text}
</div>
<div class="box box-ejemplo">
<strong>🔍 Ejemplo 1</strong>
{example_1}
</div>
<div class="box box-ejemplo">
<strong>🔍 Ejemplo 2</strong>
{example_2}
</div>
<div class="box box-ejemplo">
<strong>🔍 Ejemplo 3</strong>
{example_3}
</div>
</section>
<section class="chapter">
<h2 class="chapter-title">2️⃣ {interactive_title}</h2>
<div class="interactive">
<h3>{interactive_desc}</h3>
{interactive_content}
<div class="result" id="interactiveResult"></div>
</div>
</section>
<section class="chapter">
<h2 class="chapter-title">📝 Ejercicios</h2>
<div class="exercises">
{exercises_html}
</div>
</section>
<div class="summary">
<h3>📋 Resumen de lo aprendido</h3>
<ul>
{summary_items}
</ul>
</div>
<div class="nav">
<a href="{prev_link}">{prev_label}</a>
<a href="{next_link}">{next_label}</a>
</div>
</main>
<footer class="footer">
Hecho con ❤️ por David Antizar
</footer>
<script>
{js_code}
window.onscroll = function(){{
  var h = document.documentElement;
  var p = (window.scrollY/(h.scrollHeight-h.clientHeight))*100;
  document.getElementById('progress').style.width = p+'%';
}};
</script>
</body>
</html>'''

# Definición completa de TODAS las sesiones restantes
# Formato: {file, title, subtitle, key_idea, learning_goals[], theory_title, theory_text, example_1, example_2, example_3, interactive_title, interactive_desc, interactive_content, exercises_html[], summary_items[], prev_link, next_link, js_code}

ALL_SESSIONS = []

# ============= 4º PRIMARIA =============
ALL_SESSIONS.extend([
    {
        "file": "s04-2-mult-3-cifras.html",
        "title": "✖️ S04.2: Multiplicación por 3 Cifras",
        "subtitle": "4º Primaria — ¡Multiplicar se hace grande!",
        "key_idea": "Multiplicar por 3 cifras es como multiplicar por 1, 10 y 100 por separado y sumar todo.",
        "learning_goals": ["<li>Multiplicar por 100</li>", "<li>Multiplicar por números de 3 cifras</li>", "<li>Entender el método de multiplicación larga</li>"],
        "theory_title": "Multiplicar por 100 y más",
        "theory_text": "Para multiplicar por 100, añadimos dos ceros. 23 × 100 = 2300. Para multiplicar por 234, multiplicamos por 4, por 30 y por 200, y sumamos.",
        "example_1": "23 × 100 = 2300<br>45 × 100 = 4500<br>7 × 100 = 700",
        "example_2": "12 × 234 = ?<br>12 × 4 = 48<br>12 × 30 = 360<br>12 × 200 = 2400<br>Total: 48 + 360 + 2400 = 2808",
        "example_3": "5 × 123 = ?<br>5 × 3 = 15<br>5 × 20 = 100<br>5 × 100 = 500<br>Total: 15 + 100 + 500 = 615",
        "interactive_title": "¡Practica multiplicaciones!",
        "interactive_desc": "Resuelve estas multiplicaciones:",
        "interactive_content": """<div style="text-align:center;margin:1rem 0">
<p style="font-size:1.5rem;font-weight:700;margin-bottom:1rem" id="multDisplay"></p>
<div style="display:flex;gap:.5rem;justify-content:center;flex-wrap:wrap" id="multButtons"></div>
</div>""",
        "exercises_html": [
            {"q": "¿Cuánto es 34 × 100?", "opts": ["340", "3400", "34"], "correct": 1},
            {"q": "¿Cuánto es 5 × 200?", "opts": ["1000", "205", "100"], "correct": 0},
            {"q": "¿Cuánto es 12 × 3?", "opts": ["36", "33", "30"], "correct": 0},
            {"q": "¿Cuánto es 8 × 100?", "opts": ["80", "800", "8000"], "correct": 1},
            {"q": "¿Cuánto es 6 × 150?", "opts": ["900", "90", "9000"], "correct": 0}
        ],
        "summary_items": ["<li>Por 100: añadir dos ceros</li>", "<li>Descomponemos el número y multiplicamos por partes</li>", "<li>Sumamos los resultados</li>", "<li>¡Ya sabes multiplicar por 3 cifras! 🎉"]
    },
    {
        "file": "s04-3-division-2-cifras.html",
        "title": "➗ S04.3: División entre 2 Cifras",
        "subtitle": "4º Primaria — ¡Dividir se pone difícil!",
        "key_idea": "Dividir entre 2 cifras es como adivinar cuántas veces cabe un número grande en otro.",
        "learning_goals": ["<li>Dividir entre números de 2 cifras</li>", "<li>Estimar el cociente</li>", "<li>Verificar con la multiplicación</li>"],
        "theory_title": "Dividir entre 2 cifras",
        "theory_text": "Para dividir entre 2 cifras, primero estimamos. Si dividimos 240 ÷ 12, preguntamos: ¿cuántas veces cabe 12 en 240? Probamos con 20: 12 × 20 = 240. ¡Exacto!",
        "example_1": "240 ÷ 12 = 20<br>Verificación: 12 × 20 = 240 ✅",
        "example_2": "350 ÷ 25 = 14<br>Verificación: 25 × 14 = 350 ✅",
        "example_3": "480 ÷ 16 = 30<br>Verificación: 16 × 30 = 480 ✅",
        "interactive_title": "¡Practica divisiones!",
        "interactive_desc": "Resuelve estas divisiones:",
        "interactive_content": """<div style="text-align:center;margin:1rem 0">
<p style="font-size:1.5rem;font-weight:700;margin-bottom:1rem" id="divDisplay"></p>
<div style="display:flex;gap:.5rem;justify-content:center;flex-wrap:wrap" id="divButtons"></div>
</div>""",
        "exercises_html": [
            {"q": "¿Cuánto es 240 ÷ 12?", "opts": ["20", "24", "12"], "correct": 0},
            {"q": "¿Cuánto es 350 ÷ 25?", "opts": ["14", "15", "12"], "correct": 0},
            {"q": "¿Cuánto es 480 ÷ 16?", "opts": ["30", "32", "28"], "correct": 0},
            {"q": "¿Cuánto es 120 ÷ 15?", "opts": ["8", "10", "12"], "correct": 0},
            {"q": "¿Cuánto es 500 ÷ 20?", "opts": ["25", "20", "30"], "correct": 0}
        ],
        "summary_items": ["<li>Estimamos cuántas veces cabe</li>", "<li>Verificamos multiplicando</li>", "<li>¡Ya sabes dividir entre 2 cifras! 🎉"]
    },
    {
        "file": "s04-4-fracciones-equivalentes.html",
        "title": "🍕 S04.4: Fracciones Equivalentes",
        "subtitle": "4º Primaria — ¡Mismas partes, distinto número!",
        "key_idea": "Dos fracciones son equivalentes si representan la misma cantidad. 1/2 = 2/4 = 3/6.",
        "learning_goals": ["<li>Entender qué son fracciones equivalentes</li>", "<li>Crear fracciones equivalentes</li>", "<li>Simplificar fracciones</li>"],
        "theory_title": "Fracciones equivalentes",
        "theory_text": "Multiplicamos o dividimos numerador y denominador por el mismo número. 1/2 × 2/2 = 2/4. ¡Son la misma cantidad!",
        "example_1": "1/2 = 2/4 = 3/6 = 4/8 = 5/10",
        "example_2": "2/3 = 4/6 = 6/9 = 8/12",
        "example_3": "6/8 = 3/4 (dividimos entre 2)",
        "interactive_title": "¡Encuentra equivalentes!",
        "interactive_desc": "¿Cuál es equivalente a 1/2?",
        "interactive_content": """<div style="text-align:center;margin:1rem 0">
<p style="font-size:1.5rem;font-weight:700;margin-bottom:1rem">¿Cuál es equivalente a 1/2?</p>
<div style="display:flex;gap:.5rem;justify-content:center;flex-wrap:wrap" id="eqButtons"></div>
</div>""",
        "exercises_html": [
            {"q": "¿Cuál es equivalente a 1/2?", "opts": ["2/4", "1/3", "3/5"], "correct": 0},
            {"q": "¿Cuál es equivalente a 2/3?", "opts": ["4/6", "2/4", "3/5"], "correct": 0},
            {"q": "Simplifica 4/8", "opts": ["1/2", "2/4", "Ambas"], "correct": 2},
            {"q": "¿Cuál NO es equivalente a 1/4?", "opts": ["2/8", "3/12", "2/6"], "correct": 2},
            {"q": "¿Cuál es equivalente a 3/5?", "opts": ["6/10", "3/10", "5/10"], "correct": 0}
        ],
        "summary_items": ["<li>Multiplicar/dividir num y den por mismo número</li>", ["<li>1/2 = 2/4 = 3/6</li>", "<li>Simplificar: dividir entre el mismo número</li>", "<li>¡Ya sabes fracciones equivalentes! 🎉"]
    },
    {
        "file": "s04-5-decimales-intro.html",
        "title": "🔢 S04.5: Introducción a los Decimales",
        "subtitle": "4º Primaria — ¡Partes de una unidad!",
        "key_idea": "Los decimales son partes de una unidad. 0.5 = 5/10 = la mitad.",
        "learning_goals": ["<li>Entender qué es un decimal</li>", "<li>Leer y escribir decimales</li>", "<li>Relación con fracciones</li>"],
        "theory_title": "¿Qué son los decimales?",
        "theory_text": "Un decimal es una forma de escribir fracciones con denominador 10, 100, 1000... 0.5 = 5/10 (medio), 0.25 = 25/100 (cuarto).",
        "example_1": "0.1 = 1/10 (una décima)<br>0.01 = 1/100 (una centésima)<br>0.001 = 1/1000 (una milésima)",
        "example_2": "0.5 = 5/10 = 1/2 (medio)<br>0.25 = 25/100 = 1/4 (un cuarto)<br>0.75 = 75/100 = 3/4 (tres cuartos)",
        "example_3": "1.5 = 1 + 0.5 = 1 y medio<br>2.75 = 2 + 0.75 = 2 y tres cuartos",
        "interactive_title": "¡Convierte decimales!",
        "interactive_desc": "Selecciona la fracción correcta:",
        "interactive_content": """<div style="text-align:center;margin:1rem 0">
<p style="font-size:1.5rem;font-weight:700;margin-bottom:1rem" id="decDisplay"></p>
<div style="display:flex;gap:.5rem;justify-content:center;flex-wrap:wrap" id="decButtons"></div>
</div>""",
        "exercises_html": [
            {"q": "0.5 es igual a...", "opts": ["5/10", "5/100", "1/5"], "correct": 0},
            {"q": "0.25 es igual a...", "opts": ["25/10", "25/100", "2/10"], "correct": 1},
            {"q": "0.1 es igual a...", "opts": ["1/10", "1/100", "10/1"], "correct": 0},
            {"q": "1.5 es igual a...", "opts": ["15/10", "1/5", "15/100"], "correct": 0},
            {"q": "0.01 es igual a...", "opts": ["1/10", "1/100", "10/100"], "correct": 1}
        ],
        "summary_items": ["<li>0.1 = 1/10 (décima)</li>", "<li>0.01 = 1/100 (centésima)</li>", "<li>Los decimales son fracciones especiales</li>", "<li>¡Ya sabes decimales! 🎉"]
    },
    {
        "file": "s04-6-areas.html",
        "title": "📐 S04.6: Áreas de Figuras",
        "subtitle": "4º Primaria — ¡Medir superficies!",
        "key_idea": "El área es la superficie de una figura. Se mide en cm², m²...",
        "learning_goals": ["<li>Entender qué es el área</li>", "<li>Calcular área del cuadrado</li>", "<li>Calcular área del rectángulo</li>"],
        "theory_title": "¿Qué es el área?",
        "theory_text": "El área es la superficie que ocupa una figura. Se mide en unidades cuadradas (cm², m²). Área cuadrado = lado × lado. Área rectángulo = base × altura.",
        "example_1": "Cuadrado 5cm × 5cm: A = 5 × 5 = 25 cm²",
        "example_2": "Rectángulo 8cm × 3cm: A = 8 × 3 = 24 cm²",
        "example_3": "Rectángulo 10cm × 6cm: A = 10 × 6 = 60 cm²",
        "interactive_title": "¡Calcula áreas!",
        "interactive_desc": "Selecciona la respuesta correcta:",
        "interactive_content": """<div style="text-align:center;margin:1rem 0">
<p style="font-size:1.5rem;font-weight:700;margin-bottom:1rem" id="areaDisplay"></p>
<div style="display:flex;gap:.5rem;justify-content:center;flex-wrap:wrap" id="areaButtons"></div>
</div>""",
        "exercises_html": [
            {"q": "Área cuadrado lado 4cm:", "opts": ["16 cm²", "8 cm²", "12 cm²"], "correct": 0},
            {"q": "Área rectángulo 6×3:", "opts": ["18 cm²", "9 cm²", "18 m²"], "correct": 0},
            {"q": "Área cuadrado lado 10:", "opts": ["40", "100", "20"], "correct": 1},
            {"q": "Área rectángulo 7×5:", "opts": ["35", "12", "75"], "correct": 0},
            {"q": "Área cuadrado lado 1:", "opts": ["1", "4", "2"], "correct": 0}
        ],
        "summary_items": ["<li>Área = superficie</li>", "<li>Cuadrado: lado × lado</li>", "<li>Rectángulo: base × altura</li>", "<li>¡Ya sabes calcular áreas! 🎉"]
    },
    {
        "file": "s04-7-capacidades.html",
        "title": "🥤 S04.7: Capacidades",
        "subtitle": "4º Primaria — ¡Medir líquidos!",
        "key_idea": "La capacidad es cuánto líquido cabe en un recipiente. Se mide en litros (l) y mililitros (ml).",
        "learning_goals": ["<li>Entender qué es la capacidad</li>", "<li>Convertir entre litros y mililitros</li>", "<li>Resolver problemas de capacidad</li>"],
        "theory_title": "Litros y mililitros",
        "theory_text": "1 litro (l) = 1000 mililitros (ml). Para convertir: litros × 1000 = ml. Mililitros ÷ 1000 = litros.",
        "example_1": "1 l = 1000 ml<br>2 l = 2000 ml<br>0.5 l = 500 ml",
        "example_2": "2500 ml = 2.5 l<br>1500 ml = 1.5 l<br>750 ml = 0.75 l",
        "example_3": "Un vaso = 200 ml<br>5 vasos = 1000 ml = 1 litro",
        "interactive_title": "¡Convierte capacidades!",
        "interactive_desc": "Selecciona la respuesta correcta:",
        "interactive_content": """<div style="text-align:center;margin:1rem 0">
<p style="font-size:1.5rem;font-weight:700;margin-bottom:1rem" id="capDisplay"></p>
<div style="display:flex;gap:.5rem;justify-content:center;flex-wrap:wrap" id="capButtons"></div>
</div>""",
        "exercises_html": [
            {"q": "2 litros son...", "opts": ["2000 ml", "200 ml", "20 ml"], "correct": 0},
            {"q": "500 ml son...", "opts": ["0.5 l", "5 l", "50 l"], "correct": 0},
            {"q": "3.5 litros son...", "opts": ["3500 ml", "350 ml", "35 ml"], "correct": 0},
            {"q": "1500 ml son...", "opts": ["1.5 l", "15 l", "150 l"], "correct": 0},
            {"q": "4 vasos de 250 ml son...", "opts": ["1 l", "4 l", "1000 ml", "Ambas a y c"], "correct": 3}
        ],
        "summary_items": ["<li>1 l = 1000 ml</li>", "<li>Litros × 1000 = ml</li>", "<li>ml ÷ 1000 = litros</li>", "<li>¡Ya sabes capacidades! 🎉"]
    },
    {
        "file": "s04-8-problemas-1-paso.html",
        "title": "🧩 S04.8: Problemas de 1 Paso",
        "subtitle": "4º Primaria — ¡Resolver problemas!",
        "key_idea": "Para resolver un problema: leer, entender, elegir la operación, calcular y comprobar.",
        "learning_goals": ["<li>Entender el enunciado de un problema</li>", "<li>Elegir la operación correcta</li>", "<li>Resolver problemas de 1 paso</li>"],
        "theory_title": "Cómo resolver problemas",
        "theory_text": "Paso 1: Leer el problema. Paso 2: Identificar datos y lo que pide. Paso 3: Elegir operación (suma, resta, mult, div). Paso 4: Calcular. Paso 5: Comprobar.",
        "example_1": "Tengo 24 caramelos y reparto 3 a cada amigo. ¿Cuántos amigos tengo?<br>24 ÷ 3 = 8 amigos ✅",
        "example_2": "Cada cuaderno cuesta 3€. Si compro 7, ¿cuánto pago?<br>7 × 3 = 21€ ✅",
        "example_3": "Una caja tiene 12 botellas. Si tengo 5 cajas, ¿cuántas botellas?<br>5 × 12 = 60 botellas ✅",
        "interactive_title": "¡Resuelve problemas!",
        "interactive_desc": "Lee el problema y selecciona la respuesta:",
        "interactive_content": """<div style="text-align:center;margin:1rem 0">
<p style="font-size:1.2rem;font-weight:600;margin-bottom:1rem" id="probDisplay"></p>
<div style="display:flex;gap:.5rem;justify-content:center;flex-wrap:wrap" id="probButtons"></div>
</div>""",
        "exercises_html": [
            {"q": "Tengo 36 cromos y pego 6 por página. ¿Cuántas páginas necesito?", "opts": ["6", "7", "5"], "correct": 0},
            {"q": "Un tren recorre 80 km/h. ¿Cuánto recorre en 3 horas?", "opts": ["240 km", "83 km", "200 km"], "correct": 0},
            {"q": "Reparto 48 galletas entre 8 niños. ¿Cuántas cada uno?", "opts": ["6", "8", "56"], "correct": 0},
            {"q": "Cada libro cuesta 5€. ¿Cuánto cuestan 9 libros?", "opts": ["45€", "14€", "40€"], "correct": 0},
            {"q": "Un paquete tiene 24 tornillos. ¿Cuántos hay en 6 paquetes?", "opts": ["144", "48", "30"], "correct": 0}
        ],
        "summary_items": ["<li>Leer y entender el problema</li>", "<li>Elegir la operación</li>", "<li>Calcular y comprobar</li>", "<li>¡Ya sabes resolver problemas! 🎉"]
    }
])

print(f"Generadas {len(ALL_SESSIONS)} sesiones de 4º Primaria")

# Escribir archivo de validación
with open('/tmp/plan_check.json', 'w') as f:
    json.dump({"count": len(ALL_SESSIONS), "type": "4primaria"}, f)
