# 📐 MEGA-PLAN 2: Mejora Continua Automatizada

## Objetivo

**DeSumarIntegrar** debe convertirse en el recurso definitivo para aprender matemáticas: desde contar hasta universidad. El MEGA-PLAN2 implementa un sistema de mejora continua que procesa **un tema cada 30 minutos** vía cron, mejorando:

- 📝 **Más texto explicativo** — Cada concepto explicado con intuición, no solo fórmulas
- 🧪 **Más ejercicios** — De 5 a 15 ejercicios por tema, con dificultad progresiva
- 🌍 **Casos reales** — Ejemplos de la vida cotidiana que enganchen
- 🔗 **Conexiones** — Vínculos entre temas relacionados
- 📊 **Visualizaciones** — Gráficos interactivos donde falten

---

## 🗂️ Sistema de Progreso

El archivo `progress.json` trackea el estado de cada tema:

```json
{
  "last_improved": "s01-3-sumar-hasta-10",
  "last_run": "2026-06-09T15:00:00Z",
  "total_runs": 0,
  "topics": {
    "s01-3-sumar-hasta-10": {
      "status": "pending",
      "improvements": [],
      "score": 0,
      "last_improved": null
    }
  }
}
```

### Estados de un tema

| Estado | Significado |
|--------|-------------|
| `pending` | Nunca mejorado |
| `improved_1` | Primera ronda: +ejercicios, +texto |
| `improved_2` | Segunda ronda: +visualizaciones, +casos reales |
| `improved_3` | Tercera ronda: +conexiones entre temas, +problemas avanzados |
| `complete` | Tema considerado completo |

---

## 📋 Lista Completa de Temas (107 archivos)

### Prioridad ALTA — Temas基础icos con menos contenido

| # | Archivo | Nivel | Prioridad | Razón |
|---|---------|-------|-----------|-------|
| 1 | s01-1primaria.html | 1º Primaria | 🔴 | Base del aprendizaje |
| 2 | s01-2primaria.html | 1º Primaria | 🔴 | Base del aprendizaje |
| 3 | s01-3primaria.html | 1º Primaria | 🔴 | Base del aprendizaje |
| 4 | s01-4primaria.html | 1º Primaria | 🔴 | Base del aprendizaje |
| 5 | s01-5primaria.html | 1º Primaria | 🔴 | Base del aprendizaje |
| 6 | s01-6primaria.html | 1º Primaria | 🔴 | Base del aprendizaje |
| 7 | s01-7primaria.html | 1º Primaria | 🔴 | Base del aprendizaje |
| 8 | s01-8primaria.html | 1º Primaria | 🔴 | Base del aprendizaje |
| 9 | s01-9primaria.html | 1º Primaria | 🔴 | Base del aprendizaje |
| 10 | s01-10primaria.html | 1º Primaria | 🔴 | Base del aprendizaje |

### Prioridad ALTA — Primaria fundamental

| # | Archivo | Nivel | Prioridad |
|---|---------|-------|-----------|
| 11 | s02-1primaria.html | 2º Primaria | 🔴 |
| 12 | s02-2primaria.html | 2º Primaria | 🔴 |
| 13 | s02-3primaria.html | 2º Primaria | 🔴 |
| 14 | s02-4primaria.html | 2º Primaria | 🔴 |
| 15 | s02-5primaria.html | 2º Primaria | 🔴 |
| 16 | s02-6primaria.html | 2º Primaria | 🔴 |
| 17 | s02-7primaria.html | 2º Primaria | 🔴 |
| 18 | s03-3primaria.html | 3º Primaria | 🔴 |
| 19 | s04-4primaria.html | 4º Primaria | 🟡 |
| 20 | s05-5primaria.html | 5º Primaria | 🟡 |
| 21 | s06-6primaria.html | 6º Primaria | 🟡 |
| 22 | s06-10-repasos-primaria.html | 6º Primaria | 🟡 |

