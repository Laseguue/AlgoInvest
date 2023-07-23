import csv
import itertools

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
                if price < 0 or profit < 0:
                    continue
                actions.append((name, price, profit))
            except ValueError:
                continue
    return actions

def generer_combinaisons(actions):
    combinaisons = []
    for i in range(1, len(actions) + 1):
        for subset in itertools.combinations(actions, i):
            price = sum(x[1] for x in subset)
            if price <= 500:
                combinaisons.append(subset)
    return combinaisons

def calculer_profit(combinaison):
    return sum(x[1] * (x[2] / 100) for x in combinaison)

def meilleur_invest(actions):
    combinaisons = generer_combinaisons(actions)
    meilleure_combinaison = max(combinaisons, key=calculer_profit)
    return meilleure_combinaison

def main():
    actions = lire_fichier_csv(input("Entrez le nom du fichier csv complet avec son extension :"))
    budget = int(input("Entrez le budget maximum :"))
    placement = meilleur_invest(actions)
    
    total_cost = sum([action[1] for action in placement])
    total_profit = sum([action[1] * (action[2] / 100) for action in placement])

    print("Actions à acheter :")
    for action in placement:
        print(action[0])

    print("\nCoût total: {:.2f}€".format(total_cost))
    print("Profit: {:.2f}€".format(total_profit))

if __name__ == '__main__':
    main()
