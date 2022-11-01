# Projeto para aprender TDD

Requisitos:

Ter o python 3 instalado.

Passos realizados:

1 - Download dos drivers para o selenium para o Chrome e o Firefox

1.1 Entre no diretório de ~/Downloads:

$ cd ~/Downloads

1.1 - Entrar no navegador no seguinte endereço para ver as versões disponíveis e copiar o link da versão desejada (clicar no link da versão para ver os arquivos para baixar):

https://chromedriver.chromium.org/downloads

1.2 - Em seguida, no terminal, colar o endereço do link da versão desejada para baixar com curl ou wget. Exemplo:

$ wget https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip

1.3 - Entrar no navegador no seguinte endereço para ver as versões disponíveis e copiar o link da versão desejada (está na seção de Assets):

https://github.com/mozilla/geckodriver/releases

1.4 - Em seguida, no terminal, colar o endereço do link da versão desejada para baixar com curl ou wget. Exemplo:

$ wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz

2 - Extrair os drivers:

2.1 No diretório em que foi baixado (no caso o ~/Downloads), descompacte os arquivos baixados:

$ tar -xzf geckodriver-v0.32.0-linux64.tar.gz

$ unzip chromedriver_linux64.zip

3. Mova os arquivos extraídos para um diretório que se encontre no PATH. Exemplo:

$ mkdir -p ~/.local/bin

$ echo 'PATH=~/.local/bin:$PATH' >> ~/.zshrc

$ source ~/.zshrc

ou

$ echo 'PATH=~/.local/bin:$PATH' >> ~/.bashrc

$ source ~/.bashrc

$ mv chromedriver ~/.local/bin/chromedriver

$ mv geckodriver ~/.local/bin/geckodriver

4. Teste se os drivers estão ok:

$ chromedriver --version

$ geckodriver --version


