"""Insert initial values into interest table.

Revision ID: a89401046d4f
Revises: a8f913de66d7
Create Date: 2025-05-05 03:21:54.989978

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy import Integer, String, column, table

# revision identifiers, used by Alembic.
revision: str = "a89401046d4f"
down_revision: Union[str, None] = "a8f913de66d7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    interests_table = table("interests", column("id", Integer), column("name", String))
    op.bulk_insert(
        interests_table,
        [
            {"id": 1, "name": "Hiking"},
            {"id": 2, "name": "Photography"},
            {"id": 3, "name": "Cooking"},
            {"id": 4, "name": "Reading"},
            {"id": 5, "name": "Gaming"},
            {"id": 6, "name": "Travel"},
            {"id": 7, "name": "Yoga"},
            {"id": 8, "name": "Music"},
            {"id": 9, "name": "Painting"},
            {"id": 10, "name": "Cycling"},
            {"id": 11, "name": "Dancing"},
            {"id": 12, "name": "Chess"},
            {"id": 13, "name": "Astronomy"},
            {"id": 14, "name": "Fishing"},
            {"id": 15, "name": "Programming"},
        ],
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
