from grpc import Channel


class GRPCClient:
    """
    Базовый класс gRPC-клиента.

    Этот класс хранит общий канал (Channel) для связи с gRPC-сервером.
    От него будут наследоваться все остальные специфические клиенты.
    """
    def __init__(self, channel: Channel):
        """
        Конструктор базового клиента.

        :param channel: gRPC-канал, через который происходит подключение к серверу.
                        Обычно создаётся один раз и переиспользуется.
        """
        self.channel = channel
        self._closed = False

    def close(self) -> None:
        """
        Закрывает gRPC-канал один раз.

        Для Locust interceptor-channel закрывается исходный gRPC-канал,
        сохранённый в `_close_channel`.
        """
        if self._closed:
            return

        channel_to_close = getattr(
            self.channel,
            "_close_channel",
            self.channel,
        )

        channel_to_close.close()
        self._closed = True
