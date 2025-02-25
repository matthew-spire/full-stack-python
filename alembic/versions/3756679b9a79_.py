"""empty message

Revision ID: 3756679b9a79
Revises: e559b2cb1cc4
Create Date: 2025-02-24 19:54:39.250535

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '3756679b9a79'
down_revision: Union[str, None] = 'e559b2cb1cc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contactentrymodel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contactentrymodel', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
