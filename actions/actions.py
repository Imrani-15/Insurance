# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
#from databases import Database
from integrate_database import dataupdate
#import webbrowser
#import mysql.connector

class ActionName(Action):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "action_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_name",name=tracker.get_slot("name"))
        #dataupdate(name=tracker.get_slot("name"))
        return [SlotSet('name', tracker.latest_message['text'])]


class ActionPolicy(Action):
    def name(self) -> Text:
        """Unique identifier of the form"""
        return "action_policy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_policy",policy=tracker.get_slot("policy"))
        #dataupdate(policy=tracker.get_slot("policy"))
        return [SlotSet('policy', tracker.latest_message['text'])]



class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_request_details"

    def run(self,dispatcher,tracker: Tracker,domain: "DomainDict",) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_request_details",name=tracker.get_slot("name"),
                                 policy=tracker.get_slot("policy"))
#                                 IncidentDate=tracker.get_slot("Date"),
#                                 IncidentReason=tracker.get_slot("reason"))

        dataupdate(name=tracker.get_slot("name"),policy=tracker.get_slot("policy"))
        dispatcher.utter_message("Thanks for the valuable feedback.")
        return []


#class Actionrequest_details(Action):
#    def name(self) -> Text:
#        """Unique identifier of the form"""
#        return "action_request_details"


#    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#       dataupdate(tracker.get_slot("name"),tracker.get_slot("policy"))
#       dispatcher.utter_message("Thanks for the valuable feedback. ")
#       return []


#class ActionUserdetailsForm(FormAction):
#    def name(self) -> Text:
#        return "user_details_form"

#    @staticmethod
#    def required_slots(tracker: Tracker) -> List[Text]:
#        return ["name","policy"]



#    def slot_mappings(self):
#        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

#        return {
#                "name": [self.from_entity(entity="name",intent="name"), ],
#                "policy": [self.from_text()],
#        }

#    def requestdetails(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ) -> List[Dict]:
#       dispatcher.utter_message(template="utter_request_details",
#                                name=tracker.get_slot("name"),policy=tracker.get_slot("policy"))
#       return []



#class ValidateForm(Action):

#    def name(self) -> Text:
#        return "user_details_form"

#    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:

#        required_slots = ["name","policy"]

#        for slot_name in required_slots:
#            if tracker.slots.get(slot_name) is None:
#                return [SlotSet("required_slots",slot_name)]
#        return [SlotSet("required_slots",None)]











