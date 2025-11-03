# Import all the models, so that Base has them before being
# imported by Alembic
from app.models.book import *
from app.models.inventory import *
from app.models.order import *
from app.models.user import *
