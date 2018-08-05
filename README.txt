
 Para executar o software, seguir os seguintes comandos:

  python3 server.py <porta>
  python3 client.py <nome/ip> <porta>

 Após isso, o software estará em funcionamento. 

 Os seguintes comandos podem ser executados atraves do programa cliente:

   [Registro de usuario] Cria um novo usuario e define sua senha:
    N [nome_do_usuario] [senha]
    Exemplo: N wilson 123 
   [Envio de arquivo] Envia um novo arquivo ao servidor:
    S [nome_do_usuario] [senha] [nome_do_arquivo] [conteudo_do_arquivo]
    Exemplo: S wilson 123 meu_texto Mensagem importante
   [Recebimento de conteudo de arquivo] Le um arquivo do servidor:
    R [nome_do_usuario] [senha] [nome_do_arquivo]
    Exemplo: R gabriel 12345 meu_diario
   [Listagem de arquivos] Lista os arquivos por usuario:
    L [nome_do_usuario] [senha]
    Exemplo: R gabriel 12345
 
 As respostas enviadas pelo servidor foram definidas em especificacao e estao detalhadas na documentacao

