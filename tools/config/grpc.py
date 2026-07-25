from pydantic import BaseModel


class GRPCClientConfig(BaseModel):
    host: str
    port: int

    @property
    def client_utl(self) -> str:
        return f"{self.host}:{self.port}"
