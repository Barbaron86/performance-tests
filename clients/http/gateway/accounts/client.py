
from httpx import Response, QueryParams
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import (
    build_gateway_http_client,
    build_gateway_locust_http_client
)
from clients.http.gateway.accounts.schema import (
    GetAccountsQuerySchema,
    GetAccountsResponseSchema,
    OpenDepositAccountRequestSchema,
    OpenDepositAccountResponseSchema,
    OpenSavingsAccountRequestSchema,
    OpenSavingsAccountResponseSchema,
    OpenDebitCardAccountRequestSchema,
    OpenDebitCardAccountResponseSchema,
    OpenCreditCardAccountRequestSchema,
    OpenCreditCardAccountResponseSchema
)
from tools.routes import ApiRoutes



class AccountsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/accounts сервиса http-gateway.
    """

    def get_accounts_api(self, query: GetAccountsQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение списка счетов пользователя.

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get(
            ApiRoutes.ACCOUNTS,
            params=QueryParams(**query.model_dump(by_alias=True)),
            extensions=HTTPClientExtensions(route=ApiRoutes.ACCOUNTS)
        )

    def open_deposit_account_api(self, request: OpenDepositAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия депозитного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
        f"{ApiRoutes.ACCOUNTS}/open-deposit-account",
            json=request.model_dump(by_alias=True)
        )

    def open_saving_account_api(self, request: OpenSavingsAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия сберегательного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post(
        f"{ApiRoutes.ACCOUNTS}/open-savings-account",
            json=request.model_dump(by_alias=True)
        )

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия дебетовой карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post(
        f"{ApiRoutes.ACCOUNTS}/open-debit-card-account",
            json=request.model_dump(by_alias=True)
        )

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия кредитной карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post(
        f"{ApiRoutes.ACCOUNTS}/open-credit-card-account",
            json=request.model_dump(by_alias=True)
        )

    def get_accounts(self, user_id: str) -> GetAccountsResponseSchema:
        """
        Получение списка счетов пользователя.

        :param user_id: Идентификатор пользователя.
        :return: Словарь со списком счетов пользователя (GetAccountsResponseDict).
        """
        query = GetAccountsQuerySchema(user_id=user_id)
        response = self.get_accounts_api(query)
        return GetAccountsResponseSchema.model_validate_json(response.text)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseSchema:
        """
        Открытие депозитного счёта.

        :param user_id: Идентификатор пользователя.
        :return: Словарь с данными открытого депозитного счёта (OpenDepositAccountResponseDict).
        """
        request = OpenDepositAccountRequestSchema(userId=user_id)
        response = self.open_deposit_account_api(request)
        return OpenDepositAccountResponseSchema.model_validate_json(response.text)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseSchema:
        """
        Открытие сберегательного счёта.

        :param user_id: Идентификатор пользователя.
        :return: Словарь с данными открытого сберегательного счёта (OpenSavingsAccountResponseDict).
        """
        request = OpenSavingsAccountRequestSchema(userId=user_id)
        response = self.open_saving_account_api(request)
        return OpenSavingsAccountResponseSchema.model_validate_json(response.text)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseSchema:
        """
        Открытие дебетового карточного счёта.

        :param user_id: Идентификатор пользователя.
        :return: Словарь с данными открытого дебетового карточного счёта (OpenDebitCardAccountResponseDict).
        """
        request = OpenDebitCardAccountRequestSchema(userId=user_id)
        response = self.open_debit_card_account_api(request)
        return OpenDebitCardAccountResponseSchema.model_validate_json(response.text)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseSchema:
        """
        Открытие кредитного карточного счёта.

        :param user_id: Идентификатор пользователя.
        :return: Словарь с данными открытого кредитного карточного счёта (OpenCreditCardAccountResponseDict).
        """
        request = OpenCreditCardAccountRequestSchema(userId=user_id)
        response = self.open_credit_card_account_api(request)
        return OpenCreditCardAccountResponseSchema.model_validate_json(response.text)


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
    Функция создаёт экземпляр AccountsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию AccountsGatewayHTTPClient.
    """
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())

def build_accounts_gateway_locust_http_client(environment: Environment) -> AccountsGatewayHTTPClient:
    """
    Функция создаёт экземпляр AccountsGatewayHTTPClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: Объект окружения Locust.
    :return: Экземпляр AccountsGatewayHTTPClient с хуками сбора метрик.
    """
    return AccountsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))