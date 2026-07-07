from grpc import Channel, insecure_channel, intercept_channel
from locust.env import Environment

from clients.grpc.interceptors.locust_interceptor import LocustInterceptor

_grpc_gevent_initialized = False


def init_grpc_gevent() -> None:
    """
    Включает gevent-интеграцию gRPC перед созданием Locust gRPC-каналов.
    """
    global _grpc_gevent_initialized

    if _grpc_gevent_initialized:
        return

    import grpc.experimental.gevent as grpc_gevent

    grpc_gevent.init_gevent()
    _grpc_gevent_initialized = True


def build_gateway_grpc_client() -> Channel:
    """
    Фабричная функция (билдер) для создания gRPC-канала к сервису grpc-gateway.

    :return: gRPC-канал (Channel), настроенный на адрес localhost:9003.
    """
    return insecure_channel("localhost:9003")


def build_gateway_locust_grpc_client(environment: Environment) -> Channel:
    """
    Фабричная функция для создания gRPC-канала, адаптированного для Locust.
    В канал автоматически встраивается интерцептор LocustInterceptor,
    который регистрирует вызовы в системе метрик Locust.

    :param environment: Среда выполнения Locust (необходима для отправки событий).
    :return: gRPC-канал с интерцептором, пригодный для нагрузочного тестирования.
    """
    init_grpc_gevent()

    locust_interceptor = LocustInterceptor(environment)

    channel = insecure_channel("localhost:9003")
    intercepted_channel = intercept_channel(channel, locust_interceptor)
    setattr(intercepted_channel, "_close_channel", channel)
    return intercepted_channel
