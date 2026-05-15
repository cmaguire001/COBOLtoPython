def diff_schemas(schema_a: list, schema_b: list):
    set_a = set(schema_a)
    set_b = set(schema_b)

    return {
        'added': list(set_b - set_a),
        'removed': list(set_a - set_b),
        'unchanged': list(set_a & set_b)
    }
