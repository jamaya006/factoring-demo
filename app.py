import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Demo Factoring", layout="wide")
st.title("💼 Plataforma de Automatización de Factoring")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🧾 Clientes y Contratos",
    "💰 Fondos de Inversionistas",
    "📄 Notas de Crédito",
    "📊 Comisiones y Distribución",
    "📈 Dashboard Operativo",
    "🕵️‍♂️ Análisis de Anomalías"
])

with tab1:
    st.header("Gestión de Clientes y Contratos")
    with st.form("form_cliente"):
        nombre = st.text_input("Nombre del Cliente")
        ruc = st.text_input("RUC")
        monto_financiado = st.number_input("Monto financiado del reclamo (USD)", min_value=0.0)
        tipo_reclamo = st.selectbox("Tipo de Reclamo", ["IVA", "IR", "ISD"])
        kyc_ok = st.checkbox("Documentación KYC completa")
        contrato_firmado = st.checkbox("Contrato firmado")
        garantia_validada = st.checkbox("Garantía validada")
        submit = st.form_submit_button("Registrar Cliente")
        if submit:
            if not nombre or not ruc or monto_financiado == 0.0:
                st.error("Por favor completa todos los campos obligatorios.")
            elif not (kyc_ok and contrato_firmado and garantia_validada):
                st.warning("Faltan requisitos documentales.")
            else:
                st.success(f"✅ Cliente '{nombre}' registrado con reclamo de tipo {tipo_reclamo}.")
                st.info("Cliente vinculado con el SRI para trazabilidad tributaria.")

with tab2:
    st.header("Administración de Fondos de Inversionistas")
    with st.form("form_fondos"):
        inversionista = st.text_input("Nombre del Inversionista")
        tipo = st.selectbox("Tipo de Inversionista", ["Interno", "Externo"])
        monto_aporte = st.number_input("Monto del Aporte (USD)", min_value=0.0)
        operaciones = st.number_input("Número de Operaciones Financiadas", min_value=1)
        submitted = st.form_submit_button("Registrar Aporte")
        if submitted:
            if not inversionista or monto_aporte == 0.0:
                st.error("Nombre del inversionista y monto son obligatorios.")
            else:
                rendimiento = (monto_aporte * 0.12) / operaciones
                st.success(f"Aporte registrado: {monto_aporte} USD por '{inversionista}'")
                st.info(f"Rendimiento estimado por operación: ${rendimiento:.2f} USD")
                st.warning("Evaluación de riesgo: Diversificación recomendada.")

with tab3:
    st.header("Seguimiento de Notas de Crédito")
    with st.form("form_notas"):
        cliente = st.text_input("Cliente")
        valor_nota = st.number_input("Valor de la Nota (USD)", min_value=0.0)
        fecha_esperada = st.date_input("Fecha Esperada de Emisión")
        submit_nota = st.form_submit_button("Registrar Nota")
        if submit_nota:
            if not cliente or valor_nota == 0.0:
                st.error("Por favor completa los datos obligatorios.")
            else:
                st.success(f"Nota de crédito registrada para {cliente} por ${valor_nota:.2f}")

with tab4:
    st.header("Motor de Cálculo de Comisiones")
    with st.form("form_comisiones"):
        operacion_id = st.text_input("ID de la Operación")
        monto_operacion = st.number_input("Monto de la Operación (USD)", min_value=0.0)
        porcentaje_comision = st.slider("Porcentaje de Comisión (%)", 0, 20, 10)
        submit_comision = st.form_submit_button("Calcular Comisión")
        if submit_comision:
            if not operacion_id or monto_operacion == 0.0:
                st.error("Debes ingresar los datos de operación.")
            else:
                comision = monto_operacion * (porcentaje_comision / 100)
                utilidad_neta = monto_operacion - comision
                st.success(f"Comisión calculada: ${comision:.2f}")
                st.info(f"Utilidad neta: ${utilidad_neta:.2f}")

with tab5:
    st.header("Panel de Control y Analítica Operativa")
    st.subheader("📊 Indicadores Generales")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Financiado", "$125,000")
        st.metric("Notas de Crédito Emitidas", "18")
    with col2:
        st.metric("Comisión Promedio (%)", "10%")
        st.metric("Inversionistas Activos", "5")

    st.subheader("🔍 Distribución de Aportes")
    aportes_df = pd.DataFrame({
        "Inversionista": ["Juan", "María", "Carlos", "Ana"],
        "Monto (USD)": [20000, 35000, 15000, 30000]
    })
    fig1, ax1 = plt.subplots()
    ax1.pie(aportes_df["Monto (USD)"], labels=aportes_df["Inversionista"], autopct="%1.1f%%")
    ax1.axis("equal")
    st.pyplot(fig1)

    st.subheader("📈 Comisiones por Operación")
    operaciones_df = pd.DataFrame({
        "Operación": ["OP001", "OP002", "OP003", "OP004"],
        "Monto": [30000, 25000, 40000, 30000],
        "Comisión": [3000, 2500, 4000, 3000]
    })
    fig2, ax2 = plt.subplots()
    ax2.bar(operaciones_df["Operación"], operaciones_df["Comisión"])
    ax2.set_ylabel("USD")
    ax2.set_title("Comisiones Generadas")
    st.pyplot(fig2)

with tab6:
    st.header("Detección de Anomalías (Arbutus Software)")
    st.write("- Integración en tiempo real con datos operativos")
    st.write("- Supervisión continua con reglas de auditoría")
    st.write("- Generación de alertas inteligentes")
    if st.button("🔍 Ejecutar análisis de anomalías"):
        st.warning("2 notas de crédito duplicadas encontradas.")