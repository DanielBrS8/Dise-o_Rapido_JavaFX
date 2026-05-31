# Diseño Rápido de Interfaces Gráficas JavaFX+FXML con Agentes de Codificación

**Asignatura:** Diseño de Interfaces (DI)
**Objetivo:** Guía/toolkit para que un estudiante pueda pasar de una idea (boceto en papel o mockup digital) a interfaces JavaFX funcionales (sin lógica) en el menor tiempo posible, usando agentes de codificación gratuitos.

---

## Estructura del Proyecto

```
Subida Nota/
├── README.md                          ← Este fichero (documentación principal)
├── OPENCODE-INSTRUCTIONS.md           ← Instrucciones que OpenCode lee como contexto
│
├── docs/
│   ├── etapa1-mockup-a-digital.md     ← Alternativas para pasar de mockup a digital
│   └── etapa2-digital-a-fxml-opencode.md  ← Cómo usar OpenCode para generar FXML
│
├── prompts/
│   ├── 01-analizar-mockup-con-ia-vision.md   ← Prompt para IA con visión
│   ├── 02-generar-fxml-desde-descripcion.md  ← Prompt para generar FXML
│   ├── 03-corregir-refinar-fxml.md           ← Prompts de corrección
│   ├── 04-generar-controller-y-app.md        ← Prompts para Java
│   └── 05-multiples-pantallas.md             ← Prompts para varias pantallas
│
├── scripts/
│   ├── analizar_mockup.py             ← Script: imagen → descripción estructurada
│   └── pipeline_completo.py           ← Script: imagen → FXML + Controller + App
│
├── ejemplo/
│   ├── mockups/
│   │   ├── descripcion-login.md           ← Descripción estructurada del login
│   │   └── descripcion-panel-principal.md ← Descripción del panel principal
│   └── fxml/
│       ├── login.fxml                     ← FXML generado del login
│       └── panel-principal.fxml           ← FXML generado del panel
│
└── proyecto-javafx/                   ← Proyecto Maven listo para ejecutar
    ├── pom.xml
    └── src/main/
        ├── java/com/ejemplo/
        │   ├── App.java                   ← Clase lanzadora
        │   ├── LoginController.java       ← Controller del login (vacío)
        │   └── PanelPrincipalController.java ← Controller del panel (vacío)
        └── resources/fxml/
            ├── login.fxml
            └── panel-principal.fxml
```

---

## Flujo de Trabajo Completo

```
┌─────────────────┐     ┌───────────────────┐     ┌──────────────────┐     ┌──────────────┐
│   IDEA/BOCETO   │────>│  ETAPA 1          │────>│  ETAPA 2         │────>│  RESULTADO   │
│                 │     │  Mockup → Digital  │     │  Digital → FXML  │     │              │
│  • Papel        │     │                   │     │                  │     │  • .fxml     │
│  • Wireframe    │     │  • IA con visión  │     │  • OpenCode      │     │  • .java     │
│  • Idea mental  │     │  • Script Python  │     │  • Modelo gratis │     │  • .css      │
│                 │     │  • Descripción .md│     │  • Gemini/Mistral│     │  • Lanzable  │
└─────────────────┘     └───────────────────┘     └──────────────────┘     └──────────────┘
```

---

## Guía Rápida: Paso a Paso

### Prerequisitos

1. **Java 17+** instalado
2. **Maven** instalado
3. **Python 3.8+** con pip (para los scripts auxiliares)
4. **OpenCode** instalado: `npm install -g @anthropic-ai/opencode` (o según documentación)
5. **API Key de Gemini** (gratis): https://aistudio.google.com/apikey

### Opción A: Flujo con Script Python (Más automático)

**Paso 1:** Instalar dependencias Python
```bash
pip install google-generativeai Pillow
```

**Paso 2:** Configurar API Key
```bash
export GOOGLE_API_KEY="tu-api-key-de-gemini"
```

**Paso 3:** Ejecutar el pipeline completo
```bash
# Desde la raíz de tu proyecto JavaFX
python scripts/pipeline_completo.py foto-de-tu-mockup.jpg NombrePantalla com.tupaquete
```

