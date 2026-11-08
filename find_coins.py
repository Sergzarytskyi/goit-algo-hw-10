import timeit


coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int):
    count_coins = {}
    for coin in coins:
        count = amount // coin
        if count > 0:
            count_coins[coin] = count
            amount -= coin * count
    return count_coins

def find_min_coins(amount, coins):

    min_coins_required = [0] + [float("inf")] * amount
    last_coin_used = [0] * (amount + 1)


    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                last_coin_used[i] = coin

    if min_coins_required[amount] == float("inf"):
        return {}  

    result = {}
    i = amount
    while i > 0:
        coin = last_coin_used[i]
        result[coin] = result.get(coin, 0) + 1
        i = i - coin

    return dict(sorted(result.items()))





if __name__ == "__main__":
    find_coins_amount = 113
    result_greedy = find_coins_greedy(find_coins_amount)
    print(f"Жадібний алгоритм підбору монет для суми {find_coins_amount}: {result_greedy}")
    result = find_min_coins(find_coins_amount, coins)
    print(f"Алгоритм динамічного програмування з  підбору монет для суми {find_coins_amount}: {result}\n")
# тест на швидкодію обох алгоритмів

    print(f"{'Сума':>9} | {'Жадібний, сек':>13} | {'Динамічний, сек':>10}")
    print("-" * 44)
    for amount in [113, 1000, 10000, 100000, 1000000]:
        greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=10) / 10
        dp_time = timeit.timeit(lambda: find_min_coins(amount, coins), number=10) / 10
        print(f"{amount:>9} | {greedy_time :>12.8f}  | {dp_time :>12.8f}")