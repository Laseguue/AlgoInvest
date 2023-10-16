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
                price = int(float(price) * 100)
                profit = float(profit)
                if price <= 0 or profit < 0:
                    continue
                actions.append((name, price, profit))
            except ValueError:
                continue
    return actions

def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    res = K[n][W]
    w = W
    selected_actions = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i-1][w]:
            continue
        else:
            selected_actions.append((i-1))
            res -= val[i-1]
            w -= wt[i-1]

    return K[n][W], selected_actions

if __name__ == '__main__':
    fichier = input("Entrez le nom du fichier csv complet avec son extension :")
    actions = lire_fichier_csv(fichier)

    profit = [int(action[1] * (action[2] / 100)) for action in actions]
    weight = [action[1] for action in actions]
    W = int(float(input("Entrez le budget maximum :")) * 100)
    
    n = len(profit)
    max_profit_in_cents, selected = knapSack(W, weight, profit, n)
    total_invested = sum([weight[i] for i in selected])
    print("Actions sélectionnées:")
    for i in selected:
        print(actions[i][0])
    print("Total investi : {:.2f}€".format(total_invested / 100))
    print("Profit maximal possible : {:.2f}€".format(max_profit_in_cents / 100))
