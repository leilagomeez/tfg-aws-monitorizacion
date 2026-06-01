import boto3

def get_session(region="us-east-1"):
    """
    Crea una sesión de boto3 usando las credenciales
    configuradas en AWS CLI (~/.aws/credentials).
    
    En el Learner Lab las credenciales son temporales,
    así que hay que actualizar el fichero credentials
    cada vez que se reinicia el lab.
    """
    session = boto3.Session(region_name=region)
    return session


def get_client(service, region="us-east-1"):
    """Atajo para obtener un cliente de un servicio AWS."""
    session = get_session(region)
    return session.client(service)


def verificar_conexion():
    """Verifica que las credenciales funcionan e imprime info de la cuenta."""
    sts = get_client("sts")
    identity = sts.get_caller_identity()
    print(f"Conexión exitosa!")
    print(f"  Cuenta AWS: {identity['Account']}")
    print(f"  Usuario/Rol: {identity['Arn']}")
    print(f"  Región: {get_session().region_name}")
    return identity