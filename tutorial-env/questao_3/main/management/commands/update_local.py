from django.core.management.base import BaseCommand
import psycopg2
from ...models import Doencas


class Command(BaseCommand):
    help = "Este comando é utilizado para atualizar o banco de dados local"

    def handle(self, *args, **options):
        conn_remota = psycopg2.connect(host='ec2-107-21-122-38.compute-1.amazonaws.com', port='5432',
                                       dbname='d5mma0lt0jpjfj', user='ekvytxmooqboqc',
                                       password='638c124d07e29a9bdf595724d3293a39b2b84f9c2b3f8fe6878e7975fca6efeb')

        cursor = conn_remota.cursor()

        cursor.execute('''SELECT * FROM pheno_db''')
        dados = cursor.fetchall()

        cursor.close()
        conn_remota.close()

        for i in range(len(dados)):
            if dados[i][1] is None:
                print(dados[i])
                print('finalizado')
                break

            doenca_atual = Doencas(gene=dados[i][1], doenca=dados[i][2])

            if Doencas.objects.filter(gene=doenca_atual.gene, doenca=doenca_atual.doenca):
                continue

            else:
                doenca_atual.save()
