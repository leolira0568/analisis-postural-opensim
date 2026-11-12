# Análisis Postural OpenSim

Herramienta libre y de código abierto que detecta la postura de una persona en un video, dibuja su esqueleto con los ángulos de las articulaciones **en tiempo real** y exporta:

- el **video con el esqueleto** (`.mp4`), con los ángulos y la descripción de la postura en subtítulos;
- los **ángulos articulares para OpenSim** (`.mot`), calculados en el propio navegador, de todo el video o de fotogramas elegidos;
- los **marcadores 3D** (`.trc`);
- las **posturas para 3DSSPP** (`.sloc` o archivo de lote), el programa de análisis biomecánico de la Universidad de Míchigan.

Es un proyecto derivado de [OWAS Web](https://github.com/leolira0568/owas-web), sin codificación OWAS ni gráficas de resultados. Conserva su detección de posturas, todos sus ajustes de detección y su cálculo de ángulos para OpenSim.

Es **un solo archivo HTML** que funciona sin instalación ni conexión a internet: se abre con doble clic. MediaPipe, los modelos de OpenSim y el creador de MP4 van incluidos dentro (pesa unos 30 MB).

**▶ Usar en línea:** https://leolira0568.github.io/analisis-postural-opensim/

## Funciones

- **Video**: carga un video MP4 o WebM y lo recorre fotograma a fotograma, segundo a segundo o reproduciéndolo a 0,25×, 0,5×, 1× o 2×.
- **Detección en tiempo real**: al reproducir, detecta la postura de cada fotograma que se muestra con [MediaPipe Pose](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker) y dibuja el esqueleto, los ángulos de codos, hombros, caderas y rodillas (medidos en 3D, con un compás) y la inclinación del tronco. Con el video en pausa, detecta al llegar a cada fotograma. Usa la tarjeta gráfica (WebGL) si está disponible: en un equipo de prueba, unos 25 fotogramas por segundo con un video de 1920×1080, frente a unos 5 con el procesador.
- **Postura en palabras**: los subtítulos describen la espalda (recta, inclinada, girada o inclinada y girada), los brazos (cuántos quedan por encima del hombro) y las piernas (sentado, de pie con las piernas rectas o flexionadas, sobre una pierna, arrodillado o caminando), con la inclinación, el giro y la inclinación lateral del tronco y el ángulo de las rodillas.
- **Ajustes de detección** (los mismos de OWAS Web): límites de espalda inclinada, girada o inclinada de lado, rodilla flexionada, pie levantado y «caminando»; promedio de 3 fotogramas cercanos con el video en pausa; difuminado del rostro en 3 intensidades; color y grosor del esqueleto, y color y tamaño del texto de los ángulos y del compás.
- **Tramo a analizar**: «Inicio aquí» (tecla `I`) y «Fin aquí» (tecla `O`) marcan la parte del video que se analiza y se exporta, que se ve como una franja sobre la barra de tiempo. El análisis, el video exportado, el `.mot` y el `.trc` usan solo ese tramo; «Todo el video» lo quita. Se guarda en el proyecto.
- **Analizar todo el video** (o el tramo): detecta la postura en cada fotograma. Después, la reproducción muestra el esqueleto de todos los fotogramas sin saltos. Exportar el video o el `.mot` analiza lo que falte.
- **Fotogramas guardados**: «Guardar fotograma» (tecla `Enter`) conserva la imagen del momento actual con el esqueleto, la postura, los ángulos y una nota. Aparecen como tarjetas y como marcas numeradas bajo la barra de tiempo, y se pueden ampliar, recorrer (`B` / `N`) y eliminar.
- **Exportar**:
  - **Video con esqueleto (`.mp4`)**: del video completo o del tramo elegido; se crea en el navegador, fotograma a fotograma, en H.264 y sin sonido, con el esqueleto, los ángulos, el rostro difuminado y una franja de subtítulos debajo de la imagen. Necesita Chrome o Edge actualizados (WebCodecs).
  - **OpenSim (`.mot`)**: ángulos articulares del modelo de **cuerpo completo** (por defecto) o de **Rajagopal 2016**, de todo el video o del tramo (todos los fotogramas, o 10, 5 o 1 muestras por segundo) o solo de los fotogramas guardados. Señala las posturas poco fiables, permite excluirlas y descarga una revisión de calidad (`.csv`). El modelo queda apoyado en el suelo.
  - **Marcadores (`.trc`)**: los puntos 3D del cuerpo, con las mismas posturas.
  - **3DSSPP** *(nuevo en 1.1)*: las mismas posturas como posiciones de las articulaciones en cm, en los ejes de 3DSSPP. El **`.sloc`** se abre con *Animation → Import LOC File* (una postura por fotograma, con la fuerza indicada en cada mano). El **archivo de lote** se ejecuta con *Task Input → Run Batch File*: analiza todas las posturas con el sexo, la estatura y el peso indicados (o el percentil 50), la fuerza en cada mano y la persona de pie o sentada según la postura detectada, y guarda los resultados en `…_export.txt`. Sigue el formato del manual de 3DSSPP 7.1 (secciones 6.13 y 10.4). La cabeza, C7/T1, la articulación esternoclavicular, L5/S1 y el centro de agarre se estiman a partir de los puntos detectados.
- **Proyectos `.apo`**: guardan los fotogramas guardados (con sus imágenes) y el análisis del video. El video no se copia dentro: al abrir el proyecto, se vuelve a cargar.
- **Autoguardado** en el navegador y **tema claro u oscuro**.

## Uso

1. Abra `AnalisisPosturalOpenSim.html` con doble clic (o la versión en línea).
2. Pulse **Cargar video**. Indique los **fotogramas por segundo** con los que se recorrerá al analizarlo y exportarlo (normalmente, los del video: 30 o 60).
3. Si solo le interesa una parte del video, marque el tramo con **Inicio aquí** y **Fin aquí**.
4. Reproduzca el video: el esqueleto y la postura se dibujan en tiempo real. Pause en los momentos que quiera conservar y pulse **Guardar fotograma**.
5. Pulse **Exportar** y elija el video con el esqueleto, el `.mot` o el `.trc`.

### Ver el resultado en OpenSim

1. En el diálogo **Exportar**, elija el modelo y pulse **Descargar modelo**. El de cuerpo completo se descarga como `.zip` desde GitHub: descomprímalo. El de Rajagopal 2016 va incluido en la aplicación.
2. En OpenSim, *File → Open Model* con el modelo (`cyclistFullBodyMuscle_OWAS.osim`, junto a su carpeta `Geometry`, o `Rajagopal2016_OWAS.osim`).
3. *File → Load Motion* con el `.mot`.

En el modelo de cuerpo completo, la flexión, la inclinación y el giro del tronco se reparten entre la pelvis y las 17 vértebras con proporciones supuestas, no medidas, y el cuello se estima con la nariz y las orejas. La revisión de calidad no comprueba las rodillas: sus ángulos no son fiables. El cálculo, comparado con la cinemática inversa de OpenSim 4.6 en OWAS Web, difirió como máximo 1,4° en el tronco y las piernas en las posturas fiables.

## Privacidad

Todo se procesa en el equipo: la aplicación no envía datos a ningún servidor y una política de seguridad de contenido (CSP) le impide conectarse a internet. El rostro de la persona se difumina por defecto en las imágenes guardadas y en el video exportado. Ver [PRIVACIDAD.md](PRIVACIDAD.md).

## Desarrollo

- `src/AnalisisPosturalOpenSim.html`: código fuente de la aplicación.
- `build.py`: genera `AnalisisPosturalOpenSim.html` incrustando en base64 los archivos de `vendor/` (`python build.py`).
- `vendor/`: MediaPipe Tasks Vision 0.10.35 y el modelo Pose Landmarker (full), los modelos de OpenSim y mp4-muxer 5.2.1, cada uno con su licencia.
- `herramientas/ensamblar.py` y `herramientas/plantilla.html`: cómo se derivó la fuente de OWAS Web 4.20 (se usaron una sola vez; los cambios posteriores se hacen en `src/`).

Para probar sin compilar, sirva la carpeta por HTTP (`python -m http.server`) y abra `src/AnalisisPosturalOpenSim.html`: lee los archivos de `vendor/` directamente.

## Versiones

- **1.1**: exportación de las posturas a 3DSSPP, como archivo de ubicaciones `.sloc` o como archivo de lote que analiza todas las posturas y exporta los resultados.
- **[1.0](https://github.com/leolira0568/analisis-postural-opensim/releases/tag/v1.0)**: primera versión, derivada de OWAS Web 4.20. Video con detección en tiempo real (con la tarjeta gráfica si está disponible), tramo del video a analizar y exportar, análisis de todo el video o del tramo, fotogramas guardados con nota, exportación del video con el esqueleto (`.mp4`), del `.mot` de todo el video o de los fotogramas guardados (cuerpo completo por defecto, o Rajagopal 2016) y del `.trc`, y proyectos `.apo`.

## Licencias

- Análisis Postural OpenSim: [MIT](LICENSE), © 2026 Leonardo Lira.
- MediaPipe y el modelo Pose Landmarker: [Apache 2.0](vendor/mediapipe/LICENSE), © Google LLC.
- Modelo Rajagopal 2016: [MIT](vendor/opensim/LICENSE), © 2015 Stanford University.
- Modelo de cuerpo completo: [MIT](vendor/opensim/LICENSE-wilkinson), © 2021 Ross Wilkinson.
- mp4-muxer: [MIT](vendor/mp4-muxer/LICENSE), © 2023 Vanilagy.
- Iconos basados en [Lucide](https://lucide.dev) (ISC).
