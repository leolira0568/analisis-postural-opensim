# Declaración de privacidad y seguridad de Análisis Postural OpenSim

Análisis Postural OpenSim está diseñada para proteger la identidad de las personas que aparecen en los videos que se analizan.

## Qué datos maneja la aplicación

- Los videos que el usuario abre. Pueden mostrar rostros y otros rasgos que identifican a una persona.
- Los puntos del cuerpo detectados en cada fotograma (en la imagen y en 3D), la postura y los ángulos medidos.
- Los fotogramas guardados: su imagen, su momento en el video, su postura, sus ángulos y la nota que escriba el usuario.

## Dónde se procesan

- **Todo se procesa en el equipo del usuario**, dentro del navegador: la detección de posturas, el cálculo de los ángulos para OpenSim y la creación del video exportado. La aplicación no envía datos a ningún servidor, no usa cookies, ni herramientas de analítica, ni servicios externos.
- MediaPipe Pose, los modelos de OpenSim y mp4-muxer van **incluidos dentro del archivo** y se ejecutan localmente.
- Los videos se abren desde el equipo y **nunca se suben a internet**. El video original no se copia en el proyecto.

## Medidas de seguridad

1. **Sin conexiones de red.** Una política de seguridad de contenido (Content Security Policy) impide que la aplicación se conecte a servidores externos, envíe formularios o cargue código de otros sitios. «Descargar modelo» del cuerpo completo abre su página de descarga en GitHub en una pestaña nueva, sin enviar datos.
2. **Rostros difuminados.** La opción «Difuminar el rostro en las imágenes guardadas y en el video exportado» (activada por defecto) pixela la cara de la persona detectada, de la frente al mentón, con intensidad suave, media (por defecto) o fuerte. El cuello y la postura de la cabeza siguen visibles, por lo que el pelo, las orejas o la ropa pueden seguir permitiendo reconocer a la persona. Solo funciona en los fotogramas en los que la detección encuentra a la persona: revise el resultado antes de compartirlo.
3. **Sin sonido ni metadatos.** El video exportado no lleva sonido, y las imágenes y el video se vuelven a codificar, por lo que no conservan datos como la ubicación GPS o el modelo de la cámara.
4. **Autoguardado opcional.** El trabajo se guarda automáticamente en el navegador del equipo. En equipos compartidos puede desactivarse en *Ayuda, privacidad y licencias*.
5. **Borrado de datos locales.** El botón «Borrar los datos guardados en este navegador» elimina el autoguardado y las preferencias de la aplicación y cierra el proyecto abierto.

## Dónde quedan los datos

- En el **autoguardado del navegador** del equipo, hasta que el usuario lo borre o lo desactive.
- En los **archivos que el usuario guarda o exporta**: proyectos `.apo`, videos `.mp4` y archivos para OpenSim (`.mot`, `.trc` y `.csv`). Los proyectos y los videos exportados contienen datos personales. Los proyectos y los `.trc` guardan además los puntos 3D del cuerpo de la persona.

## Versión en línea

La versión en línea se sirve desde GitHub Pages. GitHub puede registrar datos técnicos de la visita, como la dirección IP, según su [declaración de privacidad](https://docs.github.com/es/site-policy/privacy-policies/github-general-privacy-statement). Los videos y los datos del análisis no se envían. Para la máxima privacidad, descargue `AnalisisPosturalOpenSim.html` y úselo sin conexión.

## Protocolo recomendado

1. Informar a las personas grabadas del propósito del análisis y obtener su consentimiento antes de grabar.
2. Grabar solo lo necesario y, si es posible, encuadrar el cuerpo sin mostrar el rostro.
3. Mantener activado el difuminado de rostros y revisar las imágenes y el video exportado antes de compartirlos.
4. Guardar los videos y proyectos en carpetas protegidas o cifradas y compartirlos solo por medios seguros con quien deba verlos.
5. En equipos compartidos, desactivar el autoguardado y borrar los datos del navegador al terminar.
6. Eliminar los videos y proyectos cuando ya no sean necesarios, y cumplir la normativa de protección de datos personales del país.

Quien realiza el análisis es responsable de los datos que recoge. El autor de la aplicación no recibe ningún dato.
