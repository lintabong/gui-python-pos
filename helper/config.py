import os
import json

if not os.path.exists("config.json"):
    result = {
        "width": 1230,
        "height": 800,
        "ControlFrameHeight": 100,
        "COM" :{
            "port":"COM4",
            "baudrate": 115200
        },
        "velocity":{
            "5-10": 1.0,
            "10-15": 1.1,
            "15-20": 1.2,
        },
        "signal":{
            "m": 1,
            "c": 0
        },
        "sensorRange": 0.63,
        "exportHeader": ["No", 
                         "Gerbong (Ton)", 
                         "Axle (Ton)", 
                         "Boogie (Ton)", 
                         "Selisih Boogie (Ton)", 
                         "Berat Kosong (Ton)", 
                         "Berat Muatan (Ton)", 
                         "Berat Maksimum (Ton)", 
                         "Kelebihan Muatan (Ton)", 
                         "Kecepatan (km/jam)"]
    }
            
    with open("config.json", "w") as outfile:
        json.dump(result, outfile)
        
    outfile.close()


def read():
    with open("config.json", "r") as openfile:
        config = json.load(openfile)

    openfile.close()

    return config

def write(configuration):
    with open("config.json", "w") as outfile:
        json.dump(configuration, outfile)
        
    outfile.close()

    return 1