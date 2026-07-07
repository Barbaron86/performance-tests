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

    def close(self) -> None:
        """
        Закрывает gRPC-канал явно до финализации gevent greenlet.
        """
        close_channel = getattr(self.channel, "_close_channel", self.channel)

        self.channel.close()
        if close_channel is not self.channel:
            close_channel.close()
