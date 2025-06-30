#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `pdfimages` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `pdfimages` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install/use the `pdfimages` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `pdfimages`
# 
# O `pdfimages` é uma ferramenta de linha de comando que extrai imagens de arquivos `.pdf`. Ele permite converter páginas de um `.pdf` em imagens nos formatos PBM, PGM, PPM e JPEG, oferecendo opções para controlar a qualidade e o formato das imagens extraídas. Essa ferramenta é útil para extrair elementos gráficos de documentos `.pdf` para uso em outros contextos ou para análise de conteúdo visual.
# 

# ## 1. Como configurar/instalar/usar o `pdfimages` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `pdfimages` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt clean
#     ``` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
#     
#     ```bash
#     sudo apt autoclean
#     ```
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt autoremove -y
#     ```
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: 
#     
#     ```bash
#     sudo apt update
#     ```
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
#     
#     ```bash
#     sudo apt --fix-broken install
#     ```
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt clean
#     ``` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  
#     
#     ```bash
#     sudo apt list --upgradable
#     ```
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
#     
#     ```bash
#     sudo apt full-upgrade -y
#     ```

# Para instalar o `pdfimages` no `Linux Ubuntu`, você precisa instalar o pacote `poppler-utils`, que inclui o `pdfimages` junto com outras ferramentas úteis para trabalhar com arquivos `.pdf`. Você pode fazer isso usando o gerenciador de pacotes apt do Ubuntu. Siga estes passos:
# 
# 3. **Instale o pacote `poppler-utils` executando:** `sudo apt install poppler-utils -y`
# 
# Após a instalação, você poderá usar o comando pdfimages diretamente no terminal.
# 
# 4. **Verificar a Instalação:** Para verificar se o `pdfimages` foi instalado corretamente, você pode digitar no terminal: `pdfimages --version`
# 
#     Isso deve exibir a versão do `pdfimages` instalada, indicando que a ferramenta está pronta para ser usada.

# ### 1.2 Código completo para configurar/instalar
# 
# Para configurar/instalar/usar o `pdfimages` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install poppler-utils -y
#     ```
#     

# ## 2. Usar o `pdfimages` a partir do `Terminal Emulator`
# 
# ### 2.1 Extrair imagens de um arquivo `.pdf`
# 
# 1. Depois de instalar o `pdfimages`, você pode extrair imagens de um arquivo `.pdf` com um comando como:
# 
# ```bash
# pdfimages -all seu_arquivo.pdf pasta_destino/
# ```
# 
# Substitua `seu_arquivo.pdf` pelo nome do arquivo `.pdf` do qual você deseja extrair as imagens e pasta_destino pelo nome da pasta onde você deseja que as imagens sejam salvas. Se a pasta não existir, o `pdfimages` a criará.

# ### 2.2 Savar imagens na mesma pasta do arquivo `.pdf`
# 
# Se você deseja salvar as imagens extraídas na mesma pasta do arquivo `.pdf` original usando o pdfimages, você não precisa especificar um caminho para a pasta de destino. Basta omitir o nome da pasta de destino no comando. Aqui está como você pode fazer isso:
# 
# 1. Navegue até a pasta onde o arquivo `.pdf` está localizado, usando o comando cd no terminal. Por exemplo:
# 
#     ```bash
#     cd /caminho/para/sua/pasta
#     ```
# 
#     Substitua `/caminho/para/sua/pasta` pelo caminho real onde o seu arquivo `.pdf` está localizado.
# 
# 2. Execute o comando `pdfimages` sem especificar um diretório de destino, apenas o nome do arquivo `.pdf`:
# 
#     ```bash
#     pdfimages -png nome_do_arquivo.pdf prefixo_imagem
#     ```
# 
#     Substitua `nome_do_arquivo.pdf` pelo nome do seu arquivo `.pdf` e `prefixo_imagem` pelo prefixo que você deseja usar para as imagens extraídas. O `pdfimages` salvará as imagens na mesma pasta do arquivo `.pdf`, com os nomes começando pelo prefixo especificado seguido de um número sequencial.
# 
# Por exemplo, se o seu arquivo `.pdf` chama-se `documento.pdf` e você usa img como prefixo, os arquivos de imagem serão salvos como `img-000.jpg`, `img-001.jpg` etc., na mesma pasta onde `documento.pdf` está localizado.

# ## Referências
# 
# [1] OPENAI. ***Instalar odfimages Ubuntu.*** Disponível em: <https://chatgpt.com/c/6862e738-fef0-8002-b5be-30bce6a632a6> (texto adaptado). ChatGPT. Acessado em: 27/02/2024 12:00.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 27/02/2024 12:00.
# 
