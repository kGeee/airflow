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



.. _howto/connection:starburst:

Starburst Connection
====================

The Starburst connection type enables integrations with Starburst.

Authenticating to Starburst
---------------------------

Authenticate to Starburst using the trino-python-client
<https://github.com/trinodb/trino-python-client>`_.

Default Connection IDs
----------------------

Hooks, operators, and sensors related to Starburst use ``starburst_default`` by default.

Configuring the Connection
--------------------------

Login
    Specify the starburst username.

Password
    Specify the starburst password.

Host (optional)
    Specify the starburst hostname.

Schema (optional)
    Specify the starburst schema to be used.

Extra (optional)
    Specify the extra parameters (as json dictionary) that can be used in the starburst connection.
    The following parameters are all optional:

    * ``source`` : Source of request
    * ``protocol`` : HTTP Scheme ``http`` or ``https``
    * ``catalog``: Catalog to run starburst queries by default
    * ``isolation_level`` : Isolation Level, default ``AUTOCOMMIT``
    * ``auth``: To connect using Kerberos ``kerberos``, JWT ``jwt``
    * ``kerberos__config`` : Kerberos config
    * ``kerberos__service_name`` : Kerberos service name
    * ``kerberos__mutual_authentication`` : Kerberos mutual authentication
    * ``kerberos__force_preemptive`` : Kerberos Force preemptive 
    * ``kerberos__hostname_override`` : Kerberos Hostname 
    * ``kerberos__sanitize_mutual_error_response`` : Kerberos sanitize mutual error response
    * ``kerberos__principal`` : Kerberos Principal
    * ``kerberos__delegate`` : Kerberos Delegate
    * ``kerberos__ca_bundle`` : Kerberos CA Bundle
    * ``jwt_token`` : JWT Token
