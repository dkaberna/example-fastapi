"""maybe works?

Revision ID: 2f396f7bdfde
Revises: a9c4faeaf304
Create Date: 2024-03-15 22:25:11.913854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f396f7bdfde'
down_revision: Union[str, None] = 'a9c4faeaf304'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   # op.add_column('posts', sa.Column(
    #     'published', sa.Boolean(), nullable=False, server_default='TRUE'))

    # op.add_column('posts', sa.Column(
    #     'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    
    pass


def downgrade() -> None:
    # op.drop_column('posts', 'published')
    # op.drop_column('posts', 'created_at')
     pass
