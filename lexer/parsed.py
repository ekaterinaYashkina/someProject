class ParsedToken:

    def __init__(self, start,end, token_type, value, keyword_type = None ):
        self.start = start
        self.end = end
        self.token_type = token_type
        self.value = value
        self.keyword_type = keyword_type

    #works when we call 'print <ParsedToken object>'
    def __str___(self):
        if self.keyword_type is not None:
            return "'{}':\n\t{{'{}':'{}'}}".format(self.keyword_type, self.token_type.name, self.value)
        else:
            return "'{}':'{}'".format(self.token_type.name, self.value)

    #works when we call 'str(<ParsedToken object>)'
    def __repr__(self):
        if self.keyword_type is not None:
            return "'{}':\n\t{{'{}':'{}'}}".format(self.keyword_type, self.token_type.name, self.value)
        else:
            return "'{}':'{}'".format(self.token_type.name, self.value)