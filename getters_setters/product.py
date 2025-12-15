class Product:
    product_id:int
    product_name:str
    product_manu_number:str
    
    def __init__(self, product_id:int, product_name:str, product_manu_number:str):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_manu_number = product_manu_number
        
    #we create a property with @property annotation..here it define the getter property.
    #property method name must be variable name
    
    @property
    def product_id(self):
        return self.__product_id
    
    @product_id.setter
    def product_id(self, product_id:int):
        self.__product_id = product_id
        
    @property
    def product_manu_number(self):
        return self.__product_manu_number
    
    @product_manu_number.setter
    def product_manu_number(self, product_manu_number:str):
        if "@" in product_manu_number:
            self.__product_manu_number = product_manu_number
        return "Error"
    
    
    # when we accessing the pruivate varibales now we do not need the get method call set method call. normally act like calling and assigning varibales

product = Product(1,"Laptop","lap123@345")

print(product.product_id)
print(product.product_manu_number)

product.product_manu_number = "123@567"
print(product.product_manu_number)
            