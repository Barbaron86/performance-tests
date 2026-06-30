from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryQuerySchema,
    GetOperationResponseSchema,
    GetOperationsSummaryResponseSchema,
    GetOperationReceiptResponseSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeCashbackOperationResponseSchema,
    MakeTransferOperationRequestSchema,
    MakeTransferOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeCashWithdrawalOperationResponseSchema

)


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Получает список операций по счёту.

        :param query: Pydantic-схема query-параметров с accountId.
        :return: Объект httpx.Response с операциями по счёту.
        """
        return self.get(
            '/api/v1/operations',
            params=QueryParams(**query.model_dump(by_alias=True))
        )

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Получает сводную статистику операций по счёту.

        :param query: Pydantic-схема query-параметров с accountId.
        :return: Объект httpx.Response с агрегированной информацией.
        """
        return self.get(
            '/api/v1/operations/operations-summary',
            params=QueryParams(**query.model_dump(by_alias=True))
        )

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получает чек по заданной операции.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с чеком по операции.
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получает информацию об операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f'/api/v1/operations/{operation_id}')

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Создаёт операцию комиссии.

        :param request: Pydantic-схема тела запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            '/api/v1/operations/make-fee-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Создаёт операцию пополнения счёта.

        :param request: Pydantic-схема тела запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            '/api/v1/operations/make-top-up-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Создаёт операцию начисления кэшбэка.

        :param request: Pydantic-схема тела запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            '/api/v1/operations/make-cashback-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Создаёт операцию перевода средств.

        :param request: Pydantic-схема тела запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            '/api/v1/operations/make-transfer-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Создаёт операцию покупки.

        :param request: Pydantic-схема тела запроса с параметрами операции, включая категорию.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            '/api/v1/operations/make-purchase-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_bill_payment_operation_api(
            self,
            request: MakeBillPaymentOperationRequestSchema
    ) -> Response:
        """
        Создаёт операцию оплаты счёта.

        :param request: Pydantic-схема тела запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            '/api/v1/operations/make-bill-payment-operation',
            json=request.model_dump(by_alias=True)
        )

    def make_cash_withdrawal_operation_api(
            self,
            request: MakeCashWithdrawalOperationRequestSchema
    ) -> Response:
        """
        Создаёт операцию снятия наличных средств.

        :param request: Pydantic-схема тела запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post(
            '/api/v1/operations/make-cash-withdrawal-operation',
            json=request.model_dump(by_alias=True)
        )

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Получает список всех операций, привязанных к конкретному счёту.

        :param account_id: Уникальный идентификатор счёта.
        :return: Модель GetOperationsResponseSchema со списком найденных операций.
        """
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Получает агрегированную сводную статистику по операциям для счёта.

        :param account_id: Уникальный идентификатор счёта.
        :return: Модель GetOperationsSummaryResponseSchema со сводными суммами трат, поступлений и кэшбэка.
        """
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Получает десериализованный чек по заданной операции.

        :param operation_id: Уникальный идентификатор операции.
        :return: Модель GetOperationReceiptResponseSchema со ссылкой и документом чека.
        """
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Получает валидированные данные об операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции.
        :return: Модель GetOperationResponseSchema с десериализованными данными операции.
        """
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        """
        Создаёт операцию списания комиссии с предопределёнными тестовыми параметрами.

        :param card_id: Уникальный идентификатор карты для списания.
        :param account_id: Уникальный идентификатор счёта.
        :return: Модель MakeFeeOperationResponseSchema с результатом создания операции комиссии.
        """
        request = MakeFeeOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(
            self,
            card_id: str,
            account_id: str
    ) -> MakeTopUpOperationResponseSchema:
        """
        Создаёт операцию пополнения счёта с предопределёнными тестовыми параметрами.

        :param card_id: Уникальный идентификатор карты.
        :param account_id: Уникальный идентификатор счёта.
        :return: Модель MakeTopUpOperationResponseSchema с результатом создания операции пополнения.
        """
        request = MakeTopUpOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(
            self,
            card_id: str,
            account_id: str
    ) -> MakeCashbackOperationResponseSchema:
        """
        Создаёт операцию начисления кэшбэка с предопределёнными тестовыми параметрами.

        :param card_id: Уникальный идентификатор карты.
        :param account_id: Уникальный идентификатор счёта.
        :return: Модель MakeCashbackOperationResponseSchema с результатом создания операции кэшбэка.
        """
        request = MakeCashbackOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(
            self,
            card_id: str,
            account_id: str
    ) -> MakeTransferOperationResponseSchema:
        """
        Создаёт операцию перевода денежных средств с предопределёнными тестовыми параметрами.

        :param card_id: Уникальный идентификатор карты.
        :param account_id: Уникальный идентификатор счёта.
        :return: Модель MakeTransferOperationResponseSchema с результатом создания операции перевода.
        """
        request = MakeTransferOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(
            self,
            card_id: str,
            account_id: str
    ) -> MakePurchaseOperationResponseSchema:
        """
        Создаёт операцию покупки в категории "taxi" с предопределёнными тестовыми параметрами.

        :param card_id: Уникальный идентификатор карты.
        :param account_id: Уникальный идентификатор счёта.
        :return: Модель MakePurchaseOperationResponseSchema с результатом создания операции покупки.
        """
        request = MakePurchaseOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(
            self,
            card_id: str,
            account_id: str
    ) -> MakeBillPaymentOperationResponseSchema:
        """
        Создаёт операцию оплаты выставленного счёта с предопределёнными тестовыми параметрами.

        :param card_id: Уникальный идентификатор карты.
        :param account_id: Уникальный идентификатор счёта.
        :return: Модель MakeBillPaymentOperationResponseSchema с результатом создания операции оплаты счёта.
        """
        request = MakeBillPaymentOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(
            self,
            card_id: str,
            account_id: str
    ) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Создаёт операцию снятия наличных средств с предопределёнными тестовыми параметрами.

        :param card_id: Уникальный идентификатор карты.
        :param account_id: Уникальный идентификатор счёта.
        :return: Модель MakeCashWithdrawalOperationResponseSchema с результатом создания операции снятия наличных.
        """
        request = MakeCashWithdrawalOperationRequestSchema(card_id=card_id, account_id=account_id)
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Фабричная функция для создания экземпляра OperationsGatewayHTTPClient.

    Автоматически инициализирует клиент операций, внедряя в него настроенный
    базовый HTTP-клиент для шлюза (gateway).

    :return: Готовый к использованию экземпляр OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
