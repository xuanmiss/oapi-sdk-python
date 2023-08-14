from .resource import *


class V1(object):
    def __init__(self, config: Config) -> None:
        self.application: Application = Application(config)
        self.application_interview: ApplicationInterview = ApplicationInterview(config)
        self.attachment: Attachment = Attachment(config)
        self.ehr_import_task: EhrImportTask = EhrImportTask(config)
        self.ehr_import_task_for_internship_offer: EhrImportTaskForInternshipOffer = EhrImportTaskForInternshipOffer(
            config)
        self.employee: Employee = Employee(config)
        self.evaluation: Evaluation = Evaluation(config)
        self.external_application: ExternalApplication = ExternalApplication(config)
        self.external_background_check: ExternalBackgroundCheck = ExternalBackgroundCheck(config)
        self.external_interview: ExternalInterview = ExternalInterview(config)
        self.external_interview_assessment: ExternalInterviewAssessment = ExternalInterviewAssessment(config)
        self.interview: Interview = Interview(config)
        self.job: Job = Job(config)
        self.job_manager: JobManager = JobManager(config)
        self.job_process: JobProcess = JobProcess(config)
        self.job_requirement: JobRequirement = JobRequirement(config)
        self.job_requirement_schema: JobRequirementSchema = JobRequirementSchema(config)
        self.note: Note = Note(config)
        self.offer: Offer = Offer(config)
        self.offer_schema: OfferSchema = OfferSchema(config)
        self.questionnaire: Questionnaire = Questionnaire(config)
        self.referral: Referral = Referral(config)
        self.referral_website_job_post: ReferralWebsiteJobPost = ReferralWebsiteJobPost(config)
        self.registration_schema: RegistrationSchema = RegistrationSchema(config)
        self.resume_source: ResumeSource = ResumeSource(config)
        self.talent: Talent = Talent(config)
        self.talent_folder: TalentFolder = TalentFolder(config)
        self.talent_object: TalentObject = TalentObject(config)