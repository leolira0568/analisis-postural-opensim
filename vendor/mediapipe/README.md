# MediaPipe (copia local)

Archivos de terceros que `build.py` incrusta en `AnalisisPosturalOpenSim.html` para que la detección de posturas funcione sin internet.

| Archivo | Origen |
|---|---|
| `vision_bundle.mjs` | [`@mediapipe/tasks-vision` 0.10.35](https://www.npmjs.com/package/@mediapipe/tasks-vision/v/0.10.35), archivo `vision_bundle.mjs` |
| `vision_wasm_internal.js` | mismo paquete, `wasm/vision_wasm_internal.js` |
| `vision_wasm_internal.wasm` | mismo paquete, `wasm/vision_wasm_internal.wasm` |
| `pose_landmarker_full.task` | [Pose Landmarker (full), float16, versión 1](https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/1/pose_landmarker_full.task) |

El paquete se verificó con la suma de integridad publicada en npm. `SHA256SUMS` contiene las sumas de cada archivo.

MediaPipe y el modelo Pose Landmarker son © Google LLC y se distribuyen bajo la licencia Apache 2.0 (ver `LICENSE`). Solo se incluye la variante WebAssembly con SIMD, compatible con todos los navegadores actuales.
