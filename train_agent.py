from qagent import QAgent

agent = QAgent(0.5, 0.3)

agent.train(100000)

agent.save()