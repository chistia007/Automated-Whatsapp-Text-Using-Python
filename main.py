import pywhatkit as kit
import pyautogui as gui
import time

# # Send a message to the specified contact
kit.sendwhatmsg("+8801731538632", "This is an automated message", 11, 47)

# # Wait for the message window to open and the message to be typed
time.sleep(5)

# # Simulate pressing the enter key to send the message
gui.press("enter")



def on_message_received(message):
#     # Process the message and generate a reply
     reply = "Thanks for your message! I am a bot and I am currently unable to respond to individual messages. Please contact the administrator of this group if you have any questions or concerns."

#     # Send the reply to the same group that the message was received from
     kit.sendwhatmsg_to_group("Group Name", reply, 0, 0)

# # Use the listen() function to start listening for incoming messages in the specified group
kit.listen(on_message_received, group_name="Group Name")






#For automated fixed responses


fixed_response = "Thank you for your message. I am not available at the moment, but I will get back to you as soon as possible."

# Define the function to be called when a new message is received
def on_message_received(message):
    # Wait for the message window to open
    time.sleep(5)

    # Type the fixed response message and send it
    gui.typewrite(fixed_response)
    gui.press("enter")

# Use the listen() function to start listening for incoming messages
kit.listen(on_message_received)
