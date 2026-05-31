# Prompt 03: Corregir y Refinar FXML Existente

## Cuándo usar
Cuando el FXML generado necesita **ajustes, correcciones o mejoras**.

## Dónde usar
- **OpenCode** - en la terminal del proyecto

## Prompts de corrección

### Corregir errores de layout
```
Lee el fichero src/main/resources/fxml/[nombre].fxml y corrige los
siguientes problemas:
- [Describir el problema: "los botones no están centrados",
  "la tabla no ocupa todo el ancho", "falta espaciado entre elementos", etc.]

Mantén el resto del diseño igual.
```

### Mejorar estilos
```
Lee src/main/resources/fxml/[nombre].fxml y mejora los estilos visuales:
- Usar colores más modernos
- Mejorar el espaciado y padding
- Añadir bordes redondeados (-fx-background-radius)
- Añadir sombras sutiles (-fx-effect: dropshadow)
- Mejorar la tipografía
```

### Hacer responsive
```
Lee src/main/resources/fxml/[nombre].fxml y hazlo responsive:
- Añadir HBox.hgrow="ALWAYS" y VBox.vgrow="ALWAYS" donde corresponda
- Usar maxWidth="Infinity" en elementos que deben crecer
- Usar Region como espaciadores flexibles
- Asegurar que la interfaz se ve bien al redimensionar la ventana
```

### Cambiar layout principal
```
Lee src/main/resources/fxml/[nombre].fxml.
Actualmente usa [layout actual] como layout principal.
Cámbialo a [nuevo layout] manteniendo todos los componentes y sus fx:id.
Reorganiza la estructura para que sea correcta con el nuevo layout.
```

### Añadir componentes
```
Lee src/main/resources/fxml/[nombre].fxml y añade:
- [Componente]: [descripción] en [posición]

Ejemplo: "Un ComboBox con opciones de idioma en la barra superior,
a la izquierda del botón de notificaciones"

Mantén el fx:id con el prefijo apropiado (cmb, btn, txt, etc.)
```
