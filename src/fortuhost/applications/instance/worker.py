from fortuhost.applications.interfaces.instance import InstanceClient, InstanceGateway, InstanceControlGateway
from fortuhost.applications.interfaces.project import ProjectGateway
from fortuhost.domain.dto.instance import InstanceExitCodeEnum, InstanceStatusEnum


async def update_instance_status(
        client: InstanceClient,
        instance_gateway: InstanceGateway,
):
    instances = client.filter_instances()

    for instance in instances:
        await instance_gateway.update_status(instance.id, instance.status)


async def check_fallen_instances(
    client: InstanceClient,
    instance_control_gateway: InstanceControlGateway,
    project_gateway: ProjectGateway
):
    instances = client.filter_instances(
        filters={
            'exited': InstanceExitCodeEnum.APP_ERROR,
            'status': InstanceStatusEnum.EXITED
        }
    )

    for instance in instances:
        project = await client.get_instance_project(instance_id=instance.id)
        if project_gateway.is_paid(project_id=project.id):
            instance_control_gateway.start(instance.id)
