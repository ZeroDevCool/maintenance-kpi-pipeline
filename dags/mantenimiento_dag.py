from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'data-engineer',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='mantenimiento_kpis_dag',
    default_args=default_args,
    description='Pipeline de mantenimiento: Ejecuta modelos y validaciones de Dataform',
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False,
    tags=['mantenimiento', 'dataform', 'kpis'],
) as dag:

    start = BashOperator(
        task_id='start',
        bash_command='echo "🚀 Iniciando DAG de KPIs de mantenimiento"',
    )

    ejecutar_dataform = BashOperator(
        task_id='ejecutar_dataform',
        bash_command='cd /path/a/tu/proyecto/dataform && dataform run',
    )

    validar_resultados = BashOperator(
        task_id='validar_resultados',
        bash_command='echo "✅ Validaciones de assertions completadas"',
    )

    end = BashOperator(
        task_id='end',
        bash_command='echo "🏁 DAG finalizado correctamente"',
    )

    start >> ejecutar_dataform >> validar_resultados >> end