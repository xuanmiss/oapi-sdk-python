# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.vc.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: GetParticipantQualityListRequest = GetParticipantQualityListRequest.builder() \
        .meeting_start_time("1655276858") \
        .meeting_end_time("1655276858") \
        .meeting_no("123456789") \
        .join_time("1655276858") \
        .user_id("ou_3ec3f6a28a0d08c45d895276e8e5e19b") \
        .room_id("omm_eada1d61a550955240c28757e7dec3af") \
        .page_size(20) \
        .page_token("str") \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: GetParticipantQualityListResponse = client.vc.v1.participant_quality_list.get(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.participant_quality_list.get failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
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
    request: GetParticipantQualityListRequest = GetParticipantQualityListRequest.builder() \
        .meeting_start_time("1655276858") \
        .meeting_end_time("1655276858") \
        .meeting_no("123456789") \
        .join_time("1655276858") \
        .user_id("ou_3ec3f6a28a0d08c45d895276e8e5e19b") \
        .room_id("omm_eada1d61a550955240c28757e7dec3af") \
        .page_size(20) \
        .page_token("str") \
        .user_id_type("user_id") \
        .build()

    # 发起请求
    response: GetParticipantQualityListResponse = await client.vc.v1.participant_quality_list.aget(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.vc.v1.participant_quality_list.aget failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    # asyncio.run(amain()) 异步方式
    main()
