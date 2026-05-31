# Prompt 05: Generar Múltiples Pantallas de una Vez

## Cuándo usar
Cuando tu aplicación tiene **varias pantallas** y quieres generarlas todas en una sesión de OpenCode.

## Dónde usar
- **OpenCode** - en la terminal del proyecto

## Prompt: Generación por lotes

```
Necesito generar las interfaces FXML para una aplicación JavaFX con
las siguientes pantallas. Para CADA una, genera:
- El fichero .fxml en src/main/resources/fxml/
- El Controller .java vacío en src/main/java/com/ejemplo/

Pantallas:

1. LOGIN (login.fxml):
   [Descripción breve de la pantalla de login]

2. REGISTRO (registro.fxml):
   [Descripción breve de la pantalla de registro]

3. PANEL PRINCIPAL (panel-principal.fxml):
   [Descripción breve del dashboard/panel]

4. [NOMBRE] ([nombre].fxml):
   [Descripción breve]

Requisitos generales:
- Estilo visual coherente entre todas las pantallas
- Misma paleta de colores (#2c3e50 para headers, #3498db primario, #ecf0f1 fondo)
- fx:id descriptivos con prefijos (btn, txt, lbl, tbl, etc.)
- fx:controller apuntando a com.ejemplo.[Nombre]Controller
- Sin lógica de negocio en los controllers
- Incluir imports XML en cada FXML

Al final, genera también la clase App.java que cargue login.fxml
como pantalla inicial.
```

## Prompt: Añadir navegación visual (sin funcionalidad)

```
Lee todos los ficheros FXML generados en src/main/resources/fxml/.

En cada pantalla que tenga botones de navegación (por ejemplo,
"Ir a registro", menú lateral, etc.), asegúrate de que los botones
existan con fx:id apropiados para una futura navegación.

NO implementar la navegación, solo asegurar que los componentes
de navegación están presentes en el FXML.
```
