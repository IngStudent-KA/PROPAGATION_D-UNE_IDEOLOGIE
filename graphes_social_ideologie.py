import networkx as nx
import matplotlib.pyplot as plt
import random

N = 100
G = nx.barabasi_albert_graph(n=N, m=2, seed=42)
degres = dict(G.degree())

Profil = ["initiateur", "modéré", "prudent"]

Proba_profil = [0.10, 0.50, 0.40] 

for node in G.nodes():
    G.nodes[node]["Profil"] = random.choices(Profil, weights=Proba_profil)[0]
  
    G.nodes[node]["Statut"] = 1 if G.nodes[node]["Profil"] == "initiateur" else 0

historique_etapes = []
historique_activistes = []
historique_reseau = []

Seuil_modere = 0.30
Seuil_prudent = 0.60

for i in range(4):

    nbrs_activistes = sum(1 for n in G.nodes() if G.nodes[n]["Statut"] == 1)
    
    historique_etapes.append(i)
    historique_activistes.append(nbrs_activistes)

   
    couleur_etapes = ['#FF4500' if G.nodes[n]['Statut'] == 1 else '#95a5a6' for n in G.nodes()]
    historique_reseau.append(couleur_etapes)

    nouveau = []

    for node in G.nodes():
        if G.nodes[node]['Statut'] == 0:
            voisin = list(G.neighbors(node))
  
            actif = [n for n in voisin if G.nodes[n]["Statut"] == 1]

            if G.nodes[node]["Profil"] == "modéré":
                somme_totale = sum(degres[v] for v in voisin)
                somme_actif = sum(degres[v] for v in actif)
                if somme_totale > 0 and (somme_actif / somme_totale) >= Seuil_modere: 
                    nouveau.append(node)
                    
            if G.nodes[node]["Profil"] == "prudent":

                if (nbrs_activistes / N) >= Seuil_prudent:
                    nouveau.append(node)
                    
    for node in nouveau:
        G.nodes[node]["Statut"] = 1

print("[INFO] Fin du calcul. Génération des graphiques...")

# ==========================================
# AFFICHAGE DES GRAPHIQUES (POST-PROCESSING)
# ==========================================
pos = nx.spring_layout(G, seed=42) 

# A. Affichage des réseaux stockés
for idx_etape in range(len(historique_reseau)):
    plt.figure(figsize=(6, 4))
    nx.draw_networkx_nodes(G, pos, node_color=historique_reseau[idx_etape], node_size=80)
    nx.draw_networkx_edges(G, pos, alpha=0.1)
    plt.title(f"Zbellion - Graphe Réseau à l'Étape {idx_etape}")
    plt.axis('off')
    plt.show()

# B. Affichage de la courbe cinétique
plt.figure(figsize=(9, 4))
plt.plot(historique_etapes, historique_activistes, marker='o', color='#FF4500', linewidth=2.5)
plt.title("Courbe d'Évolution Temporelle de la Zbellion")
plt.xlabel("Étapes (Journées)")
plt.ylabel("Nombre total d'activistes")
plt.grid(True, linestyle=':')
plt.xticks(historique_etapes) 
plt.show()
