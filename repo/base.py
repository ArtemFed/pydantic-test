from .db import Base
from models.post import Post

# Хрень какая-то, но почему-то без этого файла не работает...
# import Base из .db не видел Post из-за чего не создавалсиь миграции