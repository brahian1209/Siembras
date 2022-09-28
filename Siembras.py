import pandas as pd

tablaMunicipios=pd.read_csv('./Siembras.csv')
#print(tablaMunicipios)
#print(tablaMunicipios.to_string())


#filtro 1 quiero obtener todos los datos de los analistas 1 y crear la tabla html

datosMunicipios=tablaMunicipios [(tablaMunicipios ['Ciudad'] == 'Barbosa')|(tablaMunicipios ['Ciudad'] == 'Andes')|(tablaMunicipios ['Ciudad'] == 'Caldas')|(tablaMunicipios ['Ciudad'] == 'Yarumal')|(tablaMunicipios ['Ciudad'] == 'Támesis')]

archivoHTML=datosMunicipios.to_html()
archivoTEXTO=open("tabla_municipios.html","w", encoding="UTF-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()
