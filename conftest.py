import importlib.util
from pathlib import Path


def pytest_configure(config):
    db_path = Path(__file__).parent / "data" / "test_data.db"
    if not db_path.exists():
        seed_path = Path(__file__).parent / "data" / "seed_db.py"
        spec = importlib.util.spec_from_file_location("seed_db", seed_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        module.seed_database()
