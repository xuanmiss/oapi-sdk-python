# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.drive.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: DeletePermissionMemberRequest = DeletePermissionMemberRequest.builder() \
        .token("doccnBKgoMyY5OMbUG6FioTXuBe") \
        .member_id("ou_7dab8a3d3cdcc9da365777c7ad535d62") \
        .type("doc") \
        .member_type("openid") \
        .request_body(DeletePermissionMemberRequestBody.builder()
                      .type("user")
                      .build()) \
        .build()

    # 发起请求
    response: DeletePermissionMemberResponse = client.drive.v1.permission_member.delete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.permission_member.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


# 异步方式
async def amain():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: DeletePermissionMemberRequest = DeletePermissionMemberRequest.builder() \
        .token("doccnBKgoMyY5OMbUG6FioTXuBe") \
        .member_id("ou_7dab8a3d3cdcc9da365777c7ad535d62") \
        .type("doc") \
        .member_type("openid") \
        .request_body(DeletePermissionMemberRequestBody.builder()
                      .type("user")
                      .build()) \
        .build()

    # 发起请求
    response: DeletePermissionMemberResponse = await client.drive.v1.permission_member.adelete(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.drive.v1.permission_member.adelete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
