import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000/JUAI/ask"

def layout():
    st.markdown("# JUAI")
    st.markdown("Ställ en fråga om avdrag i inkomstslaget tjänst (12 kap. inkomstskattelagen)")
    st.caption("Disclaimer: Detta är inte skatterådgivning")

    text_input = st.text_input(label="Din fråga")

    if st.button("Skicka") and text_input.strip() != "":
        response = requests.post(f"{BASE_URL}", json={"prompt": text_input}, timeout=60)
        
        data = response.json()
        if response.status_code != 200:
            st.error(f"Något gick fel ({response.status_code})")
            return
    

        st.markdown("## Fråga:")
        st.markdown(text_input)

        st.markdown("## Svar:")
        st.markdown(data["answer"])

        st.markdown("# Källa")
        st.markdown(f"12 kap. {data['paragraph_nr']} § - {data['title']}")

if __name__ == "__main__":
    layout()