from functools import wraps

from django.core.cache import cache


def results_db(timeout=3600, cache_key_prefix=''):
    """
    Decorator para cachear os resultados de uma função.

    Args:
        timeout: Tempo em segundos para o cache expirar (padrão: 1 hora).
        cache_key_prefix: Prefixo para a chave do cache, permitindo
                          distinguir caches diferentes para a mesma função
                          com diferentes argumentos.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Criar a chave do cache
            cache_key = f'{cache_key_prefix}:{func.__name__}:{args}:{kwargs}'

            # Tentar obter o resultado do cache
            result = cache.get(cache_key)

            if result is None:
                # Calcular o resultado se não estiver no cache
                result = func(*args, **kwargs)

                # Salvar o resultado no cache
                cache.set(cache_key, result, timeout)

            return result

        return wrapper

    return decorator
