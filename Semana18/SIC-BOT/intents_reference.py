import json

def guardar_json(datos):
    archivo=open("intents.json","w")
    json.dump(datos,archivo,indent=4)

#intents: grupos de conversaciones tipicas para nuestro objetivo
# patterns: posibles interacciones con el usuario

#dic={"intents:[[{"key":["valores"]}],"dic2"]}

def start_intents():

    biblioteca={"intents":
                [
                    {"tag":"saludos",
                     "patterns":["hola",
                                 "buenos dias",
                                 "buenas tardes",
                                 "buenas noches",
                                 "como estas",
                                 "hay alguien ahi?",
                                 "hey",
                                 "saludos",
                                 "que tal"                      
                                 ],
                     "responses":["hola soy SIC-BOT , en que puedo ayudarte"
                                 ],
                     "context":[""]
                     },

                    {"tag":"despedidas",
                     "patterns":["chao",
                                 "adios",
                                 "hasta luego",
                                 "nos vemos",
                                 "bye",
                                 "hasta pronto",
                                 "hasta la proxima"
                                 ],
                     "responses":["hasta luego, tenga un buen dia",
                     "ha sido un placer, vuelva pronto"
                                 ],
                     "context":[""]
                     },
                    {"tag":"agradecimientos",
                     "patterns":["gracias",
                                 "muchas gracias",
                                 "mil gracias",
                                 "muy amable",
                                 "se lo agradezco",
                                 "fue de ayuda",
                                 "gracias por la ayuda",
                                 "muy agradecido",
                                 "gracias por su tiempo",
                                 "ty"
                                ],
                     "responses":["de nada",
                                  "feliz por ayudarlo",
                                  "gracias a usted",
                                  "estamos para servirle",
                                  "fue un placer"
                                 ],
                     "context":[""]
                    },
                    {"tag":"norespuesta",
                     "patterns":[""],
                     "responses":["no se detecto una respuesta"
                                 ],
                     "context":[""]                    
                    }
                ] 
            }
    guardar_json(biblioteca)


# _________________________________MAIN________________________

# Driver program
if __name__ == '__main__':       
    start_intents()