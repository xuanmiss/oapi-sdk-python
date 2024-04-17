# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.corehr.v2 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: SearchBasicInfoDistrictRequest = SearchBasicInfoDistrictRequest.builder() \
        .page_size(100) \
        .page_token("6891251722631890445") \
        .request_body(SearchBasicInfoDistrictRequestBody.builder()
                      .city_id_list([])
                      .district_id_list([])
                      .status_list([])
                      .build()) \
        .build()

    # 发起请求
    response: SearchBasicInfoDistrictResponse = client.corehr.v2.basic_info_district.search(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.basic_info_district.search failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: SearchBasicInfoDistrictRequest = SearchBasicInfoDistrictRequest.builder() \
        .page_size(100) \
        .page_token("6891251722631890445") \
        .request_body(SearchBasicInfoDistrictRequestBody.builder()
                      .city_id_list([])
                      .district_id_list([])
                      .status_list([])
                      .build()) \
        .build()

    # 发起请求
    response: SearchBasicInfoDistrictResponse = await client.corehr.v2.basic_info_district.asearch(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.corehr.v2.basic_info_district.asearch failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
