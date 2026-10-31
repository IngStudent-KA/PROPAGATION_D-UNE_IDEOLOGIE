# PROPAGATION_D-UNE_IDEOLOGIE
# Zbellion - Simulateur de Propagation d'Influence et de Cliodynamique

Et si les mathématiques nous aidaient à comprendre comment un mouvement social prend de l’ampleur ?

Ce dépôt contient un simulateur multi-agents développé en Python (via la bibliothèque `NetworkX`) permettant d'étudier comment une idée se propage dans une population grâce à la théorie des graphes. 

Inspiré par la **« Zbellion »** 🤺 — nom de code d'un exercice de simulation du Pentagone qui a fuité dans la presse, imaginant une insurrection décentralisée de la génération Z —, ce projet applique les principes de la **cliodynamique**. Cette science transdisciplinaire utilise les modèles mathématiques et les simulations informatiques pour analyser l'histoire et les trajectoires sociales sur le temps long. C'est également une excellente application des probabilités, des statistiques et de la théorie des jeux.

---

## 📐 Modélisation et Formules Mathématiques

La simulation repose sur un réseau de **Barabási-Albert** ($N = 100$ nœuds, $m = 2$), un modèle de graphe qui reproduit fidèlement la structure "scale-free" (invariante d'échelle) des réseaux sociaux réels. L'information y est partagée entre des **Hubs** (comptes ultra-connectés / influenceurs) et des nœuds standards.

Chaque individu possède un état `Statut = 1` (actif/activiste) ou `Statut = 0` (inactif). Au départ, les profils sont distribués de manière stochastique :
* **Initiateurs** (10%) : Actifs dès l'étape 0 ($t=0$). Ils lancent le mouvement.
* **Modérés** (50%) : Décision basée sur une rationalité locale.
* **Prudents** (40%) : Décision basée sur une sécurité globale.

À chaque itération $t$, le simulateur évalue les conditions de bascule pour les nœuds inactifs selon deux profils stratégiques distincts :

### 1. Le Profil Modéré : Rationalité Topologique Locale
Les Modérés calculent l'influence relative de leurs contacts directs (voisins dans le graphe). Ils n'analysent pas seulement le *nombre* d'amis actifs, mais le **poids (degré)** de ces amis. Si leurs leaders ou amis influents s'activent, le risque perçu s'effondre et rejoindre le mouvement devient un choix rationnel.

Soit $i$ un nœud de profil Modéré, $V(i)$ l'ensemble de ses voisins, et $d(v)$ le degré (nombre de connexions) du voisin $v$. Le nœud $i$ devient actif si :

$$\frac{\sum_{v \in V(i) \text{ et } Statut(v)=1} d(v)}{\sum_{v \in V(i)} d(v)} \geq \text{Seuil modéré} \quad (\text{avec Seuil modéré} = 0.30)$$

### 2. Le Profil Prudent : Seuil de Granovetter Global
Les Prudents ignorent l'état de leur entourage proche et cherchent la sécurité de la masse globale (mimétisme social ou modèle de seuil de Granovetter). Ils ne basculent que si la proportion globale de la population totale engagée franchit un cap psychologique critique.

Soit $A_t$ le nombre total d'activistes dans le réseau à l'étape $t$, et $N$ la taille totale de la population. Le nœud $i$ devient actif si :

$$\frac{A_t}{N} \geq \text{Seuil prudent} \quad (\text{avec Seuil prudent} = 0.60)$$

---

## 📊 Des Résultats Fascinants (Transitions de Phase)

En modifiant légèrement les seuils de tolérance ou la topologie, le simulateur met en évidence le concept physique et sociologique de **transition de phase** :

* **Scénario 1 (Résilience / Stagnation)** : L'idéologie reste confinée et stagne à un équilibre de ~12% d'activistes (seuls les initiateurs et de rares modérés isolés s'activent). Le réseau est stable et étouffe la propagation.
* **Scénario 2 (Insurrection totale / Effet Domino)** : Les Modérés entraînent les Hubs, ce qui fait exploser le score global et brise instantanément le verrou des Prudents. Le système subit un effet domino exponentiel et sature à 100% en à peine 3 itérations.

### L'aléa du comportement stochastique
La dynamique est profondément stochastique. En relançant l'expérience avec les mêmes paramètres exacts, le résultat peut basculer du tout au tout. Si le hasard de la distribution initiale (`random.choices`) place l'idée chez des utilisateurs isolés, elle s'éteint. Si elle touche un **Hub**, le système entier bascule. L'aléa de départ dicte le destin du réseau.

---

## 🚀 Prochaines étapes : Application à la Santé Publique 💉

Cette approche par graphes et réseaux complexes s'applique aussi bien aux faits sociaux qu'à la santé publique. Le prochain module de ce projet portera sur la modélisation de **l'obligation vaccinale en Cité Universitaire**, analysant comment le refus ou l'acceptation d'un vaccin se diffuse au sein d'une communauté étudiante connectée.

## 🛠️ Installation et Lancement

```bash
# 1. Cloner le projet
git clone https://github.com
cd PROPAGATION_D-UNE_IDEOLOGIE

# 2. Installer les dépendances
pip install networkx matplotlib

# 3. Exécuter la simulation
python graphes_social_ideologie.py
```


## 🛠️ Technologies

![Python](https://shields.io) ![NetworkX](https://shields.io) ![Matplotlib](https://shields.io)
