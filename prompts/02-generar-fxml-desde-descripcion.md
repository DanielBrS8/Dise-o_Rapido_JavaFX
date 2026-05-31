# Prompt 02: Generar FXML desde Descripción Estructurada

## Cuándo usar
Cuando ya tienes la **descripción estructurada** (fichero `.md`) de la interfaz y quieres generar el fichero FXML.

## Dónde usar
- **OpenCode** (recomendado) - en la terminal del proyecto
- Cualquier agente de codificación con acceso al sistema de ficheros

## Prompt para OpenCode

```
Lee el fichero mockups/descripcion-[nombre].md y genera un fichero FXML
para JavaFX que implemente esa interfaz.

Requisitos:
- Incluir todos los <?import?> necesarios al inicio del FXML
- Usar fx:controller="com.ejemplo.[Nombre]Controller"
- Asignar fx:id a TODOS los componentes interactivos
- Usar estilos inline con style="-fx-..." para prototipado rápido
- Layout responsive: usar HBox.hgrow="ALWAYS" y VBox.vgrow="ALWAYS" donde sea necesario
- Usar Region como espaciadores flexibles
- maxWidth="Infinity" para componentes de ancho completo
- Incluir padding e Insets apropiados
- El FXML debe ser válido y abrirse en Scene Builder
- NO incluir ninguna lógica, solo interfaz visual
- Guardar en src/main/resources/fxml/[nombre].fxml
```

## Variante: Generar FXML directamente desde descripción verbal

```
Genera un fichero FXML para JavaFX con las siguientes características:

[Descripción de la interfaz en lenguaje natural]

Por ejemplo: "Una pantalla de login con campo de email, contraseña,
botón de iniciar sesión azul, y un enlace de 'olvidé mi contraseña'.
Todo centrado verticalmente con fondo gris claro."

Requisitos técnicos:
- Incluir imports XML
- fx:controller="com.ejemplo.[Nombre]Controller"
- fx:id en todos los componentes interactivos
- Estilos inline
- Guardar en src/main/resources/fxml/[nombre].fxml
```

## Instrucciones
1. Abre OpenCode en la raíz de tu proyecto JavaFX
2. Asegúrate de que el fichero de descripción `.md` está en la carpeta `mockups/`
3. Pega el prompt adaptando `[nombre]` al nombre de tu interfaz
4. Revisa el FXML generado (abrirlo en Scene Builder)
5. Si necesitas correcciones, usa el Prompt 03
