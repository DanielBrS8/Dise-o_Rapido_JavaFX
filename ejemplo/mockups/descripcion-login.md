# Interfaz: Pantalla de Login

## Layout principal: VBox (centrado verticalmente)
## Dimensiones: 400 x 550 px
## Fondo: Color claro (#f0f2f5)

## Estructura (de arriba a abajo):

1. **Espaciador superior** (flexible)

2. **Contenedor central** (VBox, fondo blanco, bordes redondeados, sombra, padding 40px):
   - **Título**: Label "Iniciar Sesión" (fuente grande 24px, negrita, color #333)
   - **Subtítulo**: Label "Accede a tu cuenta" (fuente 13px, color #888)
   - **Espaciado**: 20px
   - **Campo Usuario**: TextField con promptText "Correo electrónico" (ancho completo)
   - **Espaciado**: 10px
   - **Campo Contraseña**: PasswordField con promptText "Contraseña" (ancho completo)
   - **Espaciado**: 5px
   - **Fila opciones** (HBox, espacio entre elementos):
     - CheckBox "Recordarme"
     - Hyperlink "¿Olvidaste tu contraseña?"
   - **Espaciado**: 15px
   - **Botón Login**: Button "Iniciar Sesión" (ancho completo, color primario #3498db, texto blanco)
   - **Espaciado**: 15px
   - **Separador**: Separator con texto "o" en medio
   - **Espaciado**: 15px
   - **Botón Registro**: Button "Crear cuenta nueva" (ancho completo, estilo outline/secundario)

3. **Espaciador inferior** (flexible)

## Componentes con fx:id:
| ID | Tipo | Texto/Prompt |
|----|------|-------------|
| txtEmail | TextField | "Correo electrónico" |
| txtPassword | PasswordField | "Contraseña" |
| chkRecordarme | CheckBox | "Recordarme" |
| lnkOlvide | Hyperlink | "¿Olvidaste tu contraseña?" |
| btnLogin | Button | "Iniciar Sesión" |
| btnRegistro | Button | "Crear cuenta nueva" |
| lblTitulo | Label | "Iniciar Sesión" |
| lblSubtitulo | Label | "Accede a tu cuenta" |

## Mockup ASCII:
```
┌──────────────────────────────────────┐
│                                      │
│                                      │
│   ┌──────────────────────────────┐   │
│   │                              │   │
│   │      Iniciar Sesión          │   │
│   │     Accede a tu cuenta       │   │
│   │                              │   │
│   │  ┌──────────────────────┐    │   │
│   │  │ Correo electrónico   │    │   │
│   │  └──────────────────────┘    │   │
│   │                              │   │
│   │  ┌──────────────────────┐    │   │
│   │  │ Contraseña           │    │   │
│   │  └──────────────────────┘    │   │
│   │                              │   │
│   │  ☐ Recordarme    ¿Olvidaste? │   │
│   │                              │   │
│   │  ┌──────────────────────┐    │   │
│   │  │   INICIAR SESIÓN     │    │   │
│   │  └──────────────────────┘    │   │
│   │                              │   │
│   │  ──────── o ────────         │   │
│   │                              │   │
│   │  ┌──────────────────────┐    │   │
│   │  │  Crear cuenta nueva  │    │   │
│   │  └──────────────────────┘    │   │
│   │                              │   │
│   └──────────────────────────────┘   │
│                                      │
└──────────────────────────────────────┘
```
