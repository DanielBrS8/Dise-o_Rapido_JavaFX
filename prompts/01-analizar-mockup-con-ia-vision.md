# Prompt 01: Analizar Mockup con IA de Visión

## Cuándo usar
Cuando tienes una **foto de un boceto en papel** o una **captura de un wireframe** y quieres que una IA la convierta en una descripción estructurada para JavaFX.

## Dónde usar
- Google Gemini (gemini.google.com) - GRATIS
- ChatGPT (chatgpt.com) - versión gratuita
- Microsoft Copilot (copilot.microsoft.com) - GRATIS

## Prompt

```
Analiza esta imagen de un mockup/boceto de interfaz gráfica de usuario.

Genera una descripción estructurada en formato Markdown orientada a JavaFX/FXML con el siguiente formato:

# Interfaz: [Nombre descriptivo de la pantalla]

## Layout principal: [BorderPane/VBox/HBox/GridPane/AnchorPane/StackPane]
## Dimensiones sugeridas: [ancho x alto px]

## Estructura:
[Describe jerárquicamente cada zona/sección del mockup]
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
[... todos los componentes interactivos]

IMPORTANTE:
- Usa nombres de componentes JavaFX REALES y correctos
- Sugiere los layouts más apropiados para cada zona
- Los fx:id deben seguir convención: btn, txt, lbl, tbl, col, chk, cmb
- Incluye TODOS los elementos visibles
```

## Instrucciones
1. Sube la foto/imagen del mockup a la IA
2. Pega el prompt anterior
3. Copia la respuesta y guárdala como fichero `.md` en la carpeta `mockups/`
