# SMS-Bomber-App
This is a SMS Bomber app based on python and using selenium automation tool with chrome web driver.

Instructions : 
 > For using this selenium code you must install a Chrome Web Driver  
 
 > Alternateivly you can put following code which will insall WebDriver at runtime:
    <i> driver = webdriver.Chrome(ChromeDriverManager().install()) </i>
    you have to import <i>from webdriver_manager.chrome import ChromeDriverManager</i> which can be install using 
    pip install ChromeDriverManager
    
 > This code contains following attributes:
  1. driver :             A variable that holds current WebDriver Manager informtion
  2. driver.get('url') :  here we put the url of page which we want to open into opened web browser.(here amazon website)
  3. driver.find_element('xpath','full xpath'): it is point reference to DOM object which want to click or focus on web
        full xpath can be taken by <i>inspect > copy > copy full xpath</i>
  4. send_keys('string/value') : this method is used to send a value to the focused or clicked element like text area or boxes.
  5. click() : this method is used to click focused button or radio buthon
  6. driver.close() : finnaly this is used to close the driver.
    
