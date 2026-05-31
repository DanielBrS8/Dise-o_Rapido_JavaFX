# Interfaz: Panel Principal (Dashboard)

## Layout principal: BorderPane
## Dimensiones: 900 x 600 px

## Estructura:

### TOP - Barra de navegación superior (HBox, fondo #2c3e50, altura 50px):
- **Logo/Nombre**: Label "Mi Aplicación" (texto blanco, negrita, 16px)
- **Espaciador** (flexible, HBox.hgrow=ALWAYS)
- **Barra búsqueda**: TextField con promptText "Buscar..." (ancho 250px)
- **Icono notificaciones**: Button "🔔" (estilo flat)
- **Nombre usuario**: Label "Daniel García" (texto blanco)
- **Avatar/Menú**: MenuButton "▼" con opciones: "Perfil", "Configuración", "Cerrar Sesión"

### LEFT - Menú lateral (VBox, fondo #34495e, ancho 220px):
- **Sección principal** (VBox, padding 10px):
  - Button "🏠 Inicio" (ancho completo, estilo menú activo)
  - Button "👥 Usuarios" (ancho completo, estilo menú)
  - Button "📊 Estadísticas" (ancho completo, estilo menú)
  - Button "📋 Proyectos" (ancho completo, estilo menú)
  - Button "📅 Calendario" (ancho completo, estilo menú)
- **Espaciador** (flexible, VBox.vgrow=ALWAYS)
- **Sección inferior** (VBox, padding 10px):
  - Button "⚙ Configuración" (ancho completo, estilo menú)
  - Button "❓ Ayuda" (ancho completo, estilo menú)

### CENTER - Área de contenido principal (VBox, padding 20px, fondo #ecf0f1):
- **Título de sección**: Label "Dashboard" (24px, negrita)
- **Subtítulo**: Label "Resumen general de la actividad" (14px, color #888)
- **Espaciado**: 20px
- **Fila de tarjetas** (HBox, spacing 15px):
  - **Tarjeta 1** (VBox, fondo blanco, padding 20px, borde redondeado):
    - Label "Usuarios Activos" (12px, color #888)
    - Label "1,234" (28px, negrita, color #3498db)
  - **Tarjeta 2** (VBox, fondo blanco, padding 20px):
    - Label "Proyectos" (12px, color #888)
    - Label "56" (28px, negrita, color #2ecc71)
  - **Tarjeta 3** (VBox, fondo blanco, padding 20px):
    - Label "Tareas Pendientes" (12px, color #888)
    - Label "89" (28px, negrita, color #e74c3c)
  - **Tarjeta 4** (VBox, fondo blanco, padding 20px):
    - Label "Completadas" (12px, color #888)
    - Label "342" (28px, negrita, color #9b59b6)
- **Espaciado**: 20px
- **Tabla de datos** (TableView, ancho completo, VBox.vgrow=ALWAYS):
  - Columna: "ID" (60px)
  - Columna: "Nombre" (200px)
  - Columna: "Estado" (120px)
  - Columna: "Fecha" (120px)
  - Columna: "Acciones" (100px)

### BOTTOM - Barra de estado (HBox, fondo #bdc3c7, altura 25px, padding 5px):
- Label "Conectado" (color verde)
- Espaciador flexible
- Label "v1.0.0"
- Label "Última actualización: hace 5 min"

## Componentes con fx:id:
| ID | Tipo | Descripción |
|----|------|-------------|
| lblAppName | Label | Nombre de la app |
| txtBuscar | TextField | Barra de búsqueda |
| btnNotificaciones | Button | Icono notificaciones |
| lblUsuario | Label | Nombre del usuario |
| menuUsuario | MenuButton | Menú desplegable usuario |
| btnInicio | Button | Menú: Inicio |
| btnUsuarios | Button | Menú: Usuarios |
| btnEstadisticas | Button | Menú: Estadísticas |
| btnProyectos | Button | Menú: Proyectos |
| btnCalendario | Button | Menú: Calendario |
| btnConfiguracion | Button | Menú: Configuración |
| btnAyuda | Button | Menú: Ayuda |
| lblTituloSeccion | Label | Título del contenido |
| lblCardUsuarios | Label | Valor tarjeta usuarios |
| lblCardProyectos | Label | Valor tarjeta proyectos |
| lblCardPendientes | Label | Valor tarjeta pendientes |
| lblCardCompletadas | Label | Valor tarjeta completadas |
| tblDatos | TableView | Tabla de datos principal |
| colId | TableColumn | Columna ID |
| colNombre | TableColumn | Columna Nombre |
| colEstado | TableColumn | Columna Estado |
| colFecha | TableColumn | Columna Fecha |
| colAcciones | TableColumn | Columna Acciones |
| lblEstado | Label | Estado de conexión |
| lblVersion | Label | Versión de la app |

## Mockup ASCII:
```
┌────────────────────────────────────────────────────────────────────┐
│ Mi Aplicación          [Buscar...        ] 🔔  Daniel García  ▼  │
├──────────────┬─────────────────────────────────────────────────────┤
│              │                                                     │
│  🏠 Inicio   │  Dashboard                                         │
│  👥 Usuarios │  Resumen general de la actividad                    │
│  📊 Estadíst │                                                     │
│  📋 Proyecto │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐              │
│  📅 Calenda  │  │Usuar.│ │Proye.│ │Pendi.│ │Compl.│              │
│              │  │1,234 │ │  56  │ │  89  │ │ 342  │              │
│              │  └──────┘ └──────┘ └──────┘ └──────┘              │
│              │                                                     │
│              │  ┌─────┬────────┬───────┬───────┬────────┐         │
│              │  │ ID  │Nombre  │Estado │Fecha  │Acciones│         │
│              │  ├─────┼────────┼───────┼───────┼────────┤         │
│              │  │ 001 │Proy A  │Activo │01/05  │  ...   │         │
│              │  │ 002 │Proy B  │Pausa  │15/04  │  ...   │         │
│  ⚙ Config   │  │ ... │  ...   │ ...   │ ...   │  ...   │         │
│  ❓ Ayuda    │  └─────┴────────┴───────┴───────┴────────┘         │
├──────────────┴─────────────────────────────────────────────────────┤
│ ● Conectado                              v1.0.0  Actualizado: 5m │
└────────────────────────────────────────────────────────────────────┘
```
