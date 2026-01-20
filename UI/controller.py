import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):

        try:
            n_alb=int(self._view.txtNumAlbumMin.value)
            if n_alb<0:
                raise ValueError
        except:
            self._view.show_alert('inserire valore ')
            return
        self._model.load_all_artists()
        self._model.load_artists_with_min_albums(n_alb)
        grafo=self._model.build_graph()
        n_nodes, n_edges=self._model.get_componenti()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'Grafo creato: {grafo}, nodi e archi: {n_nodes,n_edges}'))
        self._view.ddArtist.options.clear()
        for a in grafo.artists:
            self._view.ddArtist.options.append(key=str(a.id),text=a.name)
            self._view._btnCreateGraph.disabled = False
            self._view.btnArtistsConnected.disabled=False
            self._view.btnSearchArtists.disabled=False

        self._view.update_page()




    def handle_connected_artists(self, e):
        if self._view.ddArtist.value is None:
            self._view.show_alert('inserire artista ')
            return
        grafo = self._model.build_graph()
        artist=self._model.get_componenti(grafo)
        neigh=self._model.get_neighbors(artist)
        self._view.txt_result.controls.clear()
        for a2,w in neigh:
            self._view.txt_result.controls.append(f'{a2} generi in comune {w}')





