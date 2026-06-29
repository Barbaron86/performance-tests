
from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.accounts.schema import (
    GetAccountsQuerySchema,
    GetAccountsResponseSchema,
    OpenDepositAccountRequestSchema,
    OpenDepositAccountResponseSchema,
    OpenSavingAccountRequestSchema,
    OpenSavingAccountResponseSchema,
    OpenDebitCardAccountRequestSchema,
    OpenDebitCardAccountResponseSchema,
    OpenCreditCardAccountRequestSchema,
    OpenCreditCardAccountResponseSchema
)




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
            '/api/v1/accounts',
            params=QueryParams(**query.model_dump(by_alias=True))
        )

    def open_deposit_account_api(self, request: OpenDepositAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия депозитного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            '/api/v1/accounts/open-deposit-account',
            json=request.model_dump(by_alias=True)
        )

    def open_saving_account_api(self, request: OpenSavingAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия сберегательного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post(
            '/api/v1/accounts/open-saving-account',
            json=request.model_dump(by_alias=True)
        )

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия дебетовой карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post(
            '/api/v1/accounts/open-debit-card-account',
            json=request.model_dump(by_alias=True)
        )

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestSchema) -> Response:
        """
        Выполняет POST-запрос для открытия кредитной карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post(
            '/api/v1/accounts/open-credit-card-account',
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

    def open_savings_account(self, user_id: str) -> OpenSavingAccountResponseSchema:
        """
        Открытие сберегательного счёта.

        :param user_id: Идентификатор пользователя.
        :return: Словарь с данными открытого сберегательного счёта (OpenSavingsAccountResponseDict).
        """
        request = OpenSavingAccountRequestSchema(userId=user_id)
        response = self.open_saving_account_api(request)
        return OpenSavingAccountResponseSchema.model_validate_json(response.text)

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
