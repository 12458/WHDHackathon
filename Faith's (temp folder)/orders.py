from dialogflow_gracie import Session_Client
from converter import convert_audio

sess = Session_Client()

# this is for voice inputs
#queryText = convert_audio()

# this is manual text input
queryText = "Can i have i loaf of bread, some eggs, spinach, cucumber and lettuce with some watermelon as well"

user_input, order = sess.dialogflow(queryText)

print("...")
print(user_input)
print("...")
print(order)
