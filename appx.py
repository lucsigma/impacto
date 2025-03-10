
import streamlit as st

# Funções
def converter_velocidade(velocidade_kmh):
    velocidade_ms = velocidade_kmh / 3.6  # km/h para m/s
    velocidade_km_min = velocidade_kmh / 60  # km/h para km/min
    velocidade_mph = velocidade_kmh * 0.621371  # km/h para mph
    return velocidade_ms, velocidade_km_min, velocidade_mph

def calcular_pressao(massa, area):
    g = 9.81  # Aceleração devido à gravidade em m/s²
    peso = massa * g  # Cálculo do peso (força)
    pressao = peso / area  # Cálculo da pressão
    return pressao

def calcular_impacto(massa, delta_v, delta_t):
    impacto = (massa * delta_v) / delta_t  # Fórmula da força de impacto
    return impacto

# Interface Streamlit
st.title("💥 Cálculo da Força de Impacto de um objeto")

# Conversão de Velocidade
st.header("🚗 Conversão de Velocidade")
velocidade_kmh = st.number_input("Digite a velocidade em km/h:", min_value=0.0, format="%.2f")

if st.button("Converter"):
    ms, km_min, mph = converter_velocidade(velocidade_kmh)
    st.success(f"{velocidade_kmh} km/h equivale a:\n"
               f"- {ms:.2f} metros por segundo (m/s)\n"
               f"- {km_min:.2f} quilômetros por minuto (km/min)\n"
               f"- {mph:.2f} milhas por hora (mph)")

st.divider()

# Cálculo de Pressão e Impacto
st.header("⚖ Cálculo de Pressão e Impacto")

massa = st.number_input("Digite a massa do objeto (kg):", min_value=0.1, format="%.2f")
area = st.number_input("Digite a área da superfície (m²):", min_value=0.01, format="%.2f")
vi_kmh = st.number_input("Digite a velocidade inicial (km/h):", min_value=0.0, format="%.2f")
vf_kmh = st.number_input("Digite a velocidade final (km/h):", min_value=0.0, format="%.2f")
delta_t = st.number_input("Digite o intervalo de tempo (segundos):", min_value=0.01, format="%.2f")

if st.button("Calcular Pressão e Impacto"):
    pressao = calcular_pressao(massa, area)
    vi_ms = vi_kmh / 3.6
    vf_ms = vf_kmh / 3.6
    delta_v = vf_ms - vi_ms
    impacto = calcular_impacto(massa, delta_v, delta_t)

    st.success(f"✅ Pressão exercida pelo objeto: {pressao:.2f} Pa")
    st.success(f"✅ Força de impacto: {impacto:.2f} N")