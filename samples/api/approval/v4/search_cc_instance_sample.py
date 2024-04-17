# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.approval.v4 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: SearchCcInstanceRequest = SearchCcInstanceRequest.builder() \
        .page_size(10) \
        .page_token("nF1ZXJ5VGhlbkZldGNoCgAAAAAA6PZwFmUzSldvTC1yU") \
        .user_id_type("user_id") \
        .request_body(CcSearch.builder()
                      .user_id("lwiu098wj")
                      .approval_code("EB828003-9FFE-4B3F-AA50-2E199E2ED942")
                      .instance_code("EB828003-9FFE-4B3F-AA50-2E199E2ED943")
                      .instance_external_id("EB828003-9FFE-4B3F-AA50-2E199E2ED976")
                      .group_external_id("1234567")
                      .cc_title("test")
                      .read_status("READ")
                      .cc_create_time_from("1547654251506")
                      .cc_create_time_to("1547654251506")
                      .locale("zh-CN")
                      .build()) \
        .build()

    # 发起请求
    response: SearchCcInstanceResponse = client.approval.v4.instance.search_cc(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.approval.v4.instance.search_cc failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: SearchCcInstanceRequest = SearchCcInstanceRequest.builder() \
        .page_size(10) \
        .page_token("nF1ZXJ5VGhlbkZldGNoCgAAAAAA6PZwFmUzSldvTC1yU") \
        .user_id_type("user_id") \
        .request_body(CcSearch.builder()
                      .user_id("lwiu098wj")
                      .approval_code("EB828003-9FFE-4B3F-AA50-2E199E2ED942")
                      .instance_code("EB828003-9FFE-4B3F-AA50-2E199E2ED943")
                      .instance_external_id("EB828003-9FFE-4B3F-AA50-2E199E2ED976")
                      .group_external_id("1234567")
                      .cc_title("test")
                      .read_status("READ")
                      .cc_create_time_from("1547654251506")
                      .cc_create_time_to("1547654251506")
                      .locale("zh-CN")
                      .build()) \
        .build()

    # 发起请求
    response: SearchCcInstanceResponse = await client.approval.v4.instance.asearch_cc(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.approval.v4.instance.asearch_cc failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
