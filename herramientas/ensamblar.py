"""Crea src/AnalisisPosturalOpenSim.html a partir de herramientas/plantilla.html y del código de OWAS Web.

Se usó una sola vez, al derivar este proyecto de OWAS Web 4.20: cada marcador @@COPY a-b@@ de la plantilla
se reemplaza por las líneas a..b de src/OWASWeb.html de OWAS Web (detección, dibujo del esqueleto, ajustes,
difuminado del rostro y cinemática inversa), con los pocos cambios de nombres indicados abajo.

Uso: python herramientas/ensamblar.py <ruta de src/OWASWeb.html de OWAS Web 4.20>
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
owas = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8').splitlines()
tpl = (ROOT / 'herramientas' / 'plantilla.html').read_text(encoding='utf-8')


def copia(m):
    a, b = int(m.group(1)), int(m.group(2))
    return '\n'.join(owas[a - 1:b])


out = re.sub(r'(?://|/\*)@@COPY (\d+)-(\d+)@@(?:\*/)?', copia, tpl)
CAMBIOS = [
    ("localStorage.getItem('winowas.detect')", "localStorage.getItem('apos.detect')"),
    ("localStorage.setItem('winowas.detect',", "localStorage.setItem('apos.detect',"),
    ("localStorage.setItem('owasweb.theme',", "localStorage.setItem('apos.theme',"),
    ('function classifyOWAS(W, N){', 'function classifyPosture(W, N){'),
    ('// Sin compilar (src/OWASWeb.html servido', '// Sin compilar (src/AnalisisPosturalOpenSim.html servido'),
    ('function ikFrame(s, row, prev){', 'function ikFrame(s, row, prev, fast = false){'),
    ('const starts = [start, set(start, bent), set(start, both), set(start, {...bent, ...both})].map(toP);',
     '// fast: en una secuencia continua basta con partir de la postura anterior y de la inicial\n'
     '  const starts = (fast && prev ? [start] : [start, set(start, bent), set(start, both), set(start, {...bent, ...both})]).map(toP);'),
]
for a, b in CAMBIOS:
    if out.count(a) != 1:
        raise SystemExit(f'Se esperaba una vez: {a!r} ({out.count(a)})')
    out = out.replace(a, b)
for resto in ('winowas', 'owasweb', 'OWASWeb'):
    for linea in out.splitlines():
        if resto in linea:
            print('Aviso, queda una referencia:', linea.strip()[:120])
(ROOT / 'src').mkdir(exist_ok=True)
(ROOT / 'src' / 'AnalisisPosturalOpenSim.html').write_text(out, encoding='utf-8', newline='\n')
print('src/AnalisisPosturalOpenSim.html:', len(out.splitlines()), 'líneas')
