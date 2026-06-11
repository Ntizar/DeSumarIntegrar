# 📐 MEGA-PLAN 2 v2: Mejora Continua — DeSumarIntegrar

## Filosofía

**Cada tema debe hacer que el alumno entienda, no que memorice.**

Un tema mejorado debe lograr que el alumno:
1. **Entienda el concepto** (no solo memorice la fórmula)
2. **Sepa cuándo usarlo** (vida real, no ejercicios abstractos)
3. **Lo vea visualmente** (gráficos, animaciones, Manim)
4. **No se aburra** (variedad, no repetición)
5. **Pueda practicar** (ejercicios que aporten, no rellenar)

---

## 🚫 PROHIBIDO (Quality Gates)

| Regla | Consecuencia |
|-------|-------------|
| HTML sin `</html>` | ❌ Revertir cambio |
| Ejercicios rotos (onclick sin función) | ❌ Revertir cambio |
| Enlaces internos rotos | ❌ Revertir cambio |
| CSS sin clases del template | ❌ Revertir cambio |
| Título duplicado en otro archivo | ❌ Revertir cambio |
| 3 ejercicios seguidos del mismo tipo | ❌ No cuenta como mejora |
| Más de 3 ejercicios nuevos por tema | ❌ Calidad > cantidad |
| Plotly en temas de primaria básica | ❌ No aporta nada |

---

## ✅ Lo que SÍ se debe hacer

### 1. Ejercicios variados (máximo 5-8 por tema)

Cada ejercicio debe ser de un tipo DIFERENTE:

| Tipo | Ejemplo | Para qué sirve |
|------|---------|----------------|
| **Completar** | "3 + ___ = 7" | Entender la operación |
| **Verdadero/Falso** | "5 + 3 = 9 → Falso" | Detectar errores comunes |
| **Ordenar** | "Ordena: 8, 3, 12, 1" | Comparar números |
| **Problema** | "Ana tiene 5 manzanas..." | Contextualizar |
| **Quiz visual** | Botones con opciones | Repaso rápido |
| **Canvas interactivo** | Arrastrar, contar | Vivir la experiencia |
| **Emparejar** | Une cada operación con su resultado | Asociación visual |

**Regla:** Si añades un ejercicio, debe ser diferente al anterior.

### 2. Texto explicativo con estructura 4 pasos

```
📖 CONCEPTO
┌─────────────────────────────────────┐
│ 1. ¿Qué es? (1 frase clara)        │
│ 2. ¿Para qué sirve? (ejemplo real) │
│ 3. ¿Cómo se hace? (paso a paso)    │
│ 4. ¿Qué error comete la gente?     │
└─────────────────────────────────────┘
```

### 3. Visualizaciones que aporten

| Nivel | ¿Qué visualización? |
|-------|---------------------|
| Primaria | Línea numérica, conteo visual, agrupar objetos con emojis |
| ESO | Funciones con SVG, proporciones con gráficos, estadística básica |
| Bachiller | Derivadas/integrales con SVG animados, distribuciones |
| Universidad | Manim (3D, campos vectoriales, transformaciones) |

**NO añadir Plotly a "sumar hasta 10". NO añadir SVG decorativo sin propósito.**

### 4. Integración con Manim (temas avanzados)

Para temas de bachiller y universidad, usar animaciones Manim:

```html
<div class="manim-container">
  <video controls width="100%" poster="manim/thumb-derivada.png">
    <source src="manim/derivada-definicion.mp4" type="video/mp4">
  </video>
  <p class="manim-caption">📽️ La derivada como límite de la pendiente de la secante</p>
</div>
```

**Alternativa sin GPU:** SVG animados con CSS `@keyframes` y `<animate>`.

### 5. Casos reales que enganchen

| Malo ❌ | Bueno ✅ |
|---------|----------|
| "Sumar sirve para contar" | "Si tienes 3 caramelos y te dan 2, ¿cuántos tienes?" |
| "Las fracciones son partes" | "Cortas una pizza en 8 trozos y comes 3. ¿Qué fracción comiste?" |
| "La estadística es importante" | "Tu nota media este trimestre es 7.5. ¿Necesitas subir para el siguiente?" |

---

## 📋 Criterios de calidad (v2)

### Puntuación (0-10 por dimensión)

| Dimensión | 0-3 | 4-6 | 7-8 | 9-10 |
|-----------|-----|-----|-----|------|
| **Ejercicios** | Muchos iguales | Algunos variados | 4-5 tipos diferentes | 6+ con 4+ tipos |
| **Texto** | Muro de palabras | Estructura básica | 4 pasos claros | Paso a paso + ejemplos |
| **Real** | Genérico | 1-2 ejemplos | Ejemplos que enganchan | 3+ con datos reales |
| **Visual** | Decorativo | Informativo | Interactivo y útil | Manim/SVG animado |
| **Manim** | Sin animación | SVG animado simple | Manim video básico | Manim con interacción |
| **CSS** | Faltan 5+ clases | Faltan 2-4 | Falta 1 clase | 100% template |

### Score mínimo para pasar: **7 en todas las dimensiones**

---

## 🔄 Flujo del Cron (v2 — Cada 15 minutos)

```
CADA 15 MIN:
1. Leer INVENTARIO.md
2. Leer progress.json
3. SELECCIONAR 2-3 temas:
   - ROTAR entre niveles (no solo primaria)
   - Prioridad: menos mejorados → scores más bajos
   - EXCLUIR los ya mejorados hoy
4. Para CADA tema:
   a. BACKUP: cp tema.html tema.html.bak
   b. Leer HTML actual
   c. ANALIZAR qué falta
   d. MEJORAR 2-3 dimensiones
   e. QUALITY GATES:
      - HTML válido
      - Ejercicios funcionales (onclick existe)
      - Enlaces internos existen
      - CSS coherence 100%
      - Sin títulos duplicados
   f. Si FALLA → restaurar backup
   g. Si OK → progress.json + git commit
5. Auto-auditoría CSS
6. Resumen
```

---

## 📊 Métricas de éxito

| Métrica | Objetivo |
|---------|----------|
| Ejercicios por tema | 5-8 (variedad, no cantidad) |
| Tipos de ejercicio | Mínimo 3 diferentes |
| Explicaciones | 1-2 con estructura 4 pasos |
| Casos reales | 1-2 que enganchen |
| Visualizaciones | Solo si aportan |
| Manim (temas avanzados) | 1 animación por tema |
| CSS coherence | 100% con template base |
| HTML válido | 100% (quality gates) |

---

## 🎯 Resumen

**v1:** "Añadir 10 ejercicios + 3 textos + 1 gráfico = mejorado"
**v2:** "Mejorar 2-3 temas CADA 15 MINUTOS con quality gates estrictos"

Cada tema pasa por quality gates antes de commit. Si falla, se revierte. Calidad > cantidad.

---

**Hecho con ❤️ por David Antizar**