import itchat
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

deepThought = ChatBot("deepThought")
deepThought.set_trainer(ChatterBotCorpusTrainer)
deepThought.train("chatterbot.corpus.chinese")
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    response = deepThought.get_response(msg['Text'])
    print("from",msg['FromUserName'],msg['Text'])
    print("to",response)
    itchat.send(msg=str(response), toUserName=msg['FromUserName'])
itchat.auto_login(enableCmdQR=True)
itchat.run()