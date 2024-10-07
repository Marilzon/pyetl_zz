PostgreSQL: Fonte dos dados.
SQLAlchemy + Python: Responsável por extrair os dados do PostgreSQL.
Kafka: Envia os dados extraídos para o processamento em tempo real.
Spark: Realiza transformações e processa os dados recebidos do Kafka.
Delta Lake: Armazena os dados processados, oferecendo gerenciamento de versões e transações ACID.
Airflow: Faz a orquestração, controlando a execução do pipeline.
