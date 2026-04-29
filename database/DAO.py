from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():

    @staticmethod
    def getAnni():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor()
        query="""
        SELECT Distinct Year(Date)
            from go_daily_sales gds 
        """
        cursor.execute(query)
        res=[]
        for row in cursor:
            res.append(row[0])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getBrand():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor()
        query="""
        SELECT DISTINCT  Product_Brand
            from go_products gp """
        cursor.execute(query)
        res=[]
        for row in cursor:
            res.append(row[0])
        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getRetailer():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""
        SELECT *
            from go_retailers gr """
        cursor.execute(query)
        res=[]
        for row in cursor:
            res.append(Retailer(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getTopVendite(anno,retailer,brand):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""
            SELECT gds.date AS data,
        (gds.Unit_sale_price * gds.Quantity) AS ricavo, 
        gr.Retailer_code AS retailer_code, 
        gp.Product_number AS product_number
        FROM go_daily_sales gds, 
        go_retailers gr, 
        go_products gp
        WHERE gr.Retailer_code = gds.Retailer_code 
        AND gp.Product_number = gds.Product_number 
        AND YEAR(gds.date) = COALESCE(%s, YEAR(gds.date))
        AND gr.Retailer_code = COALESCE(%s, gr.Retailer_code)
        AND gp.Product_brand = COALESCE(%s, gp.Product_brand)
        ORDER BY ricavo desc
        """
        cursor.execute(query,(anno,retailer,brand))
        res=[]
        for row in cursor:
            res.append((row["data"], row["ricavo"], row["retailer_code"], row["product_number"]))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAnalizzaVendite(anno,retailer,brand):
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)
        query="""
        SELECT gds.date AS data,
        (gds.Unit_sale_price * gds.Quantity) AS ricavo, 
        gr.Retailer_code AS retailer_code, 
        gp.Product_number AS product_number,
        COUNT(*) OVER() AS numero_vendite
        FROM go_daily_sales gds, 
        go_retailers gr, 
        go_products gp
        WHERE gr.Retailer_code = gds.Retailer_code 
        AND gp.Product_number = gds.Product_number 
        AND YEAR(gds.date) = COALESCE(%s, YEAR(gds.date))
        AND gr.Retailer_code = COALESCE(%s, gr.Retailer_code)
        AND gp.Product_brand = COALESCE(%s, gp.Product_brand)
        ORDER BY ricavo desc
        """
        cursor.execute(query,(anno,retailer,brand))
        res=[]
        for row in cursor:
            res.append((row["data"], row["ricavo"], row["retailer_code"], row["product_number"],row["numero_vendite"]))

        cursor.close()
        cnx.close()
        return res




