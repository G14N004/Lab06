import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillAnno(self):
        for elm in self._model.getYears():
            self._view.DDAnno.options.append(
                ft.dropdown.Option(key= elm, data=elm))
        self._view.DDAnno.options.append(
            ft.dropdown.Option(text="nessun filtro")
            )

    def fillBrand(self):
        for b in self._model.getBrands():
            self._view.DDBrand.options.append(
                ft.dropdown.Option(key=b , data=b)
            )
        self._view.DDBrand.options.append(
            ft.dropdown.Option(text="nessun filtro")
        )




    def fillRetailer(self):
        for r in self._model.getRetailers():
            self._view.DDRetailer.options.append(
                ft.dropdown.Option(key=r.Retailer_code , text=r.Retailer_name , data=r)
            )
        self._view.DDRetailer.options.append(
            ft.dropdown.Option(text="nessun filtro")
        )




    def handle_top_vendite(self,e):
        anno=self._view.DDAnno.value
        brand=self._view.DDBrand.value
        retailer=self._view.DDRetailer.value
        if anno == "nessun filtro" or anno is None:
            anno=None
        else:
            anno=int(anno)
        if brand == "nessun filtro" or brand is None:
            brand=None
        if retailer == "nessun filtro" or retailer is None:
            retailer=None
        else:
            retailer=int(retailer)
        lista = self._model.getTopVendites(anno,retailer,brand)
        match = lista[:5]
        self._view.txt_result.controls.clear()
        if len(match) == 0:
            self._view.txt_result.controls.append(ft.Text("Nessuna vendita trovata"))
        for elm in match:
            self._view.txt_result.controls.append(ft.Text(f"Data : {elm[0]} ; ricavo : {elm[1]} ; retailer : {elm[2]} ; Product: {elm[3]}"))

        self._view.update_page()

    def handle_analizza_vendite(self,e):
        anno = self._view.DDAnno.value
        brand = self._view.DDBrand.value
        retailer = self._view.DDRetailer.value
        if anno == "nessun filtro" or anno is None:
            anno = None
        else:
            anno = int(anno)
        if brand == "nessun filtro" or brand is None:
            brand = None
        if retailer == "nessun filtro" or retailer is None:
            retailer = None
        else:
            retailer = int(retailer)
        lista = self._model.getAnalizzaVendites(anno, retailer, brand)
        self._view.txt_result.controls.clear()
        if len(lista) == 0:
            self._view.txt_result.controls.append(ft.Text("Nessuna vendita trovata"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"statistiche vendite"))
        somma=0
        numero_vendite=lista[0][-1]
        dizionario={}
        ret=[]
        prod=[]
        for elm in lista :
            somma+=elm[1]
            ret.append(elm[2])
            prod.append(elm[3])

        set_ret=set(ret)
        set_prod=set(prod)
        numero_retailer=len(set_ret)
        numero_prodotti=len(set_prod)

        #prima_chiave=next(iter(dizionario))
        #numero_retailer=dizionario[prima_chiave]

        #it = iter(dizionario)
        #next(it)# salto la prima chiave
        #seconda_chiave=next(it)
        #numero_prodotti=dizionario[seconda_chiave]




        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari : {somma} ({somma/1000000} milioni )\nNumero vendite : {numero_vendite}\nNumero retailers coinvolti : {numero_retailer}\nNumero prodotti coinvolti : {numero_prodotti}"))
        self._view.update_page()


