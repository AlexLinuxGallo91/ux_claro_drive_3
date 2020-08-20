import src.validaciones_json.constantes_json as jsonConst
from src.utils.utils_temporizador import Temporizador
from src.utils.utils_format import FormatUtils

class UtilsEvaluaciones:

    @staticmethod
    def generar_json_inicio_de_sesion_incorrecto(jsonEval,tiempo_step_inicio, fecha_inicio, indice: int,
                                                 msg_output: str):

        jsonEval["steps"][indice]["output"][0]["status"] = jsonConst.FAILED
        jsonEval["steps"][indice]["status"] = jsonConst.FAILED
        jsonEval["steps"][indice]["output"][0]["output"] = msg_output

        tiempo_step_final = Temporizador.obtener_tiempo_timer() - tiempo_step_inicio
        fecha_fin = Temporizador.obtener_fecha_tiempo_actual()

        jsonEval["steps"][indice]["time"] = FormatUtils.truncar_float_cadena(tiempo_step_final)
        jsonEval["steps"][indice]["start"] = fecha_inicio
        jsonEval["steps"][indice]["end"] = fecha_fin

        return jsonEval

    @staticmethod
    def se_ingreso_correctamente_a_la_sesion(jsonEval):
        return True if jsonEval["steps"][0]["status"] == jsonConst.SUCCESS else False
