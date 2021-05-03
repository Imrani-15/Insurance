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
from databases import Database
from integrate_database import getData
import webbrowser


class ActionFirstname(Action):

    def name(self) -> Text:
        return "action_first_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # write the sql query here.
        query = "select * from insurance1"

        # pass the sql query to the getData method and store the results in `data` variable.
        data = getData(query)

        print("data: ", data)

        dispatcher.utter_message(text="utter_first_name", json_message=data)

        return []


class ActionPolicyNum(Action):

    def name(self) -> Text:
        return "action_policy_Num"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # write the sql query here.
        query = "select * from insurance1"

        # pass the sql query to the getData method and store the results in `data` variable.
        data = getData(query)

        print("data: ", data)

        dispatcher.utter_message(text="utter_policy_Num", json_message=data)

        return []


class ActionIncidentDate(Action):

    def name(self) -> Text:
        return "action_incident_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # write the sql query here.
        query = "select * from insurance1"

        # pass the sql query to the getData method and store the results in `data` variable.
        data = getData(query)

        print("data: ", data)

        dispatcher.utter_message(text="utter_incident_date", json_message=data)

        return []


class ActionIncidentReason(Action):

    def name(self) -> Text:
        return "action_incident_reason"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # write the sql query here.
        query = "select * from insurance1"

        # pass the sql query to the getData method and store the results in `data` variable.
        data = getData(query)

        print("data: ", data)

        dispatcher.utter_message(text="utter_incident_reason", json_message=data)

        return []


class ValidateForm(Action):
    def name(self) -> Text:
        return "user_details_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:

        required_slots = ["first_name", "policy_Num","incident_date","incident_reason"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("required_slots",slot_name)]
        return [SlotSet("required_slots",None)]


class ActionSubmit(Action):
    def name(self) -> Text:
        return "action_submit"

    def run(self,dispatcher,tracker: Tracker,domain: "DomainDict",) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_submit",Name=tracker.get_slot("name"),
                                 PolicyNumber=tracker.get_slot("policy"),
                                 IncidentDate=tracker.get_slot("Date"),
                                 IncidentReason=tracker.get_slot("reason"))










