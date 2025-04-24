import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

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
    st.header("🧮 Simulador de Liquidación de Operación")
    with st.form("form_liquidacion"):
        op_id = st.text_input("ID de la Operación", value="OP367")
        monto_anticipo = st.number_input("Monto Anticipado (USD)", min_value=0.0, value=25000.74)
        fecha_anticipo = st.date_input("Fecha de Anticipo", value=date(2024, 11, 29))
        fecha_acreditacion = st.date_input("Fecha de Acreditación (NCD)", value=date(2025, 4, 15))
        tasa_dcto = st.number_input("Tasa de Descuento (%)", min_value=0.0, max_value=100.0, value=3.0)

        accionistas = {
            "Accionista A": 0.4,
            "Accionista B": 0.35,
            "Accionista C": 0.25
        }

        submit_liq = st.form_submit_button("Calcular Liquidación")
        if submit_liq:
            dias = (fecha_acreditacion - fecha_anticipo).days
            valor_dcto = monto_anticipo * (tasa_dcto / 100) * dias / 360
            monto_neto = monto_anticipo - valor_dcto

            st.subheader("📊 Resultados")
            st.metric("Días Transcurridos", dias)
            st.metric("Valor del Descuento", f"${valor_dcto:,.2f}")
            st.metric("Monto Neto a Distribuir", f"${monto_neto:,.2f}")

            st.subheader("📋 Tabla de Distribución a Accionistas")
            distribucion = {
                "Accionista": [],
                "Participación": [],
                "Monto Recibido (USD)": []
            }
            for nombre, pct in accionistas.items():
                distribucion["Accionista"].append(nombre)
                distribucion["Participación"].append(f"{int(pct * 100)}%")
                distribucion["Monto Recibido (USD)"].append(round(monto_neto * pct, 2))

            df_dist = pd.DataFrame(distribucion)
            st.dataframe(df_dist, use_container_width=True)

# Datos históricos procesados
hist_data = {
    "Año-Mes": ['2022-04', '2022-05'],
    "Monto Total": [76879.14, 20000.00],
    "Rendimiento Promedio": [0.03, 0.0275]
}
historico_df = pd.DataFrame(hist_data)

with tab5:
    st.header("📈 Dashboard Operativo con Históricos Reales")

    st.subheader("💵 Total Financiado por Mes")
    fig1, ax1 = plt.subplots()
    ax1.plot(historico_df["Año-Mes"], historico_df["Monto Total"], marker='o')
    ax1.set_ylabel("USD")
    ax1.set_title("Monto Financiado por Mes")
    ax1.tick_params(axis='x', rotation=45)
    st.pyplot(fig1)

    st.subheader("📊 Rendimiento Promedio Mensual")
    fig2, ax2 = plt.subplots()
    ax2.bar(historico_df["Año-Mes"], historico_df["Rendimiento Promedio"])
    ax2.set_ylabel("Tasa")
    ax2.set_title("Rendimiento Promedio por Mes")
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

    st.subheader("📋 Tabla de Operaciones Históricas")
    st.dataframe(historico_df)

with tab6:
    st.header("Detección de Anomalías (Arbutus Software)")
    st.write("- Integración en tiempo real con datos operativos")
    st.write("- Supervisión continua con reglas de auditoría")
    st.write("- Generación de alertas inteligentes")
    if st.button("🔍 Ejecutar análisis de anomalías"):
        st.warning("2 notas de crédito duplicadas encontradas.")