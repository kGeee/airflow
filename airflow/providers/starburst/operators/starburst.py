from enum import auto
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
import logging
from airflow.providers.starburst.hooks.trino import TrinoHook

from typing import Optional, Union, List

class StarburstOperator(BaseOperator):
    """
    Executes sql code in a Starburst cluster

    .. seealso::
        For more information on how to use this operator, take a look at the guide:
        :ref:`howto/operator:StarburstOperator`

    :param sql: the sql code to be executed. (templated)
    :type sql: Can receive a str representing a sql statement,
        a list of str (sql statements), or reference to a template file.
        Jinja Template reference are recognized by str ending in '.sql'
    :param autocommit: reference to specific trino connection id
    :type autocommit: bool
    :param parameters: parameters to be used with query
    :type parameters: Optional[dict]
    :param xcom_push: push query result to xcom
    :type xcom_push: bool
    """
    template_fields = ['sql']
    template_fields_renderers = {'sql': 'sql'}
    template_ext = ['.sql']
    ui_color = '#ededed'

    @apply_defaults
    def __init__(
            self,
            sql: Union[str, List[str]],
            autocommit: bool = True,
            parameters: Optional[dict] = None,
            xcom_push: bool = True,
            *args,
            **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.sql = sql
        self.autocommit = autocommit
        self.parameters = parameters
        self.xcom_push = xcom_push
        self.hook = None

    def execute(self, context):
        """
        Execute query against Starburst Enterprise Platform
        """
        logging.info(f"Running SQL :{self.sql}")
        self.hook = TrinoHook()
        query = self.hook.run(self.sql, autocommit=self.autocommit, parameters=self.parameters)
        if self.xcom_push:
            return query