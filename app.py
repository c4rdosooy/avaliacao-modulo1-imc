import streamlit as st

st.title("calculadora IMC 🍂")
st.subheader("meu primeiro programa streamlit🫰")

altura = st.number_input("digite a sua altura: ", min_value = 0.0)
peso = st.number_input("digite o seu peso: ", min_value = 0.0)

if st.button("calcular"):
    imc = peso / altura ** 2

    if imc < 18.5:
        st.image("https://i.pinimg.com/736x/a6/5c/15/a65c1503699d1f18189c0b4b9f974a41.jpg",width=300)
        st.error("abaixo do peso.")
        st.audio("https://www.myinstants.com/media/sounds/papo-de-undaia.mp3")
    elif imc < 24.9:
        st.image("https://i.pinimg.com/736x/a6/5c/15/a65c1503699d1f18189c0b4b9f974a41.jpg",width=300)
        st.success("peso normal")
        st.audio("https://www.myinstants.com/media/sounds/papo-de-undaia.mp3")
    elif imc < 29.9:
        st.image("https://i.pinimg.com/736x/a6/5c/15/a65c1503699d1f18189c0b4b9f974a41.jpg",width=300)
        st.warning("sobrepeso")
        st.audio("https://www.myinstants.com/media/sounds/papo-de-undaia.mp3")
    elif imc < 34.9:
        st.image("https://i.pinimg.com/736x/a6/5c/15/a65c1503699d1f18189c0b4b9f974a41.jpg",width=300)
        st.warning("diminui a boca fia")
        st.audio("https://www.myinstants.com/media/sounds/papo-de-undaia.mp3")
        print()