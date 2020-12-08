from models import Produto, Categoria

list_produtos = []  
list_categorias = []

class Principal:
    
        
    def adicionar_produto(self):
        produtos = {'nome': None, 'quantidade': None, 'valor': None, 'descricao': None, 'categoria': [], 'subcategoria': []}   
        categoria_list = []
        p = Produto()
        p.set_nome(str(input("Digite o nome do Produto: ")))
        p.set_quantidade(int(input("Digite a quantidade do Produto: ")))
        p.set_valor(float(input("Digite o valor do Produto: ")))
        while p.get_valor() <= 0.0:
            print("\nValor invalido, informe um valor maior que 0")
            p.set_valor(float(input("Digite o valor do Produto: ")))
        p.set_descricao(str(input("Digite a descricao do Produto: ")))
        while len(p.get_descricao()) < 20:
            print("\nInforme uma descricao com no minimo 20 caracteres!")
            p.set_descricao(str(input("Digite a descricao do Produto: ")))
        print('\nCategorias: ')
        for i in range(len(list_categorias)):
            print(f'[{i}]. ' + str(list_categorias[i]['nome']))
        op = int(input('\nSelecione uma opcao: '))
        for y in range(len(list_categorias)):
            if op == y:
                categoria_list.append(list_categorias[y]['nome'])
                menu = True
                while menu:
                    print('''
                    Deseja cadastrar outra categoria para esse produto?
                    [1] - Sim
                    [2] - Nao
                        ''')
                    op = int(input('Selecione uma opcao: '))
                    if op == 1:
                        for x in range(len(list_categorias)):
                            print(f'[{x}]. ' + str(list_categorias[x]['nome']))
                        op = int(input('\nSelecione uma opcao: '))
                        for l in range(len(list_categorias)):
                            if op == l:
                                categoria_list.append(list_categorias[l]['nome'])
                    elif op == 2:
                        break
            produtos['categoria'] = categoria_list       
        produtos['nome'] = p.get_nome()
        produtos['quantidade'] = p.get_quantidade()
        produtos['valor'] = p.get_valor()
        produtos['descricao'] = p.get_descricao()
        list_produtos.append(produtos)
        print('\nProduto Cadastrado')      
    
    def remover_produto(self):
        for i in range(len(list_produtos)):
            print(f'[{i}]. ' + str(list_produtos[i]))
        op = int(input('\nSelecione uma opcao: '))
        del list_produtos[op]
    
    def editar_produto(self):
        for i in range(len(list_produtos)):
            print(f'[{i}]. ' + str(list_produtos[i]))
        op = int(input('\nSelecione uma opcao: '))
        for x in range(len(list_produtos)):
            if op == x:
                list_produtos[op]['nome'] = str(input("Digite o nome do Produto: "))
                list_produtos[op]['quantidade'] = int(input("Digite a quantidade do Produto: "))
                list_produtos[op]['valor'] = float(input("Digite o valor do Produto: "))
                while list_produtos[op]['valor'] <= 0.0:
                    print("\nValor invalido, informe um valor maior que 0")
                    list_produtos[op]['valor'] = float(input("Digite o valor do Produto: "))
                list_produtos[op]['descricao'] = str(input("Digite a descricao do Produto: ")) 
                while len(list_produtos[op]['descricao']) < 20:
                    print("\nInforme uma descricao com no minimo 20 caracteres!")
                    list_produtos[op]['descricao'] = str(input("Digite a descricao do Produto: ")) 
                    
    def listar_produto(self):
        for i in range(len(list_produtos)):
            print(f'[{i}]. ' + str(list_produtos[i]))
    
    def cadastrar_categoria(self):
        categoria = {'nome': None, 'subcategoria': []}   
        c = Categoria()
        c.set_nome(str(input("Digite o nome da categoria: ")))
        categoria['nome'] = c.get_nome()
        list_categorias.append(categoria)
        print('\nCategoria Cadastrada!') 

    def cadastrar_subcategoria(self):
        subcategoria = []
        c = Categoria()
        c.set_nome(str(input("Digite o nome da categoria: ")))
        for x in range(len(list_categorias)):
            if c.get_nome() == list_categorias[x]['nome']:
                subcategoria.append(str(input("Digite o nome da subcategoria: ")))
                op = True
                while op:
                    print('''
                    Deseja cadastrar outra subcategoria para esta categoria?
                    [1] - Sim
                    [2] - Nao
                        ''')
                    op = int(input('Selecione uma opcao: '))
                    if op == 1:
                        subcategoria.append(str(input("Digite o nome da subcategoria: ")))
                    elif op == 2:
                        break
            list_categorias[x]['subcategoria'] = subcategoria    
    
    def menu(self):
        opcoes = ['Listar Produtos','Cadastrar Produto','Editar Produto', 'Remover produto', 'Cadastrar Categoria', 'Cadastrar Subcategoria', 'Sair'] 
        print('\n-- MENU --') 
        for ops, opcao in enumerate(opcoes):
            print(f'[{ops+1}] - {opcao}')
        op = int(input('\nSelecione uma opcao: '))
        return op
                       
if __name__ == '__main__':
    
    principal = Principal()
    op = True
    while op:
        op = principal.menu()
        if op == 1:
            principal.listar_produto()
        elif op == 2:
            principal.adicionar_produto()
        elif op == 3:
            principal.editar_produto()
        elif op == 4:
            principal.remover_produto()
        elif op == 5:
            principal.cadastrar_categoria()
        elif op == 6:
            principal.cadastrar_subcategoria()         
        elif op == 7:
            exit(1) 
        elif op > 7:
            print('Opcao incorreta, tente novamente! ')
            