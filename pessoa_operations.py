import pandas
from conexao import Conexao
from pessoa import Pessoa
import json

class PessoaOperations:
    
    async def get_nome_pessoa(nome: str) -> dict:
        conexao = Conexao().conectar()
        cursor = conexao.cursor()
        
        sql = f"select id, nome, email, mensagem from sql10698414.mensagens where nome like '%{nome}%'"
        
        cursor.execute(sql)
        
        resultado = cursor.fetchall()
        
        colunas = ('id', 'nome', 'email', 'mensagem')
        
        print(resultado)
        print(type(resultado))
        
        dados = pandas.DataFrame(resultado, columns=colunas)
        
        print(dados)
        print(dados.info())
        
        Conexao().desconectar(cursor)
        return dados.to_dict()
    
    async def inserir_pessoa(pessoa: Pessoa) -> str | None :
        pessoa_local = Pessoa(pessoa.nome, pessoa.email, pessoa.mensagem)
        
        conexao = Conexao().conectar()
        cursor = conexao.cursor()
        
        sql = f"INSERT INTO sql10698414.mensagens (nome, email, mensagem) values ('{pessoa_local.nome}', '{pessoa_local.email}', '{pessoa_local.mensagem}');"
        
        try:
            resultado = cursor.execute(sql)
            if resultado <= 0:
                return {"message":"Falha na gravação da pessoa"}
        
        except ConnectionRefusedError as error2:
            return {"message":f"{error2.strerror}"}
        
        except ConnectionError as error:
            return {"message":f"{error.strerror}"}
        
        finally:
            conexao.commit()
            Conexao().desconectar(cursor)
            
        return "message Pessoa " + pessoa_local.nome + ' inserida com sucesso!'
        
        
        
        
        
        
        
        
        