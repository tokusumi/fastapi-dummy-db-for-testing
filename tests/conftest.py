import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database
from users.database import Base


@pytest.fixture(scope="function")
def SessionLocal():
    # settings of test database
    TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///./test_temp.db"
    engine = create_engine(
        TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

    assert not database_exists(
        TEST_SQLALCHEMY_DATABASE_URL
    ), "Test database already exists. Aborting tests."

    # Create test database and tables
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Run the tests
    yield SessionLocal

    # Drop the test database
    drop_database(TEST_SQLALCHEMY_DATABASE_URL)
