from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product_list = dao.select_all()
    assert len(product_list) >= 3

def test_product_insert():
    new_product = Product(None, "Test Product", "Test Brand", 9.99)
    product_id = dao.insert(new_product)
    assert product_id is not None

def test_product_update():
    product = dao.select_all()[0]
    product.name = "Updated Product"
    dao.update(product)
    updated_product = dao.select_all()[0]
    assert updated_product.name == "Updated Product"

def test_product_delete():
    product = dao.select_all()[0]
    dao.delete(product.id)
    deleted_product = dao.select_all()
    assert product not in deleted_product