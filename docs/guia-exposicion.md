# Guía de Exposición y Defensa

## Estructura sugerida de la presentación

### 1. Introducción (1-2 min)
- **Problema:** Diseñar interfaces JavaFX/FXML es lento y repetitivo
- **Solución:** Un toolkit que automatiza el proceso usando agentes de codificación gratuitos
- **Resultado:** De boceto en papel a interfaz lanzable en minutos

### 2. Demostración del flujo (3-5 min)

**Demo en vivo recomendada:**

1. Mostrar un boceto en papel (dibujar uno simple en el momento o llevar uno preparado)
2. Hacer foto con el móvil
3. Subir a Gemini → obtener descripción estructurada
4. Abrir OpenCode en el proyecto
5. Pedir que genere el FXML
6. Ejecutar con `mvn javafx:run`
7. Mostrar la interfaz funcionando

**Alternativa si no hay conexión:**
- Mostrar el ejemplo ya incluido (login + panel principal)
- Explicar cada paso con los ficheros generados
- Ejecutar el proyecto JavaFX para mostrar las interfaces

### 3. Explicación de las etapas (2-3 min)

**Etapa 1: Mockup → Digital**
- Mostrar las 4 alternativas (A, B, C, D) de `docs/etapa1-mockup-a-digital.md`
- Destacar que la Alternativa A (foto + IA visión) es la más rápida
- Mencionar el script Python como opción automatizada

**Etapa 2: Digital → FXML**
- Mostrar cómo se configura OpenCode con Gemini (gratis)
- Enseñar el fichero `OPENCODE-INSTRUCTIONS.md` que guía al agente
- Mostrar los prompts utilizados (carpeta `prompts/`)

### 4. Resultados del ejemplo (1-2 min)
- Mostrar la descripción del mockup → FXML generado → interfaz visual
- Abrir el FXML en Scene Builder para verificar que es válido
- Ejecutar la app para demostrar que se lanza sin errores

### 5. Alternativas expuestas (1 min)
- Tabla comparativa de herramientas de agentes
- Tabla comparativa de modelos gratuitos
- Tabla comparativa de herramientas de wireframing

### 6. Conclusión (1 min)
- Se acelera drásticamente el prototipado de interfaces
- Todo con herramientas gratuitas
- El estudiante mantiene el control del diseño final
- Los agentes generan código limpio y válido para JavaFX

---

## Preguntas frecuentes que pueden hacerte

**P: ¿El agente siempre genera FXML correcto a la primera?**
R: No siempre. A veces hay errores menores (imports faltantes, fx:id duplicados). Por eso el flujo incluye un paso de verificación con Scene Builder y prompts de corrección.

**P: ¿Funciona sin conexión a internet?**
R: No, se necesita acceso a las APIs de los modelos (Gemini, etc.). Pero una vez generados los ficheros, el proyecto JavaFX funciona offline.

**P: ¿Por qué no usar directamente Scene Builder?**
R: Scene Builder es visual pero lento para prototipar desde cero. Con este flujo, en un prompt generas lo que en Scene Builder tardarías mucho más arrastrando componentes.

**P: ¿Se puede usar para interfaces complejas?**
R: Sí, dividiendo la interfaz en secciones y generando cada una por separado. Los prompts 03 y 05 están diseñados para esto.

**P: ¿Cuánto cuesta?**
R: 0. Todo gratuito: Gemini API free tier, OpenCode open source, los modelos tienen planes gratuitos.

**P: ¿Y la calidad del FXML generado?**
R: Es suficiente para prototipado y demostración. Para producción, se recomienda refinar con CSS externo y ajustar manualmente los detalles.

---

## Puntos fuertes para la defensa

1. **Práctico y reutilizable**: cualquier estudiante puede usar este toolkit en sus proyectos
2. **Múltiples alternativas**: se exponen distintas opciones para cada etapa
3. **Documentación completa**: incluye prompts, scripts, ejemplos y guías
4. **Todo gratuito**: no requiere licencias ni suscripciones de pago
5. **Ejemplo funcional**: el proyecto JavaFX incluido compila y se ejecuta
6. **Extensible**: se pueden añadir más pantallas y componentes fácilmente
