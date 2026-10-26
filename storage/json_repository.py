
#storage/json_repository.py

import json
from pathlib import Path
from typing import Any


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

DATA_FILES = {
    "usuarios": "usuarios.json",
    "vehiculos": "vehiculos.json",
    "celdas": "celdas.json",
    "estancias": "estancias.json",
    "novedades": "novedades.json",
}


def initialize_data_files() -> None:
    """Crea los archivos JSON que todavía no existen."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for filename in DATA_FILES.values():
        path = DATA_DIR / filename

        if not path.exists():
            path.write_text("[]", encoding="utf-8")


def load_data(entity: str) -> list[dict[str, Any]]:
    """Carga una colección de registros desde JSON."""
    if entity not in DATA_FILES:
        raise ValueError(f"Entidad desconocida: {entity}")

    initialize_data_files()
    path = DATA_DIR / DATA_FILES[entity]

    try:
        with path.open("r", encoding="utf-8") as file:
            records = json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"El archivo {path.name} contiene JSON inválido."
        ) from exc

    if not isinstance(records, list):
        raise ValueError(
            f"El archivo {path.name} debe contener una lista."
        )

    return records


def save_data(
    entity: str,
    records: list[dict[str, Any]]
) -> None:
    """Guarda una colección de registros en JSON."""
    if entity not in DATA_FILES:
        raise ValueError(f"Entidad desconocida: {entity}")

    if not isinstance(records, list):
        raise TypeError("Los registros deben ser una lista.")

    initialize_data_files()
    path = DATA_DIR / DATA_FILES[entity]

    # Escribir primero en un archivo temporal para evitar
    # dejar el archivo principal incompleto si falla la escritura.
    temp_path = path.with_suffix(".tmp")

    try:
        with temp_path.open("w", encoding="utf-8") as file:
            json.dump(
                records,
                file,
                ensure_ascii=False,
                indent=4
            )
            file.write("\n")

        temp_path.replace(path)

    finally:
        if temp_path.exists():
            temp_path.unlink()
