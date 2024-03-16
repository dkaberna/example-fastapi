"""think this works

Revision ID: 1263ecb7030d
Revises: 2f396f7bdfde
Create Date: 2024-03-15 22:26:32.329422

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1263ecb7030d'
down_revision: Union[str, None] = '2f396f7bdfde'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    
    pass


def downgrade() -> None:

    pass