### Prioridad MEDIA — ESO

| # | Archivo | Nivel | Prioridad |
|---|---------|-------|-----------|
| 23 | eso1-1-numeros-enteros.html | ESO 1º | 🟡 |
| 24 | eso1-3-proporcionalidad.html | ESO 1º | 🟡 |
| 25 | eso1-5-intro-algebra.html | ESO 1º | 🟡 |
| 26 | eso1-7-estadistica-probabilidad.html | ESO 1º | 🟡 |
| 27 | eso2-1-ecuaciones-1grado.html | ESO 2º | 🟡 |
| 28 | eso2-3-teorema-tales.html | ESO 2º | 🟡 |
| 29 | eso2-5-funciones-intro.html | ESO 2º | 🟡 |
| 30 | eso2-7-circunferencia-circulo.html | ESO 2º | 🟡 |
| 31 | eso2-9-probabilidad.html | ESO 2º | 🟡 |
| 32 | s07-1eso.html | ESO | 🟡 |
| 33 | s08-2-3eso.html | ESO | 🟡 |

### Prioridad MEDIA — Temas específicos primaria

| # | Archivo | Nivel | Prioridad |
|---|---------|-------|-----------|
| 34 | s01-1-contar-0-10.html | 1º Primaria | 🟡 |
| 35 | s01-2-contar-10-100.html | 1º Primaria | 🟡 |
| 36 | s01-3-sumar-hasta-10.html | 1º Primaria | 🟡 |
| 37 | s01-4-sumar-hasta-20.html | 1º Primaria | 🟡 |
| 38 | s01-5-restar-hasta-10.html | 1º Primaria | 🟡 |
| 39 | s01-6-restar-hasta-20.html | 1º Primaria | 🟡 |
| 40 | s01-7-figuras-basicas.html | 1º Primaria | 🟡 |
| 41 | s01-8-medidas-tamano-peso.html | 1º Primaria | 🟡 |
| 42 | s01-9-medidas-longitud.html | 1º Primaria | 🟡 |
| 43 | s01-10-patrones.html | 1º Primaria | 🟡 |
| 44 | s02-1-sumas-llevadas.html | 2º Primaria | 🟡 |
| 45 | s02-2-restas-llevadas.html | 2º Primaria | 🟡 |
| 46 | s02-3-intro-multiplicacion.html | 2º Primaria | 🟡 |
| 47 | s02-4-tablas-1-5.html | 2º Primaria | 🟡 |
| 48 | s02-5-tablas-6-9.html | 2º Primaria | 🟡 |
| 49 | s02-6-longitud-peso.html | 2º Primaria | 🟡 |
| 50 | s02-7-dinero.html | 2º Primaria | 🟡 |
| 51 | s03-1-mult-dos-cifras.html | 3º Primaria | 🟡 |
| 52 | s03-2-division.html | 3º Primaria | 🟡 |
| 53 | s03-3-intro-fracciones.html | 3º Primaria | 🟡 |
| 54 | s03-4-comparar-fracciones.html | 3º Primaria | 🟡 |
| 55 | s03-5-perimetro.html | 3º Primaria | 🟡 |
| 56 | s03-6-estadistica.html | 3º Primaria | 🟡 |

### Prioridad MEDIA — 4º-6º Primaria

