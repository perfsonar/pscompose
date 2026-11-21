import sys
import os

from pscompose.backends.postgres import backend
from pscompose.auth.basic import backend as auth_backend
from pscompose.models import UserTable
from pscompose.settings import DataTypes, TOKEN_SCOPES

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


def seed_users():
    users = [
        {
            "email": "editor@example.com",
            "name": "Editor User",
            "password": "editor",
            "scopes": [TOKEN_SCOPES["read"], TOKEN_SCOPES["write"]],
            "favorites": [],
        },
        {
            "email": "readonly@example.com",
            "name": "Read Only User",
            "password": "readonly",
            "scopes": [TOKEN_SCOPES["read"]],
            "favorites": [],
        },
    ]

    for user in users:
        existing = auth_backend.session.query(UserTable).filter_by(username=user["email"]).first()
        if not existing:
            auth_backend.create_user(**user)
            print(f"Created user: {user['email']}")
        else:
            print(f"Skipped existing user: {user['email']}")


def seed_dummy_data():
    # Dummy addresses
    addresses = [
        {
            "name": "Test Host 1",
            "address": "test1.example.com",
            "host": None,
            "labels": None,
            "remote-addresses": None,
            "lead-bind-address": None,
            "pscheduler-address": None,
            "contexts": None,
            "tags": None,
            "disabled": None,
            "no-agent": False,
            "_meta": None,
        },
        {
            "name": "Test Host 2",
            "address": "test2.example.com",
            "host": None,
            "labels": None,
            "remote-addresses": None,
            "lead-bind-address": None,
            "pscheduler-address": None,
            "contexts": None,
            "tags": None,
            "disabled": None,
            "no-agent": True,
            "_meta": None,
        },
        {
            "name": "Test Host 3",
            "address": "test3.example.com",
            "host": None,
            "labels": None,
            "remote-addresses": None,
            "lead-bind-address": None,
            "pscheduler-address": None,
            "contexts": None,
            "tags": None,
            "disabled": None,
            "no-agent": False,
            "_meta": None,
        },
    ]

    # Create dummy address records
    for address in addresses:
        name = address.pop("name")
        backend.create_datatype(
            ref_set=[],
            datatype=DataTypes.ADDRESS,
            json=address,
            name=name,
            created_by="system",
            last_edited_by="system",
        )
        print(f"Created address: {name}")


if __name__ == "__main__":
    print("Seeding dummy data...")
    seed_users()
    seed_dummy_data()
    print("Done!")
