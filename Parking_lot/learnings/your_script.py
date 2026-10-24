from typing import final

@final
class ImmutableData:
    pass

# Type checkers will flag this inheritance as an error
class MaliciousExtension(ImmutableData): 
    pass
