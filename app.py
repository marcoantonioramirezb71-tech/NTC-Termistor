import streamlit as st
import math

# ---------------------------------------
# CONFIGURACIÓN VENTANA
# ---------------------------------------

st.set_page_config(
    page_title="Calculadora NTC",
    layout="centered"
)

# ---------------------------------------
# CSS ESTILO TIPO APP EJECUTABLE
# ---------------------------------------

st.markdown("""
<style>

.main{
    background-color:#e9e9e9;
}

.block-container{
    padding-top:1rem;
    max-width:900px;
}

h1{
    text-align:center;
}

.caja{
    background:white;
    padding:20px;
    border-radius:10px;
    border:1px solid #bdbdbd;
}

.resultado{
    background:#f7f7f7;
    padding:15px;
    border-radius:8px;
    border:1px solid #d0d0d0;
    text-align:center;
}

div.stButton > button{
    width:100%;
}

</style>
""",unsafe_allow_html=True)

# ---------------------------------------
# TÍTULO
# ---------------------------------------

st.title("Calculadora parámetros termistor NTC")
st.write("Fac. Electrónica - UPAEP")

st.markdown("<br>",unsafe_allow_html=True)

# ---------------------------------------
# PANEL PRINCIPAL
# ---------------------------------------

st.markdown('<div class="caja">',unsafe_allow_html=True)

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

with c3:

    if bits_ADC==8:
        limite=255

    elif bits_ADC==10:
        limite=1023

    elif bits_ADC==12:
        limite=4095

    else:
        limite=65535

    ADC_Dec = st.number_input(
        "Valor ADC",
        min_value=0,
        max_value=limite,
        value=min(500, limite)
    )

st.markdown("<br>",unsafe_allow_html=True)

colA,colB,colC=st.columns([1,1,1])

with colB:

    calcular=st.button(
        "Calcular"
    )

st.markdown('</div>',unsafe_allow_html=True)

# ---------------------------------------
# CÁLCULOS
# ---------------------------------------

if calcular:

    try:

        Ro=10000

        A=0.001129148
        B=0.000234125
        C=0.000000076741

        Vout=(Vin/(2**bits_ADC))*ADC_Dec

        Rt=(Vout*Ro)/(Vin-Vout)

        TempK=1/(A+
                 B*math.log(Rt)+
                 C*(math.log(Rt)**3))

        TempC=TempK-273.15

        st.markdown("<br>",unsafe_allow_html=True)

        st.subheader("Resultados")

        a,b,c,d,e=st.columns(5)

        with a:
            st.markdown(
            """
            <div class='resultado'>
            <b>ADC</b><br><br>
            {:.0f}
            </div>
            """.format(ADC_Dec),
            unsafe_allow_html=True
            )

        with b:
            st.markdown(
            """
            <div class='resultado'>
            <b>Vout</b><br><br>
            {:.3f}V
            </div>
            """.format(Vout),
            unsafe_allow_html=True
            )

        with c:
            st.markdown(
            """
            <div class='resultado'>
            <b>Rt</b><br><br>
            {:.2f}Ω
            </div>
            """.format(Rt),
            unsafe_allow_html=True
            )

        with d:
            st.markdown(
            """
            <div class='resultado'>
            <b>Temp K</b><br><br>
            {:.2f}
            </div>
            """.format(TempK),
            unsafe_allow_html=True
            )

        with e:
            st.markdown(
            """
            <div class='resultado'>
            <b>Temp °C</b><br><br>
            {:.2f}
            </div>
            """.format(TempC),
            unsafe_allow_html=True
            )

    except:

        st.error(
            "Valores inválidos"
        )