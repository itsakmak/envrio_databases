from enum import Enum

class AccountType(str, Enum):
    commercial = 'commercial'
    academic = 'academic'
    beta = 'beta'
    alpha = 'alpha'