from django.urls import path
from main.views import create_shop, show_json, show_json_by_id, show_main, show_xml, show_xml_by_id

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("create-shop", create_shop, name="create_shop"),
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<str:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<str:id>/", show_json_by_id, name="show_json_by_id"),
]
