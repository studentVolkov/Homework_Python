import pytest
import os
import requests
from dotenv import load_dotenv

load_dotenv()


def _check_status_code(status_code: int, response_status_code: int):
    assert response_status_code == status_code, f"Expected status code {
        status_code}, got {response_status_code}"


@pytest.fixture
def api_key():
    return os.environ['API_KEY']


@pytest.fixture
def r_session(api_key: str):
    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {api_key}'})
    return session


@pytest.fixture
def base_url():
    return "https://ru.yougile.com/api-v2/projects"


@pytest.fixture
def test_project(r_session: requests.Session, base_url: str):
    """Фикстура создает тестовый проект и
    возвращает его ID, удаляя после теста"""
    # Создание проекта
    title = "TEST WITH FIXTURES"
    resp_create = r_session.post(
        url=base_url + "/",
        json={"title": title, "users": {}}
    )
    _check_status_code(201, resp_create.status_code)
    project_id = resp_create.json()['id']

    # Проверка что проект создан
    resp_get = r_session.get(base_url + f"/{project_id}")
    _check_status_code(200, resp_get.status_code)

    yield project_id  # Возвращаем ID для тестов

    # Удаление проекта после теста
    r_session.delete(base_url + f"/{project_id}")


def test_create_project(test_project):
    """Тест проверяет что проект был создан"""
    assert isinstance(test_project, str), "Project ID should be string"
    # Дополнительные проверки можно добавить здесь


def test_update_project(
        r_session: requests.Session, base_url: str, test_project: str):
    """Тест проверяет обновление проекта"""
    new_title = "CHANGED TEST WITH FIXTURES"

    resp = r_session.put(
        url=base_url + f"/{test_project}",
        json={"title": new_title, "users": {}}
    )
    _check_status_code(200, resp.status_code)

    # Проверяем что название действительно изменилось
    resp_get = r_session.get(base_url + f"/{test_project}")
    assert resp_get.json()[
        'title'] == new_title, "Project title was not updated"
