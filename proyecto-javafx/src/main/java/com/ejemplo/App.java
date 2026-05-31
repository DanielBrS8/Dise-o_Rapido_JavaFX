package com.ejemplo;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

/**
 * Clase principal que lanza las interfaces generadas.
 * Se puede cambiar el FXML que carga para probar distintas interfaces.
 *
 * Uso:
 *   mvn javafx:run
 *   o
 *   mvn javafx:run -Djavafx.mainClass=com.ejemplo.App
 */
public class App extends Application {

    // Cambiar esta constante para lanzar distintas interfaces
    private static final String FXML_A_CARGAR = "/fxml/login.fxml";
    private static final String TITULO_VENTANA = "Demo - Interfaces Generadas desde Mockup";

    @Override
    public void start(Stage stage) throws Exception {
        Parent root = FXMLLoader.load(getClass().getResource(FXML_A_CARGAR));
        stage.setTitle(TITULO_VENTANA);
        stage.setScene(new Scene(root));
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
