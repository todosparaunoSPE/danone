# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 17:06:37 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import io

# Configuración de la página
st.set_page_config(
    page_title="Mi Portafolio - Analista de Datos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #004B93;
        text-align: center;
        margin-bottom: 2rem;
    }
    .danone-blue {
        color: #004B93;
    }
    .highlight {
        background-color: #fff4cc;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #004B93;
        margin: 10px 0px;
    }
    .skill-box {
        background-color: #f0f8ff;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .project-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 15px 0px;
        border-left: 5px solid #004B93;
    }
</style>
""", unsafe_allow_html=True)

# Datos de ejemplo (en una aplicación real, estos vendrían de bases de datos o APIs)
def load_sample_data():
    # Datos de ventas simuladas
    dates = pd.date_range(start='2022-01-01', end='2023-12-31', freq='D')
    products = ['Yogurt Natural', 'Yogurt de Fresa', 'Agua Mineral', 'Leche Fermentada', 'Postre lácteo']
    regions = ['Norte', 'Sur', 'Este', 'Oeste', 'Centro']
    
    sales_data = pd.DataFrame({
        'fecha': np.random.choice(dates, 1000),
        'producto': np.random.choice(products, 1000),
        'region': np.random.choice(regions, 1000),
        'ventas': np.random.randint(50, 500, 1000),
        'coste': np.random.randint(20, 200, 1000)
    })
    
    sales_data['beneficio'] = sales_data['ventas'] - sales_data['coste']
    sales_data['mes'] = sales_data['fecha'].dt.to_period('M').astype(str)
    
    # Datos de satisfacción del cliente
    satisfaction_data = pd.DataFrame({
        'producto': products * 4,
        'trimestre': sorted(['T1-2023', 'T2-2023', 'T3-2023', 'T4-2023'] * 5),
        'puntuacion': np.random.uniform(3.5, 4.9, 20)
    })
    
    return sales_data, satisfaction_data

# Cargar datos
sales_data, satisfaction_data = load_sample_data()

# Header principal
st.markdown('<h1 class="main-header">Portafolio de Analista de Datos</h1>', unsafe_allow_html=True)
st.markdown("### Demostrando mis habilidades para la vacante de **Analista de Datos** en Danone")

# Información personal
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div class="highlight">
        <h3 class="danone-blue">¡Hola equipo de Danone!</h3>
        <p>Soy [Tu Nombre], analista de datos con experiencia en transformar datos complejos en insights accionables. 
        Estoy emocionado por la oportunidad de contribuir al propósito de Danone de llevar salud a través de la alimentación 
        a tantas personas como sea posible.</p>
    </div>
    """, unsafe_allow_html=True)

# Sección de habilidades
st.markdown("---")
st.header("🛠 Habilidades Técnicas")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="skill-box">
        <h4 class="danone-blue">Excel Avanzado</h4>
        <ul>
            <li>Tablas dinámicas y dashboards</li>
            <li>Fórmulas complejas (INDEX-MATCH, OFFSET, INDIRECT)</li>
            <li>Power Query y Power Pivot</li>
            <li>Macros y VBA</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-box">
        <h4 class="danone-blue">Visualización de Datos</h4>
        <ul>
            <li>Power BI y Tableau</li>
            <li>Plotly y Matplotlib</li>
            <li>Creación de dashboards interactivos</li>
            <li>Storytelling con datos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="skill-box">
        <h4 class="danone-blue">Análisis de Datos</h4>
        <ul>
            <li>Python (Pandas, NumPy, SciPy)</li>
            <li>Análisis estadístico</li>
            <li>SQL y bases de datos</li>
            <li>Limpieza y preparación de datos</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Demostración de habilidades con datos de ejemplo
st.markdown("---")
st.header("📈 Demostración de Habilidades Analíticas")

# Selectores para el dashboard
st.sidebar.header("Filtros de Análisis")
selected_products = st.sidebar.multiselect(
    "Selecciona productos:",
    options=sales_data['producto'].unique(),
    default=sales_data['producto'].unique()
)

date_range = st.sidebar.date_input(
    "Rango de fechas:",
    value=(sales_data['fecha'].min(), sales_data['fecha'].max()),
    min_value=sales_data['fecha'].min(),
    max_value=sales_data['fecha'].max()
)

# Filtrar datos
filtered_data = sales_data[
    (sales_data['producto'].isin(selected_products)) & 
    (sales_data['fecha'] >= pd.to_datetime(date_range[0])) & 
    (sales_data['fecha'] <= pd.to_datetime(date_range[1]))
]

