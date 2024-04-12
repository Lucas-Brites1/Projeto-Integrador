from Product import Produto

class InputErrorValidation(Exception):
    def __init__(self, INPUT_VALUE, ERROR_TYPE, ERROR_PARAM, ERROR_VALUE):
        self.INPUT_VALUE = INPUT_VALUE
        self.ERROR_TYPE = ERROR_TYPE
        self.ERROR_PARAM = ERROR_PARAM
        self.ERROR_VALUE = ERROR_VALUE

def validar(PRODUTO: Produto) -> bool:
    inputs_percentuais = ["custo_fixo", "comissao", "impostos", "rentabilidade"]
    if PRODUTO.custo_produto <= 0:
        raise InputErrorValidation(PRODUTO, "InvalidProductPrice", "Custo do Produto", PRODUTO.custo_produto)
    else:
        for inputs in inputs_percentuais:
            if getattr(PRODUTO, inputs) < 0:
                raise InputErrorValidation(PRODUTO, "InvalidPorcentValue", inputs, getattr(PRODUTO, inputs))

    print("\033[92mProduto cadastrado com sucesso!\033[0m")
    return True

def __(P) -> bool:
    try:
        validar(P)
    except InputErrorValidation as err:
        print(f"\033[91mINPUT ERROR\n\033[91m{err.ERROR_TYPE} -> \033[94m{err.ERROR_PARAM}\033[0m: {err.ERROR_VALUE}")
        return False

