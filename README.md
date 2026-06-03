# AWS Monitoring Dashboard

Herramienta de monitorización y análisis de arquitecturas cloud basadas en microservicios en Amazon Web Services, desarrollada como Trabajo de Fin de Grado en la ETSI Informáticos de la Universidad Politécnica de Madrid.

**Autora:** Leila Gómez Vallejo  
**Grado:** Ingeniería Informática - UPM

---

## Descripción

La herramienta se conecta a una cuenta de AWS mediante boto3 y proporciona un dashboard interactivo en Jupyter Notebook que analiza la infraestructura desplegada desde cinco perspectivas:

- **Discovery** - Inventario automático de recursos y detección de relaciones entre servicios (directas e inferidas desde variables de entorno).
- **Health** - Estado operativo de cada recurso con clasificación en cuatro niveles: HEALTHY, WARNING, CRITICAL e INFO.
- **Metrics** - Métricas de rendimiento desde CloudWatch con ventanas temporales configurables y notas operativas automáticas.
- **Logs** - Análisis de CloudWatch Logs y CloudTrail con detección de errores en dos capas.
- **Security** - Más de 200 comprobaciones de configuración de seguridad clasificadas en CRIT, WARN, INFO y OK.

Cubre 14 servicios de AWS: Lambda, DynamoDB, API Gateway, SQS, SNS, S3, RDS, Cognito, Step Functions, WAF, Elastic Beanstalk, ElastiCache, ECR y CodeCommit.

---

## Requisitos previos

- Python 3.10 o superior
- Credenciales de AWS configuradas (mediante `~/.aws/credentials` o variables de entorno)
- Acceso a una cuenta de AWS con los servicios a monitorizar desplegados

---

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/leilagomeez/tfg-aws-monitorizacion.git
cd tfg-aws-monitorizacion
```

2. Crea un entorno virtual e instala las dependencias:

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

## Uso

1. Inicia Jupyter Notebook:

```bash
jupyter notebook
```

2. Abre `notebooks/dashboard.ipynb` y ejecuta todas las celdas en orden (Kernel → Restart & Run All).

3. Interactúa con el dashboard: selecciona el servicio y la pestaña de análisis desde los controles de la interfaz.

Los informes se guardan automáticamente en la carpeta `outputs/` al pulsar el botón de exportación.

---

## Estructura del proyecto

```
tfg-aws-monitorizacion/
├── notebooks/
│   └── dashboard.ipynb       # Notebook principal con el dashboard
├── src/
│   ├── __init__.py
│   └── aws_session.py        # Módulo de conexión con AWS
├── outputs/                  # Informes HTML generados (no incluidos en el repo)
├── requirements.txt          # Dependencias del proyecto
└── README.md
```

---

## Servicios monitorizados

| Servicio | Discovery | Health | Metrics | Logs | Security |
|---|:---:|:---:|:---:|:---:|:---:|
| Lambda | ✓ | ✓ | ✓ | ✓ | ✓ |
| DynamoDB | ✓ | ✓ | ✓ | — | ✓ |
| API Gateway | ✓ | ✓ | ✓ | ✓ | ✓ |
| SQS | ✓ | ✓ | ✓ | — | ✓ |
| SNS | ✓ | ✓ | ✓ | — | ✓ |
| S3 | ✓ | ✓ | ✓ | — | ✓ |
| RDS | ✓ | ✓ | ✓ | ✓ | ✓ |
| Cognito | ✓ | ✓ | ✓ | — | ✓ |
| Step Functions | ✓ | ✓ | ✓ | ✓ | ✓ |
| WAF | ✓ | ✓ | ✓ | ✓ | ✓ |
| Elastic Beanstalk | ✓ | ✓ | ✓ | ✓ | ✓ |
| ElastiCache | ✓ | ✓ | ✓ | — | ✓ |
| ECR | ✓ | ✓ | ✓ | — | ✓ |
| CodeCommit | ✓ | ✓ | — | — | ✓ |

---

## Tecnologías utilizadas

- **Python** - Lenguaje principal
- **boto3** - SDK oficial de AWS para Python
- **Jupyter Notebook** - Entorno de desarrollo interactivo
- **ipywidgets** - Interfaz gráfica del dashboard
- **Plotly** - Visualizaciones interactivas
- **Mermaid** — Diagramas de arquitectura
- **pandas** — Procesamiento de datos

---

