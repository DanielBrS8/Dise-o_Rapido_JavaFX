#!/usr/bin/env python3
"""
Script auxiliar para analizar imágenes de mockups y generar
descripciones estructuradas para JavaFX/FXML.

Usa la API gratuita de Google Gemini para analizar las imágenes.

Requisitos:
    pip install google-generativeai Pillow

Uso:
    python analizar_mockup.py <imagen_mockup.png> [nombre_interfaz]

Ejemplo:
    python analizar_mockup.py mockups/login.jpg Login
    python analizar_mockup.py mockups/panel.png PanelPrincipal
"""

import sys
import os
from pathlib import Path

try:
    import google.generativeai as genai
    from PIL import Image
except ImportError:
    print("ERROR: Faltan dependencias. Ejecuta:")
    print("  pip install google-generativeai Pillow")
    sys.exit(1)


# ────────────────────────────────────────────────────────────
# CONFIGURACIÓN
# ────────────────────────────────────────────────────────────

# Obtener API key de variable de entorno o pedir al usuario
API_KEY = os.environ.get("GOOGLE_API_KEY", "")

PROMPT_ANALISIS = """
Analiza esta imagen de un mockup/boceto de interfaz gráfica de usuario.

Genera una descripción estructurada en formato Markdown orientada a JavaFX/FXML con:

## Formato requerido:

```markdown
# Interfaz: [Nombre descriptivo]

## Layout principal: [BorderPane/VBox/HBox/GridPane/AnchorPane/StackPane]
## Dimensiones sugeridas: [ancho x alto px]

## Estructura:
[Describe jerárquicamente cada zona/sección usando los contenedores JavaFX apropiados]

Para cada componente indica:
- Tipo JavaFX exacto (Button, Label, TextField, PasswordField, ComboBox, TableView, etc.)
- Texto visible o promptText
- Posición dentro del layout
- Propiedades relevantes (ancho, alto, alineación)

## Componentes con fx:id:
| ID | Tipo | Descripción |
|----|------|-------------|
| btnXxx | Button | Descripción |
| txtXxx | TextField | Descripción |
| lblXxx | Label | Descripción |
[... todos los componentes interactivos]
```

IMPORTANTE:
- Usa nombres de componentes JavaFX reales y correctos
- Sugiere los layouts más apropiados para cada zona
- Los fx:id deben seguir convención: btn, txt, lbl, tbl, col, chk, cmb, etc.
- Incluye TODOS los elementos visibles en el mockup
- Si hay zonas ambiguas, interprétalas de la forma más razonable
- No incluyas código FXML, solo la descripción estructurada
"""


def analizar_mockup(ruta_imagen: str, nombre_interfaz: str = "Interfaz") -> str:
    """
    Analiza una imagen de mockup y devuelve una descripción estructurada.

    Args:
        ruta_imagen: Ruta a la imagen del mockup
        nombre_interfaz: Nombre para la interfaz

    Returns:
        Descripción en Markdown
    """
    global API_KEY

    # Verificar API key
    if not API_KEY:
        API_KEY = input("Introduce tu API Key de Google Gemini (https://aistudio.google.com/apikey): ").strip()
        if not API_KEY:
            print("ERROR: Se necesita una API Key de Gemini.")
            print("Obtén una gratis en: https://aistudio.google.com/apikey")
            sys.exit(1)

    # Configurar Gemini
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")

    # Cargar imagen
    ruta = Path(ruta_imagen)
    if not ruta.exists():
        print(f"ERROR: No se encuentra la imagen: {ruta_imagen}")
        sys.exit(1)

    print(f"Analizando imagen: {ruta.name}...")
    imagen = Image.open(ruta)

    # Hacer la petición a Gemini
    prompt_completo = f"El nombre de esta interfaz es: {nombre_interfaz}\n\n{PROMPT_ANALISIS}"

    try:
        response = model.generate_content([prompt_completo, imagen])
        descripcion = response.text
    except Exception as e:
        print(f"ERROR al analizar la imagen: {e}")
        sys.exit(1)

    return descripcion


def guardar_descripcion(descripcion: str, nombre: str, carpeta_salida: str = "mockups") -> str:
    """Guarda la descripción en un fichero .md"""
    os.makedirs(carpeta_salida, exist_ok=True)
    nombre_fichero = f"descripcion-{nombre.lower().replace(' ', '-')}.md"
    ruta_salida = os.path.join(carpeta_salida, nombre_fichero)

    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(descripcion)

    return ruta_salida


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    ruta_imagen = sys.argv[1]
    nombre = sys.argv[2] if len(sys.argv) > 2 else Path(ruta_imagen).stem.capitalize()

    print("=" * 50)
    print("  Analizador de Mockups → JavaFX/FXML")
    print("=" * 50)
    print()

    # Analizar
    descripcion = analizar_mockup(ruta_imagen, nombre)

    # Mostrar resultado
    print()
    print("─" * 50)
    print("DESCRIPCIÓN GENERADA:")
    print("─" * 50)
    print(descripcion)
    print("─" * 50)

    # Guardar
    ruta_salida = guardar_descripcion(descripcion, nombre)
    print(f"\nDescripción guardada en: {ruta_salida}")
    print()
    print("SIGUIENTE PASO:")
    print(f"  Abre OpenCode y pide que genere el FXML a partir de '{ruta_salida}'")
    print("  Ejemplo de prompt para OpenCode:")
    print(f'  "Lee el fichero {ruta_salida} y genera el FXML correspondiente"')


if __name__ == "__main__":
    main()
