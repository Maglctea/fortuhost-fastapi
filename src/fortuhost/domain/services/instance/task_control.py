from fortuhost.applications.interfaces.instance import InstanceTaskGateway, InstanceClient, InstanceControlGateway
from fortuhost.applications.interfaces.notification import InstanceNotificationGateway
from fortuhost.applications.interfaces.project import ProjectGateway
from fortuhost.applications.interfaces.wallet import WalletGateway
from fortuhost.domain.dto.instance import InstancePermissionEnum
from fortuhost.domain.exceptions.user import AccessDeniedError
from fortuhost.domain.exceptions.wallet import InsufficientFundsError
from fortuhost.domain.services.instance.access import InstanceControlAccessService
from fortuhost.instance.enum import ActionTypeEnum


async def instance_task_control(
        client: InstanceClient,
        instance_control_gateway: InstanceControlGateway,
        instance_task_gateway: InstanceTaskGateway,
        access_control_gateway: InstanceControlAccessService,
        notification_gateway: InstanceNotificationGateway,
        project_gateway: ProjectGateway,
        wallet_gateway: WalletGateway
):
    tasks = await instance_task_gateway.get_tasks(count=100)

    for task in tasks:
        user = await client.get_instance_owner(task.instance_id)
        try:
            match task.type:
                case ActionTypeEnum.START:
                    project = await client.get_instance_project(task.instance_id)
                    if project_gateway.is_paid(project.id):
                        if (
                                access_control_gateway.is_can_perform_action(
                                    user_id=user.user_id,
                                    instance_id=task.instance_id,
                                    action=InstancePermissionEnum.CAN_START
                                )
                        ):
                            instance_control_gateway.start(task.instance_id)
                        else:
                            raise AccessDeniedError('Insufficient permissions to start the instance')
                    else:
                        await wallet_gateway.pay_subscription(project.id)

                case ActionTypeEnum.STOP:
                    if access_control_gateway.is_can_perform_action(
                            user_id=user.user_id,
                            instance_id=task.instance_id,
                            action=InstancePermissionEnum.CAN_STOP,
                    ):
                        instance_control_gateway.stop(task.instance_id)
                    else:
                        raise AccessDeniedError('Insufficient permissions to stop the instance')

                case ActionTypeEnum.RESTART:
                    if access_control_gateway.is_can_perform_action(
                            user_id=user.user_id,
                            instance_id=task.instance_id,
                            action=InstancePermissionEnum.CAN_RESTART,
                    ):
                        instance_control_gateway.restart(task.instance_id)
                    else:
                        raise AccessDeniedError('Insufficient permissions to restart the instance')

                case ActionTypeEnum.DELETE:
                    if access_control_gateway.is_can_perform_action(
                            user_id=user.user_id,
                            instance_id=task.instance_id,
                            action=InstancePermissionEnum.CAN_DELETE,
                    ):
                        instance_control_gateway.delete(task.instance_id)
                    else:
                        raise AccessDeniedError('Insufficient permissions to delete the instance')
            await instance_task_gateway.success_complete_task(task.task_id)

        except AccessDeniedError:
            notification_gateway.send_task_error_report(
                task=task,
                reason='Access denied'
            )
        except InsufficientFundsError:
            notification_gateway.send_task_error_report(
                task=task,
                reason='There are not enough funds to launch the project'
            )

        finally:
            await instance_task_gateway.failed_complete_task(task.task_id)
