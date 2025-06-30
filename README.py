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
# ### `translate-shell`
# 
# O `translate-shell` é uma ferramenta de linha de comando de código aberto que oferece a capacidade de traduzir texto e palavras entre vários idiomas diretamente do `Terminal Emulator`. Ele utiliza serviços de tradução _online_, como o `Google Translate`, para fornecer traduções rápidas e precisas. O `translate-shell` suporta uma ampla variedade de idiomas e pode ser usado tanto para traduções simples de palavras e frases quanto para traduções mais complexas de texto completo. Além disso, ele oferece opções avançadas, como tradução de áudio, detecção automática de idioma e pronúncia de palavras, tornando-se uma ferramenta útil para estudantes, viajantes e qualquer pessoa que precise de traduções instantâneas e convenientes diretamente do `Terminal Emulator`.
# 
# ### `pdftotext`
# 
# O `pdftotext` é uma ferramenta de linha de comando, geralmente parte do pacote `Poppler` ou `Xpdf`, que converte o conteúdo de arquivos PDF em texto simples. Ele extrai o texto mantendo a ordem de leitura e pode preservar ou não a formatação de colunas e quebras de linha, conforme opções configuráveis. É muito útil para automatizar a extração de texto de documentos PDF em _scripts_ e fluxos de trabalho de análise de dados ou indexação.
# 
# ### `qpdf`
# 
# O `qpdf` é uma ferramenta para manipular arquivos PDF de maneira avançada. Você pode usá-lo para fazer operações como quebra de PDFs, mesclagem, e até mesmo para manipular metadados.
# 
# ### `pdfunite`
# 
# O `pdfunite` é uma ferramenta de linha de comando, integrante do pacote Poppler, que permite mesclar vários arquivos PDF em um único documento. Basta informar na chamada os arquivos de entrada e o nome do PDF de saída. É ideal para scripts e fluxos de trabalho automatizados de organização e consolidação de documentos.
# 
# ### `tesseract`
# 
# O `Tesseract` é um mecanismo de OCR (Reconhecimento Óptico de Caracteres) de código aberto, originalmente desenvolvido pela HP e atualmente mantido pelo Google. Ele converte imagens de texto em texto editável, suportando múltiplos idiomas e formatos de imagem, além de oferecer opções de treinamento para reconhecer fontes e caracteres personalizados. Muito utilizado em projetos de digitalização e extração automatizada de dados, o `Tesseract` é integrado a diversas aplicações e bibliotecas em linguagens como `Python`, `Java` e `C++`.
# 
# ### `gImageReader`
# 
# O `gImageReader` é uma aplicação de código aberto que oferece uma interface amigável para a extração de texto de imagens ou arquivos `.pdf`. Ele utiliza tecnologias de reconhecimento óptico de caracteres (OCR) para digitalizar documentos e converter o texto contido neles em formato editável. Com recursos como suporte a vários idiomas e opções de formatação, o gImageReader é uma ferramenta útil para transformar documentos digitalizados em texto pesquisável e editável.
# 
# **ATENÇÃO**: Você pode utilizar o `pdftotext` e/ou o `tesseract` em arquivos `.pdf` para converter em `.txt` e depois traduzir para o português brasileiro com os comandos do `translate-shell` que serão apresentados depois do passo a passo de como instalar o `translate-shell`.

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
