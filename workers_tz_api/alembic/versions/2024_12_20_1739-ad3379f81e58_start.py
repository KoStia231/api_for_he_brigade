"""start

Revision ID: ad3379f81e58
Revises: 
Create Date: 2024-12-20 17:39:02.803979

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ad3379f81e58"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "brigades",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_brigades")),
    )
    op.create_table(
        "workers",
        sa.Column("full_name", sa.String(), nullable=False),
        sa.Column("salary", sa.Float(), nullable=False),
        sa.Column("specialization", sa.String(), nullable=False),
        sa.Column("brigade_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["brigade_id"],
            ["brigades.id"],
            name=op.f("fk_workers_brigade_id_brigades"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_workers")),
    )


def downgrade() -> None:
    op.drop_table("workers")
    op.drop_table("brigades")
