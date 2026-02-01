def _insert_by_diff(best, diffs, product, diff, k):
    pos = 0
    while pos < len(diffs) and diffs[pos] <= diff:
        pos += 1

    best.insert(pos, product)
    diffs.insert(pos, diff)

    if len(best) > k:
        best.pop()
        diffs.pop()


def recommend_products(products, current_product, k=5, price_percent=0.2):
    if current_product.price < 0:
        return []

    threshold = current_product.price * price_percent
    best = []
    diffs = []

    for p in products:
        if p.id == current_product.id:
            continue
        if p.category != current_product.category:
            continue

        diff = p.price - current_product.price
        if diff < 0:
            diff = -diff

        if diff <= threshold:
            _insert_by_diff(best, diffs, p, diff, k)

    return best
