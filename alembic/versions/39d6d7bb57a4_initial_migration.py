"""Initial migration

Revision ID: 39d6d7bb57a4
Revises: af778961aa9b
Create Date: 2024-11-26 23:28:02.684984

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39d6d7bb57a4'
down_revision: Union[str, None] = 'af778961aa9b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('map_point',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('floor_num', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_map_point_id'), 'map_point', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_map_point_id'), table_name='map_point')
    op.drop_table('map_point')
    # ### end Alembic commands ###