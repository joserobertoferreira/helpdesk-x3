from typing import Any, Dict, Optional, Tuple

from django.db import DatabaseError, connections


class DatabaseConnection:
    def __init__(self, connection_name='default'):
        """
        Inicializa a classe Database com o nome da conexão a ser usada.
        """
        self.connection_name = connection_name
        self.connection = None  # Inicializa a conexão como None

    def __enter__(self):
        """
        Método chamado ao entrar no bloco 'with'.
        Estabelece a conexão com o banco de dados.
        """
        try:
            self.connection = connections[self.connection_name]
            self.connection.ensure_connection()
            return self.connection  # Retorna a conexão para ser usada no bloco 'with'
        except DatabaseError:
            # import logging

            # logger = logging.getLogger(__name__)
            # logger.error(f'Erro ao conectar ao banco de dados {self.connection_name}: {e}')
            return None  # Retorna None em caso de erro

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Método chamado ao sair do bloco 'with'.
        Fecha a conexão com o banco de dados, lidando com possíveis erros.
        """
        if self.connection:
            try:
                self.connection.close()
            except Exception:
                pass
                # import logging

                # logger = logging.getLogger(__name__)
                # logger.error(f'Erro ao desconectar do banco de dados: {e}')

    @staticmethod
    def build_query(
        table: str,
        columns: Optional[list[str]] = None,
        where_clauses: Optional[Dict[str, Tuple[str, Any]]] = None,
        options: Optional[Dict[str, str]] = None,
        limit: Optional[int] = None,
    ):
        # Build the SELECT clause dynamically
        select_clause = ', '.join(columns) if columns else '*'

        if limit and limit > 0:
            query = f'SELECT TOP {limit} {select_clause} FROM {table}'
        else:
            query = f'SELECT {select_clause} FROM {table}'

        # Build the WHERE clause dynamically with multiple conditions
        if where_clauses:
            where_clause = ' AND '.join([f'{column} {operator} ?' for column, (operator, _) in where_clauses.items()])
            query += f' WHERE {where_clause}'
            where_values = tuple(value for _, value in where_clauses.values())
        else:
            where_values = ()

        # Add GROUP BY clause if provided
        # Add GROUP BY and ORDER BY clauses if provided
        if options:
            if 'group_by' in options:
                query += f' GROUP BY {options["group_by"]}'
            if 'order_by' in options:
                query += f' ORDER BY {options["order_by"]}'

        return query, where_values
