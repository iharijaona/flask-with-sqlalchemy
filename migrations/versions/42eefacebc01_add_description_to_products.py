"""add description to products

Revision ID: 42eefacebc01
Revises: f622216833fc
Create Date: 2021-12-22 12:02:23.954555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42eefacebc01'
down_revision = 'f622216833fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('description', sa.Text(), nullable=True))
    op.alter_column('products', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('products', 'description')
    # ### end Alembic commands ###