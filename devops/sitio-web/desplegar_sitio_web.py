import pendulum
from airflow.decorators import dag, task
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.providers.ssh.hooks.ssh import SSHHook


cmd = (
    'docker run --rm '
    '-v "$VOLUME_NAME":/backup-volume '
    '-v "$(pwd)":/backup '
    'ubuntu '
    'tar -zcvf /backup/$VOLUME_NAME.tar.gz /backup-volume '
)

@dag(
    default_args={'owner': 'airflow'},
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz='UTC'),
    catchup=False,
    tags=['pulsar','sitio-web'],
    params={
        'cmd': 'ls'
    }
)
def desplegar_sitio_web():
    @task()
    def create_or_update_conn(**context):
        data = context["dag_run"].conf

    @task()
    def run_cmd(**context):
        data = context["dag_run"].conf

        ssh_hook = SSHHook(ssh_conn_id='pulsar')
        run_cmd = SSHOperator(
            task_id='run_cmd',
            ssh_hook=ssh_hook,
            command=(data['cmd'])
        )

        run_cmd.execute(context=context)

    @task()
    def desplegar_base_de_datos(**context):
        data = context["dag_run"].conf

        ssh_hook = SSHHook(ssh_conn_id='pulsar')
        run_cmd = SSHOperator(
            task_id='run_cmd',
            ssh_hook=ssh_hook,
            command=(
                'docker run -d -v odoo-db:/var/lib/postgresql/data -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name odoo-postgres postgres:15 '
                'docker run -v odoo-data:/var/lib/odoo -d -p 8069:8069 --name odoo --link odoo-postgres:db -t odoo:17.0 '
            )
        )

        run_cmd.execute(context=context)

    create_or_update_conn() >> run_cmd()


desplegar_sitio_web = desplegar_sitio_web()
