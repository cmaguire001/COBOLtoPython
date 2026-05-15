from pydantic import BaseModel, create_model


def generate_pydantic_model(name: str, fields: list):
    model_fields = {}

    for field in fields:
        model_fields[field.name.replace('-', '_')] = (str, ...)

    return create_model(name, **model_fields)
