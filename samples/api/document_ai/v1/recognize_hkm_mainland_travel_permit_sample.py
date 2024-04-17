# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.document_ai.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    file = open("file_path", "rb")
    request: RecognizeHkmMainlandTravelPermitRequest = RecognizeHkmMainlandTravelPermitRequest.builder() \
        .request_body(RecognizeHkmMainlandTravelPermitRequestBody.builder()
                      .file(file)
                      .build()) \
        .build()

    # 发起请求
    response: RecognizeHkmMainlandTravelPermitResponse = client.document_ai.v1.hkm_mainland_travel_permit.recognize(
        request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.document_ai.v1.hkm_mainland_travel_permit.recognize failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    file = open("file_path", "rb")
    request: RecognizeHkmMainlandTravelPermitRequest = RecognizeHkmMainlandTravelPermitRequest.builder() \
        .request_body(RecognizeHkmMainlandTravelPermitRequestBody.builder()
                      .file(file)
                      .build()) \
        .build()

    # 发起请求
    response: RecognizeHkmMainlandTravelPermitResponse = await client.document_ai.v1.hkm_mainland_travel_permit.arecognize(
        request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.document_ai.v1.hkm_mainland_travel_permit.arecognize failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
