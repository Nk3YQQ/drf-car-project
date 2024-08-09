def get_params(queryset, query_params: dict):
    """ Функция фильтрует запрос в query """

    brand = query_params.get('brand')
    model = query_params.get('model')
    year = query_params.get('year')
    fuel_type = query_params.get('fuel_type')
    transmission = query_params.get('transmission')
    mileage_min = query_params.get('mileage_min')
    mileage_max = query_params.get('mileage_max')
    price_min = query_params.get('price_min')
    price_max = query_params.get('price_max')

    if brand:
        queryset = queryset.filter(brand__iexact=brand)

    if model:
        queryset = queryset.filter(model__iexact=model)

    if year:
        queryset = queryset.filter(year=year)

    if fuel_type:
        queryset = queryset.filter(fuel_type__iexact=fuel_type)

    if transmission:
        queryset = queryset.filter(transmission__iexact=transmission)

    if mileage_min:
        queryset = queryset.filter(mileage__gte=mileage_min)

    if mileage_max:
        queryset = queryset.filter(mileage__lte=mileage_max)

    if price_min:
        queryset = queryset.filter(price__gte=price_min)

    if price_max:
        queryset = queryset.filter(price__lte=price_max)

    return queryset
