import streamlit as st

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Autodiagnóstico Integral", layout="wide")
st.title("📍 Autodiagnóstico Integral")
st.markdown("Evalúa tu estado simbólico actual en 7 dimensiones clave de tu vida cotidiana.")

# FUNCIONES AUXILIARES
st.markdown("---")

# 1. FISIOLÓGICA / BIOLÓGICA
st.header("1. Fisiológica / Biológica")
salud = st.radio("¿Cómo percibes tu salud física actual?", ["Saludable", "Síntomas leves", "En tratamiento", "Condición crónica"])
energia = st.slider("¿Cuál es tu nivel de energía vital hoy?", 0, 100, 50)
alimentacion = st.radio("¿Cómo ha sido tu alimentación reciente?", ["Caótica", "Funcional", "Consciente"])
sueno = st.slider("¿Cómo calificas la calidad de tu descanso/sueño?", 0, 10, 5)
dolor = st.multiselect("¿Sientes dolor físico en alguna zona?", ["Ninguno", "Cuello", "Espalda", "Cabeza", "Pecho", "Piernas", "Otros"])

# 2. EMOCIONAL / AFECTIVA
st.header("2. Emocional / Afectiva")
emocion = st.selectbox("¿Qué emoción predomina en ti hoy?", ["Tranquilidad", "Ansiedad", "Alegría", "Tristeza", "Ira", "Culpa", "Confusión"])
relacion_conmigo = st.slider("¿Qué tan en paz estás contigo hoy?", 0, 10, 5)
carga_emocional = st.radio("¿Cargas algo emocional que no has resuelto?", ["Sí", "No", "No lo sé"])
autoexpresion = st.slider("¿Qué tanto te estás expresando emocionalmente hoy?", 0, 10, 5)

# 3. MENTAL / COGNITIVA
st.header("3. Mental / Cognitiva")
claridad = st.slider("¿Qué tan clara está tu mente hoy?", 0, 100, 50)
dialogo_interno = st.radio("¿Cómo es tu diálogo interno hoy?", ["Apoyo", "Crítica", "Caos", "Silencio"])
rumiacion = st.radio("¿Sientes pensamientos repetitivos sin salida?", ["Sí", "No"])
imaginacion = st.slider("¿Qué tan activa está tu imaginación hoy?", 0, 10, 5)

# 4. SOCIAL / RELACIONAL
st.header("4. Social / Relacional")
contacto = st.radio("¿Has tenido conexión genuina con alguien hoy?", ["Sí", "No", "Muy poco"])
apoyo = st.slider("¿Qué tanto sientes que podrías pedir ayuda si la necesitaras?", 0, 10, 5)
pareja = st.radio("¿Cómo está tu vínculo íntimo/afectivo actual (si aplica)?", ["Conectado", "Distante", "Inexistente", "No aplica"])
comunicacion = st.slider("¿Qué tan bien te estás comunicando con tu entorno?", 0, 10, 5)

# 5. PROFESIONAL / FUNCIONAL
st.header("5. Profesional / Funcional")
proposito = st.slider("¿Tu actividad de hoy tiene sentido para ti?", 0, 10, 5)
tareas = st.slider("¿Cuántas tareas sientes pendientes simbólicamente?", 0, 20, 5)
intercambio = st.radio("¿Estás dando más energía de la que recibes?", ["Sí", "No", "Balanceado"])
trabajo_sentido = st.selectbox("¿Cómo describirías tu relación con el trabajo actual?", ["Pasión", "Carga", "Hábito", "Rechazo"])

# 6. ESPIRITUAL / EXISTENCIAL
st.header("6. Espiritual / Existencial")
sentido = st.slider("¿Sientes que tu vida avanza hacia algo significativo?", 0, 10, 5)
conexion = st.radio("¿Sientes conexión con algo más grande?", ["Sí", "No", "Lo estoy buscando"])
presente = st.slider("¿Qué tanto estás en el presente hoy?", 0, 10, 5)
silencio = st.radio("¿Tienes espacios de silencio interior hoy?", ["Sí", "No", "Muy pocos"])

# 7. ENTORNO / ESTABILIDAD
st.header("7. Entorno / Estabilidad")
orden = st.slider("¿Qué tan ordenado está tu entorno físico hoy?", 0, 10, 5)
presion = st.slider("¿Qué tanta presión externa percibes hoy?", 0, 100, 50)
ruido = st.radio("¿Tu entorno es ruidoso o caótico?", ["Sí", "No", "Intermitente"])
estabilidad = st.radio("¿Sientes estabilidad material suficiente?", ["Sí", "No", "Vulnerable"])

st.markdown("---")
st.success("Diagnóstico inicial completado. Puedes ahora pasar a tu primer módulo simbólico: NEUTRAL")
