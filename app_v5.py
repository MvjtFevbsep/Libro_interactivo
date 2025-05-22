import streamlit as st
import matplotlib.pyplot as plt

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="NEUTRAL — Presión No Expresada", layout="centered")

# ENCABEZADO
st.title("NEUTRAL — Presión No Expresada")
st.subheader("No estás en movimiento, pero ya estás encendido.")
st.markdown("Visualiza la presión que se acumula en ti cuando no accionas. No para soltarla aún, sino para entender su forma.")

# EDAD
edad = st.number_input("¿Cuál es tu edad?", min_value=10, max_value=120, value=29)

# INPUTS
deseo_no_ejecutado = st.slider(
    "¿Cuántos deseos claros tienes hoy que no has comenzado a mover?",
    0, 10, 3
)

compromisos = st.slider(
    "Número de cosas que prometiste hacer y no has hecho:",
    0, 10, 2
)

tension = st.multiselect(
    "¿Dónde sientes presión física?",
    ["Cuello", "Mandíbula", "Espalda baja", "Pecho", "Manos", "Abdomen", "Piernas"]
)

dialogos = st.radio(
    "¿Qué estás hablando contigo en silencio hoy?",
    ["Nada", "Justificaciones", "Reclamos", "Dudas", "Motivaciones", "Proyecciones"]
)

energia_cont = st.slider(
    "¿Cuán enérgico te sientes hoy?",
    0, 100, 50
)

# EVALUACIÓN
if st.button("Evaluar presión simbólica"):
    presion_total = deseo_no_ejecutado * 2 + energia_cont / 10 + len(tension) + compromisos

    st.markdown("### 🧭 Diagnóstico simbólico")
    st.write(f"**Edad declarada:** {edad} años")
    st.write(f"**Índice de presión acumulada:** {presion_total:.1f} unidades simbólicas")

    tipo = "Mental" if dialogos in ["Justificaciones", "Proyecciones"] else \
           "Emocional" if dialogos in ["Reclamos", "Dudas"] else \
           "Física" if len(tension) >= 3 else "Ligera"

    st.write(f"**Tipo de carga predominante:** {tipo}")

    if presion_total > 15:
        st.warning("⚠️ Riesgo de fuga alto: presión acumulada sin dirección puede explotar o convertirse en fatiga.")
    elif presion_total > 8:
        st.info("⚙️ Presión moderada: energía disponible para ser transformada si eliges dirección.")
    else:
        st.success("✅ Presión ligera: aún puedes contener sin consecuencias.")

    st.caption("Siente tu torque antes de avanzar.")

    # VISUALIZACIÓN EN PLANO DE 4 EJES
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_title("Mapa de presión simbólica")
    ax.set_xlabel("Deseo (+) ↔ Compromisos no resueltos (-)")
    ax.set_ylabel("Energía disponible (+) ↔ Presión física (-)")

    # Puntos individuales
    ax.scatter(deseo_no_ejecutado, 0, color='blue', label='Deseo no ejecutado')
    ax.scatter(-compromisos, 0, color='red', label='Compromisos no resueltos')
    ax.scatter(0, energia_cont / 10, color='green', label='Energía disponible')
    ax.scatter(0, -len(tension), color='orange', label='Presión física')

    ax.legend()
    st.pyplot(fig)
