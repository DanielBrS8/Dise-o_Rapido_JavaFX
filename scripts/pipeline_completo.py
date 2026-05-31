#!/usr/bin/env python3
"""
Pipeline completo: Imagen de mockup → Descripción → FXML + Controller + App.java

Este script automatiza todo el proceso:
1. Analiza la imagen del mockup con Gemini (gratis)
2. Genera la descripción estructurada
3. Genera el fichero FXML
4. Genera el Controller Java vacío
5. Genera/actualiza la clase App lanzadora

Requisitos:
    pip install google-generativeai Pillow

Uso:
    python pipeline_completo.py <imagen.png> [NombreInterfaz] [paquete.java]

Ejemplos:
    python pipeline_completo.py mockups/login.jpg Login com.miapp
    python pipeline_completo.py mockups/panel.png PanelPrincipal com.miapp
    python pipeline_completo.py mockups/registro.jpg  (usa valores por defecto)
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

API_KEY = os.environ.get("GOOGLE_API_KEY", "")
DEFAULT_PACKAGE = "com.ejemplo"

PROMPT_ANALISIS = """
Analiza esta imagen de un mockup/boceto de interfaz gráfica.
Genera una descripción estructurada en Markdown para JavaFX.
Identifica: layout principal, componentes (tipo JavaFX exacto), posiciones, textos, y fx:ids.
Usa la plantilla:

# Interfaz: [Nombre]
## Layout principal: [Tipo]
## Dimensiones: [ancho x alto]
## Estructura: [jerárquica con contenedores y componentes]
## Componentes con fx:id: [tabla con ID, Tipo, Descripción]
"""

PROMPT_FXML = """
A partir de esta descripción de interfaz JavaFX, genera ÚNICAMENTE el contenido
de un fichero FXML válido.

REGLAS:
- Incluir todos los <?import?> necesarios al inicio
- Usar fx:controller="{package}.{name}Controller"
- Asignar fx:id a todos los componentes interactivos
- Usar estilos inline con style="-fx-..."
- Layout responsive con hgrow/vgrow donde sea necesario
- El FXML debe ser válido y abrirse en Scene Builder
- NO incluir explicaciones, SOLO el XML

Descripción de la interfaz:
{description}
"""

PROMPT_CONTROLLER = """
A partir de este FXML, genera ÚNICAMENTE el código Java de la clase Controller.

REGLAS:
- Package: {package}
- Nombre clase: {name}Controller
- Incluir @FXML para cada fx:id del FXML
- Método initialize() vacío
- NO incluir lógica de negocio
- NO incluir explicaciones, SOLO el código Java

