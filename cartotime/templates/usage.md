
# Usage de cartotime

Cartotime est un projet Python/Django intégrant TimelineJS et Leaflet.JS (et Open Street Map) pour synchroniser les évènements TimelineJS à des marqueurs sur la carte.

Les évènements sont créés dans l'interface d'administration de Django, donc présents dans une base de données, et non modifiables sans les autorisations nécessaires.

Les frises et cartes sont publiques, en l'état actuel de l'implémentation.

Vous pouvez créer autant de couples frise/carte que vous le souhaitez.

Dans l'interface d'administration, ces entités correspondent à des « Timeline ».

Chaque Timeline peut contenir autant d'évènements que souhaité.

La carte peut être centrée sur une localisation arbitraire si l'attribut `center_on` de la Timeline contient des coordonnées GPS. Par exemple, pour center sur Cap Sciences, saisir « [44.85965, -0.55489] ». Attention, les virgules et points sont importants, c'est la syntaxe anglaise.


# ATTENTION

- Si un évènement a des coordonnées, alors tous autres doivent en avoir aussi ; sinon il y aura un décallage dans l'ordre des diapositive par rapport à la synchronisation avec la carte, et le rendu semblera désordonné à l'utilisateur. En cas de doute, mettre des coordonnées factices aux projets qui n'en ont pas, par exemple [0, 0] ou les coordonnées de la capitale du pays d'émergence de l'évènement.


# Bugs connus

- lors du premier chargement de la page, un clic sur un marqueur de celle-ci ne met pas à jour la frise. Alors que si l'on commence par cliquer sur la frise, les comportements par la suite sont ceux attendus, autant sur la frise que la carte.


# Suivi de projet / fonctionnel

Toutes les informations relatives sont disponibles dans un Google Doc partagé ici :

https://docs.google.com/document/d/1VDP01kBLRvxyN6s_xxjj66MUTh3LhK4xcVWAcnQLrFU/edit#
