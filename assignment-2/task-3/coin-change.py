
def greedy_coin_change(coins: list, target: int):
    if 1 not in coins:
        coins.insert(0, 1)

    chosen_coins = []

    coin_count = 0
    i = len(coins) - 1
    
    while target > 0:
        if coins[i] > target:
            i -= 1
            continue

        cur_coin = coins[i]
      
        count = target // cur_coin
        coin_count += count

        target %= coins[i]

        chosen_coins.extend([cur_coin] * count)

        i -= 1
    
    return coin_count, chosen_coins


def dynamic_coin_change(coins: list, target: int):
    if 1 not in coins:
        coins.insert(0, 1)

    min_coins_needed = [float('inf')] * (target + 1)
    min_coins_needed[0] = 0
    chosen_coins = [[] for _ in range(target + 1)]

    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0:
                new_count = min_coins_needed[i - coin] + 1

                if new_count < min_coins_needed[i]:
                    min_coins_needed[i] = new_count

                    chosen_coins[i] = chosen_coins[i - coin] + [coin]

    return min_coins_needed[target], chosen_coins[target]


if __name__ == "__main__":
    print("")
 
    coins_from_task = [1, 5, 11]
    coins_norwegian = [1, 5, 10, 20]

    # coins = coins_from_task
    coins = coins_norwegian

    print("Selectable coins: ", coins)

    target = 37
    print("Target sum: ", target)

    print("")

    greedy_count, greedy_coins = greedy_coin_change(coins, target)

    print("Greedy Solution:")
    print("Chosen coins:", greedy_coins)
    print("Num coins:", greedy_count)

    print("")

    dynamic_count, dynamic_coins = dynamic_coin_change(coins, target)

    print("Dynamic Solution:")
    print("Chosen coins:", dynamic_coins)
    print("Num coins:", dynamic_count)

    print("")