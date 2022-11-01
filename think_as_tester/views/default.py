from dataclasses import dataclass
import logging

from pyramid.view import view_config


@dataclass
class StationData:
    lorries: int
    tons: int


seen_passages = StationData(0, 0)


@view_config(route_name="home", renderer="think_as_tester:templates/mytemplate.jinja2")
def my_view(request):
    return {"station": "Station One",
            "lorries": seen_passages.lorries,
            "tons": seen_passages.tons,
            }


@view_config(route_name="register_passage", renderer="json", request_method='POST')
def register_passage(request):
    json_data = request.json
    seen_passages.lorries += json_data["lorries"]
    seen_passages.tons += json_data["tons"]
    return {"station": "Station One",
            "lorries": seen_passages.lorries,
            "tons": seen_passages.tons,
            }
