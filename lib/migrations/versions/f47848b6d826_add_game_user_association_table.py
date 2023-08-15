"""Add game_user Association Table

Revision ID: f47848b6d826
Revises: 0db971b6dae1
Create Date: 2023-08-15 11:28:48.020784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f47848b6d826'
down_revision = '0db971b6dae1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('game_users',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_game_users_game_id_games')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_game_users_user_id_users')),
    sa.PrimaryKeyConstraint('game_id', 'user_id')
    )
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reviews_game_id_games', type_='foreignkey')
        batch_op.drop_constraint('fk_reviews_user_id_users', type_='foreignkey')
        batch_op.drop_column('user_id')
        batch_op.drop_column('game_id')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('game_id', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_reviews_user_id_users', 'users', ['user_id'], ['id'])
        batch_op.create_foreign_key('fk_reviews_game_id_games', 'games', ['game_id'], ['id'])

    op.drop_table('game_users')
    # ### end Alembic commands ###
