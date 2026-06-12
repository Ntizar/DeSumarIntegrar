#!/usr/bin/env python3
"""Reescribir el contenido pedagógico de eso1-1-numeros-enteros.html manteniendo CSS y estructura."""

input_path = "/root/workspace/DeSumarIntegrar/eso1-1-numeros-enteros.html"

with open(input_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extraer CSS (entre <style> y </style>)
css_start = content.index('<style>') + len('<style>')
css_end = content.index('</style>')
css_content = content[css_start:css_end]

# Extraer JS (entre <script> del body y </script> final)
# Encontrar el último <script> que contiene el JS
js_start = content.rindex('<script>') + len('<script>')
js_end = content.rindex('</script>')
js_content = content[js_start:js_end]

# Extraer head completo (incluye link katex + style)
head_start = content.index('<head>') + len('<head>')
head_end = content.index('</head>')
head_content = content[head_start:head_end]

print(f"CSS length: {len(css_content)}")
print(f"JS length: {len(js_content)}")
print(f"Head length: {len(head_content)}")

# Nuevo contenido del body (entre <body> y </body>)
body_start = content.index('<body>') + len('<body>')
body_end = content.index('</body>')
old_body = content[body_start:body_end]
print(f"Old body length: {len(old_body)}")

# === NUEVO CONTENIDO PEDAGÓGICO ===
new_body = '''
  <div style="padding: 0.75rem 1.5rem;">
    <a href="INDEX.html" style="display: inline-flex; align-items: center; gap: 0.5rem; color: #2563eb; text-decoration: none; font-weight: 600; padding: 0.4rem 1rem; border-radius: 10px; background: rgba(255,255,255,0.6); border: 1px solid rgba(255,255,255,0.3); font-size: 0.85rem;">← Volver al índice</a>
  </div>
<header class="header">
<h1>🔢 ESO1.1: Números Enteros</h1>
<p>1º ESO — Más allá del cero: el mundo de los negativos</p>
<div class="progress-bar"><div class="progress-fill" id="progress"></div></div>
</header>
<main class="container">

<!-- OBJETIVOS -->
<section class="chapter">
<h2 class="chapter-title">🎯 ¿Qué vamos a aprender?</h2>
<div class="box box-idea">
<strong>💡 Idea clave</strong>
Los números enteros (\\(\\mathbb{Z}\\)) van más allá de los naturales: incluyen negativos, cero y positivos. \\(-3\\) es MENOR que \\(-1\\), aunque \\(3\\) es MAYOR que \\(1\\).
</div>
<p>En esta sesión aprenderás a:</p>
<ul style="margin:.8rem 0 1rem 1.5rem">
<li>Entender qué son los enteros y para qué sirven en el mundo real</li>
<li>Comparar y ordenar números enteros correctamente</li>
<li>Representarlos en la recta numérica</li>
<li>Calcular y comprender el valor absoluto</li>
<li>Resolver problemas de temperatura, altitud y ascensores</li>
</ul>
</section>

<!-- CONEXIÓN CON CONOCIMIENTOS PREVIOS -->
<div class="connection-box">
<strong>🔗 Conexión con lo que ya sabes</strong>
<p>En Primaria trabajaste los <strong>números naturales</strong> (\\(\\mathbb{N} = \\{1, 2, 3, \\ldots\\}\\)) y aprendiste a sumarlos, restarlos y ordenarlos. Los números enteros amplían ese conjunto: añadimos los <strong>negativos</strong> y el <strong>cero</strong>. Es como si tuvieras un "modo inverso" de los naturales. Piensa en un termómetro: los grados positivos suben, los negativos bajan. ¡Ya conoces la idea, ahora la vamos a formalizar!</p>
</div>

<!-- TEORÍA ESTRUCTURADA EN 4 PASOS -->
<section class="chapter">
<h2 class="chapter-title">📖 Los números enteros (\\(\\mathbb{Z}\\))</h2>

<!-- PASO 1: MIRA -->
<div class="box box-teoria">
<span class="step-indicator"><span class="step-dot"></span> Paso 1: Mira</span>
<strong>👀 ¿Qué son los números enteros?</strong>
<p>Los números enteros son el conjunto \\(\\mathbb{Z} = \\{\\ldots, -3, -2, -1, \\; 0, \\; 1, 2, 3, \\ldots\\}\\). Se leen: "… menos tres, menos dos, menos uno, cero, uno, dos, tres …"</p>
<p>Se dividen en tres grupos:</p>
<ul style="margin:.5rem 0 0 1.2rem">
<li><strong>Negativos</strong> (\\(\\mathbb{Z}^-\\)): \\(\\ldots, -3, -2, -1\\) → están por debajo de cero</li>
<li><strong>Cero</strong> (\\(0\\)): ni positivo ni negativo, es el punto de referencia</li>
<li><strong>Positivos</strong> (\\(\\mathbb{Z}^+\\)): \\(1, 2, 3, \\ldots\\) → son los naturales</li>
</ul>
</div>

<!-- PASO 2: FÍJATE -->
<div class="box box-teoria">
<span class="step-indicator"><span class="step-dot"></span> Paso 2: Fíjate</span>
<strong>🔍 ¿Para qué sirven en la vida real?</strong>
<p>Los enteros aparecen siempre que necesitamos medir algo que puede estar <strong>por debajo de un punto de referencia</strong>:</p>
<table style="width:100%;margin:.8rem 0;border-collapse:collapse;font-size:.95rem">
<tr style="background:var(--azul);color:#fff"><th style="padding:.5rem;border-radius:6px 0 0 0">Situación</th><th style="padding:.5rem;border-radius:0 6px 0 0">Positivo (+)</th><th style="padding:.5rem;border-radius:0 0 6px 0">Negativo (−)</th><th style="padding:.5rem">Referencia (0)</th></tr>
<tr><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">🌡️ Temperatura</td><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">Sobre 0°C</td><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">Bajo 0°C</td><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">0°C (congelación)</td></tr>
<tr><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">🏔️ Altitud</td><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">Sobre el nivel del mar</td><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">Bajo el nivel del mar</td><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">Nivel del mar</td></tr>
<tr><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">🏢 Plantas edificio</td><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">Plantas altas</td><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">Sótanos</td><td style="padding:.5rem;border-bottom:1px solid #e2e8f0">Planta baja</td></tr>
<tr><td style="padding:.5rem">💰 Dinero</td><td style="padding:.5rem">Ahorro / Ingreso</td><td style="padding:.5rem">Deuda / Gasto</td><td style="padding:.5rem">Saldo = 0</td></tr>
</table>
</div>

<!-- PASO 3: AHORA VES -->
<div class="box box-teoria">
<span class="step-indicator"><span class="step-dot"></span> Paso 3: Ahora ves</span>
<strong>📏 ¿Cómo se ordenan en la recta?</strong>
<p>En la recta numérica, la regla es simple:</p>
<div class="box box-ejemplo" style="margin:.5rem 0">
<strong>📐 Regla de oro</strong>
<p>Todo lo que está a la <strong>derecha</strong> es MAYOR. Todo lo que está a la <strong>izquierda</strong> es MENOR.</p>
</div>
<p>Esto significa:</p>
<ul style="margin:.5rem 0 0 1.2rem">
<li>Todo positivo \\(> 0\\) → \\(1 > 0\\), \\(100 > 0\\)</li>
<li>Todo negativo \\(< 0\\) → \\(-1 < 0\\), \\(-100 < 0\\)</li>
<li>Entre dos positivos: el mayor es el de mayor valor absoluto → \\(7 > 3\\)</li>
<li>Entre dos negativos: ¡el de menor valor absoluto es MAYOR! → \\(-1 > -7\\)</li>
</ul>
<div class="box box-ejemplo" style="margin:.5rem 0">
<strong>💡 Ejemplo visual</strong>
<p>\\(-5 < -3 < -1 < 0 < 2 < 4\\)<br>
De izquierda a derecha en la recta: siempre crecen.</p>
</div>
</div>

<!-- PASO 4: ERROR COMÚN -->
<div class="box box-error">
<span class="step-indicator"><span class="step-dot"></span> Paso 4: ¡Cuidado!</span>
<strong>🚫 Error común: "−5 es mayor que −3 porque 5 > 3"</strong>
<p>¡Falso! Este es el error más frecuente. Recuerda:</p>
<ul style="margin:.5rem 0 0 1.2rem">
<li>El <strong>valor absoluto</strong> \\(|-5| = 5\\) mide la distancia al cero, pero no el orden</li>
<li>En la recta, \\(-5\\) está más a la izquierda que \\(-3\\), así que \\(-5 < -3\\)</li>
<li><strong>Truco infalible:</strong> piensa en temperatura. \\(-5°\\text{C}\\) está MÁS FRÍO que \\(-3°\\text{C}\\). ❄️</li>
</ul>
</div>
</section>

<!-- CASO REAL DE VIDA REAL -->
<section class="chapter">
<h2 class="chapter-title">🌍 Caso real: Los ascensores del Burj Khalifa</h2>
<div class="box box-success">
<span class="real-world-badge">🌍 Vida real</span>
<strong>🏗️ El edificio más alto del mundo usa números enteros</strong>
<p>El Burj Khalifa en Dubái tiene 163 plantas. Pero también tiene <strong>sótanos</strong>: los aparcamientos están en \\(-1\\), \\(-2\\) y \\(-3\\). Si un turista está en la planta \\(124\\) (el mirador) y quiere bajar al parking \\(-2\\), ¿cuántos pisos baja?</p>
<div class="box box-ejemplo" style="margin:.5rem 0">
<strong>🧮 Resolución</strong>
<p>\\(124 - (-2) = 124 + 2 = 126\\) pisos. ¡Baja 126 plantas!</p>
</div>
<p>Los números enteros no son solo teoría: cada vez que usas un ascensor con botón de sótano, los estás usando. 🏢</p>
</div>
</section>

<!-- RECTA NUMÉRICA VISUAL -->
<section class="chapter">
<h2 class="chapter-title">📏 Recta numérica interactiva</h2>
<div class="interactive">
<h3>🖱️ Haz clic en un número para verlo en la recta</h3>
<p style="text-align:center;margin-bottom:.5rem;color:var(--gris)">Selecciona un entero y observa dónde queda en la recta</p>
<div class="number-line">
<div class="svg-container">
<svg id="numberLineSvg" width="620" height="120" viewBox="0 0 620 120">
<!-- Línea principal -->
<line x1="30" y1="60" x2="590" y2="60" stroke="#94a3b8" stroke-width="3" stroke-linecap="round"/>
<!-- Flechas -->
<polygon points="30,60 42,54 42,66" fill="#94a3b8"/>
<polygon points="590,60 578,54 578,66" fill="#94a3b8"/>
<!-- Marcas y números se generan con JS -->
</svg>
</div>
</div>
<div style="text-align:center;margin-top:.5rem">
<button class="check-btn" onclick="showRandomPoint()">🎲 Mostrar número aleatorio</button>
</div>
<div class="result" id="lineResult" style="text-align:center"></div>
</div>
</section>

<!-- COMPARAR ENTEROS -->
<section class="chapter">
<h2 class="chapter-title">⚖️ Compara enteros</h2>
<div class="interactive">
<h3>Selecciona la relación correcta:</h3>
<div style="text-align:center;margin:1rem 0">
<p style="font-size:1.5rem;font-weight:700;margin-bottom:1rem" id="enteroDisplay"></p>
<div style="display:flex;gap:.5rem;justify-content:center;flex-wrap:wrap" id="enteroButtons"></div>
</div>
<div class="result" id="interactiveResult"></div>
</div>
</section>

<!-- EJERCICIOS VARIADOS -->
<section class="chapter">
<h2 class="chapter-title">📝 Ejercicios</h2>
<div class="exercises">

<!-- TIPO 1: QUIZ — Comparar enteros -->
<div class="exercise">
<p>🔢 <strong>Ejercicio 1</strong> (Quiz): ¿Cuál de estas comparaciones es <strong>correcta</strong>?</p>
<div class="quiz-options">
<button class="quiz-btn" onclick="checkQuizMulti(this, false)">\\(-3 > -1\\)</button>
<button class="quiz-btn" onclick="checkQuizMulti(this, true)">\\(-8 < -2\\)</button>
<button class="quiz-btn" onclick="checkQuizMulti(this, false)">\\(-5 > 0\\)</button>
<button class="quiz-btn" onclick="checkQuizMulti(this, false)">\\(1 < -1\\)</button>
</div>
</div>

<!-- TIPO 2: COMPLETAR HUECO — Valor absoluto -->
<div class="exercise">
<p>📏 <strong>Ejercicio 2</strong> (Completar hueco): El valor absoluto de \\(-12\\) es \\(|-12| = \\) ___</p>
<input type="number" id="absInput" placeholder="?">
<button class="check-btn" onclick="checkAbs()">Comprobar</button>
<div class="result" id="absResult" style="display:none"></div>
</div>

<!-- TIPO 3: VERDADERO/FALSO — Propiedades del cero -->
<div class="exercise">
<p>✅❌ <strong>Ejercicio 3</strong> (Verdadero o Falso): "El cero es un número positivo porque es mayor que todos los negativos."</p>
<div class="quiz-options">
<button class="quiz-btn" onclick="checkVF(this, false)">Verdadero</button>
<button class="quiz-btn" onclick="checkVF(this, true)">Falso</button>
</div>
</div>

<!-- TIPO 4: PROBLEMA — Temperatura -->
<div class="exercise">
<p>🌡️ <strong>Ejercicio 4</strong> (Problema): En una ciudad, la temperatura a las 6:00 es \\(3°\\text{C}\\). A medianoche baja \\(8\\) grados. ¿Cuál es la temperatura a medianoche?</p>
<input type="number" id="tempInput" placeholder="°C">
<button class="check-btn" onclick="checkTemp()">Comprobar</button>
<div class="result" id="tempResult" style="display:none"></div>
</div>

<!-- TIPO 5: QUIZ — Ordenar en la recta -->
<div class="exercise">
<p>📊 <strong>Ejercicio 5</strong> (Quiz): ¿Qué número está más a la izquierda en la recta numérica?</p>
<div class="quiz-options">
<button class="quiz-btn" onclick="checkQuizMulti(this, false)">\\(0\\)</button>
<button class="quiz-btn" onclick="checkQuizMulti(this, true)">\\(-15\\)</button>
<button class="quiz-btn" onclick="checkQuizMulti(this, false)">\\(-3\\)</button>
<button class="quiz-btn" onclick="checkQuizMulti(this, false)">\\(5\\)</button>
</div>
</div>

<!-- TIPO 6: COMPLETAR HUECO — Altitud -->
<div class="exercise">
<p>🏔️ <strong>Ejercicio 6</strong> (Completar hueco): El Mar Muerto está a \\(-430\\) m y el Everest a \\(+8849\\) m. La diferencia de altitud es \\(8849 - (-430) = 8849 + 430 = \\) ___ metros.</p>
<input type="number" id="altitudeInput" placeholder="metros">
<button class="check-btn" onclick="checkAltitude()">Comprobar</button>
<div class="result" id="altitudeResult" style="display:none"></div>
</div>

<!-- TIPO 7: VERDADERO/FALSO — Error común -->
<div class="exercise">
<p>✅❌ <strong>Ejercicio 7</strong> (Verdadero o Falso): "El número \\(-1\\) es el entero negativo más grande."</p>
<div class="quiz-options">
<button class="quiz-btn" onclick="checkVF(this, true)">Verdadero</button>
<button class="quiz-btn" onclick="checkVF(this, false)">Falso</button>
</div>
</div>

<!-- TIPO 8: PROBLEMA — Parking -->
<div class="exercise">
<p>🏢 <strong>Ejercicio 8</strong> (Problema): Estás en la planta \\(3\\) de un parking. Bajas \\(5\\) plantas. ¿En qué planta quedas?</p>
<p style="font-size:.9rem;color:var(--gris);margin-bottom:.5rem">Pista: La planta \\(-2\\) es el sótano 2. La operación es \\(3 + (-5)\\)</p>
<input type="number" id="elevatorInput" placeholder="Tu respuesta">
<button class="check-btn" onclick="checkElevator()">Comprobar</button>
<div class="result" id="elevatorResult" style="display:none"></div>
</div>

<!-- TIPO 9: QUIZ — Valor absoluto -->
<div class="exercise">
<p>📐 <strong>Ejercicio 9</strong> (Quiz): ¿Cuál de estos números tiene el <strong>mayor valor absoluto</strong>?</p>
<div class="quiz-options">
<button class="quiz-btn" onclick="checkQuizMulti(this, false)">\\(-4\\)</button>
<button class="quiz-btn" onclick="checkQuizMulti(this, true)">\\(-9\\)</button>
<button class="quiz-btn" onclick="checkQuizMulti(this, false)">\\(7\\)</button>
<button class="quiz-btn" onclick="checkQuizMulti(this, false)">\\(0\\)</button>
</div>
</div>

<!-- TIPO 10: COMPLETAR HUECO — Ordenar -->
<div class="exercise">
<p>📊 <strong>Ejercicio 10</strong> (Completar hueco): Ordena de menor a mayor: \\(2, \\;-6, \\;0, \\;-1, \\;4\\).<br>
El segundo número de la lista ordenada es: ___</p>
<input type="number" id="sortInput" placeholder="nº2">
<button class="check-btn" onclick="checkSort()">Comprobar</button>
<div class="result" id="sortResult" style="display:none"></div>
</div>

</div>
</section>

<!-- RESUMEN INTERACTIVO -->
<section class="chapter">
<h2 class="chapter-title">🧠 Autoevaluación rápida</h2>
<div class="interactive">
<h3>¿Pondrías el \\(-7\\) a la izquierda o a la derecha del \\(-2\\)?</h3>
<div class="quiz-options">
<button class="quiz-btn" onclick="checkSelfEval(this, true)">A la izquierda (es menor)</button>
<button class="quiz-btn" onclick="checkSelfEval(this, false)">A la derecha (es mayor)</button>
</div>
<div class="result" id="selfEvalResult" style="display:none"></div>
</div>
</section>

<!-- RESUMEN -->
<div class="summary">
<h3>📋 Resumen de lo aprendido</h3>
<ul>
<li>Los enteros (\\(\\mathbb{Z}\\)) = \\(\\{\\ldots, -3, -2, -1, 0, 1, 2, 3, \\ldots\\}\\)</li>
<li>En la recta: a la izquierda = menor, a la derecha = mayor</li>
<li>Todo positivo \\(> 0 >\\) todo negativo</li>
<li>Entre negativos: el de menor valor absoluto es MAYOR (\\(-1 > -10\\))</li>
<li>El valor absoluto \\(|x|\\) es la distancia al cero: \\(|-7| = 7\\)</li>
<li>Temperatura y altitud son ejemplos reales de enteros</li>
<li>\\(0\\) NO es positivo ni negativo: es el punto de referencia</li>
<li>Para restar enteros: \\(a - (-b) = a + b\\) (menos por menos = más)</li>
</ul>
</div>

<nav class="nav">
<a href="#">← Anterior</a>
<a href="s07-1eso.html" style="color:#94a3b8;font-size:0.85rem">📋 Índice del nivel</a>
<a href="eso1-3-proporcionalidad.html">Siguiente: Operaciones con enteros →</a>
</nav>
</main>
<footer class="footer">
Hecho con ❤️ por David Antizar
</footer>
'''

# Construir nuevo HTML
new_html = content[:head_end] + '\n' + new_body + '\n' + content[js_end:]

with open(input_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"\n✅ Archivo reescrito: {len(new_html)} caracteres")
