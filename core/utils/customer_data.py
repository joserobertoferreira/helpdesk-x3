from decouple import config

# from core.decorators.cache_db import results_db
from core.utils.database import DatabaseConnection


# @results_db(timeout=300, cache_key_prefix='customers')
def read_customer_data():
    """Busca os clientes do banco de dados legado, usando cache."""
    schema = config('DB_SCHEMA', default='')

    if not schema:
        print('Não foi possível buscar os clientes, pois o DB_SCHEMA não foi configurado.')
        return []

    database = DatabaseConnection('default')
    customers = []

    with database as connection:
        if connection:
            # Build query to get the customers data
            query, where_clause = database.build_query(
                table=f'{schema}.BPCUSTOMER',
                columns=[
                    'ROWID',
                    'BPCNUM_0',
                    'BPCNAM_0',
                ],
                options={'ORDER BY': 'BPCNAM_0'},
                # where_clauses={'INVOICE_NUM_0': Condition('=', 'NC-01425/00001')},
            )

            try:
                with connection.cursor() as cursor:
                    print('Executando query...')
                    cursor.execute(query, where_clause)
                    for row in cursor.fetchall():
                        customers.append((row[0], row[1]))
            except Exception as e:
                print(f'Erro ao buscar clientes do banco legado: {e}')
                customers = []
        else:
            print('Não foi possível conectar ao banco de dados legado.')
            customers = []

    return customers
