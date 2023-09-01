"""User: about_me and last_seen

Revision ID: 286df86cf675
Revises: 134cbfd763c6
Create Date: 2023-09-01 15:50:23.088031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '286df86cf675'
down_revision = '134cbfd763c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
