from katakana.core.loader import LookupRunner, LookupType

token = ""  # Bot token
runner = LookupRunner(discord_token=token)

print(runner.run_lookup(LookupType.DISCORD_USER, 1234567890)) # User ID here
