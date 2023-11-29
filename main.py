# Installiere pygraphviz in Google Colab
!apt-get install -y graphviz-dev
!pip install pygraphviz
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

# Funktion zur Erstellung des erweiterten Angriffsbaums mit spezifischen Bedrohungen
def erstelle_erweiterten_angriffsbaum_mit_bedrohungen():
    G = nx.DiGraph()

    # Füge Knoten zum Baum hinzu (neue Bedrohungen eintragen)
    G.add_nodes_from([
       "Angreifer",
       "TA0043 Aufklärung",
       ("TA0027 Erster Zugriff", {"label": "EW: 04"}),
       ("TA0031 Zugriff auf Zugangsdaten", {"label": "EW: 04"}),
       ("T1464", {"label": "02"}),
       ("T1640", {"label": "02"}),
       ("T1641", {"label": "08"}),
       ("T1517&T1414", {"label": "09"}),
       ("T1517&T1634", {"label": "09"}),
       ("T1517&T1417", {"label": "09"}),
       ("T1646", {"label": "12"}),
       ("T1639", {"label": "06"}),
       ("T1660", {"label": "0"}),
       ("T1474", {"label": "0"}),
       ("T1474.001", {"label": "0"}),
       ("T1474.002", {"label": "0"}),
       ("T1474.003", {"label": "0"}),
       ("T1456", {"label": "0"}),
       ("T1517", {"label": "0"}),
       ("T1417", {"label": "0"}),
       ("T1414", {"label": "0"}),
       ("T1634", {"label": "0"}),
       ("T1661", {"label": "0"})



    ])

    G.add_edges_from([
        ("Angreifer","TA0043 Aufklärung"),
        ("TA0043 Aufklärung", "TA0027 Erster Zugriff"),
        ("TA0043 Aufklärung", "T1464"),
        ("TA0027 Erster Zugriff", "T1661"),
        ("TA0027 Erster Zugriff", "T1456"),
        ("TA0027 Erster Zugriff", "T1660"),
        ("TA0027 Erster Zugriff", "T1474"),
        ("T1474", "T1474.001"),
        ("T1474", "T1474.002"),
        ("T1474", "T1474.003"),
        ("T1661", "TA0041 Exekution"),
        ("T1456", "TA0041 Exekution"),
        ("T1660", "TA0041 Exekution"),
        ("T1661", "TA0041 Exekution"),
        ("T1474.001", "TA0041 Exekution"),
        ("T1474.002", "TA0041 Exekution"),
        ("T1474.003", "TA0041 Exekution"),
        ("TA0041 Exekution", "TA0031 Zugriff auf Zugangsdaten"),
        ("TA0031 Zugriff auf Zugangsdaten", "T1517"),
        ("TA0031 Zugriff auf Zugangsdaten", "T1414"),
        ("TA0031 Zugriff auf Zugangsdaten", "T1634"),
        ("TA0031 Zugriff auf Zugangsdaten", "T1417"),
        ("TA0041 Exekution", "T1640"),
        ("TA0041 Exekution", "T1641"),
        ("T1640", "Verfügbarkeit", {"label": ""}),
        ("T1641", "Integrität", {"label": ""}),
        ("T1464", "Verfügbarkeit", {"label": ""}),
        ("T1517", "T1517&T1414", {"label": ""}),
        ("T1414", "T1517&T1414", {"label": ""}),
        ("T1517", "T1517&T1634", {"label": ""}),
        ("T1634", "T1517&T1634", {"label": ""}),
        ("T1517", "T1517&T1417", {"label": ""}),
        ("T1417", "T1517&T1417", {"label": ""}),
        ("T1517&T1414", "T1639", {"label": ""}),
        ("T1517&T1634", "T1639", {"label": ""}),
        ("T1517&T1417", "T1639", {"label": ""}),
        ("T1517&T1414", "T1646", {"label": ""}),
        ("T1517&T1634", "T1646", {"label": ""}),
        ("T1517&T1417", "T1646", {"label": ""}),
        ("T1646", "Vertraulichkeit", {"label": ""}),
        ("T1639", "Vertraulichkeit", {"label": ""})
    ])
    # Füge Kanten hinzu (konjunktive Verzweigungen von "TA0034 Auswirkung")

    return G

def zeige_angriffsbaum(G):
    pos = graphviz_layout(G, prog="dot")  # Graphviz-Layout verwenden

    # Knotenfarben entsprechend der Notation festlegen
    node_colors = []
    for node in G.nodes():
        if node == "Angreifer":
            node_colors.append("yellow")
        elif node in ["T1464", "T1661", "T1456", "T1660", "T1474.001", "T1474.002", "T1474.003", "T1640","T1641", "T1517&T1414", "T1517&T1634", "T1517&T1417"]:
            node_colors.append("#add8e6")  # Konjunktive Knoten (blau)
        else:
            node_colors.append("darkgray")  # Disjunktive und konjunktive Knoten (dunkelgrau)

    # Angriffsbaum zeichnen
    plt.figure(figsize=(10,10))  # Größe des Diagramms anpassen
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=10, arrows=True)

    # Zahlen unter den Knoten anzeigen (rot gefärbt)
    node_labels = {node: G.nodes[node]["label"] for node in G.nodes() if "label" in G.nodes[node]}
    for node, (x, y) in pos.items():
        plt.text(x, y - 20, node_labels.get(node, ""), fontsize=10, verticalalignment="bottom", horizontalalignment="center", color="red")

    # Zahlen auf den Kanten anzeigen
    edge_labels = {(u, v): str(G[u][v]["label"]) for u, v in G.edges() if "label" in G[u][v]}
    for edge, label in edge_labels.items():
        u, v = edge
        x = (pos[u][0] + pos[v][0]) / 2
        y = (pos[u][1] + pos[v][1]) / 2
        plt.text(x, y, label, fontsize=9, horizontalalignment="center")
    plt.show()

# Hauptcode
angriffsbaum_mit_systematik = erstelle_erweiterten_angriffsbaum_mit_bedrohungen()
zeige_angriffsbaum(angriffsbaum_mit_systematik)
