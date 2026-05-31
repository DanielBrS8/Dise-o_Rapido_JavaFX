# Etapa 1: De Papel/Mockup a Diseño Digital

## Objetivo

Convertir una idea visual (boceto en papel, wireframe a mano, o mockup mental) en un **fichero digital estructurado** que un agente de codificación pueda interpretar para generar código FXML.

---

## Alternativas Disponibles

### Alternativa A: Foto del boceto + IA de visión (Recomendada para rapidez)

**Herramientas gratuitas:**
- **Google Gemini** (gemini.google.com) - Modelo gratuito con visión
- **ChatGPT Free** (chatgpt.com) - GPT-4o mini con visión
- **Microsoft Copilot** (copilot.microsoft.com) - Gratuito con visión

**Proceso:**
1. Dibujar el boceto en papel (no hace falta que sea bonito, solo claro)
2. Hacer una foto con el móvil
3. Subir la foto a una IA con visión
4. Usar el prompt adecuado (ver carpeta `/prompts/`)

**Prompt para convertir foto a descripción estructurada:**
```
Analiza esta imagen de un boceto/mockup de interfaz gráfica.
Genera una descripción estructurada en formato Markdown con:

1. LAYOUT GENERAL: Tipo de layout principal (BorderPane, VBox, HBox, GridPane, etc.)
2. COMPONENTES: Lista cada componente visible con:
   - Tipo (Button, Label, TextField, TableView, MenuBar, etc.)
   - Texto/contenido visible
   - Posición aproximada (arriba, centro, izquierda, etc.)
   - Tamaño relativo (ancho completo, mitad, etc.)
3. JERARQUÍA: Estructura anidada de contenedores y componentes
4. ESTILOS OBSERVADOS: Colores, alineaciones, espaciados notables

Formato de salida: descripción técnica orientada a JavaFX/FXML.
```

**Ventajas:** Muy rápido, natural, no requiere herramientas extra.
**Desventajas:** Depende de la calidad del boceto y de la IA.

---

### Alternativa B: Herramientas de wireframing gratuitas

**Herramientas:**
- **Figma** (figma.com) - Plan gratuito, muy popular
- **Excalidraw** (excalidraw.com) - Gratuito, estilo boceto a mano
- **draw.io / diagrams.net** (app.diagrams.net) - Gratuito, diagramas
- **Pencil Project** (pencil.evolus.vn) - Open source, prototipado GUI

**Proceso:**
1. Crear el wireframe en la herramienta elegida
2. Exportar como imagen (PNG/JPG)
3. Usar la misma técnica de Alternativa A (subir a IA con visión)
4. O bien describir manualmente la estructura

**Ventajas:** Diseño más limpio y preciso, colaborativo (Figma).
**Desventajas:** Requiere aprender la herramienta, más lento que papel.

---

### Alternativa C: Descripción textual directa (Sin imagen)

**Proceso:**
1. Describir la interfaz directamente en texto estructurado
2. Usar una plantilla Markdown (ver abajo)
3. Pasar directamente a la Etapa 2 con esta descripción

**Plantilla de descripción de interfaz:**
```markdown
# Interfaz: [Nombre de la pantalla]

## Layout principal: [BorderPane/VBox/HBox/GridPane/AnchorPane]
## Dimensiones: [ancho x alto en px]

## Estructura:
- **TOP**:
  - [Componente]: [descripción]
- **LEFT**:
  - [Componente]: [descripción]
- **CENTER**:
  - [Componente]: [descripción]
- **BOTTOM**:
  - [Componente]: [descripción]

## Componentes detallados:
| ID | Tipo | Texto | Posición | Notas |
|----|------|-------|----------|-------|
| btnLogin | Button | "Iniciar Sesión" | CENTER | Principal |
| txtUsuario | TextField | prompt: "Usuario" | CENTER | - |

## Estilos:
- Color primario: #3498db
- Fuente: System 14px
- Espaciado: 10px entre elementos
```

**Ventajas:** No necesita ninguna herramienta, máximo control, el agente lo interpreta muy bien.
**Desventajas:** Requiere conocer los componentes JavaFX de antemano.

---

### Alternativa D: Scene Builder como referencia visual

**Herramienta:** Scene Builder (gluonhq.com/products/scene-builder) - Gratuito

**Proceso:**
1. Abrir Scene Builder
2. Arrastrar componentes básicos para crear un prototipo rápido
3. Exportar el FXML generado
4. Usar ese FXML como base para que el agente lo mejore/complete

**Ventajas:** Visual, genera FXML directamente, WYSIWYG.
**Desventajas:** Más lento para prototipar, ya estás haciendo el trabajo del agente.

---

## Comparativa Resumen

| Criterio | A: Foto+IA | B: Wireframe | C: Texto | D: SceneBuilder |
|----------|-----------|-------------|----------|-----------------|
| **Velocidad** | ★★★★★ | ★★★☆☆ | ★★★★☆ | ★★☆☆☆ |
| **Precisión** | ★★★☆☆ | ★★★★☆ | ★★★★★ | ★★★★★ |
| **Facilidad** | ★★★★★ | ★★★☆☆ | ★★★☆☆ | ★★★★☆ |
| **Coste** | Gratis | Gratis | Gratis | Gratis |
| **Requiere IA** | Sí | Opcional | No | No |

## Recomendación

Para **máxima velocidad**: Alternativa A (foto) o C (texto directo).
Para **máxima precisión**: Alternativa C (texto) o D (Scene Builder).
Para **presentaciones/equipo**: Alternativa B (Figma/Excalidraw).

El flujo **más rápido** es: **Papel → Foto → IA con visión → Descripción estructurada → Etapa 2**
