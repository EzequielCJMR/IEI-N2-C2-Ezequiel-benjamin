# Diagrama de clases

```mermaid

classDiagram
    class Usuario {
        +id_usuario
        +rut
        +nombre
        +email
        +contrasena
        +rol
        +activo
        +fecha_registro

        +iniciarSesion(email: string, contrasena: string) bool
        +cerrarSesion() void
        +actualizarPerfil(usuario: Usuario) bool
        +obtenerPermisos() list
    }

    class Administrador {
        +id_administrador
        +id_usuario
        +cargo
        +fecha_contratacion

        +crearEncuesta(encuesta: Encuesta) bool
        +cerrarEncuesta(encuesta: Encuesta) bool
        +eliminarEncuesta(encuesta: Encuesta) bool
        +verEstadisticas(encuesta: Encuesta) Reporte
        +obtenerPermisos() list
    }

    class Encuestado {
        +id_usuario
        +fecha_nacimiento
        +genero
        +ocupacion
        +pais

        +responderEncuesta(encuesta: Encuesta, respuestas: list) bool
        +verHistorialRespuestas() list
        +obtenerPermisos() list
    }

    class Categoria {
        +id_categoria
        +nombre
        +descripcion

        +crearCategoria(categoria: Categoria) bool
        +listarEncuestasPorCategoria() list
    }

    class Encuesta {
        +id_encuesta
        +titulo
        +descripcion
        +estado
        +fecha_creacion
        +fecha_expiracion
        +id_admin
        +id_categoria

        +agregarPregunta(pregunta: Pregunta) bool
        +eliminarPregunta(pregunta: Pregunta) bool
        +publicar() bool
        +cerrar() bool
        +estaVigente() bool
        +obtenerResultados() Reporte
    }

    class Pregunta {
        +id_pregunta
        +id_encuesta
        +texto
        +tipo
        +orden
        +obligatoria

        +validarRespuesta(valor: string) bool
        +calcularResultado() Reporte
    }

    class PreguntaAbierta {
        +max_caracteres

        +validarRespuesta(valor: string) bool
        +calcularResultado() Reporte
    }

    class PreguntaEscala {
        +escala_min
        +escala_max

        +validarRespuesta(valor: string) bool
        +calcularResultado() Reporte
    }

    class PreguntaMultiple {
        +permite_multiples

        +agregarOpcion(opcion: Opcion) bool
        +validarRespuesta(valor: string) bool
        +calcularResultado() Reporte
    }

    class Opcion {
        +id_opcion
        +id_pregunta
        +texto
        +contador_votos

        +incrementarContador() void
        +obtenerPorcentaje(total: int) float
    }

    class Participacionencuesta {
        +id_participacion
        +id_encuesta
        +id_encuestado
        +fecha_participacion
        +completada

        +iniciarParticipacion() bool
        +finalizarParticipacion() bool
        +listarRespuestas() list
    }

    class Respuesta {
        +id_respuesta
        +id_participacion
        +id_pregunta
        +valor
        +fecha_respuesta

        +registrarRespuesta() bool
        +obtenerValor() string
    }

    class Reporte {
        +id_reporte
        +id_encuesta
        +fecha_generacion
        +total_participantes
        +total_respuestas
        
        +generarReporte(encuesta: Encuesta) void
        +exportarPDF() void
    }

    Usuario "1" --> "0..1" Administrador : id_usuario
    Usuario "1" --> "0..1" Encuestado : id_usuario
    Administrador "1" --> "*" Encuesta : id_admin
    Categoria "1" --> "*" Encuesta : id_categoria
    Encuesta "1" --> "*" Pregunta : id_encuesta
    Pregunta "1" --> "*" Opcion : id_pregunta
    Encuesta "1" --> "*" Participacionencuesta : id_encuesta
    Encuestado "1" --> "*" Participacionencuesta : id_encuestado
    Participacionencuesta "1" --> "*" Respuesta : id_participacion
    Pregunta "1" --> "*" Respuesta : id_pregunta
    Encuesta "1" --> "*" Reporte : id_encuesta

    Pregunta <|-- PreguntaAbierta
    Pregunta <|-- PreguntaEscala
    Pregunta <|-- PreguntaMultiple
