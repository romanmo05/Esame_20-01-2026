import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self.bestPath=[]
        self.best_weight=0


    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")




    def load_artists_with_min_albums(self, min_albums):
        minimo=DAO.get_artist_with_d_min(min_albums)
        return minimo


    def build_graph(self):
        self._graph.clear()
        self.artisti=DAO.get_all_artists()

        for a in self.artisti:
            self._graph_add_node(a)

        for i in range(len(self.artisti)):
            for j in range(len(self.artisti[i+1,len(self.artisti)])):
                a1=self.artisti[i]
                a2=self.artisti[j]
                g1=DAO.get_genere_per_artista(a1)
                g2=DAO.get_genere_per_artista(a2)
                comune=g1.intersection(g2)
                if comune>0:
                    self._graph.add_edge(a1,a2,weight=len(comune))

        return self._graph

    def get_componenti(self,grafo):
        return list(nx.node_connected_component(self._graph,grafo))


    def get_neighbors(self,artist):
        neig=[]
        for a2 in self._graph.neighbors(artist):
            peso=self._graph[artist][a2]['weight']
            neig.append((a2,peso))
        neig.sort(key=lambda x: x[1])
        return neig



    def cammino_massimo(self,start_artist,n_artists,d_min):
        self.bestPath=[]
        self.best_weight=0

        for nodo in self._graph.nodes:
            self._ricorsione ([start_artist,0,n_artists,nodo])

        return self.bestPath
    def _ricorsione(self,parziale,peso,n_artists,nodo):
        if len(parziale)==n_artists:
            if peso>self.best_weight:
                self.best_weight=peso
                self.bestPath=list(parziale)
            return
        last=parziale[-1]
        for neig in self._graph.neighbors(last):
            if neig not in parziale and neig not in nodo:
                w=self._graph[last][neig]['weight']
                parziale.append(neig)
                self._ricorsione ([neig,peso+w,n_artists,nodo])
                parziale.pop()











