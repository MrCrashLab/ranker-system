"""Added required tables

Revision ID: 1f0925eed80b
Revises: 3fb2e602b11c
Create Date: 2024-02-10 21:11:38.146498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f0925eed80b'
down_revision: Union[str, None] = '3fb2e602b11c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