Esto genera automáticamente:
- `mockups/descripcion-nombrepantalla.md` (descripción)
- `src/main/resources/fxml/nombrepantalla.fxml` (interfaz)
- `src/main/java/com/tupaquete/NombrePantallaController.java` (controller)
- `src/main/java/com/tupaquete/App.java` (lanzador)

**Paso 4:** Ejecutar
```bash
mvn javafx:run
```

**Paso 5:** Refinar con OpenCode si es necesario
```bash
opencode
# Dentro de OpenCode:
# "Lee src/main/resources/fxml/nombrepantalla.fxml y mejora el espaciado"
```

### Opción B: Flujo con OpenCode (Más control)

**Paso 1:** Crear la descripción del mockup

- **Si tienes foto:** Sube a Gemini/ChatGPT con el prompt de `prompts/01-analizar-mockup-con-ia-vision.md`
- **Si tienes idea:** Escribe la descripción manualmente usando la plantilla de `docs/etapa1-mockup-a-digital.md`
- Guarda el resultado como `.md` en la carpeta `mockups/`

**Paso 2:** Abrir OpenCode en tu proyecto
```bash
cd tu-proyecto-javafx
opencode
```

**Paso 3:** Pedir que lea las instrucciones
```
Lee el fichero OPENCODE-INSTRUCTIONS.md para entender tu rol.
Luego lee mockups/descripcion-[nombre].md y genera el FXML correspondiente.
```

**Paso 4:** Generar Controller y App
```
Genera el Controller Java vacío para el FXML que acabas de crear.
También genera la clase App.java que lo lance.
```

**Paso 5:** Verificar y ejecutar
```bash
mvn javafx:run
```

### Opción C: Solo OpenCode (Sin scripts, sin fotos)

```bash
cd tu-proyecto-javafx
opencode
```

Y directamente:
```
Genera una interfaz JavaFX con las siguientes pantallas:

1. LOGIN: Pantalla de login con email, contraseña, botón iniciar sesión,
   enlace de olvidé contraseña, y botón crear cuenta. Estilo moderno con
   fondo gris claro y tarjeta blanca centrada.

2. DASHBOARD: Panel principal con barra superior oscura (nombre app,
   búsqueda, usuario), menú lateral oscuro (Inicio, Usuarios, Estadísticas,
   Proyectos, Calendario, Configuración, Ayuda), y área central con
   4 tarjetas de estadísticas y una tabla.

Para cada pantalla genera:
- Fichero .fxml en src/main/resources/fxml/
- Controller .java vacío en src/main/java/com/ejemplo/
- Clase App.java que lance login.fxml

Requisitos: estilos inline, fx:id en todo, sin lógica de negocio.
```

---

## Alternativas de Herramientas

### Agentes de Codificación (para Etapa 2)

| Herramienta | Gratuito | Modelos disponibles | Acceso ficheros |
|-------------|----------|-------------------|-----------------|
| **OpenCode** | Sí | Gemini, Mistral, Codestral | Sí (terminal) |
| Claude Code | No* | Claude | Sí (terminal) |
| GitHub Copilot Chat | Con estudiante | GPT-4 | Sí (VS Code) |
| Cursor | Freemium | Varios | Sí (editor) |

*Se recomienda OpenCode por ser obligatorio y gratuito.

### Modelos Gratuitos (para usar con OpenCode)

| Modelo | Proveedor | Calidad código | Visión | API Key |
|--------|-----------|---------------|--------|---------|
| **Gemini 2.0 Flash** | Google | ★★★★☆ | Sí | aistudio.google.com |
| **Gemini 2.5 Pro** | Google | ★★★★★ | Sí | aistudio.google.com (límite) |
| Codestral | Mistral | ★★★★☆ | No | console.mistral.ai |
| Mistral Small | Mistral | ★★★☆☆ | No | console.mistral.ai |
| Modelos OpenRouter | Varios | Variable | Variable | openrouter.ai |

### IAs con Visión (para Etapa 1)

| Herramienta | Gratuito | Calidad análisis |
|-------------|----------|-----------------|
| **Google Gemini** | Sí | ★★★★★ |
| ChatGPT (GPT-4o mini) | Sí | ★★★★☆ |
| Microsoft Copilot | Sí | ★★★★☆ |
| Script Python incluido | Sí (con API Key) | ★★★★★ |

