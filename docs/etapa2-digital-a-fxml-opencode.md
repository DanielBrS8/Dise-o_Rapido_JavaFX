# Etapa 2: De Diseño Digital a FXML con OpenCode

## Objetivo

Usar un **agente de codificación** (OpenCode) con modelos gratuitos para transformar la descripción estructurada de la Etapa 1 en ficheros `.fxml` funcionales que JavaFX pueda renderizar.

---

## Qué es OpenCode

**OpenCode** es un agente de codificación en terminal (CLI), similar a Claude Code, Cursor o GitHub Copilot CLI. Permite interactuar con modelos de IA desde la terminal para generar, editar y refactorizar código.

- **Repositorio:** https://github.com/opencode-ai/opencode
- **Instalación:** `npm install -g opencode` (o según documentación actual)
- **Modelos gratuitos compatibles:** Gemini, Mistral, Codestral, entre otros

---

## Configuración de OpenCode con Modelos Gratuitos

### Opción 1: Google Gemini (Recomendado)

1. Obtener API Key gratuita en: https://aistudio.google.com/apikey
2. Configurar en OpenCode:

```bash
# Configurar la API key
export GOOGLE_API_KEY="tu-api-key-aquí"

# O configurar en el fichero de configuración de OpenCode
```

**Modelos recomendados:**
- `gemini-2.0-flash` - Rápido y capaz (recomendado)
- `gemini-2.5-pro` - Más potente, límite de uso diario gratuito

### Opción 2: Mistral / Codestral

1. Obtener API Key en: https://console.mistral.ai/
2. Modelos gratuitos disponibles:
   - `codestral-latest` - Especializado en código
   - `mistral-small-latest`

### Opción 3: OpenRouter (Acceso a múltiples modelos gratuitos)

1. Crear cuenta en: https://openrouter.ai/
2. Acceso a modelos gratuitos de distintos proveedores
3. Configurar en OpenCode con la API key de OpenRouter

---

## Flujo de Trabajo: Descripción → FXML

### Paso 1: Preparar el directorio del proyecto

```bash
# Crear estructura básica
mkdir -p mi-proyecto/src/main/resources/fxml
mkdir -p mi-proyecto/src/main/resources/css
mkdir -p mi-proyecto/src/main/java/com/miapp
cd mi-proyecto
```

### Paso 2: Crear el fichero de descripción

Guardar la descripción estructurada de la Etapa 1 en un fichero `.md`:

```bash
# Crear el fichero de descripción (ejemplo)
cat > descripcion-login.md << 'EOF'
# Interfaz: Pantalla de Login

## Layout principal: VBox (centrado)
## Dimensiones: 400x500 px

## Estructura:
- Logo/Título de la aplicación (arriba)
- Campo de texto: Usuario
- Campo de texto: Contraseña (PasswordField)
- Botón: "Iniciar Sesión" (ancho completo)
- Link: "¿Olvidaste tu contraseña?"
- Separador
- Botón secundario: "Crear cuenta"
EOF
```

### Paso 3: Lanzar OpenCode y generar FXML

```bash
# Iniciar OpenCode en el directorio del proyecto
opencode
```

### Paso 4: Usar los prompts adecuados

Ver la sección de prompts detallados más abajo y en la carpeta `/prompts/`.

---

## Prompts para OpenCode

### Prompt 1: Generación de FXML desde descripción

```
Lee el fichero descripcion-login.md y genera un fichero FXML para JavaFX
que implemente esa interfaz.

Requisitos:
- Usar los layouts apropiados de JavaFX (VBox, HBox, BorderPane, GridPane, etc.)
- Incluir fx:id en todos los componentes interactivos
- Usar fx:controller apuntando a com.miapp.LoginController
- El fichero debe ser válido y abrirse en Scene Builder
- Aplicar espaciado y padding razonables
- Dimensiones de la ventana según la descripción
- NO incluir lógica, solo la interfaz visual
- Guardar en src/main/resources/fxml/login.fxml
```

### Prompt 2: Generación de FXML desde imagen (si OpenCode soporta visión)

```
[Adjuntar imagen del mockup]

Genera un fichero FXML para JavaFX que replique esta interfaz gráfica.

Requisitos:
- Identificar todos los componentes visibles
- Usar layouts JavaFX apropiados
- Incluir fx:id en componentes interactivos
- fx:controller: com.miapp.[Nombre]Controller
- Guardar en src/main/resources/fxml/[nombre].fxml
```

### Prompt 3: Mejora/refinamiento de FXML existente

```
Lee el fichero src/main/resources/fxml/login.fxml y mejóralo:

- Añade una hoja de estilos CSS referenciada como ../css/styles.css
- Mejora el espaciado y la alineación
- Asegura que todos los componentes tienen fx:id descriptivos
- Añade tooltips a los botones
- Haz el layout responsivo usando propiedades de crecimiento (HBox.hgrow, VBox.vgrow)
```

### Prompt 4: Generar CSS básico para la interfaz

```
Genera un fichero CSS para JavaFX que aplique un estilo moderno y limpio
a la interfaz definida en src/main/resources/fxml/login.fxml.

Incluir estilos para:
- Colores primarios y secundarios
- Botones (normal, hover, pressed)
- Campos de texto
- Labels y títulos
- Fondo de la ventana

Guardar en src/main/resources/css/styles.css
```

### Prompt 5: Generar la clase Java lanzadora (sin funcionalidad)

```
Genera una clase Java que:
1. Extienda Application de JavaFX
2. Cargue el fichero FXML src/main/resources/fxml/login.fxml
3. Muestre la ventana con título "Mi Aplicación"
4. NO incluya ninguna lógica de negocio

Genera también la clase Controller vacía con los @FXML
correspondientes a los fx:id del FXML.

Guardar en:
- src/main/java/com/miapp/App.java
- src/main/java/com/miapp/LoginController.java
```

---

## Consejos para Obtener Buenos Resultados

### 1. Ser específico con los layouts
En lugar de decir "pon un formulario", decir:
> "GridPane con 2 columnas: la primera con Labels y la segunda con TextFields, 3 filas: Usuario, Contraseña, Email"

### 2. Especificar nombres de componentes JavaFX reales
Usar los nombres correctos: `Button`, `Label`, `TextField`, `PasswordField`, `ComboBox`, `TableView`, `TableColumn`, `MenuBar`, `Menu`, `MenuItem`, `ListView`, `TreeView`, `TabPane`, `Tab`, `SplitPane`, `ScrollPane`, `DatePicker`, `Spinner`, etc.

### 3. Iterar rápidamente
- Generar una primera versión
- Abrir en Scene Builder para verificar visualmente
- Pedir correcciones al agente
- Repetir hasta quedar satisfecho

### 4. Dividir interfaces complejas
Si la interfaz es muy compleja, dividirla en partes:
1. Primero el layout general (esqueleto)
2. Luego cada sección por separado
3. Finalmente integrar todo

### 5. Verificar siempre el FXML generado
- Abrirlo en Scene Builder
- O ejecutarlo con la clase lanzadora Java
- Comprobar que los fx:id son correctos
- Verificar que el fx:controller apunta a la clase correcta

---

## Errores Comunes y Soluciones

| Error | Causa | Solución |
|-------|-------|----------|
| `FXML not found` | Ruta incorrecta | Verificar que el FXML está en resources/ |
| `Controller not found` | Package incorrecto | Verificar fx:controller en el FXML |
| `fx:id not found` | ID no coincide | Comparar fx:id del FXML con @FXML del Controller |
| `No se ve nada` | Tamaños a 0 | Añadir prefWidth/prefHeight o propiedades de grow |
| `Import faltante` | Falta <?import?> | Añadir imports al inicio del FXML |

---

## Flujo Completo Resumido

```
┌─────────────────────┐
│  Descripción .md    │
│  (de Etapa 1)       │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  OpenCode           │
│  + Modelo gratuito  │
│  (Gemini/Mistral)   │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Fichero .fxml      │
│  generado           │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Verificar en       │
│  Scene Builder      │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Iterar/Refinar     │
│  con OpenCode       │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  FXML final +       │
│  CSS + Controller   │
└─────────────────────┘
```
