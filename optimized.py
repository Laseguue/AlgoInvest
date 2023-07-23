import csv

def lire_fichier_csv(fichier):
    actions = []
    with open(fichier, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            try:
                name, price, profit = row
                if not name or not price or not profit:
                    continue
                price = float(price)
                profit = float(profit)
                if price <= 0 or profit < 0:
                    continue
                actions.append((name, price, profit))
            except ValueError:
                continue
    return actions

def calcul_rendement(action):
    nom, cout, pourcentage_rendement = action
    rendement = cout * pourcentage_rendement / 100
    return (nom, rendement, cout, pourcentage_rendement)

def rendement_actions(actions):
    rendement = []
    for action in actions:
        rendement.append(calcul_rendement(action))
    return rendement

def meilleur_invest(budget, actions):
    rendements = rendement_actions(actions)

    rendements.sort(key=lambda x: x[1] / x[2], reverse=True)

    actions_selectionnees = []
    for action in rendements:
        nom, rendement, cout, pourcentage_rendement = action
        if cout <= budget:
            actions_selectionnees.append((nom, cout, pourcentage_rendement))
            budget -= cout
    return actions_selectionnees

def main():
    actions = lire_fichier_csv(input("Entrez le nom du fichier csv complet avec son extension :"))
    budget = int(input("Entrez le budget maximum :"))
    placement = meilleur_invest(budget, actions)
    
    total_cost = sum([action[1] for action in placement])
    total_profit = sum([action[1] * (action[2] / 100) for action in placement])

    print("Les meilleures actions à acheter sont :")
    for action in placement:
        print(action[0])

    print("\nCoût total: {:.2f}€".format(total_cost))
    print("Profit: {:.2f}€".format(total_profit))

if __name__ == '__main__':
    main()



