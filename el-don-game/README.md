# El Don — Lecciones de El Padrino 🎩

Un juego de decisiones para celular inspirado en las enseñanzas de *El Padrino*.

## De qué se trata

Eres el nuevo jefe de la familia. Cada semana, un personaje te presenta un dilema
y debes elegir entre dos caminos deslizando la carta (como en *Reigns*) o tocando
los botones. Cada decisión te enseña una lección real de la película:

> "Mantén cerca a tus amigos, pero más cerca a tus enemigos."

## Los cuatro recursos

Cada decisión sube o baja tus recursos. El objetivo es el **equilibrio**:
si cualquiera llega a 0 **o** a 100, tu reinado termina.

| Recurso | Significado |
|---|---|
| 🤝 Respeto | Cuánto te temen y te obedecen |
| 👪 Familia | La lealtad y unión de los tuyos |
| 💰 Dinero | Las arcas de la organización |
| 🤫 Discreción | Qué tan lejos estás de la policía y los periódicos |

Por ejemplo: mucho respeto une a tus rivales en tu contra; demasiado dinero
atrae al fisco; poca discreción trae a los federales a tu puerta.

## Cómo jugar

Es un solo archivo HTML sin dependencias. Opciones:

1. **En el celular**: abre `index.html` en el navegador (puedes subirlo a
   GitHub Pages, Netlify, etc.).
2. **En local**:
   ```bash
   cd el-don-game
   python3 -m http.server 8000
   ```
   y abre `http://localhost:8000` en tu navegador o celular (misma red WiFi).

## Controles

- **Desliza** la carta a la izquierda o derecha para elegir.
- O **toca** los botones bajo la carta.
- Al pasar el dedo, los puntos dorados sobre las barras indican qué recursos
  afectará esa decisión (pero no cuánto ni en qué dirección — como en la vida).

## Contenido

24 cartas con dilemas basados en escenas y frases de El Padrino I y II:
la oferta que no se puede rechazar, el rechazo a los narcóticos, los favores
de Bonasera, la impulsividad de Sonny, la traición de Fredo y Tessio,
la advertencia sobre Barzini, la sociedad con Hyman Roth, y más.

## Ideas para seguir creciendo

- Cadenas de cartas (una decisión desbloquea consecuencias semanas después)
- Personajes recurrentes con memoria de tus decisiones
- Logros por descubrir todos los finales
- Música y efectos de sonido
- Empaquetarlo como app con Capacitor para publicarlo en las tiendas