FXML:
{fxml}
"""


def get_api_key():
    """Obtiene la API key de Gemini."""
    global API_KEY
    if not API_KEY:
        API_KEY = input(
            "\nIntroduce tu API Key de Google Gemini\n"
            "(Obtén una gratis en https://aistudio.google.com/apikey): "
        ).strip()
    if not API_KEY:
        print("ERROR: Se necesita una API Key.")
        sys.exit(1)
    return API_KEY


def paso1_analizar_imagen(model, ruta_imagen: str, nombre: str) -> str:
    """Paso 1: Analiza la imagen y genera descripción estructurada."""
    print("\n[1/4] Analizando imagen del mockup...")
    imagen = Image.open(ruta_imagen)
    prompt = f"Nombre de la interfaz: {nombre}\n\n{PROMPT_ANALISIS}"
    response = model.generate_content([prompt, imagen])
    descripcion = response.text
    print("      ✓ Descripción generada")
    return descripcion


def paso2_generar_fxml(model, descripcion: str, nombre: str, package: str) -> str:
    """Paso 2: Genera el FXML a partir de la descripción."""
    print("[2/4] Generando fichero FXML...")
    prompt = PROMPT_FXML.format(
        package=package,
        name=nombre,
        description=descripcion
    )
    response = model.generate_content(prompt)
    fxml = response.text

    # Limpiar posibles bloques de código markdown
    if "```xml" in fxml:
        fxml = fxml.split("```xml")[1].split("```")[0].strip()
    elif "```" in fxml:
        fxml = fxml.split("```")[1].split("```")[0].strip()

    print("      ✓ FXML generado")
    return fxml


def paso3_generar_controller(model, fxml: str, nombre: str, package: str) -> str:
    """Paso 3: Genera el Controller Java vacío."""
    print("[3/4] Generando Controller Java...")
    prompt = PROMPT_CONTROLLER.format(
        package=package,
        name=nombre,
        fxml=fxml
    )
    response = model.generate_content(prompt)
    controller = response.text

    # Limpiar posibles bloques de código markdown
    if "```java" in controller:
        controller = controller.split("```java")[1].split("```")[0].strip()
    elif "```" in controller:
        controller = controller.split("```")[1].split("```")[0].strip()

    print("      ✓ Controller generado")
    return controller


def paso4_generar_app(nombre: str, package: str, titulo: str) -> str:
    """Paso 4: Genera la clase App lanzadora."""
    print("[4/4] Generando clase App lanzadora...")
    nombre_fxml = nombre.lower().replace(" ", "-")
    app = f"""package {package};

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class App extends Application {{

    @Override
    public void start(Stage stage) throws Exception {{
        Parent root = FXMLLoader.load(getClass().getResource("/fxml/{nombre_fxml}.fxml"));
        stage.setTitle("{titulo}");
        stage.setScene(new Scene(root));
        stage.show();
    }}

    public static void main(String[] args) {{
        launch(args);
    }}
}}
"""
    print("      ✓ App.java generado")
    return app


def guardar_ficheros(nombre, package, descripcion, fxml, controller, app, base_dir="."):
    """Guarda todos los ficheros generados en la estructura del proyecto."""
    nombre_lower = nombre.lower().replace(" ", "-")
    package_path = package.replace(".", "/")

    # Rutas
    rutas = {
        "descripcion": f"{base_dir}/mockups/descripcion-{nombre_lower}.md",
        "fxml": f"{base_dir}/src/main/resources/fxml/{nombre_lower}.fxml",
        "controller": f"{base_dir}/src/main/java/{package_path}/{nombre}Controller.java",
        "app": f"{base_dir}/src/main/java/{package_path}/App.java",
    }

    # Crear directorios y guardar
    for clave, ruta in rutas.items():
        os.makedirs(os.path.dirname(ruta), exist_ok=True)

    contenidos = {
        "descripcion": descripcion,
        "fxml": fxml,
        "controller": controller,
        "app": app,
    }

    for clave, ruta in rutas.items():
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(contenidos[clave])

    return rutas


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    ruta_imagen = sys.argv[1]
    nombre = sys.argv[2] if len(sys.argv) > 2 else Path(ruta_imagen).stem.capitalize()
    package = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_PACKAGE

    # Verificar imagen
    if not os.path.exists(ruta_imagen):
        print(f"ERROR: No se encuentra: {ruta_imagen}")
        sys.exit(1)

    print("=" * 55)
    print("  Pipeline Completo: Mockup → JavaFX/FXML")
    print("=" * 55)
    print(f"  Imagen:    {ruta_imagen}")
    print(f"  Interfaz:  {nombre}")
    print(f"  Package:   {package}")
    print("=" * 55)

    # Configurar Gemini
    api_key = get_api_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")

    try:
        # Ejecutar pipeline
        descripcion = paso1_analizar_imagen(model, ruta_imagen, nombre)
        fxml = paso2_generar_fxml(model, descripcion, nombre, package)
        controller = paso3_generar_controller(model, fxml, nombre, package)
        app = paso4_generar_app(nombre, package, nombre)

        # Guardar todo
        rutas = guardar_ficheros(nombre, package, descripcion, fxml, controller, app)

        # Resumen
        print()
        print("=" * 55)
        print("  FICHEROS GENERADOS:")
        print("=" * 55)
        for clave, ruta in rutas.items():
            print(f"  [{clave.upper():>12}] {ruta}")
        print()
        print("  SIGUIENTE PASO:")
        print("  1. Verifica el FXML en Scene Builder")
        print("  2. Ejecuta App.java para ver la interfaz")
        print("  3. Si algo no está bien, abre OpenCode y pide correcciones")
        print("=" * 55)

    except Exception as e:
        print(f"\nERROR: {e}")
        print("\nSi el error es de la API, verifica:")
        print("  1. Tu API Key es válida")
        print("  2. Tienes acceso a gemini-2.0-flash")
        print("  3. No has superado el límite gratuito")
        sys.exit(1)


if __name__ == "__main__":
    main()
