"""changing relation from project to scenario

Revision ID: 200aad3efdbb
Revises: d8428ca8ab9d
Create Date: 2023-10-06 12:26:49.087281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '200aad3efdbb'
down_revision: Union[str, None] = 'd8428ca8ab9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('balance_sheet', sa.Column('scenario', sa.Integer(), nullable=False))
    op.drop_index('ix_balance_sheet_project', table_name='balance_sheet')
    op.create_index(op.f('ix_balance_sheet_scenario'), 'balance_sheet', ['scenario'], unique=True)
    op.drop_column('balance_sheet', 'project')
    op.add_column('capex', sa.Column('scenario_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_capex_scenario_id'), 'capex', ['scenario_id'], unique=True)
    op.drop_column('capex', 'project_id')
    op.add_column('cash_flow_plan', sa.Column('scenario', sa.Integer(), nullable=False))
    op.drop_index('ix_cash_flow_plan_project', table_name='cash_flow_plan')
    op.create_index(op.f('ix_cash_flow_plan_scenario'), 'cash_flow_plan', ['scenario'], unique=True)
    op.drop_column('cash_flow_plan', 'project')
    op.add_column('credits', sa.Column('scenario_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_credits_scenario_id'), 'credits', ['scenario_id'], unique=True)
    op.drop_column('credits', 'project_id')
    op.add_column('expenses', sa.Column('scenario_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_expenses_scenario_id'), 'expenses', ['scenario_id'], unique=True)
    op.drop_column('expenses', 'project_id')
    op.add_column('financial_ratios', sa.Column('scenario', sa.Integer(), nullable=False))
    op.drop_index('ix_financial_ratios_project', table_name='financial_ratios')
    op.create_index(op.f('ix_financial_ratios_scenario'), 'financial_ratios', ['scenario'], unique=True)
    op.drop_column('financial_ratios', 'project')
    op.add_column('leasings', sa.Column('scenario_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_leasings_scenario_id'), 'leasings', ['scenario_id'], unique=True)
    op.drop_column('leasings', 'project_id')
    op.add_column('own_funds', sa.Column('scenario_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_own_funds_scenario_id'), 'own_funds', ['scenario_id'], unique=True)
    op.drop_column('own_funds', 'project_id')
    op.add_column('profit_loss_plan', sa.Column('scenario', sa.Integer(), nullable=False))
    op.drop_index('ix_profit_loss_plan_project', table_name='profit_loss_plan')
    op.create_index(op.f('ix_profit_loss_plan_scenario'), 'profit_loss_plan', ['scenario'], unique=True)
    op.drop_column('profit_loss_plan', 'project')
    op.add_column('project_details', sa.Column('scenario_id', sa.Integer(), nullable=False))
    op.drop_index('ix_project_details_project', table_name='project_details')
    op.create_index(op.f('ix_project_details_scenario_id'), 'project_details', ['scenario_id'], unique=True)
    op.drop_column('project_details', 'project')
    op.add_column('purchases', sa.Column('scenario_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_purchases_scenario_id'), 'purchases', ['scenario_id'], unique=True)
    op.drop_column('purchases', 'project_id')
    op.add_column('sales', sa.Column('scenario_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_sales_scenario_id'), 'sales', ['scenario_id'], unique=True)
    op.drop_column('sales', 'project_id')
    op.add_column('sales_plan', sa.Column('scenario', sa.Integer(), nullable=False))
    op.drop_index('ix_sales_plan_project', table_name='sales_plan')
    op.create_index(op.f('ix_sales_plan_scenario'), 'sales_plan', ['scenario'], unique=True)
    op.drop_column('sales_plan', 'project')
    op.add_column('taxes', sa.Column('scenario_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_taxes_scenario_id'), 'taxes', ['scenario_id'], unique=True)
    op.drop_column('taxes', 'project_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('taxes', sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_taxes_scenario_id'), table_name='taxes')
    op.drop_column('taxes', 'scenario_id')
    op.add_column('sales_plan', sa.Column('project', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_sales_plan_scenario'), table_name='sales_plan')
    op.create_index('ix_sales_plan_project', 'sales_plan', ['project'], unique=False)
    op.drop_column('sales_plan', 'scenario')
    op.add_column('sales', sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_sales_scenario_id'), table_name='sales')
    op.drop_column('sales', 'scenario_id')
    op.add_column('purchases', sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_purchases_scenario_id'), table_name='purchases')
    op.drop_column('purchases', 'scenario_id')
    op.add_column('project_details', sa.Column('project', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_project_details_scenario_id'), table_name='project_details')
    op.create_index('ix_project_details_project', 'project_details', ['project'], unique=False)
    op.drop_column('project_details', 'scenario_id')
    op.add_column('profit_loss_plan', sa.Column('project', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_profit_loss_plan_scenario'), table_name='profit_loss_plan')
    op.create_index('ix_profit_loss_plan_project', 'profit_loss_plan', ['project'], unique=False)
    op.drop_column('profit_loss_plan', 'scenario')
    op.add_column('own_funds', sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_own_funds_scenario_id'), table_name='own_funds')
    op.drop_column('own_funds', 'scenario_id')
    op.add_column('leasings', sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_leasings_scenario_id'), table_name='leasings')
    op.drop_column('leasings', 'scenario_id')
    op.add_column('financial_ratios', sa.Column('project', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_financial_ratios_scenario'), table_name='financial_ratios')
    op.create_index('ix_financial_ratios_project', 'financial_ratios', ['project'], unique=False)
    op.drop_column('financial_ratios', 'scenario')
    op.add_column('expenses', sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_expenses_scenario_id'), table_name='expenses')
    op.drop_column('expenses', 'scenario_id')
    op.add_column('credits', sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_credits_scenario_id'), table_name='credits')
    op.drop_column('credits', 'scenario_id')
    op.add_column('cash_flow_plan', sa.Column('project', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_cash_flow_plan_scenario'), table_name='cash_flow_plan')
    op.create_index('ix_cash_flow_plan_project', 'cash_flow_plan', ['project'], unique=False)
    op.drop_column('cash_flow_plan', 'scenario')
    op.add_column('capex', sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_capex_scenario_id'), table_name='capex')
    op.drop_column('capex', 'scenario_id')
    op.add_column('balance_sheet', sa.Column('project', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_index(op.f('ix_balance_sheet_scenario'), table_name='balance_sheet')
    op.create_index('ix_balance_sheet_project', 'balance_sheet', ['project'], unique=False)
    op.drop_column('balance_sheet', 'scenario')
    # ### end Alembic commands ###