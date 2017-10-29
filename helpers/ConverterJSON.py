class ConverterJSON(object):
    def __init__(self):
        pass

    def convertObjectToJSON (self, obj):
        # Se for um objeto, transforma num dict
        if hasattr(obj, '__dict__'):
            obj = obj.__dict__

        # Se for um dict, lê chaves e valores; converte valores
        if isinstance(obj, dict):
            return {k: self.convertObjectToJSON(v) for k, v in obj.items()}
        # Se for uma lista ou tupla, lê elementos; também converte
        elif isinstance(obj, list) or isinstance(obj, tuple):
            return [self.convertObjectToJSON(e) for e in obj]
        # Se for qualquer outra coisa, usa sem conversão
        else:
            return obj