### Herramientas de Wireframing (opcionales)

| Herramienta | Gratuito | Mejor para |
|-------------|----------|-----------|
| **Excalidraw** | Sí | Bocetos rápidos estilo mano |
| **Figma** | Sí (plan free) | Wireframes profesionales |
| draw.io | Sí | Diagramas de layout |
| Pencil Project | Sí (open source) | Prototipado GUI |
| Scene Builder | Sí | Ver/editar FXML directo |

---

## Ejemplo Concreto Incluido

Este proyecto incluye un ejemplo completo con dos interfaces:

### 1. Pantalla de Login
- Descripción: [ejemplo/mockups/descripcion-login.md](ejemplo/mockups/descripcion-login.md)
- FXML generado: [ejemplo/fxml/login.fxml](ejemplo/fxml/login.fxml)
- Controller: [proyecto-javafx/src/main/java/com/ejemplo/LoginController.java](proyecto-javafx/src/main/java/com/ejemplo/LoginController.java)

### 2. Panel Principal (Dashboard)
- Descripción: [ejemplo/mockups/descripcion-panel-principal.md](ejemplo/mockups/descripcion-panel-principal.md)
- FXML generado: [ejemplo/fxml/panel-principal.fxml](ejemplo/fxml/panel-principal.fxml)
- Controller: [proyecto-javafx/src/main/java/com/ejemplo/PanelPrincipalController.java](proyecto-javafx/src/main/java/com/ejemplo/PanelPrincipalController.java)

### Ejecutar el ejemplo
```bash
cd proyecto-javafx
mvn javafx:run
```

Para cambiar la interfaz que se lanza, edita la constante `FXML_A_CARGAR` en [App.java](proyecto-javafx/src/main/java/com/ejemplo/App.java):
```java
// Cambiar a panel principal:
private static final String FXML_A_CARGAR = "/fxml/panel-principal.fxml";
```

---

## Consejos y Buenas Prácticas

### Para obtener mejores resultados con los agentes

1. **Sé específico** con los nombres de componentes JavaFX (usar `TableView`, no "tabla")
2. **Divide interfaces complejas** en partes: primero el esqueleto, luego cada sección
3. **Itera rápidamente**: genera, verifica en Scene Builder, corrige con el agente
4. **Usa la convención de fx:id**: `btn`, `txt`, `lbl`, `tbl`, `col`, `chk`, `cmb`
5. **Pide estilos inline** para prototipado rápido (CSS externo para producción)

### Errores frecuentes

| Error | Solución |
|-------|----------|
| El agente genera HTML en vez de FXML | Especificar "JavaFX FXML, NO HTML" en el prompt |
| Faltan imports `<?import?>` | Pedir explícitamente que incluya todos los imports |
| fx:controller incorrecto | Especificar el package exacto en el prompt |
| Componentes no aparecen | Añadir prefWidth/prefHeight o propiedades de grow |
| Scene Builder no abre el FXML | Verificar que el XML es válido (sin errores de sintaxis) |

---

## Documentación Detallada

- [Etapa 1: De Mockup a Diseño Digital](docs/etapa1-mockup-a-digital.md) - Todas las alternativas
- [Etapa 2: De Digital a FXML con OpenCode](docs/etapa2-digital-a-fxml-opencode.md) - Configuración y uso
- [Prompts utilizados](prompts/) - Todos los prompts listos para copiar y usar
- [OPENCODE-INSTRUCTIONS.md](OPENCODE-INSTRUCTIONS.md) - Fichero que OpenCode lee como contexto

---

## Conclusión

Este toolkit permite a un estudiante **reducir drásticamente** el tiempo de diseño de interfaces JavaFX, pasando de una idea en papel a una interfaz visual lanzable usando herramientas gratuitas y agentes de codificación. El flujo más rápido posible es:

1. **Foto del boceto** → subir a Gemini/ChatGPT → descripción `.md`
2. **Abrir OpenCode** → pedir que lea la descripción → genera `.fxml`
3. **Generar Controller** → generar App.java → `mvn javafx:run`

O con el script Python incluido: **un solo comando** que hace todo automáticamente.
#   D i s e - o _ R a p i d o _ J a v a F X  
 