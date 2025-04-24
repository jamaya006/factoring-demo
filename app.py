import streamlit as st
import pandas as pd
import numpy as np
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
        st.subheader("🔹 Registro de Cliente")
        nombre = st.text_input("Nombre del Cliente")
        ruc = st.text_input("RUC")
        linea_credito = st.number_input("Línea de Financiamiento (USD)", min_value=0.0)
        kyc_ok = st.checkbox("Documentación KYC completa")
        contrato_firmado = st.checkbox("Contrato firmado")
        garantia_validada = st.checkbox("Garantía validada")
        submit = st.form_submit_button("Registrar Cliente")
        if submit:
            if not nombre or not ruc or linea_credito == 0.0:
                st.error("Por favor completa todos los campos obligatorios.")
            elif not (kyc_ok and contrato_firmado and garantia_validada):
                st.warning("Faltan requisitos documentales.")
            else:
                st.success(f"✅ Cliente '{nombre}' registrado correctamente.")
                st.info("Cliente vinculado con el SRI para trazabilidad tributaria.")

with tab2:
    st.header("Administración de Fondos de Inversionistas")
    with st.form("form_fondos"):
        st.subheader("🔹 Registro de Aporte de Inversionista")
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
        st.subheader("🔹 Registro de Nota de Crédito")
        cliente = st.text_input("Cliente")
        fecha_esperada = st.date_input("Fecha esperada de emisión")
        valor = st.number_input("Valor de la Nota (USD)", min_value=0.0)
        endoso_valido = st.checkbox("Endoso válido")
        submit3 = st.form_submit_button("Registrar Nota")
        if submit3:
            if not cliente or valor == 0.0:
                st.error("Cliente y valor son obligatorios.")
            elif not endoso_valido:
                st.warning("Nota con endoso inválido. Revisión manual requerida.")
            else:
                st.success(f"Nota registrada correctamente para {cliente}.")
                st.info("Agregada al cronograma de liquidación.")

with tab4:
    st.header("Motor de Cálculo de Comisiones")
    with st.form("form_comisiones"):
        st.subheader("🔹 Cálculo de Comisión")
        operacion_id = st.text_input("ID de Operación")
        valor_operacion = st.number_input("Valor de la Operación (USD)", min_value=0.0)
        porcentaje = st.slider("Porcentaje de Comisión (%)", 0.5, 15.0, 5.0)
        submit4 = st.form_submit_button("Calcular")
        if submit4:
            if not operacion_id or valor_operacion == 0.0:
                st.error("Todos los campos son obligatorios.")
            else:
                comision = (valor_operacion * porcentaje) / 100
                st.success(f"Comisión calculada: ${comision:.2f} USD")
                st.info("Utilidad distribuida y registro contable generado.")

with tab5:
    st.header("📈 Dashboard Operativo en Tiempo Real")
    st.subheader("📊 Indicadores Clave")
    capital = np.random.randint(100000, 500000)
    recuperacion = np.random.randint(70000, 120000)
    notas = np.random.randint(50, 150)
    clientes = ["Cliente A", "Cliente B", "Cliente C", "Cliente D"]
    financiado = np.random.randint(10000, 50000, size=4)

    col1, col2, col3 = st.columns(3)
    col1.metric("Capital Financiado", f"${capital:,}")
    col2.metric("Recuperación Total", f"${recuperacion:,}")
    col3.metric("Notas Negociadas", f"{notas} notas")

    st.subheader("📉 Financiamiento por Cliente")
    df = pd.DataFrame({
        "Cliente": clientes,
        "Monto Financiado": financiado
    })
    fig, ax = plt.subplots()
    ax.bar(df["Cliente"], df["Monto Financiado"])
    ax.set_ylabel("USD")
    ax.set_title("Distribución de Financiamiento")
    st.pyplot(fig)

with tab6:
    st.header("Detección de Anomalías (Arbutus Software)")
    with st.form("form_anomalias"):
        st.subheader("🔹 Simulación de Análisis")
        opcion = st.selectbox("Tipo de Análisis", [
            "Notas de crédito duplicadas",
            "Clientes con observaciones SRI",
            "Variaciones atípicas por cliente"
        ])
        submit6 = st.form_submit_button("Ejecutar Análisis")
        if submit6:
            if opcion == "Notas de crédito duplicadas":
                st.warning("⚠️ Se detectaron 2 notas duplicadas con valores idénticos.")
            elif opcion == "Clientes con observaciones SRI":
                st.warning("🚨 Cliente 'XYZ Corp' tiene historial de rechazos tributarios.")
            else:
                st.warning("📊 Cliente 'ABC Ltda' con variaciones > 150% en últimos 30 días.")