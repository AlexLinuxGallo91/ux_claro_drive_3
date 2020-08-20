from os import listdir
from os.path import isdir, isfile, join

class UtilsMain:

    @staticmethod
    def verificar_path_es_directorio(path_por_analizar):
        return isdir(path_por_analizar)

    @staticmethod
    def obtener_lista_ficheros_en_directorio(path_directorio):
        return [archivo for archivo in listdir(path_directorio) if isfile(join(path_directorio, archivo))]



