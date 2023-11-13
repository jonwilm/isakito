import csv
from apps.generales.models import PointOfSale

def run():
    with open('/home/jonwilm/Documentos/Development/proyectos/isakito/Material/pos.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            pos = PointOfSale()
            pos.name = row[0]
            pos.address = row[1]
            pos.locality = row[2]
            pos.save()
