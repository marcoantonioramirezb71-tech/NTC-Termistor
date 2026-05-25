import streamlit as st
import math

# ========================================
# CONFIGURACIÓN
# ========================================

st.set_page_config(
    page_title="Calculadora parámetros termistor NTC",
    layout="centered"
)

# ========================================
# ESTILO
# ========================================

st.markdown("""
<style>

.main{
    background-color:#e6e6e6;
}

.block-container{
    max-width:950px;
    padding-top:1rem;
}

h1{
    text-align:center;
}

.panel{
    background:white;
    padding:20px;
    border-radius:12px;
    border:1px solid #bbbbbb;
}

.resultado{
    background:white;
    padding:15px;
    border-radius:8px;
    border:1px solid #cccccc;
    color:black;
    text-align:center;
    min-height:120px;
}

.valor{
    font-size:28px;
    font-weight:bold;
}

.titulo{
    font-size:16px;
}

div.stButton>button{
    width:100%;
}

</style>
""",unsafe_allow_html=True)

# ========================================
# TITULO
# ========================================

st.title("Calculadora parámetros termistor NTC")

st.write(
    "Fac. Electrónica - UPAEP"
)

st.markdown("<br>",unsafe_allow_html=True)

# ========================================
# PANEL
# ========================================

st.markdown(
    '<div class="panel">',
    unsafe_allow_html=True
)

c1,c2,c3=st.columns(3)

with c1:

    Vin=st.selectbox(
        "Voltaje Vin",
        [3.3,5.0]
    )

with c2:

    bits_ADC=st.selectbox(
        "Bits ADC",
        [8,10,12,16]
    )

# valores medios automáticos

medio={

    8:128,
    10:512,
    12:2048,
    16:32768

}

limites={

    8:255,
    10:1023,
    12:4095,
    16:65535

}

with c3:

    ADC_Dec=st.number_input(
        "Valor ADC",
        min_value=0,
        max_value=limites[bits_ADC],
        value=medio[bits_ADC]
    )

st.markdown("<br>",unsafe_allow_html=True)

b1,b2,b3=st.columns([1,1,1])

with b2:

    calcular=st.button(
        "Calcular"
    )

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# ========================================
# CALCULO
# ========================================

if calcular:

    try:

        Ro=10000

        A=0.001129148
        B=0.000234125
        C=0.000000076741

        Vout=(Vin/(2**bits_ADC))*ADC_Dec

        if Vin-Vout==0:

            st.error(
                "División entre cero"
            )

            st.stop()

        Rt=(Vout*Ro)/(Vin-Vout)

        TempK=1/(

            A+
            B*math.log(Rt)+
            C*(math.log(Rt)**3)

        )

        TempC=TempK-273.15

        st.markdown("<br>",unsafe_allow_html=True)

        st.subheader(
            "Resultados"
        )

        a,b,c,d,e=st.columns(5)

        with a:

            st.markdown(
            f"""
            <div class='resultado'>
            <div class='titulo'>
            ADC
            </div>

            <hr>

            <div class='valor'>
            {ADC_Dec}
            </div>

            </div>
            """,
            unsafe_allow_html=True
            )

        with b:

            st.markdown(
            f"""
            <div class='resultado'>
            <div class='titulo'>
            Vout
            </div>

            <hr>

            <div class='valor'>
            {Vout:.3f}V
            </div>

            </div>
            """,
            unsafe_allow_html=True
            )

        with c:

            st.markdown(
            f"""
            <div class='resultado'>
            <div class='titulo'>
            Rt
            </div>

            <hr>

            <div class='valor'>
            {Rt:.1f}
            </div>

            </div>
            """,
            unsafe_allow_html=True
            )

        with d:

            st.markdown(
            f"""
            <div class='resultado'>
            <div class='titulo'>
            Temp K
            </div>

            <hr>

            <div class='valor'>
            {TempK:.2f}
            </div>

            </div>
            """,
            unsafe_allow_html=True
            )

        with e:

            st.markdown(
            f"""
            <div class='resultado'>
            <div class='titulo'>
            Temp °C
            </div>

            <hr>

            <div class='valor'>
            {TempC:.2f}
            </div>

            </div>
            """,
            unsafe_allow_html=True
            )

    except:

        st.error(
            "Error en los cálculos"
        )