# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class RefactorQuestion(Action):

    def name(self) -> Text:
        return "action_refactor_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # text_latest_message=f"text_latest_message: {tracker.latest_message}
        slotNewQuestion = tracker.get_slot('newQuestion')
        userContent = tracker.latest_message['text']
        # dispatcher.utter_message(text="get_slot(newQuestion): "+str(slotNewQuestion))
        # dispatcher.utter_message(text="get_slot(newQuestion): "+str(userContent))

        # dispatcher.utter_message(text=f"text_latest_message"+text_latest_message)

        dispatcher.utter_message(text="GPT的回應")
        return [
            SlotSet("newQuestion","Tony")
        ]
