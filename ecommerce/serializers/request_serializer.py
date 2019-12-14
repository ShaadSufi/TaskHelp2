from . import BaseSerializer, ExtDict, ExtList
from requests.models import Requests as ProductRequest


class PastRequestSerializer(BaseSerializer):
    def __init__(self, product_request: ProductRequest):
        self.product_request = product_request

    def to_dict(self) -> ExtDict:
        dic = ExtDict({
                    'id': self.product_request.id,
                    'product_name': self.product_request.product.name,
                    'status': self.product_request.status
                    })
        return dic


