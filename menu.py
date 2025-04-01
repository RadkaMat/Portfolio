import streamlit as st

# remove anchors for every markdown
st.html("""<style>[data-testid='stHeaderActionElements'] {display: none;}
                  [data-testid='StyledFullScreenButton'] {display: none;}
                  .st-emotion-cache-qcpnpn {background-color: #F5DEB3;}</style>""")

st.title('Portfolio')

img_url = r'https://github.com/RadkaMat/Streamlit_apps/blob/master/web_app_data/to_do_list_img_big.jpg?raw=true'

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.image(img_url)
    st.page_link('pages/to-do_list.py', label='run To-do List App', icon='📝')

with col3:
    with st.container(border=True):
        pass
