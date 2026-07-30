from locust import task

from clients.grpc.gateway.locust import GatewayGRPCSequentialTaskSet
from clients.grpc.gateway.users.client import CreateUserResponse
from clients.grpc.gateway.accounts.client import OpenDebitCardAccountResponse
from tools.locust.user import LocustBaseUser


class MakeCashbackOperationSequentialTaskSet(GatewayGRPCSequentialTaskSet):
    create_user_response: CreateUserResponse | None = None
    open_debit_card_account_response: OpenDebitCardAccountResponse | None = None

    @task
    def create_user(self):
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        if not self.create_user_response:
            return

        self.open_debit_card_account_response = (
            self.accounts_gateway_client.open_debit_card_account(
                user_id=self.create_user_response.user.id
            )
        )

    @task
    def make_cashback_operation(self):
        if not self.create_user_response or not self.open_debit_card_account_response:
            return

        if not self.open_debit_card_account_response.account.cards:
            return


        self.operations_gateway_client.make_cashback_operation(
            account_id=self.open_debit_card_account_response.account.id,
            card_id=self.open_debit_card_account_response.account.cards[0].id
        )


class GetAccountsScenarioUser(LocustBaseUser):
    """
    Пользователь Locust, исполняющий последовательный сценарий получения списка счетов.
    """
    tasks = [MakeCashbackOperationSequentialTaskSet]
