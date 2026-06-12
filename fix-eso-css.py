#!/usr/bin/env python3
"""
Estandarizar CSS de archivos ESO (eso1-*, eso2-*, s07-*, s08-*)
Añade clases CSS faltantes para que todos los archivos ESO tengan
el mismo nivel de calidad visual que los de Primaria y Bachiller.
"""

import os
import re

math_dir = "/root/workspace/DeSumarIntegrar"

# CSS blocks to add for ESO files
# These are the missing CSS classes that need to be added
ESO_EXTRA_CSS = """
/* Feedback para ejercicios */
.feedback{display:inline-block;padding:.3rem .8rem;border-radius:6px;font-weight:600;margin-top:.5rem}
.feedback.correct{color:#065f46;background:var(--verde-claro)}
.feedback.incorrect{color:#991b1b;background:var(--rojo-claro)}

/* Conexión con conocimiento previo */
.connection-box{background:var(--pura-claro);border:2px dashed var(--pura);border-radius:10px;padding:1rem;margin:1rem 0}
.connection-box strong{color:var(--pura)}

/* Indicador de pasos */
.step-indicator{display:inline-flex;align-items:center;gap:.3rem;background:var(--azul-claro);padding:.2rem .6rem;border-radius:12px;font-size:.8rem;font-weight:600;color:var(--azul);margin:.2rem}
.step-dot{width:8px;height:8px;border-radius:50%;background:var(--azul);display:inline-block}

/* Badge de caso real */
.real-world-badge{display:inline-block;background:var(--naranja);color:#fff;padding:.2rem .6rem;border-radius:12px;font-size:.75rem;font-weight:600}

/* Contenedor SVG */
.svg-container{background:#f8fafc;border-radius:12px;padding:1.5rem;margin:1rem 0;text-align:center}

/* Input de ejercicio */
.exercise-input input:focus{outline:none;border-color:var(--azul)}

/* Responsive mejorado */
@media(max-width:640px){
  .header h1{font-size:1.4rem}
  .chapter-title{font-size:1.1rem}
}
"""

# CSS blocks to add for Bachiller/Uni files
BACH_EXTRA_CSS = """
/* Conexión con conocimiento previo */
.connection-box{background:var(--pura-claro);border:2px dashed var(--pura);border-radius:10px;padding:1rem;margin:1rem 0}
.connection-box strong{color:var(--pura)}

/* Indicador de pasos */
.step-indicator{display:inline-flex;align-items:center;gap:.3rem;background:var(--azul-claro);padding:.2rem .6rem;border-radius:12px;font-size:.8rem;font-weight:600;color:var(--azul);margin:.2rem}
.step-dot{width:8px;height:8px;border-radius:50%;background:var(--azul);display:inline-block}

/* Badge de caso real */
.real-world-badge{display:inline-block;background:var(--naranja);color:#fff;padding:.2rem .6rem;border-radius:12px;font-size:.75rem;font-weight:600}

/* Contenedor SVG */
.svg-container{background:#f8fafc;border-radius:12px;padding:1.5rem;margin:1rem 0;text-align:center}
"""

def fix_eso_file(filepath, filename):
    """Fix CSS for an ESO file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # Check if extra CSS already exists
    if '.connection-box' in content:
        print(f"  ✅ {filename}: ya tiene CSS completo")
        return False
    
    # Extract current CSS
    css_match = re.search(r'(<style>.*?</style>)', content, re.DOTALL)
    if not css_match:
        print(f"  ❌ {filename}: no se encontró bloque <style>")
        return False
    
    old_css = css_match.group(0)
    new_css = old_css.replace('</style>', ESO_EXTRA_CSS + '</style>')
    
    # Replace CSS block
    content = content.replace(old_css, new_css)
    
    # Fix responsive: ensure @media exists with proper rules
    if '@media(max-width:640px)' in content:
        # Check if chapter-title is in the media query
        media_match = re.search(r'@media\(max-width:640px\)\{([^}]+)\}', content)
        if media_match:
            media_content = media_match.group(1)
            if '.chapter-title' not in media_content:
                # Add chapter-title to media query
                new_media = '@media(max-width:640px){\n  .header h1{font-size:1.4rem}\n  .chapter-title{font-size:1.1rem}\n}'
                content = content.replace(media_match.group(0), new_media)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    return content != original

def fix_bach_file(filepath, filename):
    """Fix CSS for a Bachiller/Uni file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original = content
    
    # Check if extra CSS already exists
    if '.connection-box' in content:
        print(f"  ✅ {filename}: ya tiene CSS completo")
        return False
    
    # Extract current CSS
    css_match = re.search(r'(<style>.*?</style>)', content, re.DOTALL)
    if not css_match:
        print(f"  ❌ {filename}: no se encontró bloque <style>")
        return False
    
    old_css = css_match.group(0)
    new_css = old_css.replace('</style>', BACH_EXTRA_CSS + '</style>')
    
    # Replace CSS block
    content = content.replace(old_css, new_css)
    
    with open(filepath, 'w') as f:
        f.write(content)
    
    return content != original


if __name__ == '__main__':
    # Fix ESO files
    print("=== FIXING ESO FILES ===")
    eso_files = [
        'eso1-1-numeros-enteros.html',
        'eso1-3-proporcionalidad.html',
        'eso1-5-intro-algebra.html',
        'eso1-7-estadistica-probabilidad.html',
        'eso2-1-ecuaciones-1grado.html',
        'eso2-3-teorema-tales.html',
        'eso2-5-funciones-intro.html',
        'eso2-7-circunferencia-circulo.html',
        'eso2-9-probabilidad.html',
        's01-8-medidas-tamano-peso.html',
        's02-6-longitud-peso.html',
        's07-1eso.html',
        's08-2-3eso.html',
    ]
    
    changed = 0
    for f in eso_files:
        path = os.path.join(math_dir, f)
        if os.path.exists(path):
            if fix_eso_file(path, f):
                changed += 1
                print(f"  ✏️ {f}: CSS mejorado")
            else:
                print(f"  - {f}: sin cambios")
        else:
            print(f"  ❌ {f}: NO EXISTE")
    
    print(f"\n  Total ESO cambiados: {changed}/{len(eso_files)}")
    
    # Fix Bachiller files
    print("\n=== FIXING BACHILLER FILES ===")
    bach_files = [f for f in os.listdir(math_dir) if f.startswith('s09') and f.endswith('.html')]
    
    changed = 0
    for f in sorted(bach_files):
        path = os.path.join(math_dir, f)
        if os.path.exists(path):
            if fix_bach_file(path, f):
                changed += 1
                print(f"  ✏️ {f}: CSS mejorado")
            else:
                print(f"  - {f}: sin cambios")
    
    print(f"\n  Total Bachiller cambiados: {changed}/{len(bach_files)}")
    
    # Fix Universidad files
    print("\n=== FIXING UNIVERSIDAD FILES ===")
    uni_files = [f for f in os.listdir(math_dir) if f.startswith('s10') and f.endswith('.html')]
    
    changed = 0
    for f in sorted(uni_files):
        path = os.path.join(math_dir, f)
        if os.path.exists(path):
            if fix_bach_file(path, f):
                changed += 1
                print(f"  ✏️ {f}: CSS mejorado")
            else:
                print(f"  - {f}: sin cambios")
    
    print(f"\n  Total Universidad cambiados: {changed}/{len(uni_files)}")
    
    print(f"\n=== DONE ===")
