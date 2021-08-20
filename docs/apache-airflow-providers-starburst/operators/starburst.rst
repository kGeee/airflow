 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.

.. _howto/operator:StarburstOperator:

StarburstOperator
=================

Use the :class:`StarburstOperator <airflow.providers.starburst.operators.starburst>` to execute
SQL commands in a `Starburst <https://trino.io>`__ cluster.


Using the Operator
^^^^^^^^^^^^^^^^^^

Use the ``starburst_conn_id`` argument to connect to your Starburst instance where
the connection metadata is structured as follows:

.. list-table:: Starburst Airflow Connection Metadata
   :widths: 25 25
   :header-rows: 1

   * - Parameter
     - Input
   * - sql: string
     - SQL Query to be executed
   * - autocommit: bool
     - Boolean value for autocommit
   * - parameters: dictionary
     - parameters to be used with query/queries
   * - xcom_push: bool
     - Boolean to push query result to xcom


An example usage of the StarburstOperator is as follows:

.. exampleinclude:: /../../airflow/providers/starburst/example_dags/example_starburst.py
    :language: python
    :start-after: [START howto_operator_starburst]
    :end-before: [END howto_operator_starburst]

.. note::

  Parameters which are passed via the operator have precedence over default connection parameters