"""Extend datasource model with total file events field

Revision ID: 180a387da650
Revises: 75af34d75b1e
Create Date: 2022-09-26 13:04:10.336534

"""

# This code is auto generated. Ignore linter errors.
# pylint: skip-file


# revision identifiers, used by Alembic.
revision = "180a387da650"
down_revision = "75af34d75b1e"

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "datasource", sa.Column("total_file_events", sa.BigInteger(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("datasource", "total_file_events")
    # ### end Alembic commands ###
