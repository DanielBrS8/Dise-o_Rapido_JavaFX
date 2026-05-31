package com.ejemplo;

import javafx.fxml.FXML;
import javafx.scene.control.*;

/**
 * Controller para la pantalla de Login.
 * Solo contiene las referencias @FXML, sin lógica de negocio.
 */
public class LoginController {

    @FXML private Label lblTitulo;
    @FXML private Label lblSubtitulo;
    @FXML private TextField txtEmail;
    @FXML private PasswordField txtPassword;
    @FXML private CheckBox chkRecordarme;
    @FXML private Hyperlink lnkOlvide;
    @FXML private Button btnLogin;
    @FXML private Button btnRegistro;

    @FXML
    private void initialize() {
        // Sin funcionalidad - solo interfaz visual
    }
}
