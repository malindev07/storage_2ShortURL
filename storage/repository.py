from dataclasses import dataclass, field
from pathlib import Path

from model.model import DataURLS, DataJSON

def get_path_db() -> Path:
    data_path = Path(__file__).parent.parent.joinpath('data').joinpath('data_base.json')
    return data_path

@dataclass
class Repository:
    path: Path = field(default_factory=get_path_db)

    def save(self, data: DataURLS) -> None:
        self.path.write_text(data.json(), encoding="utf-8")

    def load(self) -> DataURLS:
        if self.path.exists():
            return DataURLS.parse_file(self.path)
        else:
            return DataURLS()

    def add(self, long_url: str, short_url: str) -> DataURLS:
        data = self.load()
        data.urls[short_url] = DataJSON(long_url=long_url, short_url=short_url)
        self.save(data=data)
        return data

    def delete_url(self, short_url: str) -> DataURLS:
        data = self.load()
        del data.urls[short_url]
        self.save(data)
        return data


def dependency_repository() -> Repository:
    print("Create Repository")
    yield Repository()
    print("Close Repository")