# Métricas clave
st.subheader("Métricas Clave de Rendimiento")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Ventas Totales", f"${filtered_data['ventas'].sum():,}")
col2.metric("Beneficio Total", f"${filtered_data['beneficio'].sum():,}")
col3.metric("Productos Analizados", len(selected_products))
col4.metric("Margen Promedio", f"{filtered_data['beneficio'].sum()/filtered_data['ventas'].sum()*100:.2f}%")

# Gráficos
tab1, tab2, tab3 = st.tabs(["Tendencias de Ventas", "Análisis por Producto", "Satisfacción del Cliente"])

with tab1:
    # Ventas por mes
    monthly_sales = filtered_data.groupby('mes').agg({'ventas': 'sum', 'beneficio': 'sum'}).reset_index()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=monthly_sales['mes'], y=monthly_sales['ventas'], 
                            mode='lines+markers', name='Ventas', line=dict(color='#004B93')))
    fig.add_trace(go.Scatter(x=monthly_sales['mes'], y=monthly_sales['beneficio'], 
                            mode='lines+markers', name='Beneficio', line=dict(color='#FF7F50')))
    
    fig.update_layout(title='Tendencia de Ventas y Beneficios',
                      xaxis_title='Mes',
                      yaxis_title='Monto ($)')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    col1, col2 = st.columns(2)
    
    with col1:
        # Ventas por producto
        product_sales = filtered_data.groupby('producto')['ventas'].sum().reset_index()
        fig = px.bar(product_sales, x='producto', y='ventas', 
                     title='Ventas por Producto', color='ventas',
                     color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Beneficio por región
        region_profit = filtered_data.groupby('region')['beneficio'].sum().reset_index()
        fig = px.pie(region_profit, values='beneficio', names='region', 
                     title='Distribución de Beneficios por Región')
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    # Satisfacción del cliente
    fig = px.line(satisfaction_data, x='trimestre', y='puntuacion', color='producto',
                  title='Evolución de la Satisfacción del Cliente por Producto',
                  markers=True)
    fig.update_yaxes(range=[3, 5])
    st.plotly_chart(fig, use_container_width=True)

# Proyectos destacados
st.markdown("---")
st.header("🚀 Proyectos Destacados")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="project-card">
        <h4 class="danone-blue">Optimización de Cadena de Suministro</h4>
        <p><strong>Resultados:</strong> Reducción del 15% en costos logísticos y mejora del 12% en tiempos de entrega.</p>
        <p><strong>Técnicas utilizadas:</strong> Análisis predictivo, optimización de rutas, simulación de escenarios.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h4 class="danone-blue">Sistema de Pronóstico de Demandas</h4>
        <p><strong>Resultados:</strong> Precisión del 92% en pronósticos a 30 días, reducción del 20% en inventario obsoleto.</p>
        <p><strong>Técnicas utilizadas:</strong> Series de tiempo, ARIMA, machine learning.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="project-card">
        <h4 class="danone-blue">Dashboard de Performance Comercial</h4>
        <p><strong>Resultados:</strong> Centralización de 12 fuentes de datos, ahorro de 20 horas semanales en reporting.</p>
        <p><strong>Técnicas utilizadas:</strong> ETL, Power BI, integración de APIs.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h4 class="danone-blue">Análisis de Clientes</h4>
        <p><strong>Resultados:</strong> Identificación de 3 segmentos de alto valor, aumento del 18% en retención.</p>
        <p><strong>Técnicas utilizadas:</strong> Clusterización, RFM analysis, cohort analysis.</p>
    </div>
    """, unsafe_allow_html=True)

# Por qué Danone
st.markdown("---")
st.header("🎯 Por qué quiero unirme a Danone")

st.markdown("""
<div class="highlight">
    <p>Admiro el compromiso de Danone con la salud a través de la alimentación y su modelo de negocio de "doble proyecto": 
    económico y social. Como analista de datos, veo una gran oportunidad para contribuir a:</p>
    <ul>
        <li>Optimizar la cadena de suministro para reducir el desperdicio de alimentos</li>
        <li>Analizar tendencias de consumo para desarrollar productos más saludables</li>
        <li>Medir el impacto social de las iniciativas de Danone</li>
        <li>Implementar análisis predictivo para mejorar la eficiencia operativa</li>
    </ul>
    <p>Mi experiencia en análisis de datos y mi pasión por la misión de Danone me convierten en un candidato ideal 
    para impulsar la toma de decisiones basada en datos en su organización.</p>
</div>
""", unsafe_allow_html=True)

# Contacto
st.markdown("---")
st.header("📞 Contacto")

col1, col2, col3 = st.columns(3)
col1.markdown("**Email:** jahoperi@gmail.com")
col2.markdown("**Teléfono:** +52 56 1056 4095")
#col3.markdown("**LinkedIn:** [linkedin.com/in/tuperfil]")

st.markdown("---")
st.markdown("### *Estoy listo para contribuir al éxito de Danone con el poder de los datos*")