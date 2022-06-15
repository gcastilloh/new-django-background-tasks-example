from background_task import background
from logging import getLogger
from .models import Contador

logger = getLogger(__name__)
print(__name__)


"""

"""
@background(schedule=10)
def demo_task(message):
    c = Contador.objects.create(
            mensaje=message,
        )
    print(f"message[{c.pk}] = {message}")
    logger.debug('demo_task. message={0}'.format(message))

@background(schedule=5)
def saludar():
    print(f"task say: hola")
    


demo_task(message="Hola desde task.py",repeat=10,remove_existing_tasks=True)
saludar()