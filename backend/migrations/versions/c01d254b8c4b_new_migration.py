"""New migration

Revision ID: c01d254b8c4b
Revises: 
Create Date: 2025-03-26 14:00:34.300478

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c01d254b8c4b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('CF', 'record_time',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.drop_constraint('CF_ibfk_2', 'CF', type_='foreignkey')
    op.drop_constraint('CF_ibfk_3', 'CF', type_='foreignkey')
    op.drop_constraint('CF_ibfk_1', 'CF', type_='foreignkey')
    op.create_foreign_key(None, 'CF', 'CFV', ['cfv_id'], ['cfv_id'])
    op.create_foreign_key(None, 'CF', 'Product', ['product_id'], ['product_id'])
    op.create_foreign_key(None, 'CF', 'EmissionFactor', ['factor_id'], ['factor_id'])
    op.alter_column('CFV', 'start_time',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True)
    op.alter_column('CFV', 'end_time',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True)
    op.alter_column('CFV', 'updated_time',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    op.drop_constraint('CFV_ibfk_2', 'CFV', type_='foreignkey')
    op.drop_constraint('CFV_ibfk_1', 'CFV', type_='foreignkey')
    op.create_foreign_key(None, 'CFV', 'Company', ['company_id'], ['company_id'])
    op.create_foreign_key(None, 'CFV', 'Product', ['product_id'], ['product_id'])
    op.alter_column('EmissionFactor', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('EmissionFactor', 'updated_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    op.drop_constraint('Product_ibfk_1', 'Product', type_='foreignkey')
    op.create_foreign_key(None, 'Product', 'Company', ['company_id'], ['company_id'])
    op.alter_column('Report', 'created_time',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.drop_constraint('Report_ibfk_2', 'Report', type_='foreignkey')
    op.drop_constraint('Report_ibfk_1', 'Report', type_='foreignkey')
    op.create_foreign_key(None, 'Report', 'User', ['user_id'], ['user_id'])
    op.create_foreign_key(None, 'Report', 'CFV', ['cfv_id'], ['cfv_id'])
    op.alter_column('User', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('User', 'updated_at',
               existing_type=mysql.TIMESTAMP(),
               type_=sa.DateTime(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    op.drop_constraint('User_ibfk_1', 'User', type_='foreignkey')
    op.create_foreign_key(None, 'User', 'Company', ['company_id'], ['company_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'User', type_='foreignkey')
    op.create_foreign_key('User_ibfk_1', 'User', 'Company', ['company_id'], ['company_id'], ondelete='SET NULL')
    op.alter_column('User', 'updated_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    op.alter_column('User', 'created_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.drop_constraint(None, 'Report', type_='foreignkey')
    op.drop_constraint(None, 'Report', type_='foreignkey')
    op.create_foreign_key('Report_ibfk_1', 'Report', 'CFV', ['cfv_id'], ['cfv_id'], ondelete='CASCADE')
    op.create_foreign_key('Report_ibfk_2', 'Report', 'User', ['user_id'], ['user_id'], ondelete='CASCADE')
    op.alter_column('Report', 'created_time',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.drop_constraint(None, 'Product', type_='foreignkey')
    op.create_foreign_key('Product_ibfk_1', 'Product', 'Company', ['company_id'], ['company_id'], ondelete='CASCADE')
    op.alter_column('EmissionFactor', 'updated_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    op.alter_column('EmissionFactor', 'created_at',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.drop_constraint(None, 'CFV', type_='foreignkey')
    op.drop_constraint(None, 'CFV', type_='foreignkey')
    op.create_foreign_key('CFV_ibfk_1', 'CFV', 'Company', ['company_id'], ['company_id'], ondelete='CASCADE')
    op.create_foreign_key('CFV_ibfk_2', 'CFV', 'Product', ['product_id'], ['product_id'], ondelete='CASCADE')
    op.alter_column('CFV', 'updated_time',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    op.alter_column('CFV', 'end_time',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               existing_nullable=True)
    op.alter_column('CFV', 'start_time',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               existing_nullable=True)
    op.drop_constraint(None, 'CF', type_='foreignkey')
    op.drop_constraint(None, 'CF', type_='foreignkey')
    op.drop_constraint(None, 'CF', type_='foreignkey')
    op.create_foreign_key('CF_ibfk_1', 'CF', 'Product', ['product_id'], ['product_id'], ondelete='CASCADE')
    op.create_foreign_key('CF_ibfk_3', 'CF', 'EmissionFactor', ['factor_id'], ['factor_id'], ondelete='CASCADE')
    op.create_foreign_key('CF_ibfk_2', 'CF', 'CFV', ['cfv_id'], ['cfv_id'], ondelete='CASCADE')
    op.alter_column('CF', 'record_time',
               existing_type=sa.DateTime(),
               type_=mysql.TIMESTAMP(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    # ### end Alembic commands ###