| # | Archivo | Nivel | Prioridad |
|---|---------|-------|-----------|
| 57 | s04-1-fracciones-equivalentes.html | 4º Primaria | 🟡 |
| 58 | s04-2-mult-3-cifras.html | 4º Primaria | 🟡 |
| 59 | s04-3-division-2-cifras.html | 4º Primaria | 🟡 |
| 60 | s04-4-fracciones-equivalentes.html | 4º Primaria | 🟡 |
| 61 | s04-5-decimales-intro.html | 4º Primaria | 🟡 |
| 62 | s04-6-areas.html | 4º Primaria | 🟡 |
| 63 | s04-7-capacidades.html | 4º Primaria | 🟡 |
| 64 | s04-8-problemas-1-paso.html | 4º Primaria | 🟡 |
| 65 | s05-1-sumar-decimales.html | 5º Primaria | 🟡 |
| 66 | s05-3-mult-decimales.html | 5º Primaria | 🟡 |
| 67 | s05-5-areas-perimetros.html | 5º Primaria | 🟡 |
| 68 | s05-7-porcentajes.html | 5º Primaria | 🟡 |
| 69 | s05-9-tiempo-calendarios.html | 5º Primaria | 🟡 |
| 70 | s06-1-operaciones-grandes.html | 6º Primaria | 🟡 |
| 71 | s06-3-fracciones-operar.html | 6º Primaria | 🟡 |
| 72 | s06-5-proporcionalidad.html | 6º Primaria | 🟡 |
| 73 | s06-7-areas-compuestas.html | 6º Primaria | 🟡 |
| 74 | s06-9-intro-algebra.html | 6º Primaria | 🟡 |

### Prioridad MEDIA — Estadística

| # | Archivo | Nivel | Prioridad |
|---|---------|-------|-----------|
| 75 | s04-1-estadistica-conceptos-basicos.html | Estadística | 🟡 |
| 76 | s04-2-estadistica-distribuciones-frecuencia.html | Estadística | 🟡 |
| 77 | s04-3-estadistica-tendencia-central.html | Estadística | 🟡 |
| 78 | s04-4-estadistica-dispersion.html | Estadística | 🟡 |
| 79 | s04-5-estadistica-distribuciones-discretas.html | Estadística | 🟡 |
| 80 | s04-6-estadistica-distribuciones-continuas.html | Estadística | 🟡 |
| 81 | s04-7-estadistica-correlacion-regresion.html | Estadística | 🟡 |
| 82 | s04-8-estadistica-muestreo-estimacion.html | Estadística | 🟡 |
| 83 | s04-9-estadistica-hipotesis.html | Estadística | 🟡 |
| 84 | s04-10-estadistica-repaso.html | Estadística | 🟡 |
| 85 | s05-10-estadistica-avanzada.html | Estadística | 🟡 |

### Prioridad BAJA — Bachillerato

| # | Archivo | Nivel | Prioridad |
|---|---------|-------|-----------|
| 86 | s09-bachiller.html | Bachiller | 🟢 |
| 87 | s09-1-bachiller-limites.html | Bachiller | 🟢 |
| 88 | s09-2-bachiller-continuidad-derivadas.html | Bachiller | 🟢 |
| 89 | s09-3-bachiller-reglas-derivacion.html | Bachiller | 🟢 |
| 90 | s09-4-bachiller-aplicaciones-derivadas.html | Bachiller | 🟢 |
| 91 | s09-5-bachiller-integrales-indefinidas.html | Bachiller | 🟢 |
| 92 | s09-6-bachiller-integrales-definidas.html | Bachiller | 🟢 |
| 93 | s09-7-bachiller-aplicaciones-integrales.html | Bachiller | 🟢 |
| 94 | s09-8-bachiller-probabilidad-avanzada.html | Bachiller | 🟢 |
| 95 | s09-9-bachiller-distribuciones-combinadas.html | Bachiller | 🟢 |
| 96 | s09-10-bachiller-repaso.html | Bachiller | 🟢 |

### Prioridad BAJA — Universidad

| # | Archivo | Nivel | Prioridad |
|---|---------|-------|-----------|
| 97 | s10-1carrera.html | Universidad | 🟢 |
| 98 | s10-1-carrera-limites-multivariable.html | Universidad | 🟢 |
| 99 | s10-2-carrera-derivadas-parciales.html | Universidad | 🟢 |
| 100 | s10-3-carrera-integrales-multiples.html | Universidad | 🟢 |
| 101 | s10-4-carrera-edos-primer-orden.html | Universidad | 🟢 |
| 102 | s10-5-carrera-edos-segundo-orden.html | Universidad | 🟢 |
| 103 | s10-6-carrera-series-fourier.html | Universidad | 🟢 |
| 104 | s10-7-carrera-espacios-vectoriales.html | Universidad | 🟢 |
| 105 | s10-8-carrera-autovalores.html | Universidad | 🟢 |
| 106 | s10-9-carrera-transformaciones-lineales.html | Universidad | 🟢 |
| 107 | s10-10-carrera-repaso.html | Universidad | 🟢 |

