import pytest
from pytest_bdd import given
from pytest_bdd.parsers import parse


@pytest.fixture
def users():
    return {}


@given(parse("a {role} user named {name}"))
def buyer_user(users, role, name):
    users[name] = {
        "username": f"{name.lower()}@{role}.marketplace.team",
        "password": "Password1234",
    }
    return users


@given(parse("I am logged in as {name}"))
def login(users, name):
    print(f"logged in as '{users[name]['username']}'")


@given(parse("a {state:l} {name} framework"))
def get_framework(name, state):
    # do some db stuff
    print(f"setting up framework '{name}' in '{state}' state")
    pass
