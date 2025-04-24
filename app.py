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

# Simulador de liquidación en el módulo 4
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