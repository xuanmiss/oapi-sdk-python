# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.aily.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateAilySessionRunRequest = CreateAilySessionRunRequest.builder() \
        .aily_session_id("session_4dfunz7sp1g8m") \
        .request_body(CreateAilySessionRunRequestBody.builder()
                      .app_id("spring_xxx__c")
                      .skill_id("skill_6cc6166178ca")
                      .skill_input("")
                      .metadata("{}")
                      .build()) \
        .build()

    # 发起请求
    response: CreateAilySessionRunResponse = client.aily.v1.aily_session_run.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.aily.v1.aily_session_run.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: CreateAilySessionRunRequest = CreateAilySessionRunRequest.builder() \
        .aily_session_id("session_4dfunz7sp1g8m") \
        .request_body(CreateAilySessionRunRequestBody.builder()
                      .app_id("spring_xxx__c")
                      .skill_id("skill_6cc6166178ca")
                      .skill_input("")
                      .metadata("{}")
                      .build()) \
        .build()

    # 发起请求
    response: CreateAilySessionRunResponse = await client.aily.v1.aily_session_run.acreate(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.aily.v1.aily_session_run.acreate failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
