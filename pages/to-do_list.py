import streamlit as st
from functions import to_do_list_func as tdl

# Constants
PAGE_BG_STYLE = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1742336960947-d70838aa9614");
    background-size: cover;
}
[data-testid="stAppViewBlockContainer"] {
    background-color: #262626;
    border: 2px solid #555555; /* Light grey border */
    border-radius: 15px; /* Rounded corners */
    padding: 20px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}
div[data-testid="stForm"] {
    border: 2px solid #d4af37; /* Gold border */
    border-radius: 15px; /* Rounded corners */
    padding: 20px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}
[data-testid='stHeaderActionElements'] {display: none;
}
</style>
"""


def add_new_to_do():
    """ Handle the event of adding a new to-do via Streamlit widget. """
    new_to_do = st.session_state['new_to_do_widget']
    if tdl.check_valid_input(new_to_do):
        updated_to_do_list = tdl.add_new_to_do_logic(to_do_list, new_to_do)
        st.session_state['new_to_do'] = new_to_do
    st.session_state['new_to_do_widget'] = ''


st.markdown(PAGE_BG_STYLE, unsafe_allow_html=True)
st.title('')
st.page_link('menu.py', label='Menu', icon='🏠')
st.title('To-Do List 📝')

# Clean New to-do+ widget
if 'new_to_do' not in st.session_state:
    st.session_state.new_to_do = ''
to_do_list = tdl.get_to_do_list()
checkbox_state = {to_do: False for to_do in to_do_list}

form = st.form('Checking form', clear_on_submit=True)
with form:
    # Create a checkbox for each to-do item
    for index, to_do in enumerate(to_do_list):
        checkbox_state[to_do] = st.checkbox(label=to_do, key=index)

    # Actualise to-do list
    if form.form_submit_button('Done'):
        to_do_list = [to_do for to_do, checked in checkbox_state.items() if not checked]
        tdl.save_to_do_list(to_do_list)
        st.rerun()

# New to-do+ widget
st.title('New to-do +')
st.text_input(label='New to-do', placeholder='Write new to-do... [for comfirmation press Enter key]',
              on_change=add_new_to_do, key='new_to_do_widget', label_visibility='collapsed')

st.write(f'The last added to-do: {st.session_state.new_to_do}')
