from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import (
    AccountsGatewayServiceStub,
)
from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import (
    GetAccountsRequest,
    GetAccountsResponse,
)
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import (
    OpenCreditCardAccountRequest,
    OpenCreditCardAccountResponse,
)
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse,
)
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import (
    OpenDepositAccountRequest,
    OpenDepositAccountResponse,
)
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import (
    OpenSavingsAccountRequest,
    OpenSavingsAccountResponse,
)


class AccountsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с AccountsGatewayService.
    Предоставляет высокоуровневые методы для работы со счетами.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к AccountsGatewayService.
        """
        super().__init__(channel)
        self.stub = AccountsGatewayServiceStub(channel)

    def get_accounts_api(self, request: GetAccountsRequest) -> GetAccountsResponse:
        """
        Низкоуровневый вызов метода GetAccounts через gRPC.

        :param request: gRPC-запрос с ID пользователя.
        :return: Ответ от сервиса со списком счетов пользователя.
        """
        return self.stub.GetAccounts(request)

    def open_deposit_account_api(
        self,
        request: OpenDepositAccountRequest,
    ) -> OpenDepositAccountResponse:
        """
        Низкоуровневый вызов метода OpenDepositAccount через gRPC.

        :param request: gRPC-запрос с ID пользователя.
        :return: Ответ от сервиса с данными открытого депозитного счета.
        """
        return self.stub.OpenDepositAccount(request)

    def open_savings_account_api(
        self,
        request: OpenSavingsAccountRequest,
    ) -> OpenSavingsAccountResponse:
        """
        Низкоуровневый вызов метода OpenSavingsAccount через gRPC.

        :param request: gRPC-запрос с ID пользователя.
        :return: Ответ от сервиса с данными открытого сберегательного счета.
        """
        return self.stub.OpenSavingsAccount(request)

    def open_debit_card_account_api(
        self,
        request: OpenDebitCardAccountRequest,
    ) -> OpenDebitCardAccountResponse:
        """
        Низкоуровневый вызов метода OpenDebitCardAccount через gRPC.

        :param request: gRPC-запрос с ID пользователя.
        :return: Ответ от сервиса с данными открытого дебетового карточного счета.
        """
        return self.stub.OpenDebitCardAccount(request)

    def open_credit_card_account_api(
        self,
        request: OpenCreditCardAccountRequest,
    ) -> OpenCreditCardAccountResponse:
        """
        Низкоуровневый вызов метода OpenCreditCardAccount через gRPC.

        :param request: gRPC-запрос с ID пользователя.
        :return: Ответ от сервиса с данными открытого кредитного карточного счета.
        """
        return self.stub.OpenCreditCardAccount(request)

    def get_accounts(self, user_id: str) -> GetAccountsResponse:
        """
        Получение списка счетов пользователя.

        :param user_id: Идентификатор пользователя.
        :return: Ответ со списком счетов пользователя.
        """
        request = GetAccountsRequest(user_id=user_id)
        return self.get_accounts_api(request)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponse:
        """
        Открытие депозитного счета.

        :param user_id: Идентификатор пользователя.
        :return: Ответ с данными открытого депозитного счета.
        """
        request = OpenDepositAccountRequest(user_id=user_id)
        return self.open_deposit_account_api(request)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponse:
        """
        Открытие сберегательного счета.

        :param user_id: Идентификатор пользователя.
        :return: Ответ с данными открытого сберегательного счета.
        """
        request = OpenSavingsAccountRequest(user_id=user_id)
        return self.open_savings_account_api(request)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponse:
        """
        Открытие дебетового карточного счета.

        :param user_id: Идентификатор пользователя.
        :return: Ответ с данными открытого дебетового карточного счета.
        """
        request = OpenDebitCardAccountRequest(user_id=user_id)
        return self.open_debit_card_account_api(request)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponse:
        """
        Открытие кредитного карточного счета.

        :param user_id: Идентификатор пользователя.
        :return: Ответ с данными открытого кредитного карточного счета.
        """
        request = OpenCreditCardAccountRequest(user_id=user_id)
        return self.open_credit_card_account_api(request)


def build_accounts_gateway_grpc_client() -> AccountsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра AccountsGatewayGRPCClient.

    :return: Инициализированный клиент для AccountsGatewayService.
    """
    return AccountsGatewayGRPCClient(channel=build_gateway_grpc_client())
