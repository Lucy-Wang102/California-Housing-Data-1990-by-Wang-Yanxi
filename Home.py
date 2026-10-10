import streamlit as st

st.set_page_config(page_title="Home — California Housing", page_icon="🏠")

st.title("California Housing Data (1990)")
st.write(
    "Welcome — this multipage Streamlit app explores the 1990 California housing dataset. "
    "Use the button below to open the housing app page, or select pages from the sidebar."
)

st.caption("Note: the target page filename must be pages/app-housing.py (page name: `app-housing`).")

if st.button("Open Housing App"):
    # Attempt programmatic navigation by setting the query param used by Streamlit's multipage system.
    # If this isn't supported in the running Streamlit version, a fallback link is shown below.
    try:
        st.experimental_set_query_params(page="app-housing")
        st.experimental_rerun()
    except Exception:
        st.error("Automatic navigation failed. Use the link below to open the housing app.")

st.markdown("If the button doesn't navigate, click this link to open the housing page:")
st.markdown("[Open Housing App](?page=app-housing)")
