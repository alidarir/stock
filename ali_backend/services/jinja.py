
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("ali_backend"),
    autoescape=True,
)
response_templates = Jinja2Templates(directory="ali_backend/templates")

# Use the primary environment inside of the Jinja2Templates wrapper.
response_templates.env = env
