import pytest
from pages.infusion_therapy import InfusionTherapyPage

@pytest.mark.usefixtures("setup_logger")
class TestInfusionTherapyPage:  # Independent Medical Exams Page
    def test_infusion_therapy_page_title(self, infusion_therapy):
        self.logger.info("--- START: Infusion Therapy Page Title Test ---") 
        infusion_therapy.navigate()
        assert infusion_therapy.element_is_visible(InfusionTherapyPage.INFUSION_TITLE), "Infusion Therapy page title is not visible"
        self.logger.info("--- FINISH: Infusion Therapy Page Title Test ---")
        
    def test_phone(self, infusion_therapy):
        self.logger.info("--- START: Infusion Therapy Phone Test ---") 
        infusion_therapy.navigate()
        assert infusion_therapy.element_is_visible(InfusionTherapyPage.PHONE), "Phone is not visible"
        self.logger.info("--- FINISH: Infusion Therapy Phone Test ---")

    def test_address(self, infusion_therapy):
        self.logger.info("--- START: Infusion Therapy Address Test ---") 
        infusion_therapy.navigate()
        assert infusion_therapy.element_is_visible(InfusionTherapyPage.ADDRESS), "Address is not visible"
        self.logger.info("--- FINISH: Infusion Therapy Address Test ---")

    def test_phone_icon(self, infusion_therapy):
        self.logger.info("--- START: Infusion Therapy Phone Icon Test ---") 
        infusion_therapy.navigate()
        assert infusion_therapy.element_is_visible(InfusionTherapyPage.PHONE_ICON), "Phone icon is not visible"
        self.logger.info("--- FINISH: Infusion Therapy Phone Icon Test ---")

    def test_address_icon(self, infusion_therapy):
        self.logger.info("--- START: Infusion Therapy Address Icon Test ---") 
        infusion_therapy.navigate()
        assert infusion_therapy.element_is_visible(InfusionTherapyPage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Infusion Therapy Address Icon Test ---")

    def test_schedule_now_link(self, infusion_therapy):        
        self.logger.info("--- START: Infusion Therapy Schedule Now Test ---")       
        infusion_therapy.sch_now_link_flow()
        self.logger.info("--- FINISH: Infusion Therapy Schedule Now Test ---")