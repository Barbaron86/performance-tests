from httpx import Response
from locust.env import Environment

from clients.http.client import HTTPClient, HTTPClientExtensions
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.client import build_gateway_locust_http_client
from clients.http.gateway.documents.schema import (
    GetTariffDocumentResponseSchema,
    GetContractDocumentResponseSchema
)
from tools.routes import ApiRoutes

class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f'{ApiRoutes.DOCUMENTS}/tariff-document/{account_id}',
            extensions=HTTPClientExtensions(route=f"{ApiRoutes.DOCUMENTS}/tariff-document/{{account_id}}")
        )

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(
            f'{ApiRoutes.DOCUMENTS}/contract-document/{account_id}',
            extensions=HTTPClientExtensions(route=f"{ApiRoutes.DOCUMENTS}/contract-document/{{account_id}}")
        )

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseSchema:
        """
        Получение тарифного документа по счету.

        :param account_id: Идентификатор счета.
        :return: Модель GetTariffDocumentResponseSchema с данными тарифного документа.
        """
        response = self.get_tariff_document_api(account_id)
        return GetTariffDocumentResponseSchema.model_validate_json(response.text)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseSchema:
        """
        Получение документа договора по счету.

        :param account_id: Идентификатор счета.
        :return: Модель GetContractDocumentResponseSchema с данными документа договора.
        """
        response = self.get_contract_document_api(account_id)
        return GetContractDocumentResponseSchema.model_validate_json(response.text)


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())


def build_documents_gateway_locust_http_client(environment: Environment) -> DocumentsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: Объект окружения Locust.
    :return: Экземпляр DocumentsGatewayHTTPClient с хуками сбора метрик.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))