---

## 🔄 Flujo del Cron (cada 30 minutos)

```
┌─────────────────────────────────────────────────────────────┐
│  CRON JOB: Mejora Continua DeSumarIntegrar                  │
│  Frecuencia: cada 30 minutos                                │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  1. Leer progress.json  │
              └────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  2. Seleccionar tema    │
              │     (por prioridad)     │
              └────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  3. Leer HTML actual    │
              └────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  4. Analizar déficits: │
              │  - Nº ejercicios       │
              │  - Nº explicaciones     │
              │  - Visualizaciones      │
              │  - Casos reales         │
              │  - Conexiones           │
              └────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  5. Generar mejoras:   │
              │  - Añadir ejercicios   │
              │  - Mejorar texto       │
              │  - Añadir examples     │
              └────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  6. Escribir HTML       │
              │     actualizado         │
              └────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  7. Actualizar          │
              │     progress.json       │
              └────────────────────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  8. Git commit + push   │
              └────────────────────────┘
```

---

## 📊 Métricas de Calidad

Cada tema se evalúa en estas dimensiones (0-10):

| Dimensión | Qué mide | Cómo se mide |
|-----------|----------|--------------|
| **Ejercicios** | Cantidad y variedad | Contar ejercicios interactivos |
| **Texto** | Explicaciones claras | Contar párrafos explicativos |
| **Visual** | Gráficos y animaciones | Contar plotly/canvas |
| **Real** | Casos de uso real | Contar "ejemplo real" / "vida real" |
| **Conexiones** | Vínculos entre temas | Contar links a otras sesiones |
| **Difficulty** | Rango de dificultad | Ejercicios fáciles/medios/difíciles |

### Score objetivo por tema: ≥ 7/10 en todas las dimensiones

---

## 🎯 Criterios de Mejora por Nivel

### Primaria (s01-s06)
- ✅ Mínimo 8 ejercicios interactivos
- ✅ Emojis y elementos visuales
- ✅ Explicaciones con analogías cotidianas
- ✅ Botones de "mostrar solución"
- ✅ Barra de progreso

### ESO (eso1, eso2, s07, s08)
- ✅ Mínimo 10 ejercicios
- ✅ Fórmulas con KaTeX
- ✅ Al menos 1 gráfico Plotly
- ✅ Tablas de resumen
- ✅ Conexiones con temas anteriores

### Bachiller (s09)
- ✅ Mínimo 12 ejercicios
- ✅ Múltiples visualizaciones Plotly
- ✅ Demostraciones conceptuales
- ✅ Problemas de aplicación real
- ✅ Ejercicios de examen tipo

### Universidad (s10)
- ✅ Mínimo 10 ejercicios
- ✅ Gráficos 3D interactivos
- ✅ Conexiones interdisciplinares
- ✅ Problemas de ingeniería/ciencia
- ✅ Referencias a aplicaciones reales

---

## 📈 Estimación de Progreso

- **107 temas** × **4 rondas de mejora** = **428 mejoras totales**
- **1 mejora cada 30 min** = **24 mejoras/día**
- **Tiempo estimado completo:** ~18 días
- **Primer pase (todas las mejoras nivel 1):** ~4.5 días

---

## 🚀Inicio

El cron se activa inmediatamente y empieza por los temas de **Prioridad ALTA** (primaria básica), que son la base de todo el aprendizaje.

**Hecho con ❤️ por David Antizar**
