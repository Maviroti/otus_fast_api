"""Create task table

Revision ID: 5c0fb2a4844c
Revises: 732a2f1aa5ff
Create Date: 2025-12-05 17:09:08.449463

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5c0fb2a4844c"
down_revision: Union[str, Sequence[str], None] = "732a2f1aa5ff"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "task",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "title",
            sa.String(length=150),
            nullable=False,
        ),
        sa.Column(
            "user_name",
            sa.String(length=100),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "body",
            sa.String(length=500),
            server_default="",
            nullable=False,
        ),
        sa.Column(
            "end_date",
            sa.DateTime(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint(
            "id",
            name=op.f("pk_task"),
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("task")
