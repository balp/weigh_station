from pyramid.view import view_config

from .storage import seen_passages


@view_config(route_name="register_passage", renderer="json", request_method='POST')
def register_passage(request):
    json_data = request.json
    seen_passages.lorries += json_data["lorries"]
    seen_passages.tons += json_data["tons"]
    return {"station": "Station One",
            "lorries": seen_passages.lorries,
            "tons": seen_passages.tons,
            }
