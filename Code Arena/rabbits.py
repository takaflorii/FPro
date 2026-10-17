def rabbits(x, x_max, r, n):
    bunnelby = x

    for _ in range(n):
        next_gen = bunnelby * r * (x_max - bunnelby) / x_max
        bunnelby = round(next_gen)

    return bunnelby
