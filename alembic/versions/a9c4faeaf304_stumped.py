"""stumped

Revision ID: a9c4faeaf304
Revises: ace8cfda043c
Create Date: 2024-03-15 22:23:41.944096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9c4faeaf304'
down_revision: Union[str, None] = 'ace8cfda043c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    pass


def downgrade() -> None:

    pass
