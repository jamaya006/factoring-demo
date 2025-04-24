import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Demo Factoring", layout="wide")
st.title("💼 Plataforma de Automatización de Factoring")

# Cargar datos desde CSV
clientes_df = pd.read_csv("demo_data/clientes.csv")
fondos_df = pd.read_csv("demo_data/fondos.csv")
notas_df = pd.read_csv("demo_data/notas.csv")
comisiones_df = pd.read_csv("demo_data/comisiones.csv")

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
    st.dataframe(clientes_df)

with tab2:
    st.header("Administración de Fondos de Inversionistas")
    st.dataframe(fondos_df)

with tab3:
    st.header("Seguimiento de Notas de Crédito")
    st.dataframe(notas_df)

with tab4:
    st.header("Motor de Cálculo de Comisiones")
    st.dataframe(comisiones_df)

with tab5:
    st.header("Panel de Control y Analítica Operativa")
    st.subheader("📊 Indicadores Generales")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Financiado", f"${clientes_df['Monto financiado'].sum():,.2f}")
        st.metric("Notas de Crédito Emitidas", f"{len(notas_df)}")
    with col2:
        st.metric("Comisión Promedio (%)", f"{comisiones_df['Porcentaje'].mean():.1f}%")
        st.metric("Inversionistas Activos", f"{fondos_df['Inversionista'].nunique()}")

    st.subheader("🔍 Distribución de Aportes")
    fig1, ax1 = plt.subplots()
    ax1.pie(fondos_df["Monto"], labels=fondos_df["Inversionista"], autopct="%1.1f%%")
    ax1.axis("equal")
    st.pyplot(fig1)

    st.subheader("📈 Comisiones por Operación")
    fig2, ax2 = plt.subplots()
    ax2.bar(comisiones_df["Operación"], comisiones_df["Monto"] * (comisiones_df["Porcentaje"] / 100))
    ax2.set_ylabel("USD")
    ax2.set_title("Comisiones Generadas")
    st.pyplot(fig2)

    st.subheader("📋 Tabla de Clientes")
    st.dataframe(clientes_df)

    st.subheader("📋 Tabla de Aportes de Inversionistas")
    st.dataframe(fondos_df)

    st.subheader("📋 Tabla de Notas de Crédito")
    st.dataframe(notas_df)

    st.subheader("📋 Tabla de Comisiones")
    st.dataframe(comisiones_df)

with tab6:
    st.header("Detección de Anomalías (Arbutus Software)")
    st.write("- Integración en tiempo real con datos operativos")
    st.write("- Supervisión continua con reglas de auditoría")
    st.write("- Generación de alertas inteligentes")
    if st.button("🔍 Ejecutar análisis de anomalías"):
        st.warning("2 notas de crédito duplicadas encontradas.")