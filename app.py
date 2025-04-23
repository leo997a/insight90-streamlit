import streamlit as st
import requests

st.set_page_config(layout="wide")
st.title("تحليل بيانات مباريات WhoScored")

match_url = st.text_input("أدخل رابط المباراة من WhoScored:")

if st.button("تحليل"):
    with st.spinner("جارٍ استخراج البيانات..."):
        try:
            api_url = f"https://insight90-api.onrender.com/extract?url={match_url}"  # غيّر الرابط حسب ما ظهر لك من Render
            response = requests.get(api_url, timeout=30)
            data = response.json()
            if "error" in data:
                st.error("خطأ: " + data["error"])
            else:
                st.success("تم جلب البيانات بنجاح!")
                st.json(data)  # لاحقًا تستبدل هذا بتحليل mplsoccer
        except Exception as e:
            st.error(f"فشل الاتصال بالخادم: {str(e)}")
