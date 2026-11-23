-- =====================================================
-- ACTUALIZACION DE UNA BASE EXISTENTE
-- No elimina tablas ni registros.
-- Mantiene los privilegios SELECT, INSERT, UPDATE y DELETE.
-- =====================================================

CREATE DATABASE IF NOT EXISTS encuestapru
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE encuestapru;

CREATE USER IF NOT EXISTS 'ezequielmr'@'localhost'
  IDENTIFIED BY 'clave123';

GRANT SELECT, INSERT, UPDATE, DELETE
  ON encuestapru.* TO 'ezequielmr'@'localhost';

FLUSH PRIVILEGES;

ALTER TABLE usuario
  MODIFY contrasena VARCHAR(255) NOT NULL;

ALTER TABLE administrador
  ADD UNIQUE INDEX uq_administrador_usuario (id_usuario);

ALTER TABLE administrador
  ADD CONSTRAINT fk_administrador_usuario
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
  ON DELETE CASCADE;

ALTER TABLE encuestado
  ADD CONSTRAINT fk_encuestado_usuario
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
  ON DELETE CASCADE;

ALTER TABLE encuesta
  ADD CONSTRAINT fk_encuesta_administrador
  FOREIGN KEY (id_admin) REFERENCES administrador(id_usuario)
  ON DELETE CASCADE;

ALTER TABLE encuesta
  ADD CONSTRAINT fk_encuesta_categoria
  FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
  ON DELETE SET NULL;

ALTER TABLE pregunta
  ADD CONSTRAINT fk_pregunta_encuesta
  FOREIGN KEY (id_encuesta) REFERENCES encuesta(id_encuesta)
  ON DELETE CASCADE;

ALTER TABLE opcion
  ADD CONSTRAINT fk_opcion_pregunta
  FOREIGN KEY (id_pregunta) REFERENCES pregunta(id_pregunta)
  ON DELETE CASCADE;

ALTER TABLE preguntaabierta
  ADD CONSTRAINT fk_preguntaabierta_pregunta
  FOREIGN KEY (id_pregunta) REFERENCES pregunta(id_pregunta)
  ON DELETE CASCADE;

ALTER TABLE preguntaescala
  ADD CONSTRAINT fk_preguntaescala_pregunta
  FOREIGN KEY (id_pregunta) REFERENCES pregunta(id_pregunta)
  ON DELETE CASCADE;

ALTER TABLE preguntamultiple
  ADD CONSTRAINT fk_preguntamultiple_pregunta
  FOREIGN KEY (id_pregunta) REFERENCES pregunta(id_pregunta)
  ON DELETE CASCADE;

ALTER TABLE participacionencuesta
  ADD CONSTRAINT fk_participacion_encuestado
  FOREIGN KEY (id_encuestado) REFERENCES encuestado(id_usuario)
  ON DELETE CASCADE;

ALTER TABLE participacionencuesta
  ADD CONSTRAINT fk_participacion_encuesta
  FOREIGN KEY (id_encuesta) REFERENCES encuesta(id_encuesta)
  ON DELETE CASCADE;

ALTER TABLE respuesta
  ADD CONSTRAINT fk_respuesta_participacion
  FOREIGN KEY (id_participacion)
  REFERENCES participacionencuesta(id_participacion)
  ON DELETE CASCADE;

ALTER TABLE respuesta
  ADD CONSTRAINT fk_respuesta_pregunta
  FOREIGN KEY (id_pregunta) REFERENCES pregunta(id_pregunta)
  ON DELETE CASCADE;

ALTER TABLE reporte
  ADD CONSTRAINT fk_reporte_encuesta
  FOREIGN KEY (id_encuesta) REFERENCES encuesta(id_encuesta)
  ON DELETE CASCADE;
