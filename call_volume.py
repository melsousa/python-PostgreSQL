import psycopg2
from datetime import date, timedelta, datetime

conn = psycopg2.connect(
    "host=localhost dbname=nomeDoBanco user=postgres password=123456")
cur = conn.cursor()


def quesito1():

    cur.execute(f"SELECT DATE_TRUNC('week', cases.date_ref)::date, COUNT(cases.accountid), creds.shipping_address_state FROM cases INNER JOIN creds ON cases.accountid = creds.accountid WHERE date_ref BETWEEN (select max(date_ref) from cases) - interval '3 month' AND (select max(date_ref) from cases) GROUP BY 1, creds.shipping_address_state ORDER BY creds.shipping_address_state")
    recset = cur.fetchall()

    datas = []
    numero_de_chamados = []
    estados = []

    print('| Data do chamado | Número de chamados | Sigla do Estado | ')
    for rec in recset:
        datas = rec[0]
        numero_de_chamados = rec[1]
        estados = rec[2]

        print("|" ,datas,"  |  ", numero_de_chamados, "  |  " ,estados, "  |  ")



if __name__ == "__main__":

    data = input(
        'Qual Dia deseja um relátorio dia a dia referente aos ultimos 30 dias? FORMATO dd/mm/yyyy ')
    quesito1()
    