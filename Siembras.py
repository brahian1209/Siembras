import pandas as pd

tablaMunicipios=pd.read_csv('./Siembras.csv')
#print(tablaMunicipios)
#print(tablaMunicipios.to_string())

'''

#filtro 1 quiero obtener todos los datos de los analistas 1 y crear la tabla html
datosMunicipios=tablaMunicipios [(tablaMunicipios ['Ciudad'] == 'Barbosa')|(tablaMunicipios ['Ciudad'] == 'Andes')|(tablaMunicipios ['Ciudad'] == 'Caldas')|(tablaMunicipios ['Ciudad'] == 'Yarumal')|(tablaMunicipios ['Ciudad'] == 'Támesis')]

archivoHTML=datosMunicipios.to_html()
archivoTEXTO=open("tabla_municipios.html","w", encoding="UTF-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()


#filtro 2  Los datos de CAUCASIA incluyendo el número de hectáreas sembradas
datosMedellin=tablaMunicipios [(tablaMunicipios ['Ciudad'] == 'Medellín')]
datosMedellin=datosMedellin.sort_values(by="Arboles",ascending=False)


archivoHTML=datosMedellin.to_html()
archivoTEXTO=open("tabla_Medellin.html","w", encoding="UTF-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

#filtro 3  Los datos de CAUCASIA incluyendo el número de hectáreas sembradas de forma ascendente 
datosCAUCASIA=tablaMunicipios [(tablaMunicipios ['Ciudad'] == 'Caucasia')]
datosCAUCASIA=(datosCAUCASIA["Hectareas"]).to_frame()
datosCAUCASIA=datosCAUCASIA.sort_values(by="Hectareas",ascending=False)
archivoHTML=datosCAUCASIA.to_html()
archivoTEXTO=open("tabla_Caucasia.html","w", encoding="UTF-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()


#filtro 4  Los datos de Santa Fe de Antioquia donde se tengan siembras de >250 arboles 

datosSantafeAntioquia=tablaMunicipios [(tablaMunicipios ['Ciudad'] == 'Santa Fe de Antioquia')]
datosSiembra=datosSantafeAntioquia [(datosSantafeAntioquia ['Arboles']) >= 250]
print(datosSiembra)

archivoTEXTO=open("tabla_SantaFe.html","w", encoding="UTF-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

#filtro 5 Los datos de las veredas Rio Arriba y la Salazar de Belmira
datosVeredas=tablaMunicipios [(tablaMunicipios ['Vereda'] == 'Rio Arriba')|(tablaMunicipios ['Vereda'] == 'La Salazar')]
archivoHTML=datosVeredas.to_html()
archivoTEXTO=open("tabla_veredas.html","w", encoding="UTF-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

#filtro 6  Los datos de la veredas Quitasol de BELLO ordenados de menor a mayor y el promedio de arboles sembrados en esta vereda

datosBello=tablaMunicipios [(tablaMunicipios ['Ciudad'] == 'Bello')]
datoVereda=datosBello [(datosBello ['Vereda']) == "Quitasol"]
datoVereda=datoVereda.sort_values(by="Arboles")  #-----> Imprimir esta

archivoHTML=datoVereda.to_html()
archivoTEXTO=open("tabla_Bello.html","w", encoding="UTF-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()


estadisticasVereda = datoVereda.describe()
estadisticasVeredaMedias = estadisticasVereda.loc[["mean"]]
estadisticasMediaArboles=(estadisticasVeredaMedias["Arboles"]).to_frame() #-----> Imprimir esta

archivoHTML=estadisticasMediaArboles.to_html()
archivoTEXTO=open("Estadisticas_Bello.html","w", encoding="UTF-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()


#filtro 7 Los datos de las veredas Rio Arriba y la Salazar de Belmira
datosVeredas=tablaMunicipios [(tablaMunicipios ['Ciudad'] == 'Caramanta')]

archivoHTML=datosVeredas.to_html()
archivoTEXTO=open("tabla_caramanta.html","w", encoding="UTF-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()

'''


