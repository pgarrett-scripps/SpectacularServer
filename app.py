import streamlit as st
from streamlit_extras.card import card
from streamlit_extras.grid import grid

# make wide with home icon
st.set_page_config(layout="wide", page_title="Spectacular Home Page", page_icon=":house:")

c1, c2, c3 = st.columns(3, gap='large')

my_grid = grid(3)

with my_grid.container():
    card(
      title="Protein Cleaver",
      text="A Protein Digestion Calculator",
      url="http://spectacular.scripps.edu/protein-cleaver-dev"
    )

with my_grid.container():
    card(
      title="Peptide Fragmenter",
      text="A Peptide Fragmentation Calculator",
      url="http://spectacular.scripps.edu/peptide-fragmenter-dev"
    )

with my_grid.container():
    card(
      title="Spectra Viewer",
      text="A MsMs Spectra Viewer",
      url="http://spectacular.scripps.edu/spectra-viewer-dev"
    )

with my_grid.container():
    card(
      title="Skip Novo",
      text="A Denovo Search Tool",
      url="http://spectacular.scripps.edu/protein-cleaver-dev"
    )