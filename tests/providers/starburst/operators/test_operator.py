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
        args = {'owner': 'airflow', 'start_date': DEFAULT_DATE}
        dag = DAG(TEST_DAG_ID, default_args=args)
        self.dag = dag

    def tearDown(self) -> None:
        tables_to_drop = ['airflow_test']

        for table in tables_to_drop:
            sql = f"DROP TABLE IF EXISTS {table}"
            StarburstOperator(task_id="tearDown", starburst_conn_id="starburst_conn_id",sql=sql, dag=self.dag)

    def test_starburst_operator(self):
        sql = """
                CREATE TABLE IF NOT EXISTS airflow_test (
                    dummy VARCHAR(50)
                )
                """
        op = StarburstOperator(task_id='basic_starburst', starburst_conn_id='starburst_conn_id',sql=sql, dag=self.dag)

    def test_starburst_operator_multiple_stmts(self):
        sql = ["CREATE TABLE IF NOT EXISTS test_airflow (dummy VARCHAR(50))",
               "TRUNCATE TABLE test_airflow",
               "INSERT INTO test_airflow VALUES ('X')"]
        op = StarburstOperator(task_id='basic_starburst', starburst_conn_id='starburst_conn_id',sql=sql, dag=self.dag)

    