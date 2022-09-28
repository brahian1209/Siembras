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

'''



#filtro 3  Los datos de CAUCASIA incluyendo el número de hectáreas sembradas
datosCAUCASIA=tablaMunicipios [(tablaMunicipios ['Ciudad'] == 'Caucasia')]
datosCAUCASIA=(datosCAUCASIA["Hectareas"]).to_frame()
datosCAUCASIA=datosCAUCASIA.sort_values(by="Hectareas",ascending=False)
print(datosCAUCASIA)

'''
archivoHTML=datosCAUCASIA.to_html()
archivoTEXTO=open("tabla_Caucasia.html","w", encoding="UTF-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
'''


