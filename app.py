import streamlit as st

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
    st.write("- Registro y validación de clientes")
    st.write("- Control documental (KYC, contratos, garantías)")
    st.write("- Línea de financiamiento y vinculación con el SRI")
    if st.button("🔄 Simular Registro de Cliente"):
        st.success("Cliente registrado y vinculado correctamente.")

with tab2:
    st.header("Administración de Fondos de Inversionistas")
    st.write("- Registro de aportes")
    st.write("- Cálculo de rendimiento proporcional")
    st.write("- Control de riesgos")
    if st.button("📊 Simular Cálculo de Rendimiento"):
        st.info("Rendimiento calculado y riesgos evaluados.")

with tab3:
    st.header("Seguimiento de Notas de Crédito")
    st.write("- Solicitudes y fechas esperadas")
    st.write("- Validación y negociación")
    st.write("- Cronograma de liquidación")
    if st.button("📝 Cargar Nota de Crédito"):
        st.success("Nota validada y cargada con éxito.")

with tab4:
    st.header("Motor de Cálculo de Comisiones")
    st.write("- Cálculo automático por operación")
    st.write("- Distribución de utilidad")
    st.write("- Registro contable exportable")
    if st.button("💵 Calcular Comisión"):
        st.info("Comisión distribuida y registrada en ERP.")

with tab5:
    st.header("Panel de Control y Analítica")
    st.write("- Capital financiado, recuperación y notas negociadas")
    st.write("- Indicadores clave por cliente")
    st.write("- Proyecciones de flujo de fondos")
    if st.button("📊 Ver Dashboard"):
        st.success("Indicadores generados correctamente.")

with tab6:
    st.header("Detección de Anomalías (Arbutus Software)")
    st.write("- Integración en tiempo real con datos operativos")
    st.write("- Supervisión continua con reglas de auditoría")
    st.write("- Generación de alertas inteligentes")
    if st.button("🔍 Ejecutar análisis de anomalías"):
        st.warning("2 notas de crédito duplicadas encontradas.")