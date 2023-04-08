from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException,NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup 
import requests 
import easyocr
from IPython.display import Image
import time



class Fetch(webdriver.Chrome):
    def __init__(self):
        # self.opt = Options()
        # self.opt.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        
    def ChooseCourse(self,course):
        self.course = course        
        self.driver.get("http://result.rgpv.ac.in/Result/ProgramSelect.aspx")
        if self.course=="B.tech":
            Choose_course = self.driver.find_element(By.ID,'radlstProgram_1')
            Choose_course.click()
        
    def InputRollNumber(self,roll_num1,sem1):
        #filling info
        self.roll_num = roll_num1
        self.sem = sem1
        fill_sem = Select(self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$drpSemester"))
        fill_sem.select_by_visible_text(self.sem)
        fill_roll_num = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$txtrollno")
        fill_roll_num.clear()
        fill_roll_num.send_keys(self.roll_num)
        self.FillCaptcha()
        response = self.ViewResult()
        return response

    def FillCaptcha(self):
        header={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

        #getting url of captcha image  from img src
        img = self.driver.find_element(By.XPATH,'//img[@alt="Captcha"]')
        src =  img.get_attribute('src')
        print(src)

        # downloading the image
        res = requests.get(src,headers = header)
        with open(f"captcha.png",'wb') as f:
            f.write(res.content)

        #reading text from captcha image
        Reader = easyocr.Reader(['en'])
        Image(f"captcha.png")
        output = Reader.readtext(f"captcha.png")
        captcha_text = output[0][1].replace(" ","")
        print(captcha_text)
        captcha_input_box = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$TextBox1")
        captcha_input_box.clear()
        captcha_input_box.send_keys(captcha_text)
        time.sleep(1)
        # return self.ViewResult()

    # def ViewResult(self):
    #     try:
    #         view_result = self.driver.find_element(By.NAME , "ctl00$ContentPlaceHolder1$btnviewresult")
    #         view_result.click() 
            
    #     except UnexpectedAlertPresentException as e:
    #         if e.alert_text == 'Result for this Enrollment No. not Found':
    #             try:
    #                 alert = self.driver.switch_to.alert
    #                 alert.accept()
                
    #             except NoAlertPresentException:
    #                 pass
    #             finally:
    #                 self.Reset()
    #                 return 0
                            
    #         if e.alert_text =='you have entered a wrong text':
    #             print("wrong capthcha")
    #             try:
    #                 alert = self.driver.switch_to.alert
    #                 alert.accept()
    #             except NoAlertPresentException:
    #                 pass
    #         #     else:
    #         #         self.Reset()
    #         #         return 0
    #         #     # captcha_input_box = self.driver.find_element(By.NAME,"ctl00$ContentPlaceHolder1$TextBox1")
    #         #     # captcha_input_box.clear()
    #         #     self.FillCaptcha() 
    #         else:
    #             raise e
    #     else:
    #         name = self.driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_lblNameGrading').text.strip()
    #         sgpa = self.driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_lblSGPA').text
    #         cgpa = self.driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_lblcgpa').text
    #         self.Reset()
    #         return (name,self.roll_num,sgpa,cgpa)  

     
    def ViewResult(self):
        
        view_result = self.driver.find_element(By.NAME , "ctl00$ContentPlaceHolder1$btnviewresult")
        view_result.click() 
        try:
            alert = self.driver.switch_to.alert
            pop_text = alert.text
            if pop_text == 'Result for this Enrollment No. not Found':
                alert.accept()
                self.Reset()
                return 0
            elif pop_text == 'you have entered a wrong text':
                alert.accept()
                return "wrong"
        except NoAlertPresentException:
            print("no alerts")

        name = self.driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_lblNameGrading').text.strip()
        sgpa = self.driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_lblSGPA').text
        cgpa = self.driver.find_element(By.ID,'ctl00_ContentPlaceHolder1_lblcgpa').text
        self.Reset()
        return (name,self.roll_num,sgpa,cgpa)    
    def Reset(self):
        resetButton = self.driver.find_element(By.XPATH,'//input[@value="Reset"]')
        resetButton.click()
            
    def Quit(self):
        self.driver.quit()

