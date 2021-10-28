import sys
import json
from pathlib import Path

from api.server import router


if __name__ == "__main__":
    path = Path(sys.argv[1]).absolute()

    with open(path, "w") as schema_file:
        api = router.openapi()
        schema = json.dumps(api)
        schema_file.write(schema)
