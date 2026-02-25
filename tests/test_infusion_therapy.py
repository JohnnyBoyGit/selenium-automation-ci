import pytest
from pages.infusion_therapy import InfusionTherapyPage
from src.logic.infusion_therapy_logic import InfusionTherapyLogic

@pytest.mark.usefixtures("setup_logger")
class TestInfusionTherapyPage:  # Independent Medical Exams Page

    def test_infusion_therapy_page_title(self, infusion_therapy):
        self.logger.info("--- START: Infusion Therapy Page Title Test ---") 
        infusion_therapy.navigate()
        
        # Visibility check
        assert infusion_therapy.element_is_visible(InfusionTherapyPage.INFUSION_TITLE), "Title not visible"
        
        # Content check
        actual_title = infusion_therapy.driver.find_element(*InfusionTherapyPage.INFUSION_TITLE).text
        assert InfusionTherapyLogic.EXPECTED_TITLE_PART in actual_title.upper()
        
        self.logger.info("--- FINISH: Infusion Therapy Page Title Test ---")
      
        
    def test_phone_data_integrity(self, infusion_therapy):
        self.logger.info("--- START: Infusion Therapy Phone Data Integrity Test ---") 
        infusion_therapy.navigate()
        assert infusion_therapy.element_is_visible(InfusionTherapyPage.PHONE), "Phone element not visible"
        
        raw_phone = infusion_therapy.driver.find_element(*InfusionTherapyPage.PHONE).text
        assert InfusionTherapyLogic.is_valid_phone_format(raw_phone), f"Invalid phone: {raw_phone}"

        self.logger.info("--- FINISH: Infusion Therapy Phone Data Integrity Test ---")


    def test_address_data_integrity(self, infusion_therapy):
        self.logger.info("--- START: Infusion Therapy Address Data Integrity Test ---") 
        infusion_therapy.navigate()
        assert infusion_therapy.element_is_visible(InfusionTherapyPage.ADDRESS), "Address element not visible"
        
        raw_address = infusion_therapy.driver.find_element(*InfusionTherapyPage.ADDRESS).text
        assert InfusionTherapyLogic.is_valid_address(raw_address), f"Address mismatch: {raw_address}"

        self.logger.info("--- FINISH: Infusion Therapy Address Data Integrity Test ---")


    def test_icons_visibility(self, infusion_therapy):
        self.logger.info("--- START: Infusion Therapy Icons Visibility Test ---") 
        infusion_therapy.navigate()
        assert infusion_therapy.element_is_visible(InfusionTherapyPage.PHONE_ICON), "Phone icon is not visible"
        assert infusion_therapy.element_is_visible(InfusionTherapyPage.ADDRESS_ICON), "Address icon is not visible"
        self.logger.info("--- FINISH: Infusion Therapy Icons Visibility Test ---")


    def test_schedule_now_link(self, infusion_therapy):        
        self.logger.info("--- START: Infusion Therapy Schedule Now Test ---")       
        infusion_therapy.sch_now_link_flow()
        self.logger.info("--- FINISH: Infusion Therapy Schedule Now Test ---")