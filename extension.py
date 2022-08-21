
import random
#import main 


def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        
        response('Estamos ubicados en la Autopistas la Americas', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        
        response('2 años de carrera',['Cuanto dura una carrera con ustedes?'], required_words=['Cuanto'])
        
        response('50 porciento de capacidad',[ 'La universidad es presencial o Virtual?'],required_words=['La'])
        
        response('Tenemos unas guaguas,en paradas estrategicas, con el costo de 25 pesos, te montas', ['Como es el transporte en el itla? '],required_words=['transporte'])
        
        response('18 años de edad',['A que edad puedo entrar?'], required_words=['Que edad'])
        
        response('Book Shop, edificio 4 y Area de Caja, edificio 2', [ 'Donde adquirir los tickets?'], required_words=['tickets'])
        
        response('Todos lo que usted desee', ['Cuantos tickets se pueden adquirir?'],required_words=['adquirir'])
        
        response('Debera pasar a los puntos de venta para verificar la compra original y solicitar una impresión duplicada', ['Que hacer si pierdo mi ticket?'], required_words=['pirerdo'])
        
        response(' 9:00 am a 6:00 pm' ['Horarios de la bibloteca?'], required_words=['horarios'])
        
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response