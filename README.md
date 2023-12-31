 - Brutforce 

Titre: Maximisation de profit d'investissement dans des actions

Description:
Cet algorithme permet de maximiser le profit d'un investissement dans des actions en fonction d'un budget donné. Le fichier CSV contient des données sur les actions disponibles, y compris leur nom, leur prix et leur profit potentiel. L'algorithme génère ensuite toutes les combinaisons possibles d'actions dont le coût total ne dépasse pas le budget donné. Parmi ces combinaisons, il sélectionne celle qui offre le profit le plus élevé et affiche les actions à acheter, le coût total de l'investissement et le profit total.

Utilisation:

Assurez-vous que le fichier CSV contenant les données sur les actions est correctement formaté avec les colonnes "Nom", "Prix" et "Profit" dans cet ordre.
Lancez le script Python et suivez les instructions pour entrer le nom du fichier CSV et le budget maximum.
L'algorithme affichera ensuite les meilleures actions à acheter en fonction du budget donné, ainsi que le coût total et le profit total attendus.
Cas d'utilisation:

L'algorithme convient aux investisseurs cherchant à maximiser leur profit en achetant un portefeuille d'actions avec un budget donné.
Il est utile pour les gestionnaires de fonds cherchant à identifier les meilleures actions à inclure dans un portefeuille d'investissement avec des contraintes budgétaires.
Les investisseurs individuels qui souhaitent diversifier leur portefeuille avec un budget limité peuvent également utiliser cet algorithme pour prendre des décisions éclairées.
ex : 
10 actions, l'algorithme doit générer 2^10 (1024) combinaisons possibles. Avec 20 actions, il doit en générer 2^20 (1,048,576).

- Optimized 

Titre: Sélection d'actions en fonction du rendement sur investissement

Description:
Cet algorithme vise à sélectionner les meilleures actions en fonction de leur rendement sur investissement (ROI) en pourcentage. Le fichier CSV contient des données sur les actions disponibles, y compris leur nom, leur prix et le pourcentage de rendement potentiel. L'algorithme calcule le rendement pour chaque action, puis les trie en fonction du rapport rendement/coût décroissant. Il sélectionne ensuite les actions qui rentrent dans le budget donné et affiche leur nom, le coût total de l'investissement et le profit total en pourcentage attendu.

Utilisation:

Assurez-vous que le fichier CSV contenant les données sur les actions est correctement formaté avec les colonnes "Nom", "Prix" et "Pourcentage de rendement" dans cet ordre.
Lancez le script Python et suivez les instructions pour entrer le nom du fichier CSV et le budget maximum.
L'algorithme affichera ensuite les meilleures actions à acheter en fonction du budget donné, ainsi que le coût total de l'investissement et le profit total en pourcentage attendus.
Cas d'utilisation:

Cet algorithme est particulièrement utile pour les investisseurs qui souhaitent maximiser leur rendement sur investissement en priorisant les actions offrant les meilleurs pourcentages de rendement.
Il est adapté aux investisseurs qui ont un budget fixe et qui cherchent à constituer un portefeuille d'actions avec les meilleures opportunités de rendement.
Les investisseurs soucieux de leur rendement à long terme peuvent utiliser cet algorithme pour prendre des décisions d'investissement éclairées et équilibrées.
ex: 
a) Calcul du rendement de chaque action : L'algorithme commence par calculer le rendement de chaque action en multipliant le prix de l'action par son pourcentage de profit potentiel. Ainsi, nous obtenons une mesure directe de la rentabilité de chaque action.

b) Tri des actions par rendement par rapport au coût : Ensuite, l'algorithme trie les actions par rapport au rapport entre leur rendement et leur coût. Cela signifie que les actions les plus rentables se retrouvent en tête de liste.

c) Sélection des actions les plus rentables dans le budget : Enfin, l'algorithme parcourt la liste triée des actions et sélectionne les actions les plus rentables, tant que le budget disponible le permet. Ainsi, il choisit directement les actions offrant le meilleur rapport rendement/coût sans avoir besoin de générer toutes les combinaisons possibles.

Knapsack
Titre: Maximisation du profit d'investissement avec l'algorithme du sac à dos

Description:
L'algorithme du sac à dos est une méthode classique en programmation dynamique permettant de résoudre des problèmes d'optimisation. Dans ce contexte, il est utilisé pour maximiser le profit d'un investissement dans des actions, tout en respectant un budget donné. Le fichier CSV contient des données sur les actions disponibles, notamment leur nom, leur prix et leur profit potentiel. L'algorithme utilise une approche tabulaire pour déterminer le profit maximal possible pour un budget donné et retrouve ensuite les actions spécifiques qui ont été incluses dans cette solution optimale.

Utilisation:

Assurez-vous que le fichier CSV contenant les données sur les actions est correctement formaté avec les colonnes "Nom", "Prix" et "Profit" dans cet ordre.
Lancez le script Python et suivez les instructions pour entrer le nom du fichier CSV et le budget maximum.
L'algorithme affichera les actions optimales à acheter, le coût total de l'investissement et le profit maximal attendu.
Cas d'utilisation:

L'algorithme convient aux investisseurs qui veulent une solution optimale pour investir un budget fixe dans un ensemble d'actions afin de maximiser les retours.
Les gestionnaires de fonds qui cherchent à diversifier leur portefeuille tout en maximisant le profit peuvent également bénéficier de cette méthode.
Les investisseurs individuels avec un budget limité trouveront cet algorithme utile pour prendre des décisions d'investissement éclairées.
Points clés:

a) Programmation dynamique : L'algorithme utilise une table pour stocker les résultats intermédiaires, ce qui réduit le temps de calcul en évitant de recalculer les mêmes résultats.

b) Conversion en centimes : Pour éviter les erreurs d'arrondi, toutes les valeurs monétaires sont converties en centimes pour les calculs.

c) Récupération des actions sélectionnées : Une fois la table remplie, l'algorithme parcourt la table à rebours pour déterminer les actions spécifiques qui ont été incluses dans la solution optimale.

d) Efficacité : Contrairement à l'approche de force brute qui génère toutes les combinaisons possibles, l'algorithme du sac à dos est plus efficace car il utilise une approche tabulaire pour résoudre le problème. Pour un ensemble de n actions et un budget W, sa complexité est de O(nW).