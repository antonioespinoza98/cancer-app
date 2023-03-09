import streamlit as st
from streamlit.web import cli as stcli
#import folium
#from streamlit_folium import st_folium
import typer

cli = typer.Typer()

@cli.command()

def main():
    st.set_page_config('Cáncer en Costa Rica')
    st.title('Cáncer en Costa Rica')
    st.caption('TCU-758')

if __name__ == "__main__":
    cli(standalone_mode=False)