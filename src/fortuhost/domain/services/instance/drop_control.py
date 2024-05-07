from fortuhost.applications.interfaces.instance import InstanceClient, InstanceGateway, InstanceControlGateway
from fortuhost.applications.interfaces.notification import InstanceNotificationGateway
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
        notification_gateway: InstanceNotificationGateway,
):
    instances = client.filter_instances(
        filters={
            'exited': InstanceExitCodeEnum.APP_ERROR,
            'status': InstanceStatusEnum.EXITED
        }
    )

    for instance in instances:
        user = await client.get_instance_owner(instance.id)
        if is_can_run(instance):
            instance_control_gateway.start(instance.id)
        else:
            notification_gateway.send_crash_report(
                recipient_id=user.user_id,
                instance_id=instance.id
            )
