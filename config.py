import streamlit as st

def site_config():
    st.set_page_config(
        page_title='RabbitWatch - taking care of your rabbits',
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# > Creator: Gordon D. Pisciotta  ·  4M  ·  [modern.millennial.market.mapping]",
        }
    )

def site_header_info():
    col1, col2 = st.columns(2)
    col1.title('RabbitWatch')
    col1.caption('Monitoring Insects Population, Reporting Unusual Bunny Illness/Death')
    col2.markdown(' ')
    col2.markdown(' ')
    col2.markdown(' ')
    col2.markdown(' ')
    col2.markdown('        →  [Contribute Data](http://github.com)')
    with st.expander('What\'s RabbitWatch?'):
        st.markdown('''
                Australia is **not** a particular safe space for our rabbits, 
                this website will utilize user-provided data, to allows
                rabbit-keepers to be kept informed about potential risk 
                that may pose to their beloved flurry friends.
                ''')

