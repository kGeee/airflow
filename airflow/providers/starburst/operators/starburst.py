from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import logging
from airflow.providers.starburst.hooks.trino import TrinoHook

from typing import Union, List

class StarburstOperator(BaseOperator):
    """
    Executes sql code in a Starburst cluster

    :param sql: the sql code to be executed. (templated)
    :type sql: Can receive a str representing a sql statement,
        a list of str (sql statements), or reference to a template file.
        Template reference are recognized by str ending in '.sql'
    :param starburst_conn_id: reference to specific trino connection id
    :type starburst_conn_id: str
    :param schema: schema to run queries on; overloads connection provided schema
    """
    template_fields = ['sql']
    template_fields_renderers = {'sql': 'sql'}
    template_ext = ['.sql']
    ui_color = '#ededed'

    @apply_defaults
    def __init__(
            self,
            sql: Union[str, List[str]],
            starburst_conn_id: str = 'trino',
            *args,
            **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.sql = sql
        self.starburst_conn_id = starburst_conn_id
        self.hook = None

    def execute(self, context) -> None:
        """
        Execute query against Starburst Enterprise Platform
        :return: None
        """
        logging.info(f"Running SQL :{self.sql}")
        self.hook = TrinoHook()
        self.hook.run(self.sql)
