import pendulum
from airflow.decorators import dag, task
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.providers.ssh.hooks.ssh import SSHHook

from pulsar.respaldos.volumenes import volumenes

@dag(
    default_args={'owner': 'airflow'},
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz='UTC'),
    catchup=False,
    tags=['pulsar','respaldos'],
    params={
        'nombre_del_respaldo': 'automatico'
    }
)
def pulsar_guardar_respaldo():
    @task()
    def calcular_tamaño_respaldo(**context):
        data = context["dag_run"].conf

        ssh_hook = SSHHook(ssh_conn_id='pulsar')
        run_cmd = SSHOperator(
            task_id='calcular_tamaño_respaldo',
            ssh_hook=ssh_hook,
            command=(
                'df -h'
            )
        )

        run_cmd.execute(context=context)

    @task()
    def generar_respaldo(**context):
        data = context["dag_run"].conf

        for volumen in volumenes.keys():
            nombre_volumen = volumenes[volumen]["Name"]
            ssh_hook = SSHHook(ssh_conn_id='pulsar')
            run_cmd = SSHOperator(
                task_id='generar_respaldo_'+volumen,
                ssh_hook=ssh_hook,
                command=(
                    'docker run --rm '
                    f'-v "{nombre_volumen}":/volume '
                    '-v ~/respaldos:/backup '
                    'ubuntu '
                    f'tar -zcvf /backup/{volumen}.tar.gz /volume '
                )
            )

            run_cmd.execute(context=context)

    @task()
    def guardar_respaldo(**context):
        data = context["dag_run"].conf

        ssh_hook = SSHHook(ssh_conn_id='pulsar')
        run_cmd = SSHOperator(
            task_id='guardar_respaldo',
            ssh_hook=ssh_hook,
            command=(
                'ls ~/respaldos -la'
            )
        )

        run_cmd.execute(context=context)

    calcular_tamaño_respaldo() >> \
    generar_respaldo() >> \
    guardar_respaldo()


pulsar_guardar_respaldo = pulsar_guardar_respaldo()
