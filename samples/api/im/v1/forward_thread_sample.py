# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.im.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ForwardThreadRequest = ForwardThreadRequest.builder() \
        .thread_id("ot_dc13264520392913993dd051dba21dcf") \
        .receive_id_type("open_id") \
        .uuid("b13g2t38-1jd2-458b-8djf-dtbca5104204") \
        .request_body(ForwardThreadRequestBody.builder()
                      .receive_id("oc_a0553eda9014c201e6969b478895c230")
                      .build()) \
        .build()

    # 发起请求
    response: ForwardThreadResponse = client.im.v1.thread.forward(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.im.v1.thread.forward failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: ForwardThreadRequest = ForwardThreadRequest.builder() \
        .thread_id("ot_dc13264520392913993dd051dba21dcf") \
        .receive_id_type("open_id") \
        .uuid("b13g2t38-1jd2-458b-8djf-dtbca5104204") \
        .request_body(ForwardThreadRequestBody.builder()
                      .receive_id("oc_a0553eda9014c201e6969b478895c230")
                      .build()) \
        .build()

    # 发起请求
    response: ForwardThreadResponse = await client.im.v1.thread.aforward(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.im.v1.thread.aforward failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
