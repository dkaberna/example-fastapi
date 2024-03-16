"""still stuck

Revision ID: 8c90adf829fb
Revises: 3e4cdca83cb4
Create Date: 2024-03-15 22:19:39.008970

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c90adf829fb'
down_revision: Union[str, None] = '3e4cdca83cb4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   
    pass


def downgrade() -> None:

    pass
