from import_export import resources, fields
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from .models import Veterinarian, Delivered
from ..accounts.models import User



class VeterinarianResource(resources.ModelResource):
    f = Field(
        column_name="Xadim Ismi",
        attribute="user",
        widget=ForeignKeyWidget(User, field="first_name")
    )
    l = Field(
        column_name="Xodim Familyasi",
        attribute="user",
        widget=ForeignKeyWidget(User, field="last_name")
    )

    class Meta:
        model = Veterinarian
        fields = (
            "first_name",
            "moisture",
            "temperature",
            "day",
            "conclusion",
            "addition",
        )


class DeliveredResource(resources.ModelResource):
    f = Field(
        column_name="Xadim Ismi",
        attribute="user",
        widget=ForeignKeyWidget(User, field="first_name")
    )
    l = Field(
        column_name="Xodim Familyasi",
        attribute="user",
        widget=ForeignKeyWidget(User, field="last_name")
    )

    class Meta:
        model = Delivered
        fields = (
            "first_name",
            "phone",
            "product_count",
            "addition",
        )
