import csv
from apps.generales.models import PointOfSale

def run():
    with open('/home/jonwilm/Documentos/Development/proyectos/isakito/Material/PointOfSale-2023-11-13.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            pos = PointOfSale()
            pos.name = row[0]
            pos.address = row[1]
            pos.locality = row[2]
            pos.lat = row[3]
            pos.lng = row[4]
            pos.save()
