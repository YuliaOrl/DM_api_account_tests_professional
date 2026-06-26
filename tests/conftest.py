import os
import pytest
from datetime import datetime
from collections import namedtuple
from swagger_coverage_py.reporter import CoverageReporter
from vyper import v
from pathlib import Path
from helpers.account_helper import AccountHelper
from packages.restclient.configuration import Configuration as MailhogConfiguration
from packages.restclient.configuration import Configuration as DMApiConfiguration
from services.dm_api_account import DMApiAccount
from services.api_mailhog import MailHogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(
            indent=4,
            ensure_ascii=True,
            # sort_keys=True
        )
    ]
)

options = (
    'service.dm_api_account',
    'service.mailhog',
    'user.login',
    'user.password',
    'telegram.chat_id',
    'telegram.token',
)


@pytest.fixture(scope="session", autouse=True)
def setup_swagger_coverage():
    reporter = CoverageReporter(api_name='dm-api-account', host='http://185.185.143.231:5051')
    reporter.cleanup_input_files()
    reporter.setup('/swagger/Account/swagger.json')
    yield
    reporter.generate_report()


@pytest.fixture(scope="session", autouse=True)
def set_config(request):
    config = Path(__file__).joinpath('../../').joinpath('config')
    config_name = request.config.getoption('--env')
    v.set_config_name(config_name)
    v.add_config_path(config)
    v.read_in_config()
    for option in options:
        v.set(f'{option}', request.config.getoption(f'--{option}'))
    os.environ['TELEGRAM_BOT_CHAT_ID'] = v.get('telegram.chat_id')
    os.environ['TELEGRAM_BOT_ACCESS_TOKEN'] = v.get('telegram.token')
    request.config.stash['telegram-notifier-addfields']['enviroment'] = config_name
    request.config.stash['telegram-notifier-addfields']['report'] = 'https://api-account-tests-professional-700056.gitlab.io'


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='stg', help='run stg')
    for option in options:
        parser.addoption(f'--{option}', action='store', default=None)


@pytest.fixture()
def account_api():
    dm_api_configuration = DMApiConfiguration(host=v.get('service.dm_api_account'), disable_log=False)
    account = DMApiAccount(configuration=dm_api_configuration)
    return account


@pytest.fixture()
def mailhog_api():
    mailhog_configuration = MailhogConfiguration(host=v.get('service.mailhog'), disable_log=True)
    mailhog_client = MailHogApi(configuration=mailhog_configuration)
    return mailhog_client


@pytest.fixture()
def account_helper(account_api, mailhog_api):
    account_helper = AccountHelper(dm_account_api=account_api, mailhog=mailhog_api)
    return account_helper


@pytest.fixture()
async def auth_account_helper(account_api, mailhog_api, prepare_user):
    auth_account_helper = AccountHelper(dm_account_api=account_api, mailhog=mailhog_api)
    await auth_account_helper.register_new_user(login=prepare_user.login, password=prepare_user.password, email=prepare_user.email)
    await auth_account_helper.auth_client(login=prepare_user.login, password=prepare_user.password)
    return auth_account_helper


@pytest.fixture
def prepare_user():
    now = datetime.now()
    time = now.strftime('%H_%M_%S_%f')
    login = f"{v.get('user.login')}_{time}"
    password = v.get('user.password')
    email = f"{login}@yandex.ru"
    User = namedtuple('User', ['login', 'password', 'email'])
    user = User(login=login, password=password, email=email)
    return user
