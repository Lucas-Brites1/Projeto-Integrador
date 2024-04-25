def tentar_novamente_cadastro(produto):
    while True:
        erro_tentar_cadastrar_novamente = input(f"\nDados de entrada que deveriam ser um número foram inseridos errados, gostaria de tentar cadastrar o produto: {produto[0]} novamente? [S/N]").upper()
        if erro_tentar_cadastrar_novamente == "S":
            return "CADASTRAR NOVAMENTE"
        elif erro_tentar_cadastrar_novamente == "N":
            return None
        else:
            erro_tentar_cadastrar_novamente = input(f"\nDados de entrada que deveriam ser um número foram inseridos errados, gostaria de tentar cadastrar o produto: {produto[0]} novamente? [S/N]").upper()


def inputs_produto():
    """
    PV: Preço de Venda (SERÁ GERADO)
    CP: Custo do Produto [R$]
    CF: Custo Fixo/Administrativo [%]
    CV: Comissão de Vendas [%]
    IV: Impostos sobre produto [%]
    ML: Rentabilidade (Margem de Lucro) [%]
    """
    print("\n\033[3;34;40mCadastrando Produto:\033[m")

    produto = [
        input("  .\033[1;37;40mNome do Produto: \033[m"), 
        input("  .\033[1;37;40mDescrição do Produto: \033[m"),
        input("  .\033[1;37;40mCusto do Produto (R$): \033[m"),
        input("  .\033[1;37;40mCusto Fixo/Administrativo [%]: \033[m"),
        input("  .\033[1;37;40mComissão de Vendas [%]: \033[m"),
        input("  .\033[1;37;40mImpostos sobre Produto [%]: \033[m"),
        input("  .\033[1;37;40mRentabilidade (Margem de Lucro) [%]: \033[m"),
        input("  .\033[1;37;40mCategoria do Produto: \033[m")
    ]

    for c in range(2, len(produto)-1):
        if c == 2:  # Custo do Produto
            try:
                conversao_tipo = float(produto[c])
                produto[c] = conversao_tipo
            except ValueError as ERR:
                return tentar_novamente_cadastro(produto)
        else:  # Outros campos numéricos
            try:
                conversao_tipo = int(produto[c])
                produto[c] = conversao_tipo
            except ValueError as ERR:
                return tentar_novamente_cadastro(produto)
                
    return produto
