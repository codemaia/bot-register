from botcity.web import WebBot, Browser, By



def cadastro_livro():  
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.FIREFOX
    bot.driver_path = r"D:\dev\bot-register\geckodriver.exe"

    name_livro = 'Criando bots em python'
    author_livro = 'Renan Maia'
    editora = 'Futuro'
    
    bot.browse("http://localhost:3000/")
    bot.maximize_window()
    bot.wait(2000)

    button_cadastro = bot.find_element('button')
    button_cadastro.click()
    bot.wait(1000)
    
    # -- Cadastro
    #Nome do livro
    input_name = bot.find_element("name", By.ID)
    input_name.click()
    bot.paste(name_livro)
    bot.wait(1000)
    
    #Autor
    input_author = bot.find_element("author", By.ID)
    input_author.click()
    bot.paste(author_livro)
    bot.wait(1000)
    
    #Editora
    input_editora = bot.find_element("editora", By.ID)
    input_editora.click()
    bot.paste(editora)
    bot.wait(1000)
    
    button_save = bot.find_element("save", By.ID)
    button_save.click()

    input()

cadastro_livro()

def main():
    
    cadastro_livro()
    
    