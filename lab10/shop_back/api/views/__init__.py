# Активен Level 5 (Generics)
# Чтобы переключить — поменяй строку ниже:
# Level 2: from api.views.fbv    import products_list, product_detail
# Level 3: from api.views.cbv    import ProductListAPIView, ProductDetailAPIView
# Level 4: from api.views.mixins import ProductListAPIView, ProductDetailAPIView

from api.views.generics import (
    ProductListAPIView,
    ProductDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    CategoryProductsAPIView,
)
from api.views.fbv import products_list, product_detail