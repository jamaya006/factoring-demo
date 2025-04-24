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