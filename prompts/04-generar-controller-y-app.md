# Prompt 04: Generar Controller Vacío y Clase App

## Cuándo usar
Cuando ya tienes el FXML y necesitas las **clases Java** para que la aplicación compile y se pueda lanzar.

## Dónde usar
- **OpenCode** - en la terminal del proyecto

## Prompt: Generar Controller

```
Lee el fichero src/main/resources/fxml/[nombre].fxml y genera la clase
Controller Java correspondiente.

Requisitos:
- Package: com.ejemplo (o el que use tu proyecto)
- Nombre: [Nombre]Controller
- Incluir @FXML para CADA fx:id que aparezca en el FXML
- Incluir los imports necesarios (javafx.fxml.FXML, javafx.scene.control.*, etc.)
- Método initialize() vacío
- NO incluir ninguna lógica de negocio
- Solo la estructura del Controller

Guardar en src/main/java/com/ejemplo/[Nombre]Controller.java
```

## Prompt: Generar clase App lanzadora

```
Genera una clase App.java que:
1. Extienda javafx.application.Application
2. En el método start(), cargue el FXML: /fxml/[nombre].fxml
3. Muestre la ventana con título "[Título de la ventana]"
4. Tenga un método main() que llame a launch()
5. Package: com.ejemplo

Guardar en src/main/java/com/ejemplo/App.java
```

## Prompt: Generar todo de una vez

```
Lee TODOS los ficheros .fxml en src/main/resources/fxml/ y para cada uno:

1. Genera su Controller Java vacío con todos los @FXML correspondientes
2. Guárdalo en src/main/java/com/ejemplo/[Nombre]Controller.java

Además, genera una clase App.java que cargue [nombre].fxml como
pantalla principal.

Package para todo: com.ejemplo
Guardar controllers en: src/main/java/com/ejemplo/
```

## Prompt: Generar pom.xml para Maven

```
Genera un fichero pom.xml para un proyecto JavaFX con Maven que:
- Use Java 17
- Incluya dependencias de javafx-controls y javafx-fxml (versión 17.0.2)
- Incluya el plugin javafx-maven-plugin
- La clase principal sea com.ejemplo.App
- GroupId: com.ejemplo
- ArtifactId: mi-app-javafx
```
