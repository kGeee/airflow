# Starburst

Starburst 

## Installation

Clone the git repository via 

```bash
git clone https://github.com/kGeee/airflow.git
```

## Create a local environment to run airflow with Breeze

Navigate to the airflow directory and run the following command to start airflow webserver and scheduler with trino integration

```bash
./breeze start-airflow --integration trino
```

The command should pull the docker images required to run and start the containers. You should be able to access airflow at `localhost:28080`.
The default login is : `admin:admin`.

## Using the connection
The starburst connection must be configured in airflow connections before running the operator. The default connection string is **starburst_default**.

- Connection Id : starburst_default
- Connection Type : Starburst
- Host : Host Address
- Port : Host Port `38080`
- Login : User login `trino`
- Password : User password

Note: When running airflow with breeze, the trino host address should be the IPv4 address of the local machine with port 38080 and the login should be `trino`. 

## Running the example dag
Ensure that the connection is properly configured within airflow via the web ui.
Airflow defaults to finding dags in `~/airflow/files/dags`. The example dag is located in `airflow.providers.starburst.example_dags`. Move the contents of this folder into your `~/airflow/files/dags` folder to allow airflow to find the dag and the included sql file.


## Running the tests via Breeze


Airflow uses pytests to ensure that the provider will work correctly with Airflow. Tests module can be found at `~/airflow/tests/providers/starburst/`

There are two integrations used with the Starburst provider package `trino` and `kerberos`. 

In order to run tests you must execute the breeze script with the integration flags you wish to test
```bash
./breeze --integration trino --integration kerberos
```

 *When running trino integration tests you must add the connection for trino*
- Run the following command to add the connection  
    ```bash
        airflow connections add \
        --conn-login trino \
        --conn-type starburst \
        --conn-host `TRINO HOST IP HERE` \
        --conn-port 38080 \
        --conn-extra {} \
        starburst_default
    ```

Once the integration is running and the connection is configured you can then run the pytests with the integration flag you wish to test.
```bash
pytests tests/providers/starburst/ --integration trino --integration kerberos
```

Note : Tests with integration flags will only be run if the integration is enabled



[Example Dags](https://github.com/kGeee/airflow/tree/main/airflow/providers/starburst/example_dags)

## Additional documentation
[Connection Docs](https://github.com/kGeee/airflow/blob/main/docs/apache-airflow-providers-starburst/connections/starburst.rst)\
[Operator Docs](https://github.com/kGeee/airflow/blob/main/docs/apache-airflow-providers-starburst/operators/starburst.rst)


## Provider files added
 - `airflow.providers.starburst`
 - `tests.providers.starburst`
 - `docs.apache-airflow-providers-starburst`

## Possible running issues and fixes
When running airflow via WSL2 its possible that you run into `$' r' command not found` when starting airflow via the breeze script. This is an issue regarding the script having embedded `\r` characters. To solve this issue you can use dos2unix.

```bash
sudo apt-get install dos2unix
sudo find . -type f -exec dos2unix {} \; 
```

Solution Resources: 
- [StackOverflow](https://stackoverflow.com/questions/29045140/env-bash-r-no-such-file-or-directory)
- [AskUbuntu](https://askubuntu.com/questions/803162/how-to-change-windows-line-ending-to-unix-version)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
