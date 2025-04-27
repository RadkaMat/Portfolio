import streamlit as st

# remove anchors for every markdown
st.html("""<style>[data-testid='stHeaderActionElements'] {display: none;}
                  [data-testid='StyledFullScreenButton'] {display: none;}
                  .st-emotion-cache-qcpnpn {background-color: #F5DEB3;}</style>""")

st.title('Portfolio')

img_url = r'https://github.com/RadkaMat/Portfolio/blob/main/images/to_do_list_img.jpg?raw=true'

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.image(img_url)
    st.page_link('pages/to-do_list.py', label='run To-do List App', icon='📝')

with col2:
    with st.container(border=True):
        pass
