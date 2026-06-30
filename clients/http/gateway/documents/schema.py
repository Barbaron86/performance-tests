from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """
    Структура данных для описания документа (содержит ссылку и название).
    """
    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении тарифного документа по счету.
    """
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Описание структуры ответа при получении документа договора по счету.
    """
    contract: DocumentSchema