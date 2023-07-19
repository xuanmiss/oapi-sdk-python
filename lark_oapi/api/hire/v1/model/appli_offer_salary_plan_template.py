# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init


class AppliOfferSalaryPlanTemplate(object):
    _types = {
        "template_key": str,
        "total_amount": str,
        "currency": str,
        "salary_content": str,
    }

    def __init__(self, d):
        self.template_key: Optional[str] = None
        self.total_amount: Optional[str] = None
        self.currency: Optional[str] = None
        self.salary_content: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppliOfferSalaryPlanTemplateBuilder":
        return AppliOfferSalaryPlanTemplateBuilder()


class AppliOfferSalaryPlanTemplateBuilder(object):
    def __init__(self, appli_offer_salary_plan_template: AppliOfferSalaryPlanTemplate = AppliOfferSalaryPlanTemplate(
        {})) -> None:
        self._appli_offer_salary_plan_template: AppliOfferSalaryPlanTemplate = appli_offer_salary_plan_template

    def template_key(self, template_key: str) -> "AppliOfferSalaryPlanTemplateBuilder":
        self._appli_offer_salary_plan_template.template_key = template_key
        return self

    def total_amount(self, total_amount: str) -> "AppliOfferSalaryPlanTemplateBuilder":
        self._appli_offer_salary_plan_template.total_amount = total_amount
        return self

    def currency(self, currency: str) -> "AppliOfferSalaryPlanTemplateBuilder":
        self._appli_offer_salary_plan_template.currency = currency
        return self

    def salary_content(self, salary_content: str) -> "AppliOfferSalaryPlanTemplateBuilder":
        self._appli_offer_salary_plan_template.salary_content = salary_content
        return self

    def build(self) -> "AppliOfferSalaryPlanTemplate":
        return self._appli_offer_salary_plan_template