from dataclasses import dataclass


@dataclass
class DBConfig:
    host: str
    port: int
    database: str
    user: str
    password: str
    echo: bool
    driver: str
    db_type: str


    @property
    def full_url(self) -> str:
        return f"{self.db_type}+{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
