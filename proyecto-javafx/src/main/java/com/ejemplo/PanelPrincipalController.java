package com.ejemplo;

import javafx.fxml.FXML;
import javafx.scene.control.*;

/**
 * Controller para el Panel Principal (Dashboard).
 * Solo contiene las referencias @FXML, sin lógica de negocio.
 */
public class PanelPrincipalController {

    // Barra superior
    @FXML private Label lblAppName;
    @FXML private TextField txtBuscar;
    @FXML private Button btnNotificaciones;
    @FXML private Label lblUsuario;
    @FXML private MenuButton menuUsuario;

    // Menú lateral
    @FXML private Button btnInicio;
    @FXML private Button btnUsuarios;
    @FXML private Button btnEstadisticas;
    @FXML private Button btnProyectos;
    @FXML private Button btnCalendario;
    @FXML private Button btnConfiguracion;
    @FXML private Button btnAyuda;

    // Contenido central
    @FXML private Label lblTituloSeccion;
    @FXML private Label lblCardUsuarios;
    @FXML private Label lblCardProyectos;
    @FXML private Label lblCardPendientes;
    @FXML private Label lblCardCompletadas;
    @FXML private TableView<?> tblDatos;
    @FXML private TableColumn<?, ?> colId;
    @FXML private TableColumn<?, ?> colNombre;
    @FXML private TableColumn<?, ?> colEstado;
    @FXML private TableColumn<?, ?> colFecha;
    @FXML private TableColumn<?, ?> colAcciones;

    // Barra de estado
    @FXML private Label lblEstado;
    @FXML private Label lblVersion;

    @FXML
    private void initialize() {
        // Sin funcionalidad - solo interfaz visual
    }
}
