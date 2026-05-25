import streamlit as st
import math

st.set_page_config(
    page_title="Calculadora NTC"
)

st.title(
    "Calculadora Termistor NTC"
)

Vin=st.selectbox(
    "Vin",
    [3.3,5.0]
)

bits=st.selectbox(
    "Bits ADC",
    [8,10,12,16],
    index=2
)

ADC_Dec=st.number_input(
    "ADC Decimal",
    value=2048
)

if st.button(
    "Calcular"
):

    Ro=10000

    A=0.001129148
    B=0.000234125
    C=0.000000076741

    Vout=(Vin/(2**bits))*ADC_Dec

    Rt=(Vout*Ro)/(Vin-Vout)

    TempK=1/(A+
             B*math.log(Rt)+
             C*(math.log(Rt)**3))

    TempC=TempK-273.15

    c1,c2,c3,c4=st.columns(4)

    c1.metric(
        "Vout(V)",
        f"{Vout:.3f}"
    )

    c2.metric(
        "Rt(Ω)",
        f"{Rt:.1f}"
    )

    c3.metric(
        "TempK",
        f"{TempK:.2f}"
    )

    c4.metric(
        "TempC",
        f"{TempC:.2f}"
    )