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
Airflow defaults to finding dags in `files/dags`. The example dag for starburst is included in this fork. 

## Additional documentation
[Connection Docs](https://github.com/kGeee/airflow/blob/main/docs/apache-airflow-providers-starburst/connections/starburst.rst)\
[Operator Docs](https://github.com/kGeee/airflow/blob/main/docs/apache-airflow-providers-starburst/operators/starburst.rst)

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
