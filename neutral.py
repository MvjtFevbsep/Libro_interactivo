import streamlit as st
import matplotlib.pyplot as plt

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="NEUTRAL — Presión No Expresada", layout="centered")

# ENCABEZADO
st.title("NEUTRAL — Presión No Expresada")
st.subheader("No estás en movimiento, pero ya estás encendido.")
st.markdown("Visualiza la presión que se acumula en ti cuando no accionas. No para soltarla aún, sino para entender su forma.")

# INPUTS
deseo_no_ejecutado = st.slider(
    "¿Cuántos deseos claros tienes hoy que no has comenzado a mover?",
    0, 10, 3
)

compromisos = st.text_area(
    "Enumera brevemente 1 a 3 cosas que te prometiste hacer y no has hecho:",
    placeholder="Ej. Terminar ese pendiente, hablar con alguien, etc."
)

tension = st.multiselect(
    "¿Dónde sientes presión física no liberada?",
    ["Cuello", "Mandíbula", "Espalda baja", "Pecho", "Manos", "Abdomen", "Piernas"]
)

dialogos = st.radio(
    "¿Qué estás hablando contigo en silencio hoy?",
    ["Nada", "Justificaciones", "Reclamos", "Dudas", "Motivaciones", "Proyecciones"]
)

energia_cont = st.slider(
    "¿Cuánta energía sientes acumulada sin dirección?",
    0, 100, 50
)

# EVALUACIÓN
if st.button("Evaluar presión simbólica"):
    presion_total = deseo_no_ejecutado * 2 + energia_cont / 10 + len(tension)

    st.markdown("### 🧭 Diagnóstico simbólico")
    st.write(f"**Índice de presión acumulada:** {presion_total:.1f} unidades simbólicas")
    
    tipo = "Mental" if dialogos in ["Justificaciones", "Proyecciones"] else \
           "Emocional" if dialogos in ["Reclamos", "Dudas"] else \
           "Física" if len(tension) >= 3 else "Ligera"
    
    st.write(f"**Tipo de carga predominante:** {tipo}")
    
    if presion_total > 12:
        st.warning("⚠️ Riesgo de fuga alto: presión acumulada sin dirección puede explotar o convertirse en fatiga.")
    elif presion_total > 6:
        st.info("⚙️ Presión moderada: energía disponible para ser transformada si eliges dirección.")
    else:
        st.success("✅ Presión ligera: aún puedes contener sin consecuencias.")

    st.caption("Siente tu torque antes de avanzar.")

    # VISUALIZACIÓN
    fig, ax = plt.subplots()
    niveles = [deseo_no_ejecutado, len(tension), energia_cont / 10]
    etiquetas = ["Deseo", "Tensión física", "Energía sin salida"]
    ax.bar(etiquetas, niveles, color=["#ff6666", "#ffcc99", "#66b3ff"])
    ax.set_ylabel("Nivel simbólico")
    st.pyplot(fig)
  
