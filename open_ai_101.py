import pandas as pd
# list all open ai models
engines = openai.Engine.list()
pd = pd.DataFrame(openai.Engine.list()['data'])
display(pd[['id', 'owner']])
