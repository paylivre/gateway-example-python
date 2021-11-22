from argon2 import PasswordHasher
from argon2.low_level import Type

ph = PasswordHasher(time_cost=2, memory_cost=16, parallelism=2,
                    hash_len=16, salt_len=16, encoding='utf-8',
                    type=Type.I)
password = "h97HSGfA7p0NHWUYM5HJW3v5ok8ne6Iwhttps://playground.gateway.paylivre.com/?merchant_id=99&operati on=5&email=john.doe@gmail.com&document=55913301005&merchant_transaction_id=pl12345&amount=43298& currency=USD&type=1&account_id=C1001&callback_url=https://www.jackpot-merchant.com&redirect_url= https://www.jackpot-merchant.com/thank-you"
hash = ph.hash(password)
print(hash)
