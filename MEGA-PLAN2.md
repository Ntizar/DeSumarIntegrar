# 📐 MEGA-PLAN 2: Mejora Continua — Calidad sobre Cantidad

## Filosofía

**No se trata de añadir más ejercicios. Se trata de que cada tema enseñe mejor.**

Un tema mejorado debe lograr que el alumno:
1. **Entienda el concepto** (no solo memorice la fórmula)
2. **Sepa cuándo usarlo** (vida real, no ejercicios abstractos)
3. **No se aburra** (variedad, no repetición)
4. **Pueda practicar** (ejercicios que aporten, no rellenar)

---

## ❌ Lo que NO se debe hacer

- Añadir 10 ejercicios del mismo tipo (5+5=?, 3+2=?, 4+1=?)
- Copiar la misma estructura en todos los temas
- Añadir dibujos solo por cumplir
- Ejercicios con errores (opciones duplicadas, respuestas mal)
- Texto largo sin estructura (muro de palabras)

## ✅ Lo que SÍ se debe hacer

### 1. Ejercicios variados (máximo 5-8 por tema)

Cada ejercicio debe ser de un tipo diferente:

| Tipo | Ejemplo | Para qué sirve |
|------|---------|----------------|
| **Completar** | "3 + ___ = 7" | Entender la operación |
| **Verdadero/Falso** | "5 + 3 = 9 → Falso" | Detectar errores comunes |
| **Ordenar** | "Ordena: 8, 3, 12, 1" | Comparar números |
| **Problema** | "Ana tiene 5 manzanas..." | Contextualizar |
| **Quiz visual** | Botones con opciones | Repaso rápido |
| **Canvas interactivo** | Arrastrar, contar | Vivir la experiencia |

**Regla: Si añades un ejercicio, debe ser diferente al anterior.**

### 2. Texto explicativo con estructura

Cada explicación debe seguir este patrón:
```
📖 CONCEPTO
┌─────────────────────────────────────┐
│ 1. ¿Qué es? (1 frase clara)        │
│ 2. ¿Para qué sirve? (ejemplo real) │
│ 3. ¿Cómo se hace? (paso a paso)     │
│ 4. ¿Qué error comete la gente?     │
└─────────────────────────────────────┘
```

### 3. Visualizaciones SOLO si aportan

| Nivel | ¿Cuándo añadir gráfico? |
|-------|-------------------------|
| Primaria | Línea numérica, conteo visual, agrupar objetos |
| ESO | Funciones, proporciones, estadística básica |
| Bachiller | Derivadas, integrales, distribuciones |
| Universidad | 3D, campos vectoriales, ondas |

**No añadir Plotly a "sumar hasta 10" — no aporta nada.**

### 4. Casos reales que enganchen

| Malo ❌ | Bueno ✅ |
|---------|----------|
| "Sumar sirve para contar" | "Si tienes 3 caramelos y te dan 2, ¿cuántos tienes?" |
| "Las fracciones son partes" | "Cortas una pizza en 8 trozos y comes 3. ¿Qué fracción comiste?" |
| "La estadística es importante" | "Tu nota media este trimestre es 7.5. ¿Necesitas subir para el siguiente?" |

---

## 📋 Criterios de calidad por tema

### Puntuación (0-10 por dimensión)

| Dimensión | 0-3 (Malo) | 4-6 (Aceptable) | 7-10 (Excelente) |
|-----------|------------|-----------------|------------------|
| **Ejercicios** | Muchos iguales | Algunos variados | 5-8 tipos diferentes |
| **Texto** | Muro de palabras | Estructura básica | Concepto → Ejemplo → Error |
| **Real** | Genérico | 1-2 ejemplos | Ejemplos que enganchan |
| **Visual** | Decorativo | Informativo | Interactivo y útil |

### Score mínimo para pasar a "mejorado": **6 en todas las dimensiones**

---

## 🔄 Flujo del Cron (ajustado)

```
1. Leer progress.json
2. Seleccionar tema (prioridad)
3. Leer HTML actual
4. ANALIZAR qué falta (no asumir)
5. SELECCIONAR mejoras concretas:
   - ¿Faltan tipos de ejercicio? → Añadir 2-3 tipos diferentes
   - ¿Falta texto explicativo? → Añadir 1 explicación clara
   - ¿Faltan casos reales? → Añadir 1-2 ejemplos cotidianos
   - ¿Falta visualización? → Añadir SOLO si aporta
6. ESCRIBIR mejoras (verificando calidad)
7. ACTUALIZAR progress.json
8. GIT commit
```

---

## 📊 Métricas de éxito

| Métrica | Objetivo |
|---------|----------|
| Ejercicios por tema | 5-8 (variedad, no cantidad) |
| Tipos de ejercicio | Mínimo 3 diferentes |
| Explicaciones | 1-2 claras, no 5 confusas |
| Casos reales | 1-2 que enganchen |
| Visualizaciones | Solo si aportan |

---

## 🎯 Resumen

**Antes:** "Añadir 10 ejercicios + 3 textos + 1 gráfico = mejorado"
**Ahora:** "Que el alumno entienda mejor = mejorado"

La cantidad no importa. Lo que importa es que cada elemento añadido **aporte algo nuevo** al aprendizaje.

---

**Hecho con ❤️ por David Antizar**
