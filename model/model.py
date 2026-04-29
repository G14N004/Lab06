from database.DAO import DAO
class Model:
    def __init__(self):
        pass

    def getYears(self):
        return DAO.getAnni()

    def getBrands(self):
        return DAO.getBrand()

    def getRetailers(self):
        return DAO.getRetailer()

    def getTopVendites(self,anno,retailer,brand):
        return DAO.getTopVendite(anno,retailer,brand)

    def getAnalizzaVendites(self,anno,retailer,brand):
        return DAO.getAnalizzaVendite(anno,retailer,brand)
