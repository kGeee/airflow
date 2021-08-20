import unittest
import pytest


from airflow.models.dag import DAG
from airflow.providers.starburst.operators.starburst import StarburstOperator
from airflow.utils import timezone


DEFAULT_DATE = timezone.datetime(2015, 1, 1)
DEFAULT_DATE_ISO = DEFAULT_DATE.isoformat()
DEFAULT_DATE_DS = DEFAULT_DATE_ISO[:10]
TEST_DAG_ID = 'unit_test_dag'

class TestStarburst(unittest.TestCase):
    def setUp(self):
        super().setUp()
        args = {'owner': 'airflow', 'start_date': DEFAULT_DATE}
        dag = DAG(TEST_DAG_ID, default_args=args)
        self.dag = dag

    def test_starburst_operator(self):
        sql = """
                SHOW CATALOGS;
                """
        op = StarburstOperator(task_id='basic_starburst',sql=sql, xcom_push=False, dag=self.dag)

    def test_starburst_operator_multiple_stmts(self):
        sql = ["SHOW CATALOGS",
               "SHOW SCHEMAS IN TPCH"]
        op = StarburstOperator(task_id='basic_starburst',sql=sql, xcom_push=False, dag=self.dag)

